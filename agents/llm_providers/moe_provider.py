"""Mixture of Experts (MoE) provider - combines multiple LLM providers."""

import logging
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

from .base_provider import LLMProvider, LLMResponse
# Note: LLMProviderFactory is imported locally to avoid circular import


class MoEStrategy:
    """Strategies for routing and combining provider responses."""

    VOTING = "voting"           # Send to all, use majority vote
    CASCADE = "cascade"         # Try providers in order until success
    TASK_BASED = "task_based"   # Route based on task characteristics
    BEST_OF_N = "best_of_n"     # Query multiple, pick best response
    SPECIALIST = "specialist"   # Each provider handles specific tools


class MixtureOfExpertsProvider(LLMProvider):
    """
    Mixture of Experts (MoE) provider that combines multiple LLM providers.

    This provider can use different strategies to leverage the strengths of
    multiple LLM providers simultaneously, creating a "Frankenstein" API-based
    ensemble system.

    Strategies:
        - voting: Send request to all providers, use consensus/voting
        - cascade: Try providers in order until one succeeds
        - task_based: Route to best provider based on task type
        - best_of_n: Query N providers, pick best response
        - specialist: Route tool calls to specialized providers

    Example:
        provider = MixtureOfExpertsProvider(
            providers=["anthropic", "deepseek", "mistral"],
            strategy="task_based"
        )
        response = provider.create_completion(messages)
    """

    def __init__(
        self,
        providers: List[str] = None,
        strategy: str = MoEStrategy.TASK_BASED,
        fallback_order: List[str] = None,
        specialist_map: Optional[Dict[str, str]] = None,
        voting_threshold: float = 0.5,
        parallel_workers: int = 3,
        llm_provider_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize MoE provider.

        Args:
            providers: List of provider names to use (default: all available)
            strategy: MoE strategy to use (see MoEStrategy)
            fallback_order: Order for cascade strategy (default: anthropic, deepseek, mistral)
            specialist_map: Map task types to providers for specialist routing
            voting_threshold: Confidence threshold for voting (0.0-1.0)
            parallel_workers: Number of parallel workers for concurrent requests
            llm_provider_config: Full llm_provider config dict containing API keys for sub-providers
        """
        self.logger = logging.getLogger(f"noseeum.moe_provider")

        # Default to all providers if none specified
        if providers is None:
            providers = ["anthropic", "deepseek", "mistral"]

        # Import factory locally to avoid circular import
        from .factory import LLMProviderFactory

        # Create provider instances
        self.providers = {}
        self.available_providers = []

        for provider_name in providers:
            try:
                # Extract API key and config from llm_provider_config if available
                api_key = None
                model = None
                provider_kwargs = {}

                if llm_provider_config and provider_name in llm_provider_config:
                    provider_config = llm_provider_config.get(provider_name, {})
                    api_key = provider_config.get('api_key')
                    model = provider_config.get('model')

                    self.logger.debug(f"MoE: {provider_name} config found, api_key={'set' if api_key else 'missing'}, model={model}")

                    # Handle DeepSeek base_url if present
                    if provider_name == 'deepseek' and 'base_url' in provider_config:
                        provider_kwargs['base_url'] = provider_config['base_url']
                else:
                    self.logger.debug(f"MoE: No config found for {provider_name} in llm_provider_config")

                provider = LLMProviderFactory.create_provider(
                    provider_name,
                    api_key=api_key,
                    model=model,
                    **provider_kwargs
                )
                self.providers[provider_name] = provider

                if provider.is_available():
                    self.available_providers.append(provider_name)
                    self.logger.info(f"MoE: Loaded provider {provider_name}")
                else:
                    self.logger.warning(f"MoE: Provider {provider_name} not available (no API key)")

            except Exception as e:
                self.logger.error(f"MoE: Failed to load provider {provider_name}: {e}")

        self.strategy = strategy
        self.fallback_order = fallback_order or ["anthropic", "deepseek", "mistral"]
        self.voting_threshold = voting_threshold
        self.parallel_workers = parallel_workers

        # Specialist mapping: task keywords -> provider
        self.specialist_map = specialist_map or {
            "code": "deepseek",
            "python": "deepseek",
            "javascript": "deepseek",
            "programming": "deepseek",
            "function": "deepseek",
            "creative": "mistral",
            "story": "mistral",
            "write": "mistral",
            "compose": "mistral",
            "analysis": "anthropic",
            "analyze": "anthropic",
            "explain": "anthropic",
            "research": "anthropic"
        }

        self.logger.info(
            f"MoE Provider initialized: strategy={strategy}, "
            f"available={len(self.available_providers)}/{len(self.providers)}"
        )

    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Create completion using MoE strategy.

        Args:
            messages: List of messages
            tools: Optional tool definitions
            max_tokens: Maximum tokens
            temperature: Sampling temperature
            **kwargs: Additional parameters

        Returns:
            LLMResponse with MoE-enhanced response
        """
        if not self.available_providers:
            return self._demo_response("MoE: No providers available")

        # Route based on strategy
        if self.strategy == MoEStrategy.VOTING:
            return self._voting_strategy(messages, tools, max_tokens, temperature, **kwargs)

        elif self.strategy == MoEStrategy.CASCADE:
            return self._cascade_strategy(messages, tools, max_tokens, temperature, **kwargs)

        elif self.strategy == MoEStrategy.TASK_BASED:
            return self._task_based_strategy(messages, tools, max_tokens, temperature, **kwargs)

        elif self.strategy == MoEStrategy.BEST_OF_N:
            return self._best_of_n_strategy(messages, tools, max_tokens, temperature, **kwargs)

        elif self.strategy == MoEStrategy.SPECIALIST:
            return self._specialist_strategy(messages, tools, max_tokens, temperature, **kwargs)

        else:
            self.logger.warning(f"Unknown strategy {self.strategy}, falling back to task_based")
            return self._task_based_strategy(messages, tools, max_tokens, temperature, **kwargs)

    def _voting_strategy(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]],
        max_tokens: int,
        temperature: float,
        **kwargs
    ) -> LLMResponse:
        """
        Send request to all providers and use voting/consensus.

        Returns the response that appears most frequently (for text)
        or has the highest aggregate confidence.
        """
        self.logger.info("MoE: Using VOTING strategy")

        responses = []

        # Query all available providers in parallel
        with ThreadPoolExecutor(max_workers=self.parallel_workers) as executor:
            futures = {}

            for provider_name in self.available_providers:
                provider = self.providers[provider_name]
                future = executor.submit(
                    provider.create_completion,
                    messages, tools, max_tokens, temperature, **kwargs
                )
                futures[future] = provider_name

            # Collect responses
            for future in as_completed(futures):
                provider_name = futures[future]
                try:
                    response = future.result(timeout=60)
                    responses.append((provider_name, response))
                    self.logger.debug(f"MoE: Got response from {provider_name}")
                except Exception as e:
                    self.logger.error(f"MoE: {provider_name} failed: {e}")

        if not responses:
            return self._demo_response("MoE: All providers failed in voting")

        # Extract text responses
        texts = []
        for provider_name, response in responses:
            for block in response.content:
                if block.get("type") == "text":
                    texts.append((provider_name, block.get("text", "")))

        if not texts:
            # No text responses, return first response
            return responses[0][1]

        # Use majority vote for short responses, or longest for detailed responses
        if len(texts[0][1]) < 100:
            # Short responses - use voting
            text_counter = Counter([t[1] for t in texts])
            winning_text = text_counter.most_common(1)[0][0]
            winning_provider = next(p for p, t in texts if t == winning_text)
        else:
            # Long responses - use longest/most detailed
            winning_provider, winning_text = max(texts, key=lambda x: len(x[1]))

        # Return winning response
        for provider_name, response in responses:
            if provider_name == winning_provider:
                self.logger.info(f"MoE: Voting winner = {winning_provider}")
                return self._annotate_response(response, f"moe-voting-{winning_provider}")

        return responses[0][1]

    def _cascade_strategy(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]],
        max_tokens: int,
        temperature: float,
        **kwargs
    ) -> LLMResponse:
        """
        Try providers in order until one succeeds (fallback chain).
        """
        self.logger.info("MoE: Using CASCADE strategy")

        # Try providers in fallback order
        for provider_name in self.fallback_order:
            if provider_name not in self.available_providers:
                continue

            provider = self.providers[provider_name]

            try:
                self.logger.debug(f"MoE: Trying {provider_name}")
                response = provider.create_completion(
                    messages, tools, max_tokens, temperature, **kwargs
                )

                self.logger.info(f"MoE: Cascade success with {provider_name}")
                return self._annotate_response(response, f"moe-cascade-{provider_name}")

            except Exception as e:
                self.logger.warning(f"MoE: {provider_name} failed, trying next: {e}")
                continue

        return self._demo_response("MoE: All providers failed in cascade")

    def _task_based_strategy(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]],
        max_tokens: int,
        temperature: float,
        **kwargs
    ) -> LLMResponse:
        """
        Route to best provider based on task characteristics.

        Analyzes the task/message content and routes to the provider
        best suited for that type of task.
        """
        self.logger.info("MoE: Using TASK_BASED strategy")

        # Extract task text from messages
        task_text = ""
        for msg in messages:
            if isinstance(msg.get("content"), str):
                task_text += msg["content"].lower() + " "

        # Determine best provider based on keywords
        provider_scores = {p: 0 for p in self.available_providers}

        for keyword, preferred_provider in self.specialist_map.items():
            if keyword in task_text and preferred_provider in self.available_providers:
                provider_scores[preferred_provider] += 1

        # Select provider with highest score, or default to first available
        if max(provider_scores.values()) > 0:
            selected_provider = max(provider_scores, key=provider_scores.get)
        else:
            # No keyword match, use first available provider
            selected_provider = self.available_providers[0]

        self.logger.info(f"MoE: Task routed to {selected_provider} (scores: {provider_scores})")

        # Execute with selected provider
        provider = self.providers[selected_provider]

        try:
            response = provider.create_completion(
                messages, tools, max_tokens, temperature, **kwargs
            )
            return self._annotate_response(response, f"moe-taskbased-{selected_provider}")

        except Exception as e:
            self.logger.error(f"MoE: {selected_provider} failed: {e}")
            # Fallback to cascade
            return self._cascade_strategy(messages, tools, max_tokens, temperature, **kwargs)

    def _best_of_n_strategy(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]],
        max_tokens: int,
        temperature: float,
        **kwargs
    ) -> LLMResponse:
        """
        Query N providers in parallel and pick the best response.

        "Best" is determined by response length and stop reason.
        Prefers complete responses over truncated ones.
        """
        self.logger.info("MoE: Using BEST_OF_N strategy")

        responses = []

        # Query all available providers in parallel
        with ThreadPoolExecutor(max_workers=self.parallel_workers) as executor:
            futures = {}

            for provider_name in self.available_providers:
                provider = self.providers[provider_name]
                future = executor.submit(
                    provider.create_completion,
                    messages, tools, max_tokens, temperature, **kwargs
                )
                futures[future] = provider_name

            # Collect responses
            for future in as_completed(futures):
                provider_name = futures[future]
                try:
                    response = future.result(timeout=60)
                    responses.append((provider_name, response))
                except Exception as e:
                    self.logger.error(f"MoE: {provider_name} failed: {e}")

        if not responses:
            return self._demo_response("MoE: All providers failed in best_of_n")

        # Score responses
        def score_response(resp: LLMResponse) -> float:
            score = 0.0

            # Prefer complete responses
            if resp.stop_reason == "end_turn":
                score += 100

            # Prefer longer responses (more detailed)
            total_length = sum(
                len(block.get("text", ""))
                for block in resp.content
                if block.get("type") == "text"
            )
            score += min(total_length / 10, 50)  # Cap at 50 points

            # Prefer responses with tool calls (if tools provided)
            if tools:
                tool_calls = sum(
                    1 for block in resp.content
                    if block.get("type") == "tool_use"
                )
                score += tool_calls * 20

            return score

        # Pick best response
        best_provider, best_response = max(
            responses,
            key=lambda x: score_response(x[1])
        )

        self.logger.info(f"MoE: Best response from {best_provider}")
        return self._annotate_response(best_response, f"moe-bestof-{best_provider}")

    def _specialist_strategy(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]],
        max_tokens: int,
        temperature: float,
        **kwargs
    ) -> LLMResponse:
        """
        Route different tool calls to specialized providers.

        This strategy is useful when different providers excel at different
        types of operations (e.g., DeepSeek for code analysis, Mistral for
        text generation, Claude for reasoning).
        """
        self.logger.info("MoE: Using SPECIALIST strategy")

        # For now, use task-based routing as a proxy for specialist routing
        # In a full implementation, this would:
        # 1. Analyze which tools are likely to be called
        # 2. Route to the best provider for those tools
        # 3. Potentially split the task across multiple providers

        return self._task_based_strategy(messages, tools, max_tokens, temperature, **kwargs)

    def _annotate_response(self, response: LLMResponse, moe_info: str) -> LLMResponse:
        """
        Annotate response with MoE metadata.

        Args:
            response: Original response
            moe_info: MoE strategy info to add

        Returns:
            Annotated response
        """
        # Update model field to include MoE info
        response.model = f"{response.model} (moe: {moe_info})"
        return response

    def is_available(self) -> bool:
        """Check if at least one provider is available."""
        return len(self.available_providers) > 0

    def get_provider_name(self) -> str:
        """Get provider name."""
        return "moe"

    def get_strategy_info(self) -> Dict[str, Any]:
        """
        Get information about MoE configuration.

        Returns:
            Dictionary with MoE configuration details
        """
        return {
            "provider": "moe",
            "strategy": self.strategy,
            "available_providers": self.available_providers,
            "total_providers": len(self.providers),
            "fallback_order": self.fallback_order,
            "specialist_map": self.specialist_map
        }
