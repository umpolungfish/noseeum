import click
import unicodedata
import re
from typing import Set, Optional

# Import configuration utilities
from noseeum.config import get_config

# Characters to detect, grouped by category
SUSPICIOUS_CHARS: dict = {
    "Bidirectional Control": {
        '\u202a', # LRE
        '\u202b', # RLE
        '\u202c', # PDF
        '\u202d', # LRO
        '\u202e', # RLO
        '\u2066', # LRI
        '\u2067', # RLI
        '\u2068', # FSI
        '\u2069', # PDI
    },
    "Zero-Width": {
        '\u200b', # Zero Width Space
        '\u200c', # Zero Width Non-Joiner
        '\u200d', # Zero Width Joiner
        '\uFEFF', # Zero Width No-Break Space (BOM)
        '\u00AD', # Soft Hyphen
    },
}

def get_confusable_scripts() -> Set[str]:
    """
    Get the confusable scripts for homoglyph detection from configuration.
    """
    return set(get_config('detector_confusable_scripts', [
        'LATIN', 'CYRILLIC', 'GREEK'
    ]))

# Confusable scripts that can be used for homoglyph attacks
CONFUSABLE_SCRIPTS: Set[str] = get_confusable_scripts()

def get_script(char: str) -> Optional[str]:
    """Gets the script name for a character."""
    try:
        # We only care about the first part of the name (e.g., "LATIN")
        return unicodedata.name(char).split(' ')[0]
    except (ValueError, IndexError):
        return None

@click.command(name='detect')
@click.option('--file', 'file_path', required=True, type=click.Path(exists=True, dir_okay=False), help='The file to scan for Unicode smuggling vulnerabilities.')
def detect_command(file_path: str) -> None:
    """
    Scans a specified file for various Unicode smuggling vulnerabilities.
    """
    click.echo(f"Scanning file: {file_path}...")
    findings: list = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                # Check for suspicious control characters
                for char_category, chars in SUSPICIOUS_CHARS.items():
                    for char in chars:
                        if char in line:
                            findings.append(f"L{i}: Found {char_category} character U+{ord(char):04X}")

                # Check for mixed-script homoglyphs in identifiers
                # More comprehensive regex for identifiers in various programming languages
                # This includes identifiers starting with alphabetic characters or underscore
                # along with numbers and other valid identifier characters
                identifiers = re.findall(r'[\w\u0080-\uFFFF][\w\u0080-\uFFFF]*', line)
                for identifier in identifiers:
                    # Ignore purely numeric identifiers
                    if identifier.isnumeric():
                        continue

                    scripts = {get_script(char) for char in identifier if get_script(char) is not None}

                    # Check if an identifier mixes confusable scripts
                    if len(scripts.intersection(CONFUSABLE_SCRIPTS)) > 1:
                        finding = f"L{i}: Potential Homoglyph attack in identifier '{identifier}'. Contains mixed scripts: {', '.join(sorted(list(scripts)))}"
                        if finding not in findings: # Avoid duplicate findings on the same line
                            findings.append(finding)

    except UnicodeDecodeError:
        click.echo(f"Error: Could not read file {file_path} as UTF-8. It may be a binary file.", err=True)
        return
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)
        return

    if findings:
        click.echo(click.style("--- VULNERABILITIES DETECTED ---", fg='red', bold=True))
        for finding in sorted(list(set(findings))): # Print unique, sorted findings
            click.echo(f"- {finding}")
        click.echo("--------------------------------")
    else:
        click.echo(click.style("Scan complete. No common Unicode smuggling patterns were detected.", fg='green'))

