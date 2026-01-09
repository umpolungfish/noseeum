"""Mistral AI API provider implementation."""

import json
from typing import List, Dict, Any, Optional

from .base_provider import LLMProvider, LLMResponse
from .schema_converter import SchemaConverter
from .message_formatter import MessageFormatter


class MistralProvider(LLMProvider):
    """
    Mistral AI API provider.

    Uses the official mistralai Python SDK to interact with Mistral's API.

    Example:
        provider = MistralProvider(api_key="...", model="mistral-large-latest")
        response = provider.create_completion(messages=[...], tools=[...])
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "mistral-large-latest"):
        """
        Initialize Mistral provider.

        Args:
            api_key: Mistral API key. If None, demo mode is activated.
            model: Model identifier to use (default: mistral-large-latest)
        """
        self.api_key = api_key
        self.model = model
        self.client = None

        # Try to import and initialize Mistral client
        if api_key:
            try:
                from mistralai import Mistral
                self.client = Mistral(api_key=api_key)
            except ImportError:
                # mistralai package not installed
                pass
            except Exception as e:
                # Other initialization errors
                pass

    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Create a completion using Mistral API.

        Args:
            messages: List of messages in standard format
            tools: Optional list of tool definitions (in Anthropic format)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional Mistral-specific parameters

        Returns:
            LLMResponse with standardized response data

        Raises:
            Exception: If API call fails or mistralai package not installed
        """
        if not self.client:
            if not self.api_key:
                return self._demo_response("Demo mode - Mistral API key not set")
            else:
                return self._demo_response(
                    "Mistral provider unavailable - mistralai package not installed. "
                    "Run: pip install mistralai>=1.0.0"
                )

        try:
            # Prepare API call kwargs
            api_kwargs = {
                "model": kwargs.get("model", self.model),
                "messages": MessageFormatter.normalize_messages(messages, "mistral"),
                "max_tokens": max_tokens,
                "temperature": temperature
            }

            # Convert and add tools if provided
            if tools:
                mistral_tools = SchemaConverter.to_mistral(tools)
                api_kwargs["tools"] = mistral_tools
                api_kwargs["tool_choice"] = kwargs.get("tool_choice", "auto")

            # Add additional parameters
            for key in ["top_p", "random_seed", "safe_prompt"]:
                if key in kwargs:
                    api_kwargs[key] = kwargs[key]

            # Make API call
            response = self.client.chat.complete(**api_kwargs)

            # Convert to standardized response
            return self._convert_response(response)

        except ImportError:
            raise Exception("mistralai package not installed. Run: pip install mistralai>=1.0.0")
        except Exception as e:
            raise Exception(f"Mistral provider error: {e}")

    def is_available(self) -> bool:
        """
        Check if Mistral provider is available.

        Returns:
            True if API key is present and client is initialized
        """
        return self.client is not None

    def get_provider_name(self) -> str:
        """
        Get provider name.

        Returns:
            "mistral"
        """
        return "mistral"

    def _convert_response(self, response: Any) -> LLMResponse:
        """
        Convert Mistral API response to standardized LLMResponse.

        Args:
            response: Raw Mistral API response

        Returns:
            Standardized LLMResponse object
        """
        # Extract content blocks
        content_blocks = []

        if hasattr(response, "choices") and len(response.choices) > 0:
            message = response.choices[0].message

            # Extract text content
            if hasattr(message, "content") and message.content:
                content_blocks.append({
                    "type": "text",
                    "text": message.content
                })

            # Extract tool calls
            if hasattr(message, "tool_calls") and message.tool_calls:
                for tc in message.tool_calls:
                    # Parse function arguments
                    args = tc.function.arguments
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except json.JSONDecodeError:
                            args = {}

                    content_blocks.append({
                        "type": "tool_use",
                        "id": getattr(tc, "id", ""),
                        "name": tc.function.name,
                        "input": args
                    })

        # Extract usage
        usage = {}
        if hasattr(response, "usage"):
            usage_obj = response.usage
            usage = {
                "input_tokens": getattr(usage_obj, "prompt_tokens", 0),
                "output_tokens": getattr(usage_obj, "completion_tokens", 0),
                "total_tokens": getattr(usage_obj, "total_tokens", 0)
            }

        # Extract stop reason
        stop_reason = "end_turn"
        if hasattr(response, "choices") and len(response.choices) > 0:
            finish_reason = response.choices[0].finish_reason
            stop_reason_mapping = {
                "stop": "end_turn",
                "tool_calls": "tool_use",
                "length": "max_tokens",
                "model_length": "max_tokens"
            }
            stop_reason = stop_reason_mapping.get(finish_reason, finish_reason)

        # Get model
        model = getattr(response, "model", self.model)

        return LLMResponse(
            content=content_blocks,
            stop_reason=stop_reason,
            usage=usage,
            model=model,
            raw_response=response
        )
