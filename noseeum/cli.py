import click

# Import attack modules
from noseeum.attacks.bidi import bidi
from noseeum.attacks.homoglyph import homoglyph
from noseeum.attacks.invisible import invisible
from noseeum.attacks.language import language

# Import detector module
from noseeum.detector.scanner import detect_command

# Import core modules for the new architecture
from noseeum.core.engine import engine, ObfuscationTechnique, LanguageSupport
from noseeum.core.grammar_db import grammar_db
from noseeum.core.stealth_engine import stealth_engine
from noseeum.core.evasion_library import evasion_library

# Import new advanced attack modules
from noseeum.attacks.normalization import normalization
from noseeum.attacks.unassigned_planes import unassigned_planes
from noseeum.attacks.payload_injection import payload_injection
from noseeum.attacks.hangul_encoding import hangul_encoding

# Import language-specific modules
from noseeum.attacks.go_attack import go_attack
from noseeum.attacks.kotlin_attack import kotlin_attack
from noseeum.attacks.javascript_attack import javascript_attack
from noseeum.attacks.swift_attack import swift_attack


@click.group()
def main():
    """
    Noseeum: A Unified Framework for Unicode-Based Exploitation.

    The noseeum framework provides advanced Unicode-based obfuscation techniques
    for offensive security research and penetration testing. It includes modules
    for exploiting Unicode normalization inconsistencies, unassigned Unicode planes,
    payload injection via identifier characters, and language-specific vulnerabilities.
    """
    pass

# Register the detect command
main.add_command(detect_command)

@click.group()
def attack():
    """
    A group of commands for various attack vectors.

    These commands implement various Unicode-based obfuscation and exploitation techniques.
    """
    pass

@click.group()
def advanced():
    """
    Advanced obfuscation techniques beyond basic attacks.

    These commands implement sophisticated Unicode exploitation techniques
    including normalization exploits, unassigned planes usage, and payload injection.
    """
    pass

@click.group()
def language_specific():
    """
    Language-specific obfuscation techniques.

    These commands target specific programming languages' Unicode handling vulnerabilities.
    """
    pass

# Register existing basic attack commands
attack.add_command(bidi)
attack.add_command(homoglyph)
attack.add_command(invisible)
attack.add_command(language)

# Register new advanced attack commands under the advanced group
advanced.add_command(normalization)
advanced.add_command(unassigned_planes)
advanced.add_command(payload_injection)
advanced.add_command(hangul_encoding)

# Register language-specific attack commands
language_specific.add_command(go_attack)
language_specific.add_command(kotlin_attack)
language_specific.add_command(javascript_attack)
language_specific.add_command(swift_attack)

# Add the advanced and language-specific groups to the attack group
attack.add_command(advanced)
attack.add_command(language_specific)

main.add_command(attack)

# Add commands for the new architecture features
@main.command()
def info():
    """
    Display information about the noseeum framework architecture.

    Shows registered modules, supported languages, and available tactics.
    """
    click.echo("Noseeum Framework - Modular Architecture Information")
    click.echo("=" * 50)
    click.echo(f"Registered modules: {len(engine.get_all_modules())}")
    click.echo(f"Supported languages: {len(grammar_db.get_all_languages())}")
    click.echo(f"Available evasion tactics: {len(evasion_library.get_available_tactics())}")
    click.echo()

    click.echo("Supported Languages:")
    for lang in grammar_db.get_all_languages():
        vulnerabilities = grammar_db.get_vulnerabilities(lang)
        click.echo(f"  - {lang.value}: {len(vulnerabilities)} vulnerabilities")

    click.echo()
    click.echo("Available Evasion Tactics:")
    for tactic in evasion_library.get_available_tactics():
        click.echo(f"  - {tactic}")

@main.command()
def techniques():
    """
    List all available obfuscation techniques with descriptions.
    """
    click.echo("Available Obfuscation Techniques:")
    click.echo("=" * 35)

    # Show all registered modules with their descriptions
    for technique, module in engine.get_all_modules().items():
        click.echo(f"{technique.value.upper()}: {module.get_description()}")
        click.echo(f"  Supported languages: {[lang.value for lang in module.get_supported_languages()]}")
        click.echo()

@main.command()
@click.option('--target-language', '-l', default='python',
              type=click.Choice([lang.value for lang in grammar_db.get_all_languages()]),
              help='Target programming language for vulnerability scan')
def vulnerabilities(target_language):
    """
    Show vulnerabilities for a specific programming language.
    """
    lang_support = next((lang for lang in grammar_db.get_all_languages()
                        if lang.value == target_language), None)
    if not lang_support:
        click.echo(f"Language {target_language} not supported", err=True)
        return

    vulnerabilities = grammar_db.get_vulnerabilities(lang_support)
    click.echo(f"Vulnerabilities for {target_language.upper()}:")
    click.echo("=" * (20 + len(target_language)))

    if vulnerabilities:
        for i, vuln in enumerate(vulnerabilities, 1):
            click.echo(f"{i}. {vuln}")
    else:
        click.echo("No specific vulnerabilities documented for this language.")


if __name__ == '__main__':
    main()