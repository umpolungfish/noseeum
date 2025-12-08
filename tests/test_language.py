from click.testing import CliRunner
from noseeum.attacks.language import language

def test_py_nfkc_generation():
    """Tests the generation of NFKC variants."""
    runner = CliRunner()
    identifier = "test"
    count = 5
    result = runner.invoke(language, [
        'py-nfkc',
        '--identifier', identifier,
        '--count', str(count)
    ])
    
    assert result.exit_code == 0
    assert "GENERATED VARIANTS" in result.output
    
    lines = result.output.splitlines()
    # Find where the variants start
    variant_lines = [line for line in lines if "GENERATED VARIANTS" not in line and "---" not in line and line.strip()]
    
    # It might generate fewer if the identifier is short and collisions are high
    assert len(variant_lines) > 0 
    assert all(line != identifier for line in variant_lines)

def test_js_permissive_id_obfuscation(tmp_path):
    """Tests the JS identifier obfuscation."""
    runner = CliRunner()
    input_file = tmp_path / "test.js"
    output_file = tmp_path / "obfuscated.js"
    original_content = "function helloWorld() { const test = 1; }"
    input_file.write_text(original_content)
    
    result = runner.invoke(language, [
        'js-permissive-id',
        '--input-file', str(input_file),
        '--output-file', str(output_file)
    ])
    
    assert result.exit_code == 0
    assert output_file.exists()
    
    obfuscated_content = output_file.read_text(encoding="utf-8")
    # Check for a character from our hardcoded Japanese map
    assert 'く' in obfuscated_content or 'と' in obfuscated_content
    assert "helloWorld" not in obfuscated_content

def test_java_unicode_escape(tmp_path):
    """Tests the Java Unicode escape obfuscation."""
    runner = CliRunner()
    input_file = tmp_path / "Test.java"
    output_file = tmp_path / "Obfuscated.java"
    original_content = "public class Test { }"
    input_file.write_text(original_content)
    
    result = runner.invoke(language, [
        'java-unicode-escape',
        '--input-file', str(input_file),
        '--output-file', str(output_file),
        '--probability', '1.0' # Ensure everything is escaped
    ])
    
    assert result.exit_code == 0
    assert output_file.exists()
    
    obfuscated_content = output_file.read_text(encoding="utf-8")
    assert "\\u0070\\u0075\\u0062\\u006c\\u0069\\u0063" in obfuscated_content # "public"
    # The original characters should not be present
    assert "public" not in obfuscated_content
