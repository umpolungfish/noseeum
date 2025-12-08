import click
import json
import random
from typing import Dict, Any, Optional

# Import configuration and error handling utilities
from noseeum.config import get_config
from noseeum.utils.error_handlers import handle_registry_load_error

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

# Import error handling utilities
from noseeum.utils.error_handlers import handle_registry_load_error

def read_file_with_encoding(file_path: str) -> str:
    """
    Read a file with automatic encoding detection.
    Tries UTF-8 first, then falls back to other common encodings.
    """
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue

    # If all encodings fail, raise an exception
    raise ValueError(f"Could not decode file '{file_path}' with any of the tried encodings: {encodings}")


@click.command()
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The source file to apply homoglyph obfuscation to.')
@click.option('--output-file', required=True, type=click.Path(), help='The output file for the obfuscated code.')
@click.option('--density', default=0.1, type=float, help='The density of homoglyph substitutions (0.0 to 1.0).')
def homoglyph(input_file: str, output_file: str, density: float) -> None:
    """
    Performs homoglyph obfuscation on identifiers in a source file.
    Substitutes ASCII characters with visually similar Unicode characters.
    """
    click.echo(f"Executing Homoglyph obfuscation on {input_file} to {output_file} with density {density}...")

    try:
        homoglyph_map = load_homoglyph_registry()
    except (IOError, json.JSONDecodeError) as e:
        handle_registry_load_error('homoglyph_registry.json', e)
        return

    try:
        content: str = read_file_with_encoding(input_file)
    except Exception as e:
        click.echo(f"Error reading input file '{input_file}': {str(e)}", err=True)
        return

    new_content: list = []
    for char in content:
        # Check if the character is a key in our homoglyph map
        if char in homoglyph_map and random.random() < density:
            # Choose a random homoglyph from the list of available ones
            new_char = random.choice(homoglyph_map[char])
            new_content.append(new_char)
        else:
            new_content.append(char)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("".join(new_content))
    except IOError as e:
        click.echo(f"Error writing output file '{output_file}': {str(e)}", err=True)
        return

    click.echo("Homoglyph obfuscation complete.")
