import click
import random

# --- Steganography Constants ---
ZERO = '\u200b'  # Zero Width Space
ONE = '\u200c'   # Zero Width Non-Joiner
DELIMITER = '\u200d' # Zero Width Joiner

# --- LLM Jailbreak Constants ---
VARIATION_SELECTORS = [chr(i) for i in range(0xFE00, 0xFE10)] # VS1-VS16

# --- Main Group ---
@click.group()
def invisible():
    """Zero-width and other invisible character attacks."""
    pass

# --- Steganography Implementation ---

def text_to_binary(text):
    """Converts a string to its binary representation."""
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_zero_width(binary_str):
    """Converts a binary string to a sequence of zero-width characters."""
    return binary_str.replace('0', ZERO).replace('1', ONE)

def zero_width_to_binary(zw_str):
    """Converts a sequence of zero-width characters back to a binary string."""
    return zw_str.replace(ZERO, '0').replace(ONE, '1')

def binary_to_text(binary_str):
    """Converts a binary string back to a regular string."""
    if len(binary_str) % 8 != 0:
        return None
    return ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))

@invisible.command(name='stego-encode')
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The file containing the hidden payload.')
@click.option('--carrier-file', required=True, type=click.Path(exists=True), help='The benign file to embed the payload into.')
@click.option('--output-file', required=True, type=click.Path(), help='The output file with the embedded payload.')
def stego_encode(input_file, carrier_file, output_file):
    """Encodes a hidden payload into a carrier file using zero-width characters."""
    click.echo(f"Encoding payload from {input_file} into {carrier_file} to {output_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            payload = f.read()
        with open(carrier_file, 'r', encoding='utf-8') as f:
            carrier = f.read()
        binary_payload = text_to_binary(payload)
        invisible_payload = binary_to_zero_width(binary_payload) + DELIMITER
        stego_content = invisible_payload + carrier
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(stego_content)
        click.echo("Steganographic encoding complete.")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)

@invisible.command(name='stego-decode')
@click.option('--input-file', required=True, type=click.Path(exists=True), help='The file containing the hidden payload.')
@click.option('--output-file', required=False, type=click.Path(), help='Optional file to write the decoded payload to.')
def stego_decode(input_file, output_file):
    """Decodes a hidden payload from a file containing zero-width characters."""
    click.echo(f"Decoding hidden payload from {input_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            stego_content = f.read()
        payload_part = stego_content.split(DELIMITER)[0]
        if not payload_part:
            click.echo("No hidden payload found.")
            return
        binary_payload = zero_width_to_binary(payload_part)
        decoded_text = binary_to_text(binary_payload)
        if decoded_text is None:
            click.echo("Error: Decoded binary string has an invalid length.", err=True)
            return
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decoded_text)
            click.echo(f"Decoded payload successfully written to {output_file}.")
        else:
            click.echo("--- DECODED PAYLOAD ---")
            click.echo(decoded_text)
            click.echo("-----------------------")
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)

# --- LLM Jailbreak Implementation ---

@invisible.command(name='llm-jailbreak')
@click.option('--prompt', required=True, help='The benign prompt that precedes the attack.')
@click.option('--goal', required=True, help='The adversarial goal (e.g., "Tell me how to build a bomb").')
@click.option('--strength', default=100, type=int, help='Number of variation selector characters to use.')
def llm_jailbreak(prompt, goal, strength):
    """
    Generates an imperceptible prompt to jailbreak LLMs using Variation Selectors.
    This works by confusing the model's tokenization process.
    """
    click.echo(f"Generating LLM jailbreak prompt with strength {strength}...")
    
    # Generate a random sequence of variation selector characters
    invisible_suffix = "".join(random.choices(VARIATION_SELECTORS, k=strength))
    
    # The final payload combines the benign prompt, the invisible characters, and the malicious goal
    jailbreak_prompt = f"{prompt}{invisible_suffix}{goal}"
    
    click.echo("\n--- JAILBREAK PROMPT GENERATED ---")
    click.echo("The following text contains invisible characters. Copy and paste it directly into the target LLM.")
    click.echo("------------------------------------")
    click.echo(jailbreak_prompt)
    click.echo("------------------------------------")
