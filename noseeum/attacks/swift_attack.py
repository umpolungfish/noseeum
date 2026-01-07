"""
Swift Language Attack Module for the noseeum framework.
Implements Swift-specific Unicode obfuscation techniques based on its ambiguous identifier handling.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class SwiftAttackModule(ObfuscationModule):
    """Module for Swift-specific Unicode obfuscation techniques."""
    
    def get_name(self) -> str:
        return "Swift Language Attack"
    
    def get_description(self) -> str:
        return "Implements Swift-specific Unicode obfuscation using its ambiguous identifier handling and unassigned planes support"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.SWIFT]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply Swift-specific obfuscation techniques to content."""
        import re
        
        if target_language != LanguageSupport.SWIFT:
            return content  # Only apply to Swift files
        
        result = content
        
        # Swift's identifier grammar ambiguously permits unassigned planes (U+20000–U+2FFFD)
        # This creates opportunities for novel obfuscation techniques
        
        # 1. Generate identifiers using characters from unassigned planes
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.finditer(identifier_pattern, result)
        
        # Keep track of replacements to avoid position issues
        replacements = []
        for match in matches:
            identifier = match.group(1)
            
            # Skip keywords and built-ins
            swift_keywords = {
                'class', 'struct', 'enum', 'func', 'var', 'let', 'if', 'else', 'for', 
                'while', 'return', 'import', 'public', 'private', 'internal', 'static',
                'final', 'override', 'init', 'deinit', 'get', 'set', 'willSet', 'didSet',
                'true', 'false', 'nil', 'self', 'Self', 'super', 'try', 'catch', 'throw',
                'throws', 'rethrows', 'as', 'is', 'dynamicType', 'false', 'is', 'nil',
                'self', 'Self', 'super', 'true', 'break', 'case', 'continue', 'default',
                'do', 'else', 'fallthrough', 'for', 'guard', 'if', 'in', 'repeat', 'switch',
                'where', 'while', '__COLUMN__', '__FILE__', '__FUNCTION__', '__LINE__'
            }
            
            if identifier.lower() in swift_keywords or len(identifier) < 3:
                continue  # Skip keywords and very short identifiers
            
            # Add a character from an unassigned plane to this identifier
            # U+20000 is the start of the Supplementary Multilingual Plane
            modified_identifier = f"{identifier}\U00020000"  # Add character from Plane 2
            
            replacements.append((match.span(), identifier, modified_identifier))
        
        # Apply replacements in reverse order to maintain string positions
        for span, old, new in reversed(replacements):
            start, end = span
            result = result[:start] + new + result[end:]
        
        # 2. Exploit parser ambiguities to create confusing code structures
        # Add visually similar but different characters to operators or identifiers
        
        # 3. Use Unicode default-ignorable characters within identifiers
        # According to UAX #31, these include zero-width joiners and variation selectors
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.finditer(identifier_pattern, result)
        
        replacements = []
        for match in matches:
            identifier = match.group(1)
            
            # Skip if it's already been modified or is a keyword
            swift_keywords = {
                'class', 'struct', 'enum', 'func', 'var', 'let', 'if', 'else', 'for', 
                'while', 'return', 'import', 'public', 'private', 'internal', 'static'
            }
            
            if identifier.lower() in swift_keywords or '\U00020000' in identifier:  # Skip if already modified
                continue
                
            # Add a variation selector (U+FE00–U+FE0F) to the identifier
            modified_identifier = f"{identifier}\uFE00"  # Variation selector-1
            
            replacements.append((match.span(), identifier, modified_identifier))
        
        # Apply these replacements in reverse order
        for span, old, new in reversed(replacements):
            start, end = span
            result = result[:start] + new + result[end:]
        
        return result


# Create an instance of the module
swift_attack_module = SwiftAttackModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input Swift file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
def swift_attack(input_file: str, output_file: str) -> None:
    """
    Apply Swift-specific obfuscation techniques to a file.
    Uses unassigned planes and parser ambiguities to create confusing code structures.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Swift-specific obfuscation
    result = engine.apply_obfuscation(
        content,
        ObfuscationTechnique.LANGUAGE_SPECIFIC,
        LanguageSupport.SWIFT
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Swift-specific obfuscation applied to {input_file} -> {output_file}")
