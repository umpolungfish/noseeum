import click

# Import attack modules
from noseeum.attacks.bidi import bidi
from noseeum.attacks.homoglyph import homoglyph
from noseeum.attacks.invisible import invisible
from noseeum.attacks.language import language

# Import detector module
from noseeum.detector.scanner import detect_command

@click.group()
def main():
    """
    Noseeum: A Unified Framework for Unicode-Based Exploitation.
    """
    pass

# Register the detect command
main.add_command(detect_command)

@click.group()
def attack():
    """A group of commands for various attack vectors."""
    pass

# Register attack commands
attack.add_command(bidi)
attack.add_command(homoglyph)
attack.add_command(invisible)
attack.add_command(language)

main.add_command(attack)

if __name__ == '__main__':
    main()