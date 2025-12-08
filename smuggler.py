#!/usr/bin/env python3
"""
This script, "Noseeum," is a tool for injecting and removing Unicode Bidi (Bi-directional) override characters 
and other confusable characters into source code files. This technique, known as "Unicode Smuggling," 
can be used to create source code that appears benign to a human reviewer but has a different 
meaning to the compiler or interpreter.

This can be used to bypass static analysis tools and hide malicious code in plain sight.

For more information on the vulnerabilities, see:
- https://trojansource.codes/
- https://github.com/nickboucher/trojan-source
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from enum import Enum, auto


class Language(Enum):
    """
    Enum for supported programming languages.
    """
    JAVA = auto()
    CSHARP = auto()
    CPP = auto()
    JAVASCRIPT = auto()
    TYPESCRIPT = auto()
    PYTHON = auto()
    RUST = auto()
    KOTLIN = auto()
    SCALA = auto()
    SWIFT = auto()
    RUBY = auto()
    PHP = auto()
    FSHARP = auto()
    HASKELL = auto()
    GO = auto()
    UNKNOWN = auto()


def detect_language(file_path: str) -> Language:
    """
    Detects the programming language of a file based on its extension.

    Args:
        file_path: The path to the file.

    Returns:
        The detected language as a Language enum member.
    """
    ext_map = {
        '.java': Language.JAVA,
        '.cs': Language.CSHARP,
        '.cpp': Language.CPP,
        '.cxx': Language.CPP,
        '.h': Language.CPP,
        '.hpp': Language.CPP,
        '.js': Language.JAVASCRIPT,
        '.mjs': Language.JAVASCRIPT,
        '.ts': Language.TYPESCRIPT,
        '.tsx': Language.TYPESCRIPT,
        '.py': Language.PYTHON,
        '.pyw': Language.PYTHON,
        '.rs': Language.RUST,
        '.kt': Language.KOTLIN,
        '.kts': Language.KOTLIN,
        '.scala': Language.SCALA,
        '.sc': Language.SCALA,
        '.swift': Language.SWIFT,
        '.rb': Language.RUBY,
        '.php': Language.PHP,
        '.fs': Language.FSHARP,
        '.hs': Language.HASKELL,
        '.go': Language.GO,
    }
    _, ext = os.path.splitext(file_path)
    return ext_map.get(ext.lower(), Language.UNKNOWN)


# List of Unicode characters to be used for injection.
# Sourced from https://trojansource.codes/ and NOSEEUMS_list.json
UNICODE_TROJANS = [
    '\u202A',  # LRE: LEFT-TO-RIGHT EMBEDDING
    '\u202B',  # RLE: RIGHT-TO-LEFT EMBEDDING
    '\u202C',  # PDF: POP DIRECTIONAL FORMATTING
    '\u202D',  # LRO: LEFT-TO-RIGHT OVERRIDE
    '\u202E',  # RLO: RIGHT-TO-LEFT OVERRIDE
    '\u2066',  # LRI: LEFT-TO-RIGHT ISOLATE
    '\u2067',  # RLI: RIGHT-TO-LEFT ISOLATE
    '\u2068',  # FSI: FIRST STRONG ISOLATE
    '\u2069',  # PDI: POP DIRECTIONAL ISOLATE
    '\u200B',  # ZERO WIDTH SPACE
    '\u200C',  # ZERO WIDTH NON-JOINER
    '\u200D',  # ZERO WIDTH JOINER
    '\u00AD',  # SOFT HYPHEN
]


def get_escape_sequence(hex_code: str, lang: Language) -> str:
    """
    Returns the language-specific escape sequence for a Unicode character.

    Args:
        hex_code: The hexadecimal representation of the Unicode character.
        lang: The programming language.

    Returns:
        The escaped Unicode character as a string.
    """
    if lang in [
        Language.JAVA,
        Language.JAVASCRIPT,
        Language.TYPESCRIPT,
        Language.PYTHON,
        Language.KOTLIN,
        Language.SCALA,
        Language.SWIFT,
        Language.RUBY,
        Language.PHP,
        Language.FSHARP,
        Language.HASKELL,
        Language.RUST,
        Language.GO,
    ]:
        return f'\\u{hex_code}'
    elif lang in [Language.CPP, Language.CSHARP]:
        return f'\\U{hex_code.zfill(8)}'
    else:
        # Default to a common format
        return f'\\u{hex_code}'


def inject_unicode_smuggler(code: str, lang: Language) -> str:
    """
    Injects Unicode Bidi override characters into strings and identifiers in the code.

    Args:
        code: The source code to modify.
        lang: The programming language of the code.

    Returns:
        The modified code with injected Unicode characters.
    """
    # This regex is designed to be language-agnostic and handle most common cases.
    pattern = re.compile(r'(?P<string>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')|(?P<comment>/\*[\s\S]*?\*/|//.*|#.*)|(?P<identifier>[a-zA-Z_]\w*)')

    def replace_match(match: re.Match) -> str:
        """
        Callback function for re.sub to replace matched strings and identifiers.
        """
        text = match.group(0)
        if match.lastgroup == 'string':
            # It's a string literal
            # Inject RLO and LRO characters at the beginning and end of the string
            rlo = get_escape_sequence('202E', lang)  # Right-to-Left Override
            lro = get_escape_sequence('202D', lang)  # Left-to-Right Override
            pdf = get_escape_sequence('202C', lang)  # Pop Directional Formatting
            return f'{text[0]}{rlo}{lro}{text[1:-1]}{pdf}{text[-1]}'
        elif match.lastgroup == 'comment':
            # It's a comment, leave it alone
            return text
        elif match.lastgroup == 'identifier':  # It's an identifier
            # Inject a Zero Width Space into the identifier
            zwsp = get_escape_sequence('200B', lang)
            return f'{text[0]}{zwsp}{text[1:]}'
        else:
            return text

    return pattern.sub(replace_match, code)


def clean_unicode_smuggler(code: str) -> str:
    """
    Removes injected Unicode Bidi override characters from the code.

    Args:
        code: The source code to clean.

    Returns:
        The cleaned code.
    """
    for trojan in UNICODE_TROJANS:
        code = code.replace(trojan, '')
    return code


def main():
    """
    Main function to parse arguments and run the script.
    """
    parser = argparse.ArgumentParser(
        description='A tool to inject or clean Unicode Trojan Source characters in source code files.'
    )
    parser.add_argument('file', help='The source code file to process.')
    parser.add_argument(
        '-c',
        '--clean',
        action='store_true',
        help='Clean the file of injected Unicode characters.',
    )
    parser.add_argument(
        '-i',
        '--inplace',
        action='store_true',
        help='Modify the file in place. A backup of the original file will be created.',
    )
    parser.add_argument(
        '-o',
        '--output',
        help='The path to the output file. Defaults to <original_name>_smuggled.<ext> or <original_name>_cleaned.<ext>.',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enable verbose output.',
    )

    args = parser.parse_args()

    file_path = args.file
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    lang = detect_language(file_path)
    if lang == Language.UNKNOWN:
        print(
            f"Warning: Unsupported language for file '{file_path}'. Proceeding with default settings.",
            file=sys.stderr,
        )

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        if args.clean:
            modified_code = clean_unicode_smuggler(code)
            action = 'cleaned'
        else:
            modified_code = inject_unicode_smuggler(code, lang)
            action = 'smuggled'

        if args.inplace:
            backup_path = f"{file_path}.bak"
            if args.verbose:
                print(f"Creating backup of '{file_path}' at '{backup_path}'")
            os.rename(file_path, backup_path)
            output_path = file_path
        elif args.output:
            output_path = args.output
        else:
            base, ext = os.path.splitext(file_path)
            output_path = f"{base}_{action}{ext}"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_code)

        if args.verbose:
            print(f"Successfully {action} '{file_path}'.")
        print(f"Output saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
