"""
Language Grammars Database for the noseeum framework.
This module stores detailed information about the lexical and parsing behaviors 
of various programming languages regarding Unicode.
"""
from typing import Dict, Any, List
from enum import Enum
from .engine import LanguageSupport


class UnicodeBehavior(str, Enum):
    """Types of Unicode behavior in programming languages."""
    WHITESPACE = "whitespace"
    IDENTIFIER = "identifier"
    COMMENT = "comment"
    STRING_LITERAL = "string_literal"
    NORMALIZATION = "normalization"


class LanguageGrammarDatabase:
    """Database storing language-specific Unicode behaviors."""
    
    def __init__(self):
        self.grammars: Dict[LanguageSupport, Dict[str, Any]] = {}
        self.keywords: Dict[LanguageSupport, List[str]] = {}
        self._initialize_default_grammars()
        self._initialize_default_keywords()

    def _initialize_default_keywords(self):
        """Initialize default keywords for supported languages."""
        self.keywords[LanguageSupport.PYTHON] = [
            "import", "from", "def", "class", "return", "if", "else", "elif",
            "for", "while", "try", "except", "finally", "with", "as", "pass",
            "continue", "break", "yield", "lambda", "async", "await"
        ]
        self.keywords[LanguageSupport.JAVASCRIPT] = [
            "function", "var", "let", "const", "return", "if", "else", "for",
            "while", "do", "switch", "case", "default", "try", "catch", "finally",
            "class", "extends", "constructor", "this", "import", "export", "from",
            "async", "await", "yield"
        ]
        self.keywords[LanguageSupport.JAVA] = [
            "public", "private", "protected", "static", "final", "class", "interface",
            "extends", "implements", "import", "package", "return", "if", "else",
            "for", "while", "do", "switch", "case", "default", "try", "catch",
            "finally", "throw", "throws", "new", "this", "super"
        ]
        self.keywords[LanguageSupport.GO] = [
            "package", "import", "func", "type", "struct", "interface", "var", "const",
            "return", "if", "else", "for", "range", "switch", "case", "default",
            "defer", "go", "select", "map", "chan", "make", "new"
        ]
        self.keywords[LanguageSupport.KOTLIN] = [
            "fun", "class", "interface", "object", "package", "import", "return",
            "if", "else", "when", "for", "while", "try", "catch", "finally",
            "val", "var", "public", "private", "protected", "internal", "data",
            "sealed", "abstract", "enum", "companion", "inline", "override"
        ]
        self.keywords[LanguageSupport.SWIFT] = [
            "func", "class", "struct", "enum", "protocol", "extension", "import",
            "let", "var", "return", "if", "else", "for", "while", "switch", "case",
            "default", "try", "catch", "throw", "throws", "rethrows", "as", "is",
            "self", "Self", "super", "public", "private", "internal", "fileprivate"
        ]
    
    def _initialize_default_grammars(self):
        """Initialize default grammar information for supported languages."""
        # Go grammar - based on text/scanner package behavior
        self.grammars[LanguageSupport.GO] = {
            "name": "Go",
            "whitespace_chars": [],
            "identifier_chars": ["zero_width_space", "bidirectional_controls", "variation_selectors"],
            "normalization_behavior": "none",  # Go scanner doesn't normalize by default
            "backend_restrictions": [],
            "vulnerabilities": [
                "Configurable scanner (IsIdentRune)",
                "No default normalization",
                "Treats many Unicode chars as non-whitespace"
            ]
        }
        
        # Kotlin grammar
        self.grammars[LanguageSupport.KOTLIN] = {
            "name": "Kotlin",
            "whitespace_chars": [],
            "identifier_chars": ["Lu", "Ll", "Lt", "Lm", "Lo", "Nl", "Nd"],  # Unicode categories
            "normalization_behavior": "standard",
            "backend_restrictions": ["JVM filename limitations", "OS-specific restrictions"],
            "vulnerabilities": [
                "Permissive lexer accepting most Unicode",
                "Backend restrictions via JVM and OS",
                "Backticked identifiers with almost any Unicode"
            ]
        }
        
        # Swift grammar
        self.grammars[LanguageSupport.SWIFT] = {
            "name": "Swift",
            "whitespace_chars": [],
            "identifier_chars": ["unassigned_planes"],  # U+20000–U+2FFFD permitted
            "normalization_behavior": "standard",
            "backend_restrictions": [],
            "vulnerabilities": [
                "Ambiguous identifier/operator head categorization",
                "Permits unassigned planes (U+20000–U+2FFFD)"
            ]
        }
        
        # JavaScript grammar
        self.grammars[LanguageSupport.JAVASCRIPT] = {
            "name": "JavaScript",
            "whitespace_chars": [],
            "identifier_chars": ["all_unicode_categories"],
            "normalization_behavior": "standard",
            "backend_restrictions": [],
            "vulnerabilities": [
                "AST-based analysis vulnerabilities",
                "Entropy-based detection bypass opportunities",
                "Proxy-based payload extraction"
            ]
        }
        
        # Python grammar (existing in the framework)
        self.grammars[LanguageSupport.PYTHON] = {
            "name": "Python",
            "whitespace_chars": [],
            "identifier_chars": ["all_unicode_categories"],
            "normalization_behavior": "standard",
            "backend_restrictions": [],
            "vulnerabilities": [
                "Trojan Source vulnerabilities",
                "Homoglyph substitution",
                "Invisible character encoding"
            ]
        }

        # Java grammar
        self.grammars[LanguageSupport.JAVA] = {
            "name": "Java",
            "whitespace_chars": [],
            "identifier_chars": ["unicode_letters_digits"],
            "normalization_behavior": "none",
            "backend_restrictions": ["JVM bytecode restrictions"],
            "vulnerabilities": [
                "Trojan Source (Bidi) vulnerabilities",
                "Homoglyph substitution in identifiers",
                "Unicode escapes (\\uXXXX) in source code"
            ]
        }

        # Rust grammar
        self.grammars[LanguageSupport.RUST] = {
            "name": "Rust",
            "whitespace_chars": [],
            "identifier_chars": ["XID_Start", "XID_Continue"],
            "normalization_behavior": "nfc",  # Rust uses NFC normalization
            "backend_restrictions": [],
            "vulnerabilities": [
                "Trojan Source vulnerabilities despite warnings",
                "Homoglyph attacks in identifiers",
                "Mixed-script confusables"
            ]
        }

        # C grammar
        self.grammars[LanguageSupport.C] = {
            "name": "C",
            "whitespace_chars": [],
            "identifier_chars": ["ascii_alphanumeric", "underscore"],
            "normalization_behavior": "none",
            "backend_restrictions": ["compiler-specific"],
            "vulnerabilities": [
                "Trigraphs and digraphs (legacy)",
                "Comment injection via Bidi controls",
                "Limited Unicode support (C99+)"
            ]
        }

        # C++ grammar
        self.grammars[LanguageSupport.CPP] = {
            "name": "C++",
            "whitespace_chars": [],
            "identifier_chars": ["ascii_alphanumeric", "underscore", "unicode_c11"],
            "normalization_behavior": "none",
            "backend_restrictions": ["compiler-specific"],
            "vulnerabilities": [
                "Trojan Source (Bidi) vulnerabilities",
                "Comment injection attacks",
                "Universal character names (\\uXXXX, \\UXXXXXXXX)"
            ]
        }

    def add_language(self, language: LanguageSupport, grammar_data: Dict[str, Any]):
        """Add or update grammar information for a language."""
        self.grammars[language] = grammar_data
        
    def get_language_info(self, language: LanguageSupport) -> Dict[str, Any]:
        """Get grammar information for a specific language."""
        return self.grammars.get(language, {})
        
    def get_all_languages(self) -> List[LanguageSupport]:
        """Get list of all supported languages."""
        return list(self.grammars.keys())
        
    def get_vulnerabilities(self, language: LanguageSupport) -> List[str]:
        """Get vulnerability information for a specific language."""
        lang_info = self.get_language_info(language)
        return lang_info.get("vulnerabilities", [])
        
    def get_identifier_chars(self, language: LanguageSupport) -> List[str]:
        """Get identifier character information for a specific language."""
        lang_info = self.get_language_info(language)
        return lang_info.get("identifier_chars", [])

    def get_keywords(self, language: LanguageSupport) -> List[str]:
        """Get keyword information for a specific language."""
        return self.keywords.get(language, [])


# Global instance of the database
grammar_db = LanguageGrammarDatabase()
