"""
Linguistic Noise Generator for the noseeum framework.
This module intelligently inserts comments, variable names, and function calls 
that blend in with the surrounding code to provide contextual camouflage.
"""
import random
from typing import Dict, List
from enum import Enum
from .engine import LanguageSupport


class LinguisticNoiseGenerator:
    """Generator for contextual linguistic noise that blends with target code."""
    
    def __init__(self):
        self.language_keywords = {
            LanguageSupport.PYTHON: [
                "import", "from", "def", "class", "return", "if", "else", "elif",
                "for", "while", "try", "except", "finally", "with", "as", "pass",
                "continue", "break", "yield", "lambda", "async", "await"
            ],
            LanguageSupport.JAVASCRIPT: [
                "function", "var", "let", "const", "return", "if", "else", "for",
                "while", "do", "switch", "case", "default", "try", "catch", "finally",
                "class", "extends", "constructor", "this", "import", "export", "from",
                "async", "await", "yield", "const"
            ],
            LanguageSupport.JAVA: [
                "public", "private", "protected", "static", "final", "class", "interface",
                "extends", "implements", "import", "package", "return", "if", "else",
                "for", "while", "do", "switch", "case", "default", "try", "catch",
                "finally", "throw", "throws", "new", "this", "super"
            ],
            LanguageSupport.GO: [
                "package", "import", "func", "type", "struct", "interface", "var", "const",
                "return", "if", "else", "for", "range", "switch", "case", "default",
                "defer", "go", "select", "map", "chan", "make", "new"
            ],
            LanguageSupport.KOTLIN: [
                "fun", "class", "interface", "object", "package", "import", "return",
                "if", "else", "when", "for", "while", "try", "catch", "finally",
                "val", "var", "public", "private", "protected", "internal", "data",
                "sealed", "abstract", "enum", "companion", "inline", "override"
            ],
            LanguageSupport.SWIFT: [
                "func", "class", "struct", "enum", "protocol", "extension", "import",
                "let", "var", "return", "if", "else", "for", "while", "switch", "case",
                "default", "try", "catch", "throw", "throws", "rethrows", "as", "is",
                "self", "Self", "super", "public", "private", "internal", "fileprivate"
            ]
        }
        
        self.language_conventions = {
            LanguageSupport.PYTHON: {
                "naming_style": "snake_case",
                "common_patterns": [
                    "def {name}():",
                    "{name} = value",
                    "class {name}:",
                    "# TODO: {comment}",
                    "# FIXME: {comment}",
                    "# NOTE: {comment}"
                ],
                "typical_comments": [
                    "Initialize the required variables",
                    "Process the input data", 
                    "Perform validation",
                    "Return the processed result",
                    "Handle potential errors",
                    "Optimize for performance"
                ]
            },
            LanguageSupport.JAVASCRIPT: {
                "naming_style": "camelCase",
                "common_patterns": [
                    "function {name}() {{}}",
                    "const {name} = value;",
                    "var {name} = value;", 
                    "let {name} = value;",
                    "// TODO: {comment}",
                    "// FIXME: {comment}"
                ],
                "typical_comments": [
                    "Initialize components",
                    "Process user input",
                    "Handle asynchronous operations",
                    "Format response data",
                    "Validate input parameters",
                    "Update UI elements"
                ]
            },
            LanguageSupport.JAVA: {
                "naming_style": "camelCase",
                "common_patterns": [
                    "public void {name}() {{}}",
                    "private static final {type} {name} = value;",
                    "public class {name} {{}}",
                    "/* TODO: {comment} */",
                    "// TODO: {comment}"
                ],
                "typical_comments": [
                    "Initialize required resources",
                    "Process business logic",
                    "Handle exceptions appropriately",
                    "Return computed result",
                    "Validate method parameters",
                    "Clean up resources"
                ]
            },
            LanguageSupport.GO: {
                "naming_style": "camelCase",
                "common_patterns": [
                    "func {name}() {{}}",
                    "func {name}() {type} {{}}",
                    "var {name} {type} = value",
                    "// TODO: {comment}",
                    "// {comment}"
                ],
                "typical_comments": [
                    "Initialize configuration",
                    "Process the request",
                    "Handle errors gracefully",
                    "Return appropriate response",
                    "Validate input parameters",
                    "Close resources properly"
                ]
            },
            LanguageSupport.KOTLIN: {
                "naming_style": "camelCase",
                "common_patterns": [
                    "fun {name}(): {type} {{}}",
                    "val {name}: {type} = value",
                    "var {name}: {type} = value",
                    "// TODO: {comment}",
                    "/* {comment} */"
                ],
                "typical_comments": [
                    "Initialize dependencies",
                    "Perform data transformation",
                    "Handle coroutine execution",
                    "Validate input values",
                    "Return processed result",
                    "Dispose of resources"
                ]
            },
            LanguageSupport.SWIFT: {
                "naming_style": "camelCase",
                "common_patterns": [
                    "func {name}() -> {type} {{}}",
                    "let {name}: {type} = value",
                    "var {name}: {type} = value",
                    "// TODO: {comment}",
                    "// {comment}"
                ],
                "typical_comments": [
                    "Initialize properties",
                    "Process the input data",
                    "Handle delegate callbacks",
                    "Validate required parameters",
                    "Return formatted result",
                    "Clean up resources"
                ]
            }
        }
    
    def generate_contextual_noise(self, language: LanguageSupport, code_snippet: str = "") -> str:
        """
        Generate contextual noise for the specified language.
        This creates plausible-looking code that blends in with the surrounding context.
        """
        noise_parts = []
        
        # Generate plausible comments
        for _ in range(2):  # Add 2 comment lines
            comment = self._generate_comment(language)
            noise_parts.append(comment)
        
        # Generate plausible variable/function names
        for _ in range(1):  # Add 1 dummy function or variable
            code_line = self._generate_dummy_code(language)
            noise_parts.append(code_line)
        
        # Add a few random language keywords in comments to appear more authentic
        for _ in range(1):
            keyword = random.choice(self.language_keywords.get(language, ["value"]))
            noise_parts.append(f"// {keyword.upper()} handling")
        
        return "\n".join(noise_parts)
    
    def _generate_comment(self, language: LanguageSupport) -> str:
        """Generate a plausible comment for the language."""
        comment_templates = self.language_conventions[language]["typical_comments"]
        
        # Select a random comment template
        template = random.choice(comment_templates)
        
        # Format based on language
        if language == LanguageSupport.PYTHON:
            return f"# {template}"
        elif language in [LanguageSupport.JAVASCRIPT, LanguageSupport.KOTLIN, LanguageSupport.SWIFT]:
            return f"// {template}"
        elif language == LanguageSupport.JAVA:
            return f"/* {template} */"
        elif language == LanguageSupport.GO:
            return f"// {template}"
        else:
            return f"// {template}"
    
    def _generate_dummy_code(self, language: LanguageSupport) -> str:
        """Generate a plausible dummy code line for the language."""
        patterns = self.language_conventions[language]["common_patterns"]
        pattern = random.choice(patterns)
        
        # Generate a name based on language conventions
        name = self._generate_name(language)
        
        # Fill in the pattern
        filled_pattern = pattern.format(
            name=name,
            type=random.choice(['String', 'int', 'bool', 'void', 'Object', 'Any']),
            comment=random.choice(['implementation pending', 'needs review', 'requires testing'])
        )
        
        return filled_pattern
    
    def _generate_name(self, language: LanguageSupport) -> str:
        """Generate a name following the language's naming conventions."""
        naming_style = self.language_conventions[language]["naming_style"]
        
        # Base words to create names from
        words = [
            "process", "handle", "manage", "compute", "calculate", "transform",
            "validate", "verify", "initialize", "setup", "configure", "update",
            "fetch", "retrieve", "store", "save", "delete", "remove", "create",
            "build", "generate", "prepare", "format", "parse", "serialize",
            "deserialize", "encode", "decode", "encrypt", "decrypt", "authenticate",
            "authorize", "validate", "sanitize", "filter", "map", "reduce",
            "find", "search", "sort", "compare", "merge", "split", "join"
        ]
        
        # Select 1-2 random words
        num_words = random.randint(1, 2)
        selected_words = random.choices(words, k=num_words)
        
        if naming_style == "snake_case":
            name = "_".join(selected_words).lower()
        elif naming_style == "camelCase":
            name = selected_words[0].lower() + "".join(word.capitalize() for word in selected_words[1:])
        else:
            name = "_".join(selected_words).lower()  # Default to snake_case
            
        # Add a random number to avoid conflicts
        name += str(random.randint(10, 99))
        
        return name


# Global instance of the generator
linguistic_generator = LinguisticNoiseGenerator()