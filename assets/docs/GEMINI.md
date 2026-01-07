# Project Overview

This project, "Noseeums," is a Python-based tool for demonstrating and executing "Unicode Smuggling" attacks. The core of the project is the `smuggler.py` script, which injects invisible or misleading Unicode characters into the source code of various programming languages. This can be used to obfuscate code, bypass static analysis tools, and create Trojan Source vulnerabilities.

The project includes:

*   **`noseeums.md`**: A markdown file containing the `smuggler.py` script, a detailed explanation of its functionality, and examples of its use.
*   **`NOSEEUMS_list.json`**: A JSON file containing data on which programming languages are vulnerable to this type of attack, and a list of the Unicode characters that are most effective for this purpose.

## Building and Running

The `smuggler.py` script can be executed directly from the command line.

**To run the script:**

1.  Extract the python code from `noseeums.md` and save it as `smuggler.py`.
2.  Run the script with the following command:

```bash
python smuggler.py <file_to_smuggle>
```

For example, to smuggle a Java file named `example.java`, you would run:

```bash
python smuggler.py example.java
```

The script will create a new file with the `_smuggled` suffix (e.g., `example_smuggled.java`) containing the obfuscated code.

## Development Conventions

The project follows standard Python coding conventions. The `smuggler.py` script is well-documented and includes type hinting. The data in `NOSEEUMS_list.json` is structured for easy parsing and use by the script.
