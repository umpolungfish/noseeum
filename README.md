# Noseeum: A Unified Framework for Unicode-Based Exploitation

Noseeum is a modular offensive security framework designed for executing Unicode-based attacks. This tool consolidates a range of advanced obfuscation and exploitation techniques into a single, extensible command-line interface. It is built for precision, power, and operational security.

---

## Features

- **Unified CLI**: A single, clean command-line interface powered by Python's `click` library.
- **Modular Architecture**: Each attack vector is a self-contained module, allowing for rapid development and integration of new exploits.
- **Multiple Attack Vectors**:
    - **Bidi (Trojan Source)**: Make malicious code appear as harmless comments.
    - **Homoglyph**: Evade signature-based detection and confuse human analysts by substituting characters with visually identical ones.
    - **Invisible Ink**: Hide payloads steganographically within benign text or generate imperceptible prompts to jailbreak LLMs.
    - **Language-Specific Exploits**: Target unique weaknesses in Python, JavaScript, and Java.
- **Enhanced Security**: Improved security measures including safe code execution, path validation, and input sanitization.
- **Performance Optimizations**: Registry caching and efficient string processing for better performance.
- **Detection Module**: Includes a scanner to identify the presence of these same Unicode smuggling vulnerabilities in source code.
- **Configurable Settings**: Centralized configuration system allows for customizable paths and parameters.
- **Globally Installable**: Can be installed as a system-wide command-line tool using pip.

---

## Installation

### Global Installation (Recommended)

Noseeum can be installed as a globally accessible command-line tool:

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd noseeum
    ```

2. **Install required data files:**
    Before using the framework, you need to generate the required registry files:
    ```bash
    python3 create_registry.py      # Creates homoglyph_registry.json
    python3 create_nfkc_map.py      # Creates nfkc_map.json
    ```

3. **Install the package:**
    ```bash
    pip install .
    ```
    or using the Makefile:
    ```bash
    make install
    ```

This will install the `noseeum` command globally on your system, making it accessible from any directory.

### Uninstallation

To remove the globally installed package:
```bash
make uninstall
```

---

## Basic Usage

All functionality is accessed through the `noseeum` command.

**View all available commands:**
```bash
noseeum --help
```

**View attack-specific commands:**
```bash
noseeum attack --help
```

**Scan a file for vulnerabilities:**
```bash
noseeum detect --file /path/to/your/file.js
```

For a complete breakdown of every command, option, and argument, refer to the [**USAGE.md**](./docs/USAGE.md) document.

---

## Security Improvements

The framework has been enhanced with several security measures:

- **Safe Code Execution**: The `exec()` vulnerability in glassworm has been replaced with safer AST-based validation and restricted namespaces.
- **Path Validation**: Directory traversal attacks are prevented with proper path validation.
- **Input Sanitization**: Payloads are now sanitized to prevent injection attacks.
- **Encoding Detection**: Automatic encoding detection prevents issues with different file encodings.

---

## Performance Improvements

- **Registry Caching**: The homoglyph registry is now cached to avoid repeated file loading.
- **Efficient Processing**: Improved string processing algorithms for faster execution.
- **Configurable Settings**: Centralized configuration for optimized parameters.

---

## Development

This project uses a `Makefile` to streamline common development tasks.

-   **`make install`**: Sets up the development environment, installs dependencies from `requirements.txt`, creates required data files, and installs the `noseeum` package in editable mode.
-   **`make uninstall`**: Removes the `noseeum` package from your system.
-   **`make clean`**: Deletes all build artifacts, such as `build/`, `dist/`, and `.egg-info/` directories.

---

## Package Structure

The framework is organized as follows:
- `noseeum/`: Main Python package containing:
  - `attacks/`: Individual modules for each attack vector
  - `detector/`: Scanning and detection functionality
  - `utils/`: Helper utilities and error handling
  - `data/`: Embedded data files (homoglyph_registry.json, nfkc_map.json)
- `create_registry.py`: Script to generate the homoglyph registry
- `create_nfkc_map.py`: Script to generate the NFKC mapping
- `smuggler.py`, `glassworm.py`, `smuggler_dropper.py`: Standalone scripts with specific attack techniques
