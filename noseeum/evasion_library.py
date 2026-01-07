"""
Evasion Tactics Library for the noseeum framework.
This module contains advanced strategies for bypassing specific types of analysis.
"""
from typing import Dict, List, Any, Callable
import re
import unicodedata


class EvasionTacticsLibrary:
    """Library of advanced evasion tactics for bypassing analysis tools."""

    def __init__(self):
        self.tactics: Dict[str, Callable] = {
            "avoid_simple_whitespace_detection": self._avoid_simple_whitespace_detection,
            "create_low_entropy_payloads": self._create_low_entropy_payloads,
            "exploit_normalization_gaps": self._exploit_normalization_gaps,
            "bypass_yara_signatures": self._bypass_yara_signatures,
            "yara_resilient_payloads": self._yara_resilient_payloads
        }

    def _avoid_simple_whitespace_detection(self, content: str) -> str:
        """
        Replace simple whitespace-based obfuscation with more complex sequences
        that are less likely to be detected by basic scanners.
        """
        # Replace zero-width space (U+200B) with more complex sequences
        # that achieve similar effects but are less commonly flagged
        replacements = {
            # Instead of simple U+200B, use combinations that are less obvious
            '\u200B': '\u200C\u200D',  # Zero-width non-joiner + joiner
        }

        result = content
        for old, new in replacements.items():
            result = result.replace(old, new)

        return result

    def _create_low_entropy_payloads(self, content: str) -> str:
        """
        Transform content to reduce entropy while preserving functionality.
        This helps bypass entropy-based detection systems.
        """
        # Instead of high-entropy Base64 encoding, use string splitting or shifting
        # This is a simplified example - real implementation would be more complex
        if len(content) > 100:  # Only for larger payloads
            # Split content into chunks and reassemble at runtime
            chunk_size = 10
            chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
            # Return a representation that will be assembled at runtime
            chunk_strings = [f'"{chunk}"' for chunk in chunks]
            return f'eval("".join([{", ".join(chunk_strings)}]))'
        return content

    def _exploit_normalization_gaps(self, content: str) -> str:
        """
        Exploit gaps in Unicode normalization between different analysis tools.
        """
        # Replace characters with their decomposed forms where applicable
        # For example, replace é (U+00E9) with e + combining acute (U+0065 U+0301)
        normalized_content = unicodedata.normalize('NFD', content)
        return normalized_content

    def _bypass_yara_signatures(self, content: str) -> str:
        """
        Modify content to bypass common YARA signature patterns.
        """
        # Avoid non-printable ASCII characters that YARA 4.1+ rejects in string literals
        result = content
        for i, char in enumerate(result):
            if ord(char) < 32 or ord(char) > 126:  # Non-printable ASCII
                # Replace with printable equivalent where possible
                if char == '\t':
                    result = result[:i] + '    ' + result[i+1:]  # Tab to 4 spaces
                elif char == '\n':
                    result = result[:i] + '\\n' + result[i+1:]   # Newline as literal
                elif char == '\r':
                    result = result[:i] + '\\r' + result[i+1:]   # Carriage return as literal
                else:
                    # For other non-printable chars, use Unicode escapes
                    result = result.replace(char, f'\\u{ord(char):04x}')

        return result

    def _yara_resilient_payloads(self, content: str) -> str:
        """
        Create YARA-resilient payloads using advanced techniques.
        """
        from .yara_generator import yara_generator

        # Generate multiple variations of the content using different techniques
        techniques = ["normalization_gap", "printable_ascii", "utf16_like"]

        # Apply the first technique as default
        result = yara_generator.generate_yara_resilient_payload(content, techniques[0])

        # For more advanced protection, we could combine techniques,
        # but for this implementation we'll use the first one
        return result

    def apply_tactic(self, tactic_name: str, content: str) -> str:
        """Apply a specific evasion tactic to the content."""
        if tactic_name in self.tactics:
            return self.tactics[tactic_name](content)
        else:
            raise ValueError(f"Unknown evasion tactic: {tactic_name}")

    def get_available_tactics(self) -> List[str]:
        """Get list of all available evasion tactics."""
        return list(self.tactics.keys())

    def apply_all_tactics(self, content: str) -> str:
        """Apply all available evasion tactics in sequence."""
        result = content
        for tactic_name in self.tactics:
            try:
                result = self.apply_tactic(tactic_name, result)
            except Exception as e:
                print(f"Error applying tactic {tactic_name}: {e}")

        return result


# Global instance of the library
evasion_library = EvasionTacticsLibrary()