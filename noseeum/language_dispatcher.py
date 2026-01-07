"""
Language-specific attack dispatcher module for the noseeum framework.
Routes to appropriate language-specific obfuscation modules based on target language.
"""
from typing import List, Dict, Optional
from .engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class LanguageSpecificDispatcherModule(ObfuscationModule):
    """Dispatcher module that routes to appropriate language-specific modules."""

    def __init__(self):
        self.language_modules: Dict[LanguageSupport, ObfuscationModule] = {}
        
    def register_language_module(self, language: LanguageSupport, module: ObfuscationModule):
        """Register a language-specific module for dispatch."""
        self.language_modules[language] = module
        
    def get_name(self) -> str:
        return "Language-Specific Attack Dispatcher"
    
    def get_description(self) -> str:
        return "Routes to appropriate language-specific obfuscation techniques based on target language"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return list(self.language_modules.keys())
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Route to the appropriate language-specific module."""
        module = self.language_modules.get(target_language)
        if not module:
            raise ValueError(f"No language-specific module registered for {target_language}")
            
        return module.obfuscate(content, target_language, **kwargs)


# Create a global instance of the dispatcher
language_dispatcher_module = LanguageSpecificDispatcherModule()