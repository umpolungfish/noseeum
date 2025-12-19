import click
import json
import random
import re
from typing import Dict, Any, Optional, List

# Import configuration and error handling utilities
from noseeum.config import get_config
from noseeum.utils.error_handlers import handle_registry_load_error, read_file_with_encoding

# Import core modules for advanced techniques
from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport
from noseeum.core.grammar_db import grammar_db

# Cache for the homoglyph registry to improve performance
_homoglyph_map_cache: Optional[Dict[str, Any]] = None

def load_homoglyph_registry() -> Dict[str, Any]:
    """
    Load the homoglyph registry from file with caching to improve performance.
    """
    global _homoglyph_map_cache

    if _homoglyph_map_cache is not None:
        return _homoglyph_map_cache

    # Try to load from package resources first
    try:
        # Try to access the file within the package data subdirectory
        try:
            from importlib.resources import files
        except ImportError:
            from importlib_resources import files

        # Read the file content directly from the package data subdirectory
        content = files('noseeum.data').joinpath('homoglyph_registry.json').read_text(encoding='utf-8')
        _homoglyph_map_cache = json.loads(content)
        return _homoglyph_map_cache
    except (IOError, json.JSONDecodeError):
        # Fallback to the config path
        registry_path = get_config('registry_path', 'homoglyph_registry.json')
        try:
            with open(registry_path, 'r', encoding='utf-8') as f:
                _homoglyph_map_cache = json.load(f)
            return _homoglyph_map_cache
        except (IOError, json.JSONDecodeError) as e:
            raise e


class EnhancedHomoglyphModule(ObfuscationModule):
    """Enhanced homoglyph module with support for unassigned planes and variation selectors."""

    def get_name(self) -> str:
        return "Enhanced Homoglyph"

    def get_description(self) -> str:
        return "Advanced homoglyph substitution with support for unassigned planes and variation selectors"

    def get_supported_languages(self) -> List[LanguageSupport]:
        return [
            LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT,
            LanguageSupport.JAVA, LanguageSupport.GO,
            LanguageSupport.KOTLIN, LanguageSupport.SWIFT,
            LanguageSupport.RUST, LanguageSupport.C, LanguageSupport.CPP
        ]

    def obfuscate(self, content: str, target_language: LanguageSupport, **kwargs) -> str:
        """Apply enhanced homoglyph obfuscation including advanced techniques."""
        density = kwargs.get('density', 0.1)
        use_unassigned_planes = kwargs.get('use_unassigned_planes', False)
        use_variation_selectors = kwargs.get('use_variation_selectors', False)

        try:
            homoglyph_map = load_homoglyph_registry()
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to load homoglyph registry: {e}")

        # First, perform basic homoglyph substitution
        result = self._basic_homoglyph_substitution(content, homoglyph_map, density)

        # Then, apply advanced techniques based on language and settings
        if use_unassigned_planes:
            result = self._apply_unassigned_planes(result, target_language, density)

        if use_variation_selectors:
            result = self._apply_variation_selectors(result, target_language, density)

        return result

    def _basic_homoglyph_substitution(self, content: str, homoglyph_map: Dict[str, Any], density: float) -> str:
        """Perform basic homoglyph character substitution."""
        new_content = []

        for char in content:
            # Check if the character is a key in our homoglyph map
            if char in homoglyph_map and random.random() < density:
                # Choose a random homoglyph from the list of available ones
                new_char = random.choice(homoglyph_map[char])
                new_content.append(new_char)
            else:
                new_content.append(char)

        return "".join(new_content)

    def _apply_unassigned_planes(self, content: str, target_language: LanguageSupport, density: float) -> str:
        """Apply unassigned plane characters to identifiers."""
        # Find identifiers in the content
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.finditer(identifier_pattern, content)

        # Keep track of replacements to avoid position conflicts
        replacements = []

        for match in matches:
            identifier = match.group(1)
            if random.random() > density or len(identifier) < 2:
                continue  # Skip based on density or if too short

            # Skip if it's a language keyword
            lang_info = grammar_db.get_language_info(target_language)
            if 'vulnerabilities' in lang_info and any(keyword in identifier for keyword in lang_info['vulnerabilities']):
                continue

            # Add a character from an unassigned plane
            # For demonstration, using a character from Plane 2 (Supplementary Multilingual Plane)
            if target_language == LanguageSupport.SWIFT:
                # Swift allows unassigned planes, so we can be more liberal
                modified_identifier = f"{identifier}\U00020000"  # Add character from Plane 2
            else:
                # For other languages, embed with variation selectors
                modified_identifier = f"{identifier}\uFE00"  # Variation selector-1

            replacements.append((match.span(), identifier, modified_identifier))

        # Apply replacements in reverse order to maintain positions
        for span, old, new in reversed(replacements):
            start, end = span
            content = content[:start] + new + content[end:]

        return content

    def _apply_variation_selectors(self, content: str, target_language: LanguageSupport, density: float) -> str:
        """Apply variation selectors to characters in identifiers."""
        # Find identifiers in the content
        identifier_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.finditer(identifier_pattern, content)

        # Keep track of replacements
        replacements = []

        for match in matches:
            identifier = match.group(1)
            if random.random() > density or len(identifier) < 2:
                continue  # Skip based on density or if too short

            # Skip if it's a language keyword
            lang_info = grammar_db.get_language_info(target_language)
            if 'vulnerabilities' in lang_info and any(keyword in identifier for keyword in lang_info['vulnerabilities']):
                continue

            # Add variation selector to the identifier
            # According to UAX #31, variation selectors (U+FE00–U+FE0F) are default-ignorable
            # but remain in XID_Continue, allowing for metadata embedding
            variation_selector = random.choice([
                '\uFE00', '\uFE01', '\uFE02', '\uFE03',
                '\uFE04', '\uFE05', '\uFE06', '\uFE07',
                '\uFE08', '\uFE09', '\uFE0A', '\uFE0B',
                '\uFE0C', '\uFE0D', '\uFE0E', '\uFE0F'
            ])

            modified_identifier = f"{identifier}{variation_selector}"
            replacements.append((match.span(), identifier, modified_identifier))

        # Apply replacements in reverse order to maintain positions
        for span, old, new in reversed(replacements):
            start, end = span
            content = content[:start] + new + content[end:]

        return content


