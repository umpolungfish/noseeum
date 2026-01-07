"""
Kotlin Language Attack Module for the noseeum framework.
Implements Kotlin-specific Unicode obfuscation techniques based on its permissive frontend.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class KotlinAttackModule(ObfuscationModule):
    """Module for Kotlin-specific Unicode obfuscation techniques."""
    
    def get_name(self) -> str:
        return "Kotlin Language Attack"
    
    def get_description(self) -> str:
        return "Implements Kotlin-specific Unicode obfuscation using its permissive lexer and restrictive backend"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.KOTLIN]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply Kotlin-specific obfuscation techniques to content."""
        import re
        
        if target_language != LanguageSupport.KOTLIN:
            return content  # Only apply to Kotlin files
        
        result = content
        
        # Kotlin's lexer is very permissive and accepts a wide range of Unicode characters
        # in identifiers, including Lu, Ll, Lt, Lm, Lo, Nl, and Nd categories
        # However, the backend has restrictions via JVM and OS
        
        # Use backticked identifiers with Unicode characters that are valid in .kt file
        # but result in invalid class filenames (e.g., containing characters not allowed in JVM class files)
        
        # First, identify class declarations
        class_pattern = r'(class\s+)([A-Za-z_][A-Za-z0-9_]*)'
        matches = re.finditer(class_pattern, result)
        
        for match in reversed(list(matches)):
            start, end = match.span()
            full_match = match.group(0)
            class_keyword = match.group(1)
            class_name = match.group(2)
            
            # Replace the class name with a backticked identifier containing problematic characters
            # For example, using characters that would create invalid filenames
            # In this case, we'll use Unicode characters that might not be valid in filesystems
            # Use a character that's valid in Kotlin but could cause issues with JVM/OS
            problematic_name = f"`{class_name}\u200B\u200C`"  # Adding zero-width chars
            
            new_string = f"{class_keyword}{problematic_name}"
            result = result[:start] + new_string + result[end:]
        
        # Also add Unicode characters to function names to create potential conflicts
        fun_pattern = r'(fun\s+)([A-Za-z_][A-Za-z0-9_]*)'
        matches = re.finditer(fun_pattern, result)
        
        for match in reversed(list(matches)):
            start, end = match.span()
            full_match = match.group(0)
            fun_keyword = match.group(1)
            fun_name = match.group(2)
            
            # Add Unicode characters to function names
            problematic_name = f"`{fun_name}\u200D`"  # Zero-width joiner
            
            new_string = f"{fun_keyword}{problematic_name}"
            result = result[:start] + new_string + result[end:]
        
        return result


# Create an instance of the module
kotlin_attack_module = KotlinAttackModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input Kotlin file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
def kotlin_attack(input_file: str, output_file: str) -> None:
    """
    Apply Kotlin-specific obfuscation techniques to a file.
    Creates code that passes syntax analysis but fails during compilation.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Kotlin-specific obfuscation
    result = engine.apply_obfuscation(
        content,
        ObfuscationTechnique.LANGUAGE_SPECIFIC,
        LanguageSupport.KOTLIN
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"Kotlin-specific obfuscation applied to {input_file} -> {output_file}")