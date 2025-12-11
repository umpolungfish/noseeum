"""
Configuration management for the Noseeum framework.
"""
import json
import os
import click
from typing import Dict, Any, Optional
try:
    # For Python 3.9+
    from importlib.resources import files
except ImportError:
    # For older Python versions
    from importlib_resources import files

# Default configuration values
DEFAULT_CONFIG = {
    'registry_path': None,  # Will be determined dynamically
    'nfkc_map_path': None,  # Will be determined dynamically
    'default_encoding': 'utf-8',
    'detector_confusable_scripts': [
        'LATIN', 'CYRILLIC', 'GREEK', 'ARMENIAN', 'HEBREW', 'ARABIC', 'SYRIAC',
        'THAANA', 'NKO', 'SAMARITAN', 'MANDAIC', 'ARABIC_MATH', 'ARABIC_EXTENDED_A',
        'GEORGIAN', 'HANGUL', 'HAN', 'HIRAGANA', 'KATAKANA', 'BOPOMOFO',
        'DEVANAGARI', 'BENGALI', 'GURMUKHI', 'GUJARATI', 'ORIYA', 'TAMIL',
        'TELUGU', 'KANNADA', 'MALAYALAM', 'SINHALA', 'THAI', 'LAO', 'TIBETAN',
        'MYANMAR', 'GEORGIAN', 'ETHIOPIC', 'CHEROKEE', 'CANADIAN_ABORIGINAL',
        'OGHAM', 'RUNIC', 'TAGALOG', 'HANUNOO', 'BUHID', 'TAGBANWA', 'KHMER',
        'MONGOLIAN', 'LIMBU', 'TAI_LE', 'NEW_TAI_LUE', 'BUGINESE', 'TAI_THAM',
        'BALINESE', 'SUNDANESE', 'LEPCHA', 'OL_CHIKI', 'MALAYALAM_ARABIC',
        'VEDIC_EXTENSIONS', 'LISU', 'VAI', 'CYRILLIC_EXTENDED_A', 'CYRILLIC_EXTENDED_B',
        'BAMUM', 'MODIFIER_TONE_LETTERS', 'LATIN_EXTENDED_D', 'SYLOTI_NAGRI',
        'COMMON', 'INHERITED'
    ]
}

class ConfigManager:
    """
    Manages configuration for the Noseeum framework.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the configuration manager.
        
        Args:
            config_path: Optional path to a custom configuration file
        """
        self.config_path = config_path or 'config.json'
        self.config = DEFAULT_CONFIG.copy()
        
        # Load configuration from file if it exists
        if os.path.exists(self.config_path):
            self.load_config()
    
    def load_config(self) -> bool:
        """
        Load configuration from the configuration file.
        
        Returns:
            True if configuration was loaded successfully, False otherwise
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                file_config = json.load(f)
                # Update default config with values from file
                self.config.update(file_config)
            return True
        except (IOError, json.JSONDecodeError, ValueError) as e:
            click.echo(f"Warning: Could not load configuration from '{self.config_path}': {e}", err=True)
            return False
    
    def save_config(self) -> bool:
        """
        Save current configuration to the configuration file.
        
        Returns:
            True if configuration was saved successfully, False otherwise
        """
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
            return True
        except (IOError, ValueError) as e:
            click.echo(f"Error: Could not save configuration to '{self.config_path}': {e}", err=True)
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: The configuration key
            default: Default value to return if key is not found
            
        Returns:
            The configuration value or the default value
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        
        Args:
            key: The configuration key
            value: The value to set
        """
        self.config[key] = value


# Global configuration manager instance
_config_manager: Optional[ConfigManager] = None


def get_config_manager() -> ConfigManager:
    """
    Get the global configuration manager instance.
    
    Returns:
        The configuration manager instance
    """
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager


def get_config(key: str, default: Any = None) -> Any:
    """
    Get a configuration value from the global configuration manager.

    Args:
        key: The configuration key
        default: Default value to return if key is not found

    Returns:
        The configuration value or the default value
    """
    config_manager = get_config_manager()

    # Special handling for data file paths to use package resources
    if key == 'registry_path':
        if config_manager.get('registry_path') is None:
            try:
                # Try to access the file within the package
                from importlib.resources import files
            except ImportError:
                from importlib_resources import files
            return str(files('noseeum').joinpath('homoglyph_registry.json'))
        else:
            return config_manager.get(key, default)
    elif key == 'nfkc_map_path':
        if config_manager.get('nfkc_map_path') is None:
            try:
                # Try to access the file within the package
                from importlib.resources import files
            except ImportError:
                from importlib_resources import files
            return str(files('noseeum').joinpath('nfkc_map.json'))
        else:
            return config_manager.get(key, default)

    return config_manager.get(key, default)