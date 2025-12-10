"""
YARA-Resilient Payload Generator for the noseeum framework.
This module crafts payloads that are resilient to YARA detection by exploiting 
Unicode normalization gaps and avoiding non-printable ASCII characters.
"""
from typing import Dict, Any, List
from noseeum.core.evasion_library import evasion_library


class YARAResilientPayloadGenerator:
    """Generator for YARA-resilient payloads."""
    
    def __init__(self):
        self.printable_ascii_range = set(range(32, 127))  # Printable ASCII characters
        
    def generate_yara_resilient_payload(self, original_payload: str, 
                                           technique: str = "normalization_gap") -> str:
        """
        Generate a YARA-resilient version of the payload.
        
        Args:
            original_payload: The original payload to make YARA-resilient
            technique: The evasion technique to use ('normalization_gap', 'printable_ascii', 'utf16_like')
        
        Returns:
            A YARA-resilient version of the payload
        """
        if technique == "normalization_gap":
            return self._exploit_normalization_gaps(original_payload)
        elif technique == "printable_ascii":
            return self._ensure_printable_ascii(original_payload)
        elif technique == "utf16_like":
            return self._create_utf16_like_payload(original_payload)
        else:
            # Default to using the evasion library
            return evasion_library.apply_tactic("bypass_yara_signatures", original_payload)
    
    def _exploit_normalization_gaps(self, payload: str) -> str:
        """
        Exploit normalization gaps where YARA rules might miss equivalent characters.
        For example, é (U+00E9) vs. e + combining acute (U+0065 U+0301).
        """
        import unicodedata
        
        # Convert the payload to decomposed form (NFD) to exploit normalization gaps
        decomposed_payload = unicodedata.normalize('NFD', payload)
        
        # For certain characters, we can create variants that normalize differently
        # This creates a payload that might match different rules depending on normalization
        result = ""
        for char in decomposed_payload:
            codepoint = ord(char)
            
            # For some characters, add variation selectors which normalize differently
            if 0x0300 <= codepoint <= 0x036F:  # Combining Diacritical Marks
                # Add a variation selector to the combining character
                result += char + '\uFE01'  # Variation selector-1
            else:
                result += char
        
        return result
    
    def _ensure_printable_ascii(self, payload: str) -> str:
        """
        Transform the payload to use only printable ASCII characters (32-126).
        This bypasses YARA 4.1+ restrictions on non-printable characters in string literals.
        """
        result = ""
        
        for char in payload:
            codepoint = ord(char)
            
            if codepoint in self.printable_ascii_range:
                # Character is already in printable range
                result += char
            elif codepoint < 32:
                # Control character - convert to escape sequence
                if char == '\t':
                    result += '\\t'
                elif char == '\n':
                    result += '\\n'
                elif char == '\r':
                    result += '\\r'
                else:
                    # Other control characters as hex escapes
                    result += f'\\x{codepoint:02x}'
            elif codepoint > 126:
                # Non-ASCII character - convert to Unicode escape
                if codepoint < 0xFFFF:
                    result += f'\\u{codepoint:04x}'
                else:
                    result += f'\\U{codepoint:08x}'
        
        # Additional step: Ensure any high-entropy sequences are disguised
        # by breaking them into smaller parts
        return self._disguise_high_entropy_sequences(result)
    
    def _create_utf16_like_payload(self, payload: str) -> str:
        """
        Create a payload that looks like UTF-16 but is actually just ASCII characters.
        This exploits YARA's limited Unicode handling.
        """
        # Create a string that looks like UTF-16 with null byte interleaving
        # but is actually just a sequence of printable ASCII characters
        utf16_like = ""
        for i, char in enumerate(payload):
            if i > 0:  # Add a space between characters to make it more 'normal'
                utf16_like += " "
            utf16_like += f"\\u{ord(char):04x}"
        
        return utf16_like
    
    def _disguise_high_entropy_sequences(self, payload: str) -> str:
        """
        Disguise high-entropy sequences that might trigger YARA rules.
        """
        # For longer sequences of hex escapes or other high-entropy content,
        # break them into smaller chunks and join them
        import re
        
        # Look for hex escape sequences
        hex_pattern = r'(?:\\x[0-9a-fA-F]{2}){3,}'  # At least 3 hex escapes in a row
        matches = list(re.finditer(hex_pattern, payload))
        
        # Replace in reverse order to not affect positions of subsequent matches
        result = payload
        for match in reversed(matches):
            start, end = match.span()
            hex_sequence = match.group(0)
            
            # Break the sequence into smaller chunks
            chunk_size = 6  # 3 hex escapes per chunk
            chunks = [hex_sequence[i:i+chunk_size] for i in range(0, len(hex_sequence), chunk_size)]
            
            # Join the chunks with a variable that would be resolved at runtime
            if len(chunks) > 1:
                var_name = f"part{''.join([str(ord(c)) for c in payload[:2]])}"
                var_chunks = [f'"{chunk}"' for chunk in chunks]
                new_sequence = f"({'+'.join(var_chunks)})"
                
                result = result[:start] + new_sequence + result[end:]
        
        return result


# Global instance of the YARA-resilient payload generator
yara_generator = YARAResilientPayloadGenerator()