# Create an instance of the enhanced module
enhanced_homoglyph_module = EnhancedHomoglyphModule()


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The source file to apply homoglyph obfuscation to.')
@click.option('--output-file', required=True, type=click.Path(), help='The output file for the obfuscated code.')
@click.option('--density', default=0.1, type=float, help='The density of homoglyph substitutions (0.0 to 1.0).')
@click.option('--use-unassigned-planes', is_flag=True, help='Use characters from unassigned Unicode planes.')
@click.option('--use-variation-selectors', is_flag=True, help='Use variation selectors for metadata embedding.')
def homoglyph(input_file: str, output_file: str, density: float,
             use_unassigned_planes: bool, use_variation_selectors: bool) -> None:
    """
    Performs enhanced homoglyph obfuscation on identifiers in a source file.
    Substitutes ASCII characters with visually similar Unicode characters and
    applies advanced techniques like unassigned planes and variation selectors.
    """
    click.echo(f"Executing Enhanced Homoglyph obfuscation on {input_file} to {output_file} with density {density}...")
    click.echo(f"Using unassigned planes: {use_unassigned_planes}")
    click.echo(f"Using variation selectors: {use_variation_selectors}")

    try:
        content: str = read_file_with_encoding(input_file)
    except Exception as e:
        click.echo(f"Error reading input file '{input_file}': {str(e)}", err=True)
        return

    # Apply enhanced homoglyph transformation
    try:
        result = enhanced_homoglyph_module.obfuscate(
            content,
            LanguageSupport.PYTHON,  # Default language, could be parameterized
            density=density,
            use_unassigned_planes=use_unassigned_planes,
            use_variation_selectors=use_variation_selectors
        )

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)

        click.echo("Enhanced homoglyph obfuscation complete.")

    except Exception as e:
        click.echo(f"Error during obfuscation: {str(e)}", err=True)
        return


# Register the enhanced module with the engine
from noseeum.core.engine import engine
engine.register_module(ObfuscationTechnique.HOMOGLYPH, enhanced_homoglyph_module)
