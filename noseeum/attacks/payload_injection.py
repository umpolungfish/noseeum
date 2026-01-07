"""
Payload Injection via Identifier Characters Module for the noseeum framework.
This module encodes malicious data within language constructs like object properties, class names, or function names.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class PayloadInjectionModule(ObfuscationModule):
    """Module for encoding malicious data within identifiers using visually distinct Unicode characters."""
    
    def get_name(self) -> str:
        return "Payload Injection via Identifier Characters"
    
    def get_description(self) -> str:
        return "Encodes malicious data within language constructs like object properties, class names, or function names using visually distinct but valid Unicode characters"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.JAVASCRIPT, LanguageSupport.JAVA, LanguageSupport.CPP, 
                LanguageSupport.PYTHON, LanguageSupport.GO, LanguageSupport.SWIFT]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply payload injection obfuscation to content."""
        import re
        import base64
        
        # For JavaScript, implement the Hangul-based payload injection technique
        if target_language == LanguageSupport.JAVASCRIPT:
            # This mimics the JavaScript phishing kit technique using Hangul characters
            # The payload is stored as property names in object literals and extracted via Proxy
            
            # First, let's identify code that might contain payloads
            # For this example, we'll look for string literals that might be malicious
            string_pattern = r'(["\'])(.*?)(\1)'
            matches = re.finditer(string_pattern, content)
            
            result = content
            for match in reversed(list(matches)):
                start, end = match.span()
                full_match = match.group(0)
                quote_char = match.group(1)
                string_content = match.group(2)
                
                # Encode the original content using Hangul characters
                # U+FFA0 is a Hangul half-width character, U+3164 is a Hangul fill character
                # These can be used to encode payload data
                encoded_parts = []
                for char in string_content:
                    # Convert character to its codepoint and represent using Hangul characters
                    codepoint = ord(char)
                    
                    # Use a mapping to Hangul characters to encode the payload
                    # This is a simplified version of the technique
                    hangul_encoded = self._encode_to_hangul(codepoint)
                    encoded_parts.append(hangul_encoded)
                
                # Join the encoded parts
                encoded_payload = "".join(encoded_parts)
                
                # Create a new representation that uses the Hangul encoding
                # This is a simplification of how the Proxy would decode it
                new_string = f"`/*HANGUL_ENCODED:{encoded_payload}*/`"
                
                # Replace in the result
                result = result[:start] + new_string + result[end:]
                
            # Add a Proxy or other decoding mechanism
            proxy_code = """
// Proxy to decode Hangul-encoded payload
const hangulDecoder = new Proxy({}, {
  get: function(target, prop) {
    // Decoding logic would go here
    if (prop.startsWith('U+')) {
      // Convert Hangul characters back to original
      return decodeHangulPayload(prop);
    }
    return target[prop];
  }
});
"""
            result = proxy_code + "\n" + result
            
        elif target_language == LanguageSupport.JAVA:
            # In Java, embed payload in class names or method names using valid identifiers
            # Use the same Hangul encoding technique for class name obfuscation
            class_pattern = r'(class\s+)([A-Za-z_][A-Za-z0-9_]*)'
            matches = re.finditer(class_pattern, content)
            
            result = content
            for match in reversed(list(matches)):
                start, end = match.span()
                full_match = match.group(0)
                class_keyword = match.group(1)
                class_name = match.group(2)
                
                # Encode part of the payload in the class name using Hangul characters
                if len(class_name) > 2:
                    prefix = class_name[:2]
                    suffix = class_name[2:]
                    
                    # Encode the suffix in Hangul characters
                    encoded_suffix = self._encode_to_hangul_text(suffix)
                    
                    new_class_name = f"{prefix}{encoded_suffix}"
                    new_string = f"{class_keyword}{new_class_name}"
                    
                    # Replace in the result
                    result = result[:start] + new_string + result[end:]
            
        elif target_language == LanguageSupport.CPP:
            # In C++, use namespace names or class names to encode payload data
            namespace_pattern = r'(namespace\s+)([A-Za-z_][A-Za-z0-9_]*)'
            matches = re.finditer(namespace_pattern, content)
            
            result = content
            for match in reversed(list(matches)):
                start, end = match.span()
                full_match = match.group(0)
                ns_keyword = match.group(1)
                ns_name = match.group(2)
                
                # Encode part of the payload in the namespace name
                if len(ns_name) > 2:
                    prefix = ns_name[:2]
                    suffix = ns_name[2:]
                    
                    # Encode the suffix in Hangul characters
                    encoded_suffix = self._encode_to_hangul_text(suffix)
                    
                    new_ns_name = f"{prefix}{encoded_suffix}"
                    new_string = f"{ns_keyword}{new_ns_name}"
                    
                    # Replace in the result
                    result = result[:start] + new_string + result[end:]
        
        else:
            # For other languages, use a generic approach
            # Insert payload data within identifiers using default-ignorable characters
            identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
            identifiers = re.findall(identifier_pattern, content)
            
            result = content
            for identifier in identifiers[:5]:  # Only modify first 5 identifiers
                # Add payload data using variation selectors
                payload_data = kwargs.get('payload_data', 'malicious_payload')
                encoded_payload = self._encode_to_hangul_text(payload_data[:3])  # Small payload for demo
                modified_identifier = f"{identifier}{encoded_payload}"
                
                # Replace only the specific instance of the identifier
                result = re.sub(rf'\b{re.escape(identifier)}\b', modified_identifier, result, count=1)
        
        return result
    
    def _encode_to_hangul(self, codepoint: int) -> str:
        """Encode a character codepoint using Hangul characters."""
        # Map the codepoint to Hangul characters
        # This is a simplified implementation of the encoding
        # In a real implementation, we'd use a more sophisticated mapping
        
        # Use Hangul half-width (U+FFA0) and full-width (U+3164) characters
        base_hangul = 0xFFA0  # Hangul half-width
        offset = codepoint % 128  # Keep it within a reasonable range
        
        # Convert to a Hangul character
        hangul_char = chr(base_hangul + offset)
        return hangul_char
    
    def _encode_to_hangul_text(self, text: str) -> str:
        """Encode text using Hangul characters."""
        result = ""
        for char in text:
            codepoint = ord(char)
            result += self._encode_to_hangul(codepoint)
        return result


# Create an instance of the module
payload_injection_module = PayloadInjectionModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
@click.option('--language', default='javascript', type=click.Choice(['python', 'javascript', 'java', 'go', 'kotlin', 'swift', 'rust', 'c', 'cpp']), 
              help='Target programming language.')
@click.option('--payload-data', default='malicious_payload', help='Data to encode in the payload.')
def payload_injection(input_file: str, output_file: str, language: str, payload_data: str) -> None:
    """
    Apply payload injection obfuscation to a file.
    Encodes malicious data within language constructs using visually distinct Unicode characters.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply payload injection obfuscation
    target_lang = LanguageSupport(language)
    result = engine.apply_obfuscation(
        content, 
        ObfuscationTechnique.PAYLOAD_INJECTION, 
        target_lang,
        payload_data=payload_data
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Payload injection obfuscation applied to {input_file} -> {output_file}")