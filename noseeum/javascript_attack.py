"""
JavaScript Language Attack Module for the noseeum framework.
Implements JavaScript-specific Unicode obfuscation techniques for AST-based evasion.
"""
import click
from typing import List
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class JavaScriptAttackModule(ObfuscationModule):
    """Module for JavaScript-specific Unicode obfuscation techniques."""
    
    def get_name(self) -> str:
        return "JavaScript Language Attack"
    
    def get_description(self) -> str:
        return "Implements JavaScript-specific Unicode obfuscation targeting AST-based analysis tools"
    
    def get_supported_languages(self) -> List[LanguageSupport]:
        return [LanguageSupport.JAVASCRIPT]
    
    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply JavaScript-specific obfuscation techniques to content."""
        import re
        
        if target_language != LanguageSupport.JAVASCRIPT:
            return content  # Only apply to JavaScript files
        
        result = content
        
        # JavaScript is heavily analyzed by AST-based tools like ESLint and GuardDog
        # To evade detection, we need to perform transformations on the AST itself
        # such as control-flow flattening or insertion of junk code
        
        # 1. Create low-entropy payloads instead of high-entropy encoded blobs
        string_pattern = r'(["\'])(.*?)(\1)'
        matches = re.finditer(string_pattern, result)
        
        for match in reversed(list(matches)):
            start, end = match.span()
            quote_char = match.group(1)
            string_content = match.group(2)
            
            # Instead of keeping high-entropy strings, break them into smaller parts
            # This helps avoid entropy-based detection
            if len(string_content) > 20:  # Only for longer strings
                # Split into smaller parts and reconstruct using array access
                parts = []
                chunk_size = 5  # Small chunks to keep entropy low
                for i in range(0, len(string_content), chunk_size):
                    parts.append(string_content[i:i+chunk_size])
                
                # Create an array of string parts
                array_parts = [f'"{part}"' for part in parts]
                array_name = f"str_{abs(hash(string_content)) % 10000}"  # Create unique name
                
                # Add the array definition before the usage
                array_def = f"var {array_name}=[{','.join(array_parts)}];"
                
                # Replace the original string with array reconstruction
                reconstruction = f"{array_name}.join('')"
                
                # Add array definition and replace usage
                result = array_def + result[:start] + reconstruction + result[end:]
        
        # 2. Insert junk/anti-analysis code to complicate AST
        lines = result.split('\n')
        modified_lines = []
        
        for i, line in enumerate(lines):
            modified_lines.append(line)
            
            # Add junk code on lines that contain key operations
            if any(keyword in line for keyword in ['function', 'if', 'for', 'while', 'return']):
                # Add junk code that doesn't affect execution but complicates analysis
                junk_code = f"/*junk*/var _0x{abs(hash(line[:10])) % 10000} = Date.now();"
                modified_lines.append(junk_code)
        
        result = '\n'.join(modified_lines)
        
        # 3. Use Unicode character substitution for common patterns
        # Replace common JavaScript keywords with Unicode equivalents where applicable
        # This is subtle and needs to maintain functionality
        
        return result


# Create an instance of the module
javascript_attack_module = JavaScriptAttackModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='Input JavaScript file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='Output file for obfuscated content.')
def javascript_attack(input_file: str, output_file: str) -> None:
    """
    Apply JavaScript-specific obfuscation techniques to a file.
    Targets AST-based analysis and avoids high-entropy strings.
    """
    from noseeum.core.engine import engine, ObfuscationTechnique
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply JavaScript-specific obfuscation
    result = engine.apply_obfuscation(
        content,
        ObfuscationTechnique.LANGUAGE_SPECIFIC,
        LanguageSupport.JAVASCRIPT
    )
    
    # Write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    click.echo(f"JavaScript-specific obfuscation applied to {input_file} -> {output_file}")