"""
Go Language Attack Module for the noseeum framework.
Implements Go-specific Unicode obfuscation techniques based on its configurable lexer.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class GoAttackModule(ObfuscationModule):
    """Module for Go-specific Unicode obfuscation techniques."""
    
    def get_name(self) -> str:
        return "Go Language Attack"
    
    def get_description(self) -> str:
        return "Implements Go-specific Unicode obfuscation using its configurable lexer and permissive Unicode handling"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.GO]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply Go-specific obfuscation techniques to content."""
        import re
        
        if target_language != LanguageSupport.GO:
            return content  # Only apply to Go files
        
        result = content
        
        # Go's text/scanner package doesn't treat many Unicode characters as whitespace by default
        # This allows for identifiers containing zero-width spaces, bidirectional controls, and variation selectors
        
        # Find identifiers and add zero-width characters
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.finditer(identifier_pattern, result)
        
        # Process matches in reverse order to not affect positions of subsequent matches
        for match in reversed(list(matches)):
            start, end = match.span()
            identifier = match.group(1)
            
            # Add zero-width space (U+200B) to identifiers - this is allowed by Go scanner
            # but may cause issues in later processing
            modified_identifier = f"{identifier}\u200B"  # Zero-width space
            
            result = result[:start] + modified_identifier + result[end:]
        
        # Also add bidirectional override characters to certain statements
        # These are not treated as whitespace by default in Go
        lines = result.split('\n')
        modified_lines = []
        
        for line in lines:
            # Add bidirectional control characters to potentially confusing strings
            if any(keyword in line for keyword in ['if ', 'else ', 'for ', 'func ', 'var ', 'const ']):
                # Add Right-to-Left Override (U+202E) in a non-disruptive way
                # This is for demonstration - in practice, this would be more carefully applied
                modified_line = line.replace(' ', '\u200B ')  # Replace spaces with zero-width + space
                modified_lines.append(modified_line)
            else:
                modified_lines.append(line)
        
        result = '\n'.join(modified_lines)
        
        # Go doesn't normalize identifiers by default, which means we can create identifiers
        # that look different but are treated as the same by the scanner
        # This can be used for Trojan Source attacks
        
        return result


# Create an instance of the module
go_attack_module = GoAttackModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input Go file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
def go_attack(input_file: str, output_file: str) -> None:
    """
    Apply Go-specific obfuscation techniques to a file.
    Uses Go's configurable scanner to create syntactically valid but potentially failing code.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Go-specific obfuscation
    result = engine.apply_obfuscation(
        content,
        ObfuscationTechnique.LANGUAGE_SPECIFIC,
        LanguageSupport.GO
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Go-specific obfuscation applied to {input_file} -> {output_file}")