"""Tool schema format conversion between LLM providers."""

from typing import List, Dict, Any, Optional
import copy


class SchemaConverter:
    """
    Convert tool schemas between different LLM provider formats.

    Anthropic Format (base format):
    {
        "name": "function_name",
        "description": "Function description",
        "input_schema": {
            "type": "object",
            "properties": {...},
            "required": [...]
        }
    }

    OpenAI Format (used by DeepSeek):
    {
        "type": "function",
        "function": {
            "name": "function_name",
            "description": "Function description",
            "parameters": {
                "type": "object",
                "properties": {...},
                "required": [...]
            }
        }
    }

    Mistral Format (similar to OpenAI):
    Same as OpenAI format
    """

    @staticmethod
    def to_anthropic(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert tools to Anthropic format.

        Since Anthropic format is our base format, this is typically a no-op.
        However, if tools are provided in another format, this will convert them.

        Args:
            tools: List of tool definitions (in any format)

        Returns:
            List of tools in Anthropic format
        """
        if not tools:
            return []

        result = []
        for tool in tools:
            # If already in Anthropic format (has input_schema), keep as-is
            if "input_schema" in tool:
                result.append(copy.deepcopy(tool))
            # If in OpenAI format (has function wrapper), convert
            elif "type" in tool and tool["type"] == "function" and "function" in tool:
                func = tool["function"]
                result.append({
                    "name": func["name"],
                    "description": func.get("description", ""),
                    "input_schema": func.get("parameters", {
                        "type": "object",
                        "properties": {},
                        "required": []
                    })
                })
            else:
                # Unknown format, keep as-is
                result.append(copy.deepcopy(tool))

        return result

    @staticmethod
    def to_openai(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert tools to OpenAI format (for DeepSeek).

        Converts Anthropic format tools to OpenAI function calling format.

        Args:
            tools: List of tool definitions in Anthropic format

        Returns:
            List of tools in OpenAI format
        """
        if not tools:
            return []

        result = []
        for tool in tools:
            # If already in OpenAI format, keep as-is
            if "type" in tool and tool["type"] == "function":
                result.append(copy.deepcopy(tool))
                continue

            # Convert from Anthropic format
            if "name" in tool and "input_schema" in tool:
                openai_tool = {
                    "type": "function",
                    "function": {
                        "name": tool["name"],
                        "description": tool.get("description", ""),
                        "parameters": copy.deepcopy(tool["input_schema"])
                    }
                }
                result.append(openai_tool)
            else:
                # Unknown format, try to keep as-is
                result.append(copy.deepcopy(tool))

        return result

    @staticmethod
    def to_mistral(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert tools to Mistral format.

        Mistral uses the same format as OpenAI, so this is effectively
        an alias for to_openai().

        Args:
            tools: List of tool definitions in Anthropic format

        Returns:
            List of tools in Mistral format
        """
        return SchemaConverter.to_openai(tools)

    @staticmethod
    def convert(
        tools: List[Dict[str, Any]],
        target_provider: str
    ) -> List[Dict[str, Any]]:
        """
        Convert tools to the appropriate format for the target provider.

        Args:
            tools: List of tool definitions (in Anthropic format)
            target_provider: Target provider name ("anthropic", "deepseek", "mistral")

        Returns:
            List of tools in the appropriate format

        Raises:
            ValueError: If target_provider is unknown
        """
        if not tools:
            return []

        provider = target_provider.lower()

        if provider == "anthropic":
            return SchemaConverter.to_anthropic(tools)
        elif provider in ["deepseek", "openai"]:
            return SchemaConverter.to_openai(tools)
        elif provider == "mistral":
            return SchemaConverter.to_mistral(tools)
        else:
            # Unknown provider, return as-is (Anthropic format)
            return SchemaConverter.to_anthropic(tools)

    @staticmethod
    def validate_anthropic_schema(tool: Dict[str, Any]) -> bool:
        """
        Validate that a tool definition follows Anthropic format.

        Args:
            tool: Tool definition to validate

        Returns:
            bool: True if valid Anthropic format, False otherwise
        """
        if not isinstance(tool, dict):
            return False

        # Must have name and input_schema
        if "name" not in tool or "input_schema" not in tool:
            return False

        # input_schema must be a dict with type: object
        schema = tool["input_schema"]
        if not isinstance(schema, dict):
            return False

        if schema.get("type") != "object":
            return False

        # Must have properties dict
        if "properties" not in schema or not isinstance(schema["properties"], dict):
            return False

        return True

    @staticmethod
    def validate_openai_schema(tool: Dict[str, Any]) -> bool:
        """
        Validate that a tool definition follows OpenAI format.

        Args:
            tool: Tool definition to validate

        Returns:
            bool: True if valid OpenAI format, False otherwise
        """
        if not isinstance(tool, dict):
            return False

        # Must have type: function
        if tool.get("type") != "function":
            return False

        # Must have function object
        if "function" not in tool or not isinstance(tool["function"], dict):
            return False

        func = tool["function"]

        # Function must have name and parameters
        if "name" not in func:
            return False

        if "parameters" in func:
            params = func["parameters"]
            if not isinstance(params, dict):
                return False
            if params.get("type") != "object":
                return False
            if "properties" not in params:
                return False

        return True
