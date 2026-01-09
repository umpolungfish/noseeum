"""Base provider interface for LLM integrations."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional


@dataclass
class LLMResponse:
    """
    Standardized response format across all LLM providers.

    This dataclass ensures consistent response handling regardless of
    the underlying provider implementation.
    """
    content: List[Dict[str, Any]] = field(default_factory=list)
    """Content blocks from the response (text, tool_use, etc.)"""

    stop_reason: str = "end_turn"
    """Reason generation stopped (end_turn, tool_use, max_tokens, etc.)"""

    usage: Dict[str, int] = field(default_factory=dict)
    """Token usage statistics (input_tokens, output_tokens, total_tokens)"""

    model: str = ""
    """Model identifier used for this completion"""

    raw_response: Any = None
    """Original provider-specific response object"""


class LLMProvider(ABC):
    """
    Abstract base class for LLM provider implementations.

    All provider implementations must inherit from this class and implement
    the required abstract methods. This ensures a consistent interface across
    different LLM providers (Anthropic, DeepSeek, Mistral, etc.).

    Example:
        class MyProvider(LLMProvider):
            def __init__(self, api_key: str, model: str):
                self.api_key = api_key
                self.model = model

            def create_completion(self, messages, tools=None, **kwargs):
                # Implementation here
                pass

            def is_available(self) -> bool:
                return bool(self.api_key)

            def get_provider_name(self) -> str:
                return "my_provider"
    """

    @abstractmethod
    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Create a completion with the LLM.

        Args:
            messages: List of message dictionaries in standard format:
                     [{"role": "user/assistant", "content": "..."}]
            tools: Optional list of tool definitions in Anthropic format.
                  The provider should convert these to its native format.
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature (0.0 to 1.0)
            **kwargs: Additional provider-specific parameters

        Returns:
            LLMResponse object with standardized response data

        Raises:
            Exception: If API call fails or other errors occur
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if the provider is available and ready to use.

        This typically checks if an API key is present and valid.
        Returns False for demo mode (no API key).

        Returns:
            bool: True if provider is available, False otherwise
        """
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """
        Get the provider name identifier.

        Returns:
            str: Provider name (e.g., "anthropic", "deepseek", "mistral")
        """
        pass

    def _demo_response(self, message: str = "Demo mode - no API call made") -> LLMResponse:
        """
        Create a demo response when API is not available.

        This is used when no API key is present, allowing agents to run
        in demo mode for testing or development.

        Args:
            message: Custom message for demo response

        Returns:
            LLMResponse with demo content
        """
        return LLMResponse(
            content=[{
                "type": "text",
                "text": message
            }],
            stop_reason="end_turn",
            usage={
                "input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0
            },
            model="demo",
            raw_response={"demo_mode": True}
        )
