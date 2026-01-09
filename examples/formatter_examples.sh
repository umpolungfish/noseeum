#!/bin/bash
# Noseeum Formatter Examples
# ==========================
# Demonstrates various ways to use the noseeum formatter

echo "Noseeum Formatter Examples"
echo "=========================="
echo ""

# Example 1: Basic file formatting
echo "1. Format a single file (basic)"
echo "   noseeum format file script.py -o output.json"
echo ""

# Example 2: Format with obfuscation
echo "2. Format with bidi obfuscation"
echo "   noseeum format file script.py --obfuscate -a bidi -o obfuscated.json"
echo ""

# Example 3: Format and display
echo "3. Format and display without saving"
echo "   noseeum format file script.py --show"
echo ""

# Example 4: Format directory
echo "4. Format entire directory"
echo "   noseeum format dir ./src output.json"
echo ""

# Example 5: Format with pattern
echo "5. Format JavaScript files only"
echo "   noseeum format dir ./src output.json -p '**/*.js'"
echo ""

# Example 6: Batch format specific files
echo "6. Format multiple specific files"
echo "   noseeum format batch file1.py file2.py file3.py -o batch.json"
echo ""

# Example 7: Format string
echo "7. Format code string directly"
echo "   noseeum format string 'print(\"hello\")' -l python --show"
echo ""

# Example 8: View template
echo "8. View JSON template"
echo "   noseeum format template"
echo ""

# Example 9: Complete workflow
echo "9. Complete workflow - Format, obfuscate, and use with agents"
echo "   # Step 1: Format with obfuscation"
echo "   noseeum format file payload.py --obfuscate -a homoglyph -o payload.json"
echo ""
echo "   # Step 2: Use with noseeum agent"
echo "   python -m agents.orchestrator run --agent payload_artisan --input payload.json"
echo ""

# Python API examples
echo "10. Python API usage"
cat << 'PYTHON'
# Example Python code
from noseeum.formatter import CodeFormatter, format_code_file

# Quick single file format
result = format_code_file("script.py", output_path="output.json")

# Advanced usage with formatter class
formatter = CodeFormatter(obfuscate=True, attack_type="bidi")
formatter.format_file("file1.py")
formatter.format_file("file2.py")
formatter.save_to_file("combined.json", task="Multi-file processing")
PYTHON
