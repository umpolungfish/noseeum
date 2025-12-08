from click.testing import CliRunner
from noseeum.attacks.homoglyph import homoglyph
import json

# Load the homoglyph map to check for specific character substitutions
with open('homoglyph_registry.json', 'r', encoding='utf-8') as f:
    HOMOGLYPH_MAP = json.load(f)

# Get a set of all possible homoglyph characters for easy checking
ALL_HOMOGLYPH_CHARS = {item for sublist in HOMOGLYPH_MAP.values() for item in sublist}

def test_homoglyph_obfuscation(tmp_path):
    """Tests that the homoglyph command successfully obfuscates a file."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    original_content = "some text to obfuscate with common letters"
    input_file.write_text(original_content)

    # Run with high density to ensure substitution
    result = runner.invoke(homoglyph, [
        '--input-file', str(input_file),
        '--output-file', str(output_file),
        '--density', '1.0'
    ])
    
    assert result.exit_code == 0
    assert "Homoglyph obfuscation complete" in result.output
    
    obfuscated_content = output_file.read_text(encoding="utf-8")
    assert original_content != obfuscated_content
    
    # Check that at least one substituted character exists in the output
    assert any(c in ALL_HOMOGLYPH_CHARS for c in obfuscated_content)

def test_homoglyph_density_zero(tmp_path):
    """Tests that density 0.0 results in no changes."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    original_content = "some text that should not change"
    input_file.write_text(original_content)

    result = runner.invoke(homoglyph, [
        '--input-file', str(input_file),
        '--output-file', str(output_file),
        '--density', '0.0'
    ])
    
    assert result.exit_code == 0
    obfuscated_content = output_file.read_text(encoding="utf-8")
    assert original_content == obfuscated_content

def test_homoglyph_file_not_found():
    """Tests the command's failure on a non-existent input file."""
    runner = CliRunner()
    result = runner.invoke(homoglyph, [
        '--input-file', 'non_existent_file.txt',
        '--output-file', 'output.txt'
    ])
    
    assert result.exit_code != 0
    # Click automatically provides an error message for non-existent files
    assert "Error: Invalid value for '--input-file'" in result.output
