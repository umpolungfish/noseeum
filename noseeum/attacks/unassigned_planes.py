"""
Unassigned Planes Module for the noseeum framework.
This module generates syntactically valid identifiers using characters from unassigned Unicode planes.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class UnassignedPlanesModule(ObfuscationModule):
    """Module for using unassigned Unicode planes in identifiers."""
    
    def get_name(self) -> str:
        return "Unassigned Planes"
    
    def get_description(self) -> str:
        return "Generates syntactically valid identifiers using characters from unassigned Unicode planes (U+20000–U+2FFFD)"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        # Swift is particularly susceptible to this technique
        return [LanguageSupport.SWIFT, LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT, 
                LanguageSupport.JAVA, LanguageSupport.GO, LanguageSupport.KOTLIN]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply unassigned planes obfuscation to content."""
        import re
        import tokenize
        import token

        # For unassigned planes (U+20000–U+2FFFD), we need to be more strategic
        # These characters can be used in identifiers in languages with permissive grammars like Swift

        # First, let's identify all identifier-like tokens in the content
        # For demonstration, we'll use a simple regex approach for common identifier patterns
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'

        # Find all identifiers in the content
        identifiers = re.findall(identifier_pattern, content)

        result = content

        # For Swift specifically, we can use characters from unassigned planes more freely
        if target_language == LanguageSupport.SWIFT:
            # In Swift, identifiers can include characters from unassigned planes (U+20000–U+2FFFD)
            # We'll strategically add these characters to make identifiers ambiguous

            # Replace some identifiers with versions that include unassigned plane characters
            # For the purposes of this module, we'll use characters from Supplementary Multilingual Plane (SMP)
            # U+1F000 to U+1F02B are Miscellaneous Symbols and Arrows
            # We'll use U+1F000 as a sample unassigned character (in actual implementation, we should use valid ones)
            for identifier in identifiers[:10]:  # Only modify first 10 identifiers to avoid too much corruption
                # Add an unassigned plane character to the identifier
                # In a real implementation, we'd use actual valid unassigned characters for the target language
                modified_identifier = f"{identifier}\U00020000"  # Using Plane 2 character

                # Replace only the specific instance of the identifier
                # Use word boundaries to avoid partial matches
                result = re.sub(rf'\b{re.escape(identifier)}\b', modified_identifier, result, count=1)

        elif target_language in [LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT, LanguageSupport.JAVA]:
            # For other languages, we can insert default-ignorable code points
            # According to UAX #31, these include zero-width joiners (U+200D), zero-width non-joiners (U+200C)
            # and variation selectors (U+FE00–U+FE0F), which remain in XID_Continue but should be profile-based excluded
            ignorable_chars = ['\u200C', '\u200D']  # Zero-width non-joiner and joiner
            variation_selectors = ['\uFE00', '\uFE01', '\uFE02', '\uFE03', '\uFE04', '\uFE05', '\uFE06', '\uFE07',
                                  '\uFE08', '\uFE09', '\uFE0A', '\uFE0B', '\uFE0C', '\uFE0D', '\uFE0E', '\uFE0F']

            # Add these to identifiers to embed invisible instructions or metadata
            for identifier in identifiers[:10]:  # Only modify first 10 identifiers
                # Add a variation selector to the end of the identifier
                modified_identifier = f"{identifier}{variation_selectors[0]}"

                # Replace only the specific instance of the identifier
                result = re.sub(rf'\b{re.escape(identifier)}\b', modified_identifier, result, count=1)

        # Additionally, we could apply more complex transformations based on the target language
        # For example, in Python we can create identifiers with characters that are default-ignorable
        if target_language == LanguageSupport.PYTHON:
            # Python allows a wide range of Unicode characters in identifiers
            # We can embed extra information using default-ignorable code points
            for identifier in identifiers[10:20]:  # Process next set of identifiers differently
                # Add multiple ignorable characters to embed more data
                embedded_identifier = f"{identifier}\u200C\u200D"  # Non-joiner + Joiner
                result = re.sub(rf'\b{re.escape(identifier)}\b', embedded_identifier, result, count=1)

        return result


# Create an instance of the module
unassigned_planes_module = UnassignedPlanesModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
@click.option('--language', default='swift', type=click.Choice(['python', 'javascript', 'java', 'go', 'kotlin', 'swift', 'rust', 'c', 'cpp']), 
              help='Target programming language.')
def unassigned_planes(input_file: str, output_file: str, language: str) -> None:
    """
    Apply unassigned planes obfuscation to a file.
    Uses characters from unassigned Unicode planes to create identifiers.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply unassigned planes obfuscation
    target_lang = LanguageSupport(language)
    result = engine.apply_obfuscation(
        content, 
        ObfuscationTechnique.UNASSIGNED_PLANES, 
        target_lang
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Unassigned planes obfuscation applied to {input_file} -> {output_file}")