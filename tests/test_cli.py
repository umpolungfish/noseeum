from click.testing import CliRunner
from noseeum.cli import main

def test_main_cli():
    """Test the main entry point."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'Noseeum: A Unified Framework for Unicode-Based Exploitation.' in result.output

def test_attack_group():
    """Test the 'attack' command group."""
    runner = CliRunner()
    result = runner.invoke(main, ['attack', '--help'])
    assert result.exit_code == 0
    assert 'A group of commands for various attack vectors.' in result.output
    assert 'bidi' in result.output
    assert 'homoglyph' in result.output
    assert 'invisible' in result.output
    assert 'language' in result.output

def test_detect_command():
    """Test the 'detect' command."""
    runner = CliRunner()
    result = runner.invoke(main, ['detect', '--help'])
    assert result.exit_code == 0
    assert 'Scans a specified file for various Unicode smuggling vulnerabilities.' in result.output

def test_invisible_subcommands():
    """Test the subcommands of the 'invisible' group."""
    runner = CliRunner()
    result = runner.invoke(main, ['attack', 'invisible', '--help'])
    assert result.exit_code == 0
    assert 'stego-encode' in result.output
    assert 'stego-decode' in result.output
    assert 'llm-jailbreak' in result.output

def test_language_subcommands():
    """Test the subcommands of the 'language' group."""
    runner = CliRunner()
    result = runner.invoke(main, ['attack', 'language', '--help'])
    assert result.exit_code == 0
    assert 'py-nfkc' in result.output
    assert 'js-permissive-id' in result.output
    assert 'java-unicode-escape' in result.output
