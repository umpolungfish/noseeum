"""
LLM Provider Abstraction Layer for Noseeum Agents.

This module provides a unified interface for integrating multiple LLM providers
(Anthropic Claude, DeepSeek, Mistral AI) into the Noseeum Agent Framework.

Example Usage:
    from agents.llm_providers import LLMProviderFactory

    # Create a provider instance
    provider = LLMProviderFactory.create_provider("deepseek")

    # Make an API call
    response = provider.create_completion(
        messages=[{"role": "user", "content": "Hello!"}]
    )

    # Check response
    for block in response.content:
        if block["type"] == "text":
            print(block["text"])
"""

# Core abstractions
from .base_provider import LLMProvider, LLMResponse

# Provider implementations
from .anthropic_provider import AnthropicProvider
from .deepseek_provider import DeepSeekProvider
from .mistral_provider import MistralProvider
from .moe_provider import MixtureOfExpertsProvider, MoEStrategy

# Factory and utilities
from .factory import LLMProviderFactory
from .schema_converter import SchemaConverter
from .message_formatter import MessageFormatter

__all__ = [
    # Core abstractions
    "LLMProvider",
    "LLMResponse",

    # Provider implementations
    "AnthropicProvider",
    "DeepSeekProvider",
    "MistralProvider",
    "MixtureOfExpertsProvider",
    "MoEStrategy",

    # Factory and utilities
    "LLMProviderFactory",
    "SchemaConverter",
    "MessageFormatter",
]

__version__ = "1.0.0"
