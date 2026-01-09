# Noseeum Code Formatter

The Noseeum formatter module provides a powerful way to convert source code files into properly formatted JSON for noseeum ingestion and processing.

## Features

- 🔍 **Auto-detection** - Automatically detects programming language from file extension
- 🎯 **Multiple input modes** - Format single files, directories, or code strings
- 🔐 **Built-in obfuscation** - Apply obfuscation techniques during formatting
- 📦 **Batch processing** - Process multiple files at once
- 🎨 **Template support** - Generate template JSON structures
- 🌍 **Multi-language** - Supports 15+ programming languages

## Installation

The formatter is included with noseeum. Make sure you have installed noseeum:

```bash
pip install -e .
```

## Quick Start

### Format a Single File

```bash
# Basic formatting
noseeum format file script.py -o output.json

# With obfuscation
noseeum format file script.py --obfuscate -a bidi -o output.json

# Show output without saving
noseeum format file script.py --show
```

### Format a Directory

```bash
# Format all Python files in a directory
noseeum format dir ./src output.json

# Format JavaScript files with pattern
noseeum format dir ./src output.json -p "**/*.js"

# With obfuscation
noseeum format dir ./src output.json --obfuscate -a homoglyph
```

### Format Multiple Specific Files

```bash
# Format specific files
noseeum format batch file1.py file2.py file3.py -o output.json

# With wildcards
noseeum format batch src/**/*.py -o output.json
```

### Format Code String Directly

```bash
# Format a code string
noseeum format string "print('hello')" -l python --show

# Save to file
noseeum format string "console.log('test')" -l javascript -o test.json
```

### View Template

```bash
# Show template structure
noseeum format template

# Save template to file
noseeum format template -l javascript -a bidi -o template.json
```

## Command Reference

### `noseeum format file`

Format a single source code file.

**Arguments:**
- `INPUT_FILE` - Path to source code file

**Options:**
- `-o, --output PATH` - Output JSON file path
- `-l, --language TEXT` - Programming language (auto-detected if not provided)
- `--obfuscate` - Apply obfuscation techniques
- `-a, --attack-type CHOICE` - Attack type: clean, bidi, homoglyph, normalization (default: clean)
- `-t, --task TEXT` - Task description
- `--minify` - Minify JSON output
- `--show` - Display JSON to console

### `noseeum format dir`

Format all code files in a directory.

**Arguments:**
- `DIRECTORY` - Directory to search
- `OUTPUT` - Output JSON file path

**Options:**
- `-p, --pattern TEXT` - Glob pattern (default: `**/*.py`)
- `-l, --language TEXT` - Programming language
- `--obfuscate` - Apply obfuscation techniques
- `-a, --attack-type CHOICE` - Attack type
- `-t, --task TEXT` - Task description
- `--minify` - Minify JSON output

### `noseeum format batch`

Format multiple specific files.

**Arguments:**
- `FILES...` - One or more file paths

**Options:**
- `-o, --output PATH` - Output JSON file path (required)
- `-l, --language TEXT` - Programming language
- `--obfuscate` - Apply obfuscation techniques
- `-a, --attack-type CHOICE` - Attack type
- `-t, --task TEXT` - Task description
- `--minify` - Minify JSON output

### `noseeum format string`

Format a code string directly.

**Arguments:**
- `CODE` - Code string to format

**Options:**
- `-l, --language TEXT` - Programming language (required)
- `-o, --output PATH` - Output JSON file path
- `--obfuscate` - Apply obfuscation techniques
- `-a, --attack-type CHOICE` - Attack type
- `-d, --description TEXT` - Code description
- `--minify` - Minify JSON output

### `noseeum format template`

Show a template JSON structure.

**Options:**
- `-l, --language CHOICE` - Programming language (default: python)
- `-a, --attack-type CHOICE` - Attack type (default: clean)
- `-o, --output PATH` - Save template to file

## Python API

You can also use the formatter programmatically:

```python
from noseeum.formatter import CodeFormatter, format_code_file, format_code_directory

# Format a single file
result = format_code_file(
    file_path="script.py",
    output_path="output.json",
    obfuscate=True,
    attack_type="bidi"
)

# Format a directory
result = format_code_directory(
    directory="./src",
    output_path="output.json",
    pattern="**/*.py",
    obfuscate=True
)

# Use the formatter class
formatter = CodeFormatter(obfuscate=True, attack_type="homoglyph")

# Format multiple files
formatter.format_file("file1.py")
formatter.format_file("file2.py")
formatter.format_file("file3.py")

# Build output
output = formatter.build_output(task="My task")

# Save to file
formatter.save_to_file("output.json")
```

