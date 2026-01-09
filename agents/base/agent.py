"""Base agent class for all noseeum agents."""

import os
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Any, Optional
from datetime import datetime
import anthropic


class AgentStatus(Enum):
    """Agent execution status."""
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"


class AgentCapability(Enum):
    """Agent capabilities."""
    RESEARCH = "research"
    ATTACK_DEV = "attack_development"
    DEFENSE = "defense"
    ANALYSIS = "analysis"
    TESTING = "testing"
    DOCUMENTATION = "documentation"


class BaseAgent(ABC):
    """Base class for all noseeum agents."""

    def __init__(self, agent_id: str, name: str, description: str,
                 capabilities: List[AgentCapability], config: Dict[str, Any]):
        """
        Initialize base agent.

        Args:
            agent_id: Unique identifier for agent
            name: Human-readable agent name
            description: Agent description
            capabilities: List of agent capabilities
            config: Agent configuration dictionary
        """
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.capabilities = capabilities
        self.config = config
        self.status = AgentStatus.IDLE
        self.logger = self._setup_logger()

        # NEW: Set up LLM provider (unified interface)
        self.provider = self._setup_llm_provider()

        # KEEP: For backward compatibility
        self.client = self._setup_anthropic_client()

        self.memory: Dict[str, Any] = {}
        self.results: List[Dict[str, Any]] = []
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def _setup_logger(self) -> logging.Logger:
        """Set up agent logger."""
        # Get log level from config, default to DEBUG for verbose output
        log_level_str = self.config.get('log_level', 'DEBUG')
        log_level = getattr(logging, log_level_str.upper(), logging.DEBUG)

        logger = logging.getLogger(f"noseeum.agent.{self.agent_id}")
        logger.setLevel(log_level)

        # Console handler - use the same level as configured
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter(
            f'[%(asctime)s] [{self.name}] %(levelname)s: %(message)s'
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler
        os.makedirs("agents/logs", exist_ok=True)
        file_handler = logging.FileHandler(f"agents/logs/{self.agent_id}.log")
        file_handler.setLevel(logging.DEBUG)  # Always log DEBUG to file for detailed records
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    def _setup_anthropic_client(self) -> anthropic.Anthropic:
        """Set up Anthropic API client."""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            self.logger.warning("ANTHROPIC_API_KEY not set, using demo mode")
            return None
        return anthropic.Anthropic(api_key=api_key)

    def _setup_llm_provider(self):
        """
        Set up LLM provider based on configuration.

        Returns:
            LLMProvider instance
        """
        try:
            from agents.llm_providers.factory import LLMProviderFactory

            provider_name = self.config.get('llm_provider', 'anthropic')
            api_key = self.config.get('api_key')  # Optional override
            model = self.config.get('model')

            # Collect additional provider-specific kwargs
            kwargs = {}

            # MoE-specific configuration
            if provider_name == 'moe':
                kwargs['moe_providers'] = self.config.get('moe_providers', ['anthropic', 'deepseek', 'mistral'])
                kwargs['moe_strategy'] = self.config.get('moe_strategy', 'task_based')
                kwargs['fallback_order'] = self.config.get('fallback_order')
                kwargs['specialist_map'] = self.config.get('specialist_map')
                kwargs['voting_threshold'] = self.config.get('voting_threshold', 0.5)
                # Pass the full llm_provider config so MoE can extract API keys for sub-providers
                kwargs['llm_provider_config'] = self.config.get('llm_provider_config')

            # DeepSeek-specific configuration
            if provider_name == 'deepseek' and 'base_url' in self.config:
                kwargs['base_url'] = self.config['base_url']

            provider = LLMProviderFactory.create_provider(
                provider_name=provider_name,
                api_key=api_key,
                model=model,
                **kwargs
            )

            if provider.is_available():
                self.logger.info(
                    f"Using {provider_name} provider with model {getattr(provider, 'model', 'unknown')}"
                )
            else:
                self.logger.warning(
                    f"{provider_name} provider not available (demo mode)"
                )

            return provider

        except Exception as e:
            self.logger.error(f"Failed to setup provider: {e}")
            self.logger.warning("Falling back to Anthropic provider")
            # Fallback to Anthropic
            from agents.llm_providers.factory import LLMProviderFactory
            return LLMProviderFactory.create_provider("anthropic")

    @abstractmethod
    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute agent task.

        Args:
            task: Task description
            context: Optional context dictionary

        Returns:
            Result dictionary
        """
        pass

    @abstractmethod
    def get_tools(self) -> List[Dict[str, Any]]:
        """
        Get agent-specific tools.

        Returns:
            List of tool definitions for Claude API
        """
        pass

    def start(self):
        """Start agent execution."""
        self.status = AgentStatus.RUNNING
        self.start_time = datetime.now()
        self.logger.info(f"Agent {self.name} started")

    def complete(self, result: Dict[str, Any]):
        """Mark agent as completed."""
        self.status = AgentStatus.COMPLETED
        self.end_time = datetime.now()
        self.results.append(result)
        duration = (self.end_time - self.start_time).total_seconds()
        self.logger.info(f"Agent {self.name} completed in {duration:.2f}s")

    def fail(self, error: str):
        """Mark agent as failed."""
        self.status = AgentStatus.FAILED
        self.end_time = datetime.now()
        self.logger.error(f"Agent {self.name} failed: {error}")

    def pause(self):
        """Pause agent execution."""
        self.status = AgentStatus.PAUSED
        self.logger.info(f"Agent {self.name} paused")

    def resume(self):
        """Resume agent execution."""
        self.status = AgentStatus.RUNNING
        self.logger.info(f"Agent {self.name} resumed")

    def save_artifact(self, artifact_name: str, content: Any,
                      artifact_type: str = "text") -> str:
        """
        Save agent artifact.

        Args:
            artifact_name: Name of artifact
            content: Artifact content
            artifact_type: Type of artifact (text, json, binary)

        Returns:
            Path to saved artifact
        """
        os.makedirs("agents/artifacts", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.agent_id}_{artifact_name}_{timestamp}"

        if artifact_type == "json":
            import json
            filepath = f"agents/artifacts/{filename}.json"
            with open(filepath, 'w') as f:
                json.dump(content, f, indent=2)
        elif artifact_type == "binary":
            filepath = f"agents/artifacts/{filename}.bin"
            with open(filepath, 'wb') as f:
                f.write(content)
        else:
            filepath = f"agents/artifacts/{filename}.txt"
            with open(filepath, 'w') as f:
                f.write(str(content))

        self.logger.info(f"Artifact saved: {filepath}")
        return filepath

    def store_in_memory(self, key: str, value: Any):
        """Store data in agent memory."""
        self.memory[key] = value
        self.logger.debug(f"Stored in memory: {key}")

    def retrieve_from_memory(self, key: str) -> Optional[Any]:
        """Retrieve data from agent memory."""
        return self.memory.get(key)

    def _extract_from_context(self, context: Optional[Dict[str, Any]],
                               key: str, default: Any = None) -> Any:
        """
        Intelligently extract data from context, handling various formats.

        Supports:
        - Direct key access: context.get(key)
        - Agent output format: detects previous agent outputs and extracts relevant data
        - Nested structures: searches within arrays and objects

        Args:
            context: Context dictionary (may be None)
            key: Key to extract
            default: Default value if not found

        Returns:
            Extracted value or default
        """
        if not context:
            return default

        # Direct access first (most common case)
        if key in context:
            return context[key]

        # Handle agent output formats
        # Check if this is output from unicode_archaeologist
        if "findings" in context and isinstance(context["findings"], list):
            if key == "language":
                # Try to infer from findings
                for finding in context["findings"]:
                    if finding.get("type") == "language_quirk":
                        return finding.get("language", default)
                return "python"  # Default for unicode research
            elif key == "attack_type":
                # Infer from CVE data
                for finding in context["findings"]:
                    if finding.get("type") == "cve_research":
                        cves = finding.get("cves", [])
                        for cve in cves:
                            if "bidirectional" in cve.get("description", "").lower():
                                return "bidi"
                            elif "homoglyph" in cve.get("description", "").lower():
                                return "homoglyph"
                return "bidi"  # Default from unicode research
            elif key == "suspicious_chars" or key == "unicode_chars":
                # Extract all suspicious characters
                chars = []
                for finding in context["findings"]:
                    if "suspicious_chars" in finding:
                        chars.extend(finding["suspicious_chars"])
                return chars if chars else default

        # Check if this is output from payload_artisan
        if "payloads" in context and isinstance(context["payloads"], list):
            if key == "attack" or key == "payload":
                # Get the first payload
                payloads = context["payloads"]
                if payloads:
                    return payloads[0].get("payload", default)
            elif key == "language":
                payloads = context["payloads"]
                if payloads:
                    return payloads[0].get("language", "python")
            elif key == "attack_type":
                payloads = context["payloads"]
                if payloads:
                    return payloads[0].get("attack_type", "bidi")

        # Check if this is output from red_team_validator
        if "test_results" in context:
            if key == "validation_results" or key == "test_results":
                return context["test_results"]
            elif key == "effectiveness_score":
                return context.get("effectiveness_score", default)

        return default

    def get_status_report(self) -> Dict[str, Any]:
        """Get agent status report."""
        duration = None
        if self.start_time:
            end = self.end_time or datetime.now()
            duration = (end - self.start_time).total_seconds()

        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "status": self.status.value,
            "capabilities": [c.value for c in self.capabilities],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "duration_seconds": duration,
            "results_count": len(self.results),
            "memory_size": len(self.memory),
        }

    def call_llm(self, messages: List[Dict[str, Any]],
                 tools: Optional[List[Dict[str, Any]]] = None,
                 max_tokens: int = 4000,
                 **kwargs):
        """
        Call LLM provider with messages and tools (provider-agnostic).

        This is the recommended method for making LLM calls. It works with
        any configured provider (Anthropic, DeepSeek, Mistral).

        Args:
            messages: List of message dictionaries
            tools: Optional list of tool definitions (in Anthropic format)
            max_tokens: Maximum tokens in response
            **kwargs: Additional provider-specific parameters

        Returns:
            LLMResponse object with standardized response data

        Example:
            response = self.call_llm(
                messages=[{"role": "user", "content": "Hello"}],
                tools=self.get_tools()
            )

            for block in response.content:
                if block["type"] == "text":
                    print(block["text"])
        """
        if not self.provider:
            self.logger.warning("LLM provider not available (demo mode)")
            from agents.llm_providers.base_provider import LLMResponse
            return LLMResponse(
                content=[{"type": "text", "text": "Demo mode - no API call made"}],
                stop_reason="end_turn",
                usage={"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
                model="demo",
                raw_response=None
            )

        try:
            response = self.provider.create_completion(
                messages=messages,
                tools=tools,
                max_tokens=max_tokens,
                **kwargs
            )

            self.logger.debug(
                f"LLM call completed: {response.usage.get('total_tokens', 0)} tokens used"
            )

            return response

        except Exception as e:
            self.logger.error(f"LLM API call failed: {e}")
            raise

    def call_claude(self, messages: List[Dict[str, Any]],
                    tools: Optional[List[Dict[str, Any]]] = None,
                    max_tokens: int = 4000) -> Any:
        """
        Call Claude API with messages and tools.

        DEPRECATED: This method is maintained for backward compatibility.
        New code should use call_llm() for provider-agnostic calls.

        Args:
            messages: List of message dictionaries
            tools: Optional list of tool definitions
            max_tokens: Maximum tokens in response

        Returns:
            API response (provider-specific format)
        """
        # Use provider abstraction if available
        if hasattr(self, 'provider') and self.provider:
            provider_name = self.provider.get_provider_name()

            # If using Anthropic provider, return native response
            if provider_name == "anthropic":
                response = self.call_llm(messages, tools, max_tokens)
                return response.raw_response

            # For other providers, warn and return raw response
            self.logger.warning(
                f"call_claude() called with {provider_name} provider. "
                "Consider using call_llm() for provider-agnostic code."
            )
            response = self.call_llm(messages, tools, max_tokens)
            return response.raw_response

        # Fallback to old implementation if provider not set up
        if not self.client:
            self.logger.warning("Claude API client not available (demo mode)")
            return {"type": "text", "text": "Demo mode - no API call made"}

        try:
            kwargs = {
                "model": self.config.get("model", "claude-sonnet-4-5-20250929"),
                "max_tokens": max_tokens,
                "messages": messages,
            }

            if tools:
                kwargs["tools"] = tools

            response = self.client.messages.create(**kwargs)
            return response
        except Exception as e:
            self.logger.error(f"Claude API call failed: {e}")
            raise
