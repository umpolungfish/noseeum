"""
Core Obfuscation Engine for the noseeum framework.
This module provides the foundational architecture for modular obfuscation techniques.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from enum import Enum
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ObfuscationTechnique(str, Enum):
    """Enumeration of supported obfuscation techniques."""
    BIDI = "bidi"
    HOMOGLYPH = "homoglyph"
    INVISIBLE = "invisible"
    LANGUAGE_SPECIFIC = "language_specific"
    NORMALIZATION = "normalization"
    UNASSIGNED_PLANES = "unassigned_planes"
    PAYLOAD_INJECTION = "payload_injection"
    HANGUL_ENCODING = "hangul_encoding"


class LanguageSupport(str, Enum):
    """Enumeration of supported programming languages."""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    JAVA = "java"
    GO = "go"
    KOTLIN = "kotlin"
    SWIFT = "swift"
    RUST = "rust"
    C = "c"
    CPP = "cpp"


class ObfuscationModule(ABC):
    """Abstract base class for all obfuscation modules."""
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the obfuscation technique."""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Return the description of the obfuscation technique."""
        pass
    
    @abstractmethod
    def get_supported_languages(self) -> List[LanguageSupport]:
        """Return the list of supported languages."""
        pass
    
    @abstractmethod
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply the obfuscation technique to the given content."""
        pass


class ObfuscationEngine:
    """Core engine to orchestrate different obfuscation modules."""
    
    def __init__(self):
        self.modules: Dict[ObfuscationTechnique, ObfuscationModule] = {}
        self.language_grammars: Dict[LanguageSupport, Dict[str, Any]] = {}
        
    def register_module(self, technique: ObfuscationTechnique, module: ObfuscationModule):
        """Register a new obfuscation module."""
        self.modules[technique] = module
        logger.info(f"Registered obfuscation module: {module.get_name()}")
    
    def get_module(self, technique: ObfuscationTechnique) -> Optional[ObfuscationModule]:
        """Get a registered obfuscation module."""
        return self.modules.get(technique)
    
    def get_all_modules(self) -> Dict[ObfuscationTechnique, ObfuscationModule]:
        """Get all registered obfuscation modules."""
        return self.modules
    
    def apply_obfuscation(self, content: str, technique: ObfuscationTechnique, 
                         target_language: LanguageSupport, **kwargs) -> str:
        """Apply a specific obfuscation technique to content."""
        module = self.get_module(technique)
        if not module:
            raise ValueError(f"Unknown obfuscation technique: {technique}")
            
        if target_language not in module.get_supported_languages():
            raise ValueError(f"Language {target_language} not supported by {technique}")
            
        logger.info(f"Applying {technique} obfuscation to content for {target_language}")
        return module.obfuscate(content, target_language, **kwargs)
    
    def register_language_grammar(self, language: LanguageSupport, grammar_data: Dict[str, Any]):
        """Register language-specific grammar information."""
        self.language_grammars[language] = grammar_data
        logger.info(f"Registered grammar for language: {language}")
    
    def get_language_grammar(self, language: LanguageSupport) -> Optional[Dict[str, Any]]:
        """Get language-specific grammar information."""
        return self.language_grammars.get(language)


# Global instance of the engine
engine = ObfuscationEngine()