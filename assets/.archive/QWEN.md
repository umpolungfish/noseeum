# Noseeum Framework - Development Context

## Project Overview

Noseeum is a modular offensive security framework designed for executing Unicode-based attacks. It consolidates various advanced obfuscation and exploitation techniques into a single, extensible command-line interface. The framework is built for precision, power, and operational security, targeting Unicode smuggling vulnerabilities in source code.

**Project Type**: Offensive Security Tool (Unicode-based exploitation framework)

**Primary Technologies**:
- Python 3 (primary implementation)
- Rust (secondary implementation for some components)
- Unicode control characters for attack vectors

## Architecture

The framework follows a modular architecture with the following key components:

### Core Components
- **CLI Module** (`noseeum/cli.py`): Main command-line interface using Click
- **Attack Modules** (`noseeum/attacks/`): Various attack vectors implemented as separate modules
- **Detector Module** (`noseeum/detector/`): Scanning and detection capabilities
- **Registry Data** (`homoglyph_registry.json`): Large database of homoglyph character mappings

### Attack Vectors
1. **Bidi (Bidirectional/Trojan Source)**: Hides malicious code using bidirectional Unicode characters
2. **Homoglyph**: Evades detection by substituting visually similar characters
3. **Invisible Ink**: Hides content steganographically within text
4. **Language-Specific Exploits**: Targets unique weaknesses in specific programming languages

### Additional Tools
- `smuggler.py`: Original implementation for injecting Unicode Bidi characters
- `glassworm.py`: Self-propagating worms using invisible code encoding
- `smuggler_dropper.py`: Dropper script for encoded payloads

## Building and Running

### Installation
```bash
make install
```
This command:
- Installs dependencies from `requirements.txt`
- Installs the `noseeum` package in editable mode
- Makes the `noseeum` command globally available

### Usage Examples
```bash
# Show all available commands
noseeum --help

# Show attack-specific commands
noseeum attack --help

# Scan a file for vulnerabilities
noseeum detect --file /path/to/your/file.js

# Execute a bidi attack
noseeum attack bidi --payload-code "malicious_code" --target-file target.js

# Execute homoglyph obfuscation
noseeum attack homoglyph --input-file input.py --output-file output.py --density 0.1
```

### Development Commands
- `make install`: Setup development environment
- `make uninstall`: Remove the `noseeum` package
- `make clean`: Delete build artifacts

## Development Conventions

### Code Structure
- All attack modules follow the same pattern with Click decorators
- Attack modules are self-contained in the `attacks` directory
- The detector module provides scanning functionality
- Configuration is handled via JSON files and command-line options

### Dependencies
- Primary: `click` for CLI framework
- Primary: `requests` for HTTP operations
- No complex dependency management beyond basic packages

### Data Files
- `homoglyph_registry.json`: Massive mapping of visually similar Unicode characters (19,000+ entries)
- `nfkc_map.json`: NFKC normalization mappings
- Other data files support various attack vectors

## Security and Ethical Considerations

Noseeum is designed as an offensive security tool for:
- Researching Unicode smuggling vulnerabilities
- Testing source code for bidirectional and homoglyph attacks
- Understanding potential security risks in code review processes

The framework implements several attack techniques that could be used maliciously, including:
- Trojan Source attacks (bidirectional text exploits)
- Homoglyph substitution for code obfuscation
- Invisible character encoding

## Testing and Validation

The framework includes:
- A detector module to identify Unicode smuggling vulnerabilities
- Command-line interface validation
- File processing error handling
- Cross-language support for multiple programming languages

## Maintenance Notes

- The framework requires careful handling due to its offensive nature
- Regular updates to Unicode character mappings may be necessary
- The homoglyph registry is a large file (>19K entries) that could impact performance
- Multiple stand-alone scripts (`smuggler.py`, `glassworm.py`) exist alongside the main framework