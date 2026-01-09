"""DeepSeek API provider implementation."""

import requests
import json
from typing import List, Dict, Any, Optional

from .base_provider import LLMProvider, LLMResponse
from .schema_converter import SchemaConverter
from .message_formatter import MessageFormatter


class DeepSeekProvider(LLMProvider):
    """
    DeepSeek API provider (OpenAI-compatible).

    DeepSeek uses an OpenAI-compatible API endpoint, so we implement
    it using HTTP requests with the requests library.

    Example:
        provider = DeepSeekProvider(api_key="sk-...", model="deepseek-chat")
        response = provider.create_completion(messages=[...], tools=[...])
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "deepseek-chat",
        base_url: str = "https://api.deepseek.com"
    ):
        """
        Initialize DeepSeek provider.

        Args:
            api_key: DeepSeek API key. If None, demo mode is activated.
            model: Model identifier to use (default: deepseek-chat)
            base_url: Base URL for DeepSeek API (default: https://api.deepseek.com)
        """
        self.api_key = api_key
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.endpoint = f"{self.base_url}/v1/chat/completions"

    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Create a completion using DeepSeek API.

        Args:
            messages: List of messages in standard format
            tools: Optional list of tool definitions (in Anthropic format)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional DeepSeek-specific parameters

        Returns:
            LLMResponse with standardized response data

        Raises:
            Exception: If API call fails
        """
        if not self.api_key:
            return self._demo_response("Demo mode - DeepSeek API key not set")

        try:
            # Prepare request headers
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Prepare request payload
            payload = {
                "model": kwargs.get("model", self.model),
                "messages": MessageFormatter.normalize_messages(messages, "deepseek"),
                "max_tokens": max_tokens,
                "temperature": temperature
            }

            # Convert and add tools if provided
            if tools:
                openai_tools = SchemaConverter.to_openai(tools)
                payload["tools"] = openai_tools
                payload["tool_choice"] = kwargs.get("tool_choice", "auto")

            # Add additional parameters
            for key in ["top_p", "frequency_penalty", "presence_penalty", "stop"]:
                if key in kwargs:
                    payload[key] = kwargs[key]

            # Make API request
            response = requests.post(
                self.endpoint,
                headers=headers,
                json=payload,
                timeout=kwargs.get("timeout", 120)
            )

            # Check for errors
            if response.status_code != 200:
                error_msg = f"DeepSeek API error (status {response.status_code}): {response.text}"
                raise Exception(error_msg)

            # Parse response
            response_data = response.json()

            # Convert to standardized response
            return self._convert_response(response_data)

        except requests.exceptions.Timeout:
            raise Exception("DeepSeek API request timed out")
        except requests.exceptions.RequestException as e:
            raise Exception(f"DeepSeek API request error: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"DeepSeek API response parsing error: {e}")
        except Exception as e:
            raise Exception(f"DeepSeek provider error: {e}")

    def is_available(self) -> bool:
        """
        Check if DeepSeek provider is available.

        Returns:
            True if API key is present
        """
        return bool(self.api_key)

    def get_provider_name(self) -> str:
        """
        Get provider name.

        Returns:
            "deepseek"
        """
        return "deepseek"

    def _convert_response(self, response_data: Dict[str, Any]) -> LLMResponse:
        """
        Convert DeepSeek API response to standardized LLMResponse.

        Args:
            response_data: Raw DeepSeek API response (dict)

        Returns:
            Standardized LLMResponse object
        """
        # Extract content blocks
        content_blocks = []

        choices = response_data.get("choices", [])
        if choices:
            message = choices[0].get("message", {})

            # Extract text content
            text_content = message.get("content")
            if text_content:
                content_blocks.append({
                    "type": "text",
                    "text": text_content
                })

            # Extract tool calls
            tool_calls = message.get("tool_calls", [])
            for tc in tool_calls:
                # Parse function arguments
                args_str = tc.get("function", {}).get("arguments", "{}")
                try:
                    args = json.loads(args_str) if isinstance(args_str, str) else args_str
                except json.JSONDecodeError:
                    args = {}

                content_blocks.append({
                    "type": "tool_use",
                    "id": tc.get("id", ""),
                    "name": tc.get("function", {}).get("name", ""),
                    "input": args
                })

        # Extract usage
        usage_data = response_data.get("usage", {})
        usage = {
            "input_tokens": usage_data.get("prompt_tokens", 0),
            "output_tokens": usage_data.get("completion_tokens", 0),
            "total_tokens": usage_data.get("total_tokens", 0)
        }

        # Extract stop reason
        finish_reason = choices[0].get("finish_reason", "stop") if choices else "stop"
        stop_reason_mapping = {
            "stop": "end_turn",
            "tool_calls": "tool_use",
            "length": "max_tokens",
            "content_filter": "content_filter"
        }
        stop_reason = stop_reason_mapping.get(finish_reason, finish_reason)

        # Get model
        model = response_data.get("model", self.model)

        return LLMResponse(
            content=content_blocks,
            stop_reason=stop_reason,
            usage=usage,
            model=model,
            raw_response=response_data
        )