## Supported Languages

The formatter automatically detects the following languages based on file extensions:

| Language | Extension(s) |
|----------|-------------|
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| Go | `.go` |
| Rust | `.rs` |
| C | `.c` |
| C++ | `.cpp` |
| C# | `.cs` |
| Ruby | `.rb` |
| PHP | `.php` |
| Kotlin | `.kt` |
| Swift | `.swift` |
| Bash | `.sh` |
| SQL | `.sql` |
| HTML | `.html` |
| CSS | `.css` |

## Attack Types

### `clean`
No obfuscation applied. Code is formatted as-is.

### `bidi`
Applies bidirectional text attacks using Unicode RLO/LRO marks.

### `homoglyph`
Substitutes characters with visually similar Unicode characters.

### `normalization`
Exploits Unicode normalization inconsistencies.

## Output Format

The formatter produces JSON in the following structure:

```json
{
  "task": "Task description",
  "payloads": [
    {
      "id": 0,
      "payload": "# Your code here",
      "attack_type": "bidi",
      "language": "python",
      "source_file": "example.py",
      "naturalness_score": 0.8,
      "description": "Optional description",
      "metadata": {
        "custom": "fields"
      }
    }
  ],
  "total_generated": 1,
  "status": "success",
  "agent": "Code Formatter",
  "timestamp": "2026-01-08T00:00:00",
  "obfuscation_applied": true,
  "attack_type": "bidi"
}
```

## Examples

### Example 1: Basic Formatting

```bash
# Create a sample Python file
echo 'print("Hello, world!")' > hello.py

# Format it
noseeum format file hello.py -o hello.json

# View the output
cat hello.json
```

### Example 2: Obfuscation

```bash
# Format with bidi obfuscation
noseeum format file script.py --obfuscate -a bidi -o obfuscated.json

# The output will contain bidi control characters
```

### Example 3: Batch Processing

```bash
# Format all Python files in a project
noseeum format dir ./my_project output.json -p "**/*.py"

# Result: All Python files combined into one JSON
```

### Example 4: Integration with Noseeum Agents

```bash
# Format code for agent ingestion
noseeum format file malicious.py -o payload.json --obfuscate -a homoglyph

# Then use with agents
python -m agents.orchestrator run --agent payload_artisan --task "Process payload" --input payload.json
```

## Tips & Best Practices

1. **Use templates** - Start with `noseeum format template` to understand the structure
2. **Auto-detect languages** - Let the formatter detect languages automatically for better accuracy
3. **Batch similar files** - Process files of the same language together
4. **Preserve originals** - Always keep original source files when applying obfuscation
5. **Test payloads** - Test generated payloads before using them in production
6. **Document metadata** - Use the metadata field to track payload provenance

## Advanced Usage

### Custom Metadata

```python
from noseeum.formatter import CodeFormatter

formatter = CodeFormatter()
formatter.format_file(
    "script.py",
    metadata={
        "author": "security-team",
        "campaign": "test-2026",
        "target": "system-x",
        "tags": ["test", "bidi", "python"]
    }
)
```

### Chaining with Other Tools

```bash
# Format, then scan for vulnerabilities
noseeum format file script.py -o temp.json
noseeum detect temp.json

# Format, then send to agent for processing
noseeum format dir ./src payload.json --obfuscate -a bidi
python -m agents.orchestrator run --agent payload_artisan --input payload.json
```

## Troubleshooting

### File encoding errors

If you encounter encoding errors, the formatter will automatically try multiple encodings (UTF-8, Latin-1, CP1252, ISO-8859-1).

### Language not detected

Specify the language explicitly with `-l`:

```bash
noseeum format file script.txt -l python -o output.json
```

### Large directories

For very large directories, use specific patterns to limit scope:

```bash
# Instead of processing everything
noseeum format dir ./huge_project output.json -p "src/**/*.py"
```

## Contributing

To add support for new languages or attack types:

1. Update `LANGUAGE_MAP` in `noseeum/formatter.py`
2. Implement the obfuscation method in `_apply_obfuscation()`
3. Add tests
4. Submit a pull request

## License

See main LICENSE file.
