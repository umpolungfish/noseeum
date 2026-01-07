import click
import json
import random
import re

# --- `py-nfkc` Implementation ---

def generate_nfkc_variants(identifier, nfkc_map, count):
    """Generates unique NFKC variants of a given identifier."""
    if not all(c in nfkc_map for c in identifier):
        unsupported_chars = {c for c in identifier if c not in nfkc_map}
        raise click.ClickException(f"Identifier contains unsupported characters: {', '.join(unsupported_chars)}")

    variants = set()
    max_attempts = count * 100  # Avoid infinite loops
    attempts = 0

    while len(variants) < count and attempts < max_attempts:
        new_identifier = list(identifier)
        # Randomly choose how many characters to replace (at least 1)
        num_replacements = random.randint(1, len(identifier))
        # Get random indices to replace
        indices_to_replace = random.sample(range(len(identifier)), num_replacements)

        for i in indices_to_replace:
            original_char = new_identifier[i]
            if nfkc_map.get(original_char):
                new_identifier[i] = random.choice(nfkc_map[original_char])
        
        variants.add("".join(new_identifier))
        attempts += 1
    
    if attempts >= max_attempts:
        click.echo(f"Warning: Could only generate {len(variants)} unique variants after {max_attempts} attempts.", err=True)

    return variants

# --- `js-permissive-id` Implementation ---

# A simple map for demonstration. A real tool would have a much larger map.
JS_PERMISSIVE_MAP = {
    'a': 'あ', 'b': 'い', 'c': 'う', 'd': 'え', 'e': 'お',
    'f': 'か', 'g': 'き', 'h': 'く', 'i': 'け', 'l': 'こ',
    'm': 'さ', 'n': 'し', 'o': 'す', 'p': 'せ', 'r': 'そ',
    's': 'た', 't': 'ち', 'u': 'つ', 'v': 'て', 'w': 'と',
    'x': 'な', 'y': 'に', 'z': 'ぬ'
}

def obfuscate_js_identifiers(content):
    """Replaces ASCII in identifiers with Japanese characters."""
    # This regex is a simplification and might miss complex identifiers
    # or replace things in strings that look like identifiers.
    def repl(match):
        identifier = match.group(0)
        # Only replace if we have a mapping for the first character
        if identifier[0].lower() in JS_PERMISSIVE_MAP:
             return "".join(JS_PERMISSIVE_MAP.get(c.lower(), c) for c in identifier)
        return identifier

    return re.sub(r'[a-zA-Z_][a-zA-Z0-9_]*', repl, content)


# --- `java-unicode-escape` Implementation ---

def obfuscate_java_escapes(content, probability=0.5):
    """Replaces characters with their Unicode escape sequences."""
    new_content = []
    for char in content:
        # Only escape standard ASCII characters for this PoC
        if ' ' <= char <= '~' and random.random() < probability:
            new_content.append(f'\\u{ord(char):04x}')
        else:
            new_content.append(char)
    return "".join(new_content)


# --- CLI Group and Commands ---

@click.group()
def language():
    """Language-specific exploits (Python, JS, Java)."""
    pass

@language.command(name='py-nfkc')
@click.option('--identifier', required=True, help='The Python identifier to generate NFKC variants for (e.g., "__import__").')
@click.option('--count', default=10, type=int, help='Number of unique NFKC variants to generate.')
def py_nfkc(identifier, count):
    """Generates NFKC-normalized variants of a Python identifier."""
    # Load the NFKC map from package resources
    try:
        # Try to access the file within the package data subdirectory
        try:
            from importlib.resources import files
        except ImportError:
            from importlib_resources import files

        # Read the file content directly from the package data subdirectory
        content = files('noseeum.data').joinpath('nfkc_map.json').read_text(encoding='utf-8')
        nfkc_map = json.loads(content)
    except (IOError, json.JSONDecodeError):
        # Fallback to config path
        try:
            from noseeum.config import get_config
            map_path = get_config('nfkc_map_path', 'nfkc_map.json')
            with open(map_path, 'r', encoding='utf-8') as f:
                nfkc_map = json.load(f)
        except (IOError, json.JSONDecodeError):
            raise click.ClickException(f"Could not load NFKC map. Please ensure the data files are properly installed.")

    click.echo(f"Generating {count} NFKC variants for Python identifier '{identifier}'...")
    try:
        variants = generate_nfkc_variants(identifier, nfkc_map, count)
        click.echo("--- GENERATED VARIANTS ---")
        for var in sorted(list(variants)):
            click.echo(var)
        click.echo("--------------------------")
    except click.ClickException as e:
        click.echo(f"Error: {e}", err=True)


@language.command(name='js-permissive-id')
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The JavaScript file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='The output file for the obfuscated JS code.')
def js_permissive_id(input_file, output_file):
    """Obfuscates JavaScript identifiers using permissive Unicode characters."""
    click.echo(f"Obfuscating JavaScript identifiers in {input_file} to {output_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        obfuscated_content = obfuscate_js_identifiers(content)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_content)
        click.echo("Obfuscation complete.")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)


@language.command(name='java-unicode-escape')
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The Java file to obfuscate.')
@click.option('--output-file', required=True, type=click.Path(), help='The output file for the obfuscated Java code.')
@click.option('--probability', default=0.5, type=float, help='The probability (0.0 to 1.0) of escaping a character.')
def java_unicode_escape(input_file, output_file, probability):
    """Obfuscates Java code using compile-time Unicode escape sequences."""
    click.echo(f"Obfuscating Java code in {input_file} to {output_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        obfuscated_content = obfuscate_java_escapes(content, probability)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_content)
        click.echo("Obfuscation complete.")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)