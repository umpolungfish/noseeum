from click.testing import CliRunner
from noseeum.detector.scanner import detect_command

def test_detect_bidi():
    """Tests the detection of Bidirectional control characters."""
    runner = CliRunner()
    # Using the pre-made malicious file
    result = runner.invoke(detect_command, ['--file', 'tests/test_data/malicious_bidi.txt'])
    assert result.exit_code == 0
    assert "VULNERABILITIES DETECTED" in result.output
    assert "Bidirectional Control character U+202E" in result.output

def test_detect_homoglyph():
    """Tests the detection of mixed-script homoglyphs in identifiers."""
    runner = CliRunner()
    result = runner.invoke(detect_command, ['--file', 'tests/test_data/malicious_homoglyph.txt'])
    assert result.exit_code == 0
    assert "VULNERABILITIES DETECTED" in result.output
    assert "Potential Homoglyph attack in identifier 'check_аccess'" in result.output
    assert "mixed scripts: CYRILLIC, LATIN" in result.output

def test_detect_zero_width(tmp_path):
    """Tests the detection of Zero-Width characters."""
    runner = CliRunner()
    p = tmp_path / "malicious_zw.txt"
    # Create a file with an invisible zero-width space
    p.write_text("This text has a hidden\u200b character.", encoding="utf-8")
    
    result = runner.invoke(detect_command, ['--file', str(p)])
    assert result.exit_code == 0
    assert "VULNERABILITIES DETECTED" in result.output
    assert "Zero-Width character U+200B" in result.output

def test_detect_clean_file():
    """Tests that a clean file passes the scan with no findings."""
    runner = CliRunner()
    result = runner.invoke(detect_command, ['--file', 'tests/test_data/clean_file.txt'])
    assert result.exit_code == 0
    assert "No common Unicode smuggling patterns were detected" in result.output
    assert "VULNERABILITIES DETECTED" not in result.output
