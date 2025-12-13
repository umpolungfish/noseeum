<div align="center">
  <h1>noseeum</h1>
  <p><b>A FRAMEWORK FOR UNICODE-BASED EXPLOITATION</b></p>

![noseeum](https://imgur.com/pUsCMHQ)
</div>

<div align="center">

  ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
  &nbsp;
  ![Unicode](https://img.shields.io/badge/Unicode-%23000000.svg?style=for-the-badge&logo=unicode&logoColor=white)
  &nbsp;
  ![Security](https://img.shields.io/badge/Security-Offensive-%23FF0000.svg?style=for-the-badge)
  &nbsp;
  ![Cross-Platform](https://img.shields.io/badge/Cross--Platform-Windows%20%7C%20Linux%20%7C%20macOS-%230071C5.svg?style=for-the-badge)

</div>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#basic-usage">Usage</a> •
  <a href="#security-improvements">Security</a> •
  <a href="#performance-improvements">Performance</a> •
  <a href="#development">Development</a> •
  <a href="#package-structure">Structure</a>
</p>

<hr>

## OVERVIEW

**Primary Function:** Execute Unicode smuggling attacks including Trojan Source, homoglyph substitution, and invisible character encoding to hide malicious code in plain sight

`noseeum` is a modular offensive security framework for executing Unicode-based attacks  

`noseeum` encodes their payload in the same/similar fashion as exhibited in the "GlassWorm" malware of late 2025  

`noseeum` employs a range of obfuscation and encoding techniques into an extensible CLI  

## NOSEEUM IN ACTION

Below is a screencap of the VirusTotal analysis of the unencoded powershell malware (BEFORE processing with `noseeum`) as well as its "MITRE ATT&CK Tactics and Techniques" Chart  

+ **NOTE THE `8/62` DETECTION RATE**
+ HASH = `f6adc7db3ce7e756bcfd995c6bfeae1480e4626ab4c049644754903e2610a104`

![noseeum](./images/boomboom_before.png)
</div>

![noseeum](./images/boomboom_before_MITRE.png)
</div>

Below is a screencap of the VirusTotal analysis of the `Zero Width Character`-encoded powershell malware (AFTER processing with `noseeum`) as well as its "MITRE ATT&CK Tactics and Techniques" Chart 

+ **NOTE THE `0/62` DETECTION RATE**
+ HASH = `b700553732b9c8c2843885dc4f1122d2471beac47d682e67863f81cbb6d9a55f`

![noseeum](./images/boomboom_after.png)
</div>

![noseeum](./images/boomboom_after.png)
</div>  

## FEATURES

### Unified Command-Line Interface
Noseeum provides a single, clean command-line interface powered by Python's `click` library

- **Modular Architecture**: Each attack vector is a self-contained module, allowing for rapid development and integration of new exploits  

- **Multiple Attack Vectors**:  

    - **`Bidi (Trojan Source)`**: Make malicious code appear as harmless comments
    - **`Homoglyph`**: Evade signature-based detection and confuse human analysts by substituting characters with visually identical ones
    - **`Invisible Ink`**: Hide payloads steganographically within benign text or generate imperceptible prompts to jailbreak LLMs
    - **`File Steganography`**: Encode entire files as zero-width character sequences and decode them back
    - **`Language-Specific Exploits`**: Target unique weaknesses in Python, JavaScript, and Java
    - **`Normalization Exploitation`**: Craft payloads that normalize differently across system components (parser vs. scanner)
    - **`Unassigned Planes / Variation Selectors`**: Generate syntactically valid identifiers using characters from unassigned Unicode planes (U+20000–U+2FFFD)
    - **`Payload-injection via Identifier Characters`**: Encode malicious data within language constructs like object properties, class names, or function names  

- **Advanced Language Modules**:  

    - **`Go`**: Exploits Go's configurable lexer and permissive Unicode handling
    - **`Kotlin`**: Uses permissive frontend with restrictive backend to create compilation-failing code
    - **`JavaScript`**: Performs AST-level manipulations and low-entropy payload generation
    - **`Swift`**: Leverages ambiguous identifier handling and unassigned planes support  

- **Globally Installable`**: Can be installed as a system-wide command-line tool using pip

### Detection and Scanning Module  

Includes a scanner to identify the presence of these same Unicode smuggling vulnerabilities in source code

- **File Vulnerability Scanning**: Scan individual files for Unicode smuggling vulnerabilities
- **Multi-Language Support**: Detect vulnerabilities across Python, JavaScript, Java, and other languages
- **Comprehensive Detection**: Identifies various types of Unicode exploits including Bidi, homoglyphs, and invisible characters

## INSTALLATION

### Global Installation (Recommended)

`noseeum` can be installed as a globally accessible command-line tool:

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

This will install the `noseeum` command globally on your system, making it accessible from any directory

### Uninstallation

To remove the globally installed package:
```bash
make uninstall
```

## BASIC USAGE

All functionality is accessed through the `noseeum` command

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

For a complete breakdown of every command, option, and argument, refer to the [**USAGE.md**](./docs/USAGE.md) document
 
## DEVELOPMENT

This project uses a `Makefile` to streamline common development tasks.

-   **`make install`**: Sets up the development environment, installs dependencies from `requirements.txt`, creates required data files, and installs the `noseeum` package in editable mode
-   **`make uninstall`**: Removes the `noseeum` package from your system
-   **`make clean`**: Deletes all build artifacts, such as `build/`, `dist/`, and `.egg-info/` directories

## PACKAGE STRUCTURE

The framework is organized as follows:
- `noseeum/`: Main Python package containing:
  - `attacks/`: Individual modules for each attack vector
  - `core/`: Core engine, grammar database, and integration components
  - `detector/`: Scanning and detection functionality
  - `utils/`: Helper utilities and error handling
  - `data/`: Embedded data files (homoglyph_registry.json, nfkc_map.json)
- `create_registry.py`: Script to generate the homoglyph registry
- `create_nfkc_map.py`: Script to generate the NFKC mapping

## RECENT IMPROVEMENTS

### Code Quality & Reliability (Latest)
- **Fixed critical logic bug** in homoglyph identifier replacement that could cause incorrect output
- **Added Python 3.8+ compatibility** by replacing Python 3.9+ type annotations
- **Improved error handling** by replacing bare except clauses with proper exception types
- **Consolidated duplicate code** by moving file encoding logic to shared utilities
- **Enhanced CLI consistency** by standardizing error output with click.echo()
- **Completed language support** by adding grammar definitions for Java, Rust, C, and C++
- **Improved path validation** with more reliable directory traversal prevention
- **Added pytest dependency** to requirements for proper test execution

### Testing
Run the test suite with:
```bash
pip install -e ".[dev]"  # Install with dev dependencies
pytest tests/
```

## LICENSE

`noseeum` is sicced upon the Whyrld under the ![UNLICENSE](./UNLICENSE)