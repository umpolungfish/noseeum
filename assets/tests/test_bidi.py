from click.testing import CliRunner
from noseeum.attacks.bidi import bidi

def test_bidi_injection_append(tmp_path):
    """Tests that the bidi command injects a payload to the end of a file."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    original_content = "line 1\nline 2"
    input_file.write_text(original_content)
    
    payload = "system('reboot')"
    
    result = runner.invoke(bidi, [
        '--payload-code', payload,
        '--target-file', str(input_file)
    ])
    
    assert result.exit_code == 0
    assert "Appending payload to end of file" in result.output
    
    new_content = input_file.read_text(encoding="utf-8")
    assert original_content in new_content
    # Check for the key components of the bidi attack
    assert '\u202e' in new_content # RLO character
    assert payload in new_content

def test_bidi_injection_line_number(tmp_path):
    """Tests that the bidi command injects a payload at a specific line."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    original_content = "line 1\nline 3"
    input_file.write_text(original_content)
    
    payload = "injected_code"
    
    result = runner.invoke(bidi, [
        '--payload-code', payload,
        '--target-file', str(input_file),
        '--line-number', '2'
    ])
    
    assert result.exit_code == 0
    assert "Injecting payload at line 2" in result.output
    
    lines = input_file.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 3
    assert "line 1" in lines[0]
    assert payload in lines[1] # Check that the payload is on the second line
    assert "line 3" in lines[2]

def test_bidi_custom_comment(tmp_path):
    """Tests the custom comment style options."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    input_file.write_text("some code")
    
    result = runner.invoke(bidi, [
        '--payload-code', 'payload',
        '--target-file', str(input_file),
        '--comment-start', '<!--',
        '--comment-end', '-->'
    ])
    
    assert result.exit_code == 0
    new_content = input_file.read_text(encoding="utf-8")
    assert '<!--' in new_content
    assert '-->' in new_content
