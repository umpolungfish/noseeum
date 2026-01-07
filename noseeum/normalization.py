"""
Normalization Exploitation Module for the noseeum framework.
This module crafts payloads that normalize differently across system components.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class NormalizationExploitationModule(ObfuscationModule):
    """Module for exploiting Unicode normalization inconsistencies."""
    
    def get_name(self) -> str:
        return "Normalization Exploitation"
    
    def get_description(self) -> str:
        return "Crafts payloads that normalize differently across system components (parser vs. scanner)"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [
            LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT, 
            LanguageSupport.JAVA, LanguageSupport.GO,
            LanguageSupport.KOTLIN, LanguageSupport.SWIFT,
            LanguageSupport.RUST, LanguageSupport.C, LanguageSupport.CPP
        ]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply normalization-based obfuscation to content."""
        import unicodedata
        import re

        # Exploit normalization differences like CVE-2024–43093 (fullwidth apostrophe)
        # The fullwidth apostrophe (U+FF07) normalizes to standard ASCII apostrophe (U+0027) under NFKD/NFKC
        # This can enable SQL injection attacks that bypass filters checking for single quotes

        # Define potential normalization exploit characters based on common attacks
        normalization_exploits = {
            # Fullwidth apostrophe -> standard apostrophe
            '\uFF07': "'",  # Fullwidth apostrophe
            # Small less-than sign -> standard less-than
            '\uFE64': '<',  # Small less-than sign
            # Small greater-than sign -> standard greater-than
            '\uFE65': '>',  # Small greater-than sign
            # Fullwidth semicolon -> standard semicolon
            '\uFF1B': ';',  # Fullwidth semicolon
            # Small ampersand -> standard ampersand
            '\uFE60': '&',  # Small ampersand
            # Small asterisk -> standard asterisk
            '\uFE61': '*',  # Small asterisk
        }

        # Invert some characters to their decomposed forms to exploit normalization gaps
        # This creates characters that look different but normalize to the same form
        result = content
        for malicious, safe in normalization_exploits.items():
            # Replace potential injection points with normalization-exploitable characters
            result = result.replace(safe, malicious)

        # Additionally, apply decomposition normalization to create more complex variants
        # For example, replace characters with their decomposed forms
        # é (U+00E9) becomes e + combining acute (U+0065 U+0301)
        result = unicodedata.normalize('NFD', result)

        # For more advanced attacks, we could also implement custom normalization rules
        # For now, we'll add variation selectors that don't affect normalization but add obfuscation
        variation_selectors = ['\uFE00', '\uFE01', '\uFE02', '\uFE03', '\uFE04', '\uFE05', '\uFE06', '\uFE07']

        # Apply the normalization transformation based on language-specific behavior
        if target_language in [LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT]:
            # In Python and JavaScript, we might target string processing specifically
            # Find string literals and apply normalization to them
            string_pattern = r'(["\'])(.*?)(\1)'
            matches = re.finditer(string_pattern, result)

            # For each string literal, apply normalization to its content
            for match in reversed(list(matches)):
                start, end = match.span()
                full_match = match.group(0)
                quote_char = match.group(1)
                string_content = match.group(2)

                # Apply normalization to the string content
                normalized_content = string_content
                for malicious, safe in normalization_exploits.items():
                    normalized_content = normalized_content.replace(safe, malicious)

                # Also apply decomposition normalization
                normalized_content = unicodedata.normalize('NFD', normalized_content)

                # Replace in the result
                new_string = f"{quote_char}{normalized_content}{quote_char}"
                result = result[:start] + new_string + result[end:]

        return result


# Create an instance of the module
normalization_module = NormalizationExploitationModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
@click.option('--language', default='python', type=click.Choice(['python', 'javascript', 'java', 'go', 'kotlin', 'swift', 'rust', 'c', 'cpp']), 
              help='Target programming language.')
def normalization(input_file: str, output_file: str, language: str) -> None:
    """
    Apply normalization-based obfuscation to a file.
    Exploits Unicode normalization inconsistencies between parsers and scanners.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply normalization obfuscation
    target_lang = LanguageSupport(language)
    result = engine.apply_obfuscation(
        content, 
        ObfuscationTechnique.NORMALIZATION, 
        target_lang
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Normalization obfuscation applied to {input_file} -> {output_file}")