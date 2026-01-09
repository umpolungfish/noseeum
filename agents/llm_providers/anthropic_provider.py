"""Anthropic Claude provider implementation."""

import anthropic
from typing import List, Dict, Any, Optional

from .base_provider import LLMProvider, LLMResponse
from .message_formatter import MessageFormatter


class AnthropicProvider(LLMProvider):
    """
    Anthropic Claude API provider.

    Wraps the existing anthropic SDK to provide a standardized interface
    that matches our LLMProvider abstraction.

    Example:
        provider = AnthropicProvider(api_key="sk-...", model="claude-sonnet-4-5-20250929")
        response = provider.create_completion(messages=[...], tools=[...])
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-5-20250929"):
        """
        Initialize Anthropic provider.

        Args:
            api_key: Anthropic API key. If None, demo mode is activated.
            model: Model identifier to use (default: claude-sonnet-4-5-20250929)
        """
        self.api_key = api_key
        self.model = model
        self.client = anthropic.Anthropic(api_key=api_key) if api_key else None

    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Create a completion using Anthropic Claude API.

        Args:
            messages: List of messages in standard format
            tools: Optional list of tool definitions (in Anthropic format)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional Anthropic-specific parameters

        Returns:
            LLMResponse with standardized response data

        Raises:
            Exception: If API call fails
        """
        if not self.client:
            return self._demo_response("Demo mode - Anthropic API key not set")

        try:
            # Prepare API call kwargs
            api_kwargs = {
                "model": kwargs.get("model", self.model),
                "max_tokens": max_tokens,
                "messages": MessageFormatter.normalize_messages(messages, "anthropic"),
            }

            # Add temperature if not default
            if temperature != 0.7:
                api_kwargs["temperature"] = temperature

            # Add tools if provided
            if tools:
                api_kwargs["tools"] = tools

            # Add any additional kwargs (like system prompt, etc.)
            for key in ["system", "stop_sequences", "top_p", "top_k"]:
                if key in kwargs:
                    api_kwargs[key] = kwargs[key]

            # Make API call
            response = self.client.messages.create(**api_kwargs)

            # Convert to standardized response
            return self._convert_response(response)

        except anthropic.APIError as e:
            raise Exception(f"Anthropic API error: {e}")
        except Exception as e:
            raise Exception(f"Anthropic provider error: {e}")

    def is_available(self) -> bool:
        """
        Check if Anthropic provider is available.

        Returns:
            True if API key is present and client is initialized
        """
        return self.client is not None

    def get_provider_name(self) -> str:
        """
        Get provider name.

        Returns:
            "anthropic"
        """
        return "anthropic"

    def _convert_response(self, response: Any) -> LLMResponse:
        """
        Convert Anthropic API response to standardized LLMResponse.

        Args:
            response: Raw Anthropic API response

        Returns:
            Standardized LLMResponse object
        """
        # Extract content blocks
        content_blocks = []
        if hasattr(response, "content"):
            for block in response.content:
                if hasattr(block, "type"):
                    # Object-based block
                    if block.type == "text":
                        content_blocks.append({
                            "type": "text",
                            "text": block.text
                        })
                    elif block.type == "tool_use":
                        content_blocks.append({
                            "type": "tool_use",
                            "id": block.id,
                            "name": block.name,
                            "input": block.input
                        })
                elif isinstance(block, dict):
                    # Dict-based block
                    content_blocks.append(block)

        # Extract usage
        usage = {}
        if hasattr(response, "usage"):
            usage = {
                "input_tokens": getattr(response.usage, "input_tokens", 0),
                "output_tokens": getattr(response.usage, "output_tokens", 0),
                "total_tokens": (
                    getattr(response.usage, "input_tokens", 0) +
                    getattr(response.usage, "output_tokens", 0)
                )
            }

        # Extract stop reason
        stop_reason = getattr(response, "stop_reason", "end_turn")

        # Get model
        model = getattr(response, "model", self.model)

        return LLMResponse(
            content=content_blocks,
            stop_reason=stop_reason,
            usage=usage,
            model=model,
            raw_response=response
        )
