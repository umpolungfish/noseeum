"""
Hangul Encoding Module for the noseeum framework.
This module implements the JavaScript phishing kit technique using Hangul characters to encode payloads.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class HangulEncodingModule(ObfuscationModule):
    """Module for encoding payloads using Hangul half-width and full-width characters."""
    
    def get_name(self) -> str:
        return "Hangul Encoding"
    
    def get_description(self) -> str:
        return "Implements JavaScript phishing kit technique using Hangul half-width (U+FFA0) and full-width (U+3164) characters to encode payloads"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.JAVASCRIPT, LanguageSupport.PYTHON, LanguageSupport.JAVA, LanguageSupport.GO]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply Hangul-based encoding to content."""
        import re
        import base64
        
        result = content
        
        if target_language == LanguageSupport.JAVASCRIPT:
            # Implement the Hangul payload encoding technique
            # This technique stores obfuscated payload as property names in object literals
            # and uses a JavaScript Proxy 'get()' trap to decode at runtime
            
            # Find potential payload strings to encode
            string_pattern = r'(["\'])(.*?)(\1)'
            matches = re.finditer(string_pattern, result)
            
            for match in reversed(list(matches)):
                start, end = match.span()
                quote_char = match.group(1)
                string_content = match.group(2)
                
                if len(string_content) > 5:  # Only encode longer strings
                    # Encode the content using Hangul characters
                    encoded_content = self._encode_to_hangul_sequence(string_content)
                    
                    # Replace with an object property that uses Hangul characters as keys
                    new_content = f'hangulDecoder[`${encoded_content}`]'
                    
                    result = result[:start] + new_content + result[end:]
            
            # Add the Hangul decoder Proxy
            decoder_proxy = """
// Hangul Decoder Proxy
const hangulDecoder = new Proxy({}, {
  get: function(target, prop) {
    // Decode Hangul-encoded property names back to original content
    return decodeHangulPayload(prop);
  }
});

// Decoding function for Hangul-encoded strings
function decodeHangulPayload(encodedStr) {
  let decoded = '';
  for (let i = 0; i < encodedStr.length; i++) {
    const char = encodedStr.charCodeAt(i);
    // Reverse the encoding process
    if (char >= 0xFFA0 && char <= 0xFFDF) {
      // Hangul half-width range - decode back to original
      decoded += String.fromCharCode(char - 0xFF80); // Simplified decoding
    } else if (char >= 0x3130 && char <= 0x318F) {
      // Hangul compatibility jamo range
      decoded += String.fromCharCode(char - 0x3000); // Simplified decoding
    } else {
      decoded += encodedStr[i];
    }
  }
  return decoded;
}
"""
            result = decoder_proxy + "\n" + result
            
        elif target_language in [LanguageSupport.PYTHON, LanguageSupport.JAVA, LanguageSupport.GO]:
            # Adapt the technique for other languages
            # In Python, we can use the concept in string literals or identifiers
            if target_language == LanguageSupport.PYTHON:
                # For Python, encode strings in a similar way
                string_pattern = r'(["\'])(.*?)(\1)'
                matches = re.finditer(string_pattern, result)
                
                for match in reversed(list(matches)):
                    start, end = match.span()
                    quote_char = match.group(1)
                    string_content = match.group(2)
                    
                    if len(string_content) > 5:
                        # Encode using Hangul
                        encoded_content = self._encode_to_hangul_sequence(string_content)
                        
                        # Create a function call to decode it
                        new_content = f'decode_hangul_payload("{encoded_content}")'
                        
                        result = result[:start] + new_content + result[end:]
                
                # Add the decoding function
                decoder_func = '''
def decode_hangul_payload(encoded_str):
    """Decode Hangul-encoded payload."""
    decoded = ""
    for char in encoded_str:
        char_code = ord(char)
        # Apply reverse mapping
        if 0xFFA0 <= char_code <= 0xFFDF:
            # Hangul half-width range
            decoded += chr(char_code - 0xFF80)  # Simplified decoding
        elif 0x3130 <= char_code <= 0x318F:
            # Hangul compatibility jamo range
            decoded += chr(char_code - 0x3000)  # Simplified decoding
        else:
            decoded += char
    return decoded
'''
                result = decoder_func + "\n" + result
        
        return result
    
    def _encode_to_hangul_sequence(self, text: str) -> str:
        """Encode text using Hangul characters (U+FFA0 and U+3164 range)."""
        encoded = ""
        for char in text:
            codepoint = ord(char)
            
            # Map to Hangul half-width area (U+FFA0-U+FFDF) or compatibility area
            # This is a simplified version of the mapping
            if codepoint < 128:  # ASCII range
                # Map to Hangul half-width area
                mapped_code = 0xFFA0 + (codepoint % 32)
                encoded += chr(mapped_code)
            else:
                # For non-ASCII, use the Hangul compatibility jamo (U+3130-U+318F)
                mapped_code = 0x3130 + (codepoint % 96)
                encoded += chr(mapped_code)
        
        return encoded


# Create an instance of the module
hangul_encoding_module = HangulEncodingModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
@click.option('--language', default='javascript', type=click.Choice(['python', 'javascript', 'java', 'go', 'kotlin', 'swift', 'rust', 'c', 'cpp']), 
              help='Target programming language.')
def hangul_encoding(input_file: str, output_file: str, language: str) -> None:
    """
    Apply Hangul encoding obfuscation to a file.
    Uses Hangul half-width and full-width characters to encode payloads.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Hangul encoding obfuscation
    target_lang = LanguageSupport(language)
    result = engine.apply_obfuscation(
        content, 
        ObfuscationTechnique.HANGUL_ENCODING, 
        target_lang
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Hangul encoding applied to {input_file} -> {output_file}")