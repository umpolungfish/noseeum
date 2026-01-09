"""Message format standardization across LLM providers."""

from typing import List, Dict, Any, Optional


class MessageFormatter:
    """
    Standardize message formats and extract data from provider responses.

    All providers use a similar message format:
    [{"role": "user/assistant", "content": "..."}]

    However, content structure and tool call handling may vary.
    """

    @staticmethod
    def normalize_messages(
        messages: List[Dict[str, Any]],
        provider: str
    ) -> List[Dict[str, Any]]:
        """
        Ensure messages are in correct format for the target provider.

        Args:
            messages: List of message dictionaries
            provider: Target provider name ("anthropic", "deepseek", "mistral")

        Returns:
            Normalized messages for the provider
        """
        if not messages:
            return []

        provider = provider.lower()
        normalized = []

        for msg in messages:
            if not isinstance(msg, dict):
                continue

            # Ensure role is present
            if "role" not in msg:
                continue

            role = msg["role"]
            content = msg.get("content", "")

            # All providers support basic role/content structure
            normalized_msg = {
                "role": role,
                "content": content
            }

            # Add any additional fields (like tool_calls, tool_use_id, etc.)
            for key, value in msg.items():
                if key not in ["role", "content"]:
                    normalized_msg[key] = value

            normalized.append(normalized_msg)

        return normalized

    @staticmethod
    def extract_text_content(response: Any, provider: str) -> str:
        """
        Extract text content from provider response.

        Args:
            response: Provider-specific response object
            provider: Provider name ("anthropic", "deepseek", "mistral")

        Returns:
            Extracted text content
        """
        provider = provider.lower()

        try:
            if provider == "anthropic":
                # Anthropic: response.content is a list of blocks
                if hasattr(response, "content"):
                    for block in response.content:
                        if hasattr(block, "type") and block.type == "text":
                            return block.text
                        elif isinstance(block, dict) and block.get("type") == "text":
                            return block.get("text", "")
                return ""

            elif provider in ["deepseek", "openai"]:
                # OpenAI format: response.choices[0].message.content
                if hasattr(response, "choices") and len(response.choices) > 0:
                    message = response.choices[0].message
                    if hasattr(message, "content"):
                        return message.content or ""
                elif isinstance(response, dict):
                    # Dict format
                    choices = response.get("choices", [])
                    if choices:
                        content = choices[0].get("message", {}).get("content", "")
                        return content or ""
                return ""

            elif provider == "mistral":
                # Mistral: similar to OpenAI
                if hasattr(response, "choices") and len(response.choices) > 0:
                    message = response.choices[0].message
                    if hasattr(message, "content"):
                        return message.content or ""
                return ""

            else:
                # Unknown provider, try to extract text generically
                if hasattr(response, "content"):
                    return str(response.content)
                return str(response)

        except Exception as e:
            # If extraction fails, return empty string
            return ""

    @staticmethod
    def extract_tool_calls(response: Any, provider: str) -> List[Dict[str, Any]]:
        """
        Extract tool calls from provider response.

        Args:
            response: Provider-specific response object
            provider: Provider name ("anthropic", "deepseek", "mistral")

        Returns:
            List of tool call dictionaries in standardized format:
            [{"id": "...", "type": "tool_use", "name": "...", "input": {...}}]
        """
        provider = provider.lower()
        tool_calls = []

        try:
            if provider == "anthropic":
                # Anthropic: response.content may contain tool_use blocks
                if hasattr(response, "content"):
                    for block in response.content:
                        if hasattr(block, "type") and block.type == "tool_use":
                            tool_calls.append({
                                "id": getattr(block, "id", ""),
                                "type": "tool_use",
                                "name": getattr(block, "name", ""),
                                "input": getattr(block, "input", {})
                            })
                        elif isinstance(block, dict) and block.get("type") == "tool_use":
                            tool_calls.append({
                                "id": block.get("id", ""),
                                "type": "tool_use",
                                "name": block.get("name", ""),
                                "input": block.get("input", {})
                            })

            elif provider in ["deepseek", "openai"]:
                # OpenAI format: response.choices[0].message.tool_calls
                if hasattr(response, "choices") and len(response.choices) > 0:
                    message = response.choices[0].message
                    if hasattr(message, "tool_calls") and message.tool_calls:
                        for tc in message.tool_calls:
                            # Parse function arguments if string
                            args = tc.function.arguments
                            if isinstance(args, str):
                                import json
                                try:
                                    args = json.loads(args)
                                except:
                                    args = {}

                            tool_calls.append({
                                "id": tc.id,
                                "type": "tool_use",
                                "name": tc.function.name,
                                "input": args
                            })
                elif isinstance(response, dict):
                    # Dict format
                    choices = response.get("choices", [])
                    if choices:
                        msg_tool_calls = choices[0].get("message", {}).get("tool_calls", [])
                        for tc in msg_tool_calls:
                            import json
                            args = tc.get("function", {}).get("arguments", {})
                            if isinstance(args, str):
                                try:
                                    args = json.loads(args)
                                except:
                                    args = {}

                            tool_calls.append({
                                "id": tc.get("id", ""),
                                "type": "tool_use",
                                "name": tc.get("function", {}).get("name", ""),
                                "input": args
                            })

            elif provider == "mistral":
                # Mistral: similar to OpenAI
                if hasattr(response, "choices") and len(response.choices) > 0:
                    message = response.choices[0].message
                    if hasattr(message, "tool_calls") and message.tool_calls:
                        for tc in message.tool_calls:
                            args = tc.function.arguments
                            if isinstance(args, str):
                                import json
                                try:
                                    args = json.loads(args)
                                except:
                                    args = {}

                            tool_calls.append({
                                "id": getattr(tc, "id", ""),
                                "type": "tool_use",
                                "name": tc.function.name,
                                "input": args
                            })

        except Exception as e:
            # If extraction fails, return empty list
            pass

        return tool_calls

    @staticmethod
    def get_stop_reason(response: Any, provider: str) -> str:
        """
        Extract stop reason from provider response.

        Args:
            response: Provider-specific response object
            provider: Provider name

        Returns:
            Stop reason string ("end_turn", "tool_use", "max_tokens", etc.)
        """
        provider = provider.lower()

        try:
            if provider == "anthropic":
                if hasattr(response, "stop_reason"):
                    return response.stop_reason
                return "end_turn"

            elif provider in ["deepseek", "openai", "mistral"]:
                if hasattr(response, "choices") and len(response.choices) > 0:
                    finish_reason = response.choices[0].finish_reason
                    # Map OpenAI finish reasons to standardized reasons
                    mapping = {
                        "stop": "end_turn",
                        "tool_calls": "tool_use",
                        "length": "max_tokens",
                        "content_filter": "content_filter"
                    }
                    return mapping.get(finish_reason, finish_reason)
                elif isinstance(response, dict):
                    choices = response.get("choices", [])
                    if choices:
                        finish_reason = choices[0].get("finish_reason", "stop")
                        mapping = {
                            "stop": "end_turn",
                            "tool_calls": "tool_use",
                            "length": "max_tokens",
                            "content_filter": "content_filter"
                        }
                        return mapping.get(finish_reason, finish_reason)
                return "end_turn"

            else:
                return "end_turn"

        except Exception:
            return "end_turn"

    @staticmethod
    def get_usage(response: Any, provider: str) -> Dict[str, int]:
        """
        Extract token usage from provider response.

        Args:
            response: Provider-specific response object
            provider: Provider name

        Returns:
            Usage dictionary with input_tokens, output_tokens, total_tokens
        """
        provider = provider.lower()

        try:
            if provider == "anthropic":
                if hasattr(response, "usage"):
                    usage = response.usage
                    return {
                        "input_tokens": getattr(usage, "input_tokens", 0),
                        "output_tokens": getattr(usage, "output_tokens", 0),
                        "total_tokens": (
                            getattr(usage, "input_tokens", 0) +
                            getattr(usage, "output_tokens", 0)
                        )
                    }

            elif provider in ["deepseek", "openai", "mistral"]:
                if hasattr(response, "usage"):
                    usage = response.usage
                    return {
                        "input_tokens": getattr(usage, "prompt_tokens", 0),
                        "output_tokens": getattr(usage, "completion_tokens", 0),
                        "total_tokens": getattr(usage, "total_tokens", 0)
                    }
                elif isinstance(response, dict):
                    usage = response.get("usage", {})
                    return {
                        "input_tokens": usage.get("prompt_tokens", 0),
                        "output_tokens": usage.get("completion_tokens", 0),
                        "total_tokens": usage.get("total_tokens", 0)
                    }

        except Exception:
            pass

        return {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
