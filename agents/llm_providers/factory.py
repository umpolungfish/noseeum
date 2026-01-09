"""LLM provider factory for instantiation."""

import os
from typing import Optional

from .base_provider import LLMProvider
from .anthropic_provider import AnthropicProvider
from .deepseek_provider import DeepSeekProvider
from .mistral_provider import MistralProvider
from .moe_provider import MixtureOfExpertsProvider, MoEStrategy


class LLMProviderFactory:
    """
    Factory for creating LLM provider instances.

    Handles provider instantiation, API key loading from environment variables,
    and default model selection.

    Example:
        # Create with explicit API key
        provider = LLMProviderFactory.create_provider("deepseek", api_key="sk-...")

        # Create with environment variable
        provider = LLMProviderFactory.create_provider("deepseek")

        # With custom model
        provider = LLMProviderFactory.create_provider("mistral", model="mistral-large-latest")
    """

    # Environment variable mapping
    ENV_VAR_MAP = {
        "anthropic": "ANTHROPIC_API_KEY",
        "deepseek": "DEEPSEEK_API_KEY",
        "mistral": "MISTRAL_API_KEY"
    }

    # Default model mapping
    DEFAULT_MODELS = {
        "anthropic": "claude-sonnet-4-5-20250929",
        "deepseek": "deepseek-chat",
        "mistral": "mistral-large-latest",
        "moe": "mixture-of-experts"
    }

    @staticmethod
    def create_provider(
        provider_name: str,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs
    ) -> LLMProvider:
        """
        Create a provider instance.

        Args:
            provider_name: Provider name ("anthropic", "deepseek", or "mistral")
            api_key: API key. If None, attempts to load from environment variable.
            model: Model identifier. If None, uses provider default.
            **kwargs: Additional provider-specific parameters

        Returns:
            Instantiated LLMProvider subclass

        Raises:
            ValueError: If provider_name is unknown

        Example:
            >>> provider = LLMProviderFactory.create_provider("deepseek")
            >>> provider.is_available()
            True
        """
        provider_name = provider_name.lower()

        # Get API key from environment if not provided
        if api_key is None:
            api_key = LLMProviderFactory._get_api_key_from_env(provider_name)

        # Get default model if not provided
        if model is None:
            model = LLMProviderFactory._get_default_model(provider_name)

        # Create provider instance
        if provider_name == "anthropic":
            return AnthropicProvider(api_key=api_key, model=model)

        elif provider_name == "deepseek":
            base_url = kwargs.get("base_url", "https://api.deepseek.com")
            return DeepSeekProvider(api_key=api_key, model=model, base_url=base_url)

        elif provider_name == "mistral":
            return MistralProvider(api_key=api_key, model=model)

        elif provider_name == "moe":
            # MoE provider configuration from kwargs
            moe_providers = kwargs.get("moe_providers", ["anthropic", "deepseek", "mistral"])
            moe_strategy = kwargs.get("moe_strategy", "task_based")
            fallback_order = kwargs.get("fallback_order")
            specialist_map = kwargs.get("specialist_map")
            voting_threshold = kwargs.get("voting_threshold", 0.5)
            llm_provider_config = kwargs.get("llm_provider_config")

            return MixtureOfExpertsProvider(
                providers=moe_providers,
                strategy=moe_strategy,
                fallback_order=fallback_order,
                specialist_map=specialist_map,
                voting_threshold=voting_threshold,
                llm_provider_config=llm_provider_config
            )

        else:
            raise ValueError(
                f"Unknown provider: {provider_name}. "
                f"Supported providers: {', '.join(LLMProviderFactory.get_supported_providers())}"
            )

    @staticmethod
    def _get_api_key_from_env(provider_name: str) -> Optional[str]:
        """
        Get API key from environment variable for the specified provider.

        Args:
            provider_name: Provider name

        Returns:
            API key from environment, or None if not set
        """
        env_var = LLMProviderFactory.ENV_VAR_MAP.get(provider_name)
        if env_var:
            return os.getenv(env_var)
        return None

    @staticmethod
    def _get_default_model(provider_name: str) -> str:
        """
        Get default model for the specified provider.

        Args:
            provider_name: Provider name

        Returns:
            Default model identifier
        """
        return LLMProviderFactory.DEFAULT_MODELS.get(provider_name, "")

    @staticmethod
    def get_supported_providers() -> list:
        """
        Get list of supported provider names.

        Returns:
            List of supported provider names
        """
        return list(LLMProviderFactory.ENV_VAR_MAP.keys())

    @staticmethod
    def is_provider_available(provider_name: str) -> bool:
        """
        Check if a provider is available (has API key in environment).

        Args:
            provider_name: Provider name to check

        Returns:
            True if API key is present in environment, False otherwise

        Example:
            >>> LLMProviderFactory.is_provider_available("deepseek")
            True
        """
        provider_name = provider_name.lower()
        api_key = LLMProviderFactory._get_api_key_from_env(provider_name)
        return bool(api_key)

    @staticmethod
    def create_from_config(config: dict) -> LLMProvider:
        """
        Create provider from configuration dictionary.

        Args:
            config: Configuration dictionary with keys:
                   - llm_provider: Provider name (default: "anthropic")
                   - api_key: Optional API key override
                   - model: Optional model override
                   - base_url: Optional base URL (for DeepSeek)

        Returns:
            Instantiated LLMProvider

        Example:
            >>> config = {
            ...     "llm_provider": "deepseek",
            ...     "model": "deepseek-chat"
            ... }
            >>> provider = LLMProviderFactory.create_from_config(config)
        """
        provider_name = config.get("llm_provider", "anthropic")
        api_key = config.get("api_key")
        model = config.get("model")

        # Additional provider-specific config
        kwargs = {}
        if provider_name == "deepseek" and "base_url" in config:
            kwargs["base_url"] = config["base_url"]

        return LLMProviderFactory.create_provider(
            provider_name=provider_name,
            api_key=api_key,
            model=model,
            **kwargs
        )
