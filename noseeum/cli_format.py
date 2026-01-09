"""
Noseeum Format CLI Command
===========================
Command-line interface for the code formatter module.
"""

import click
import json
from pathlib import Path
from noseeum.formatter import CodeFormatter, format_code_file, format_code_directory


@click.group(name='format')
def format_cli():
    """Format source code into noseeum-compatible JSON."""
    pass


@format_cli.command(name='file')
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output JSON file path')
@click.option('-l', '--language', type=str, help='Programming language (auto-detected if not provided)')
@click.option('--obfuscate', is_flag=True, help='Apply obfuscation techniques')
@click.option('-a', '--attack-type', type=click.Choice(['clean', 'bidi', 'homoglyph', 'normalization']),
              default='clean', help='Attack type to apply')
@click.option('-t', '--task', type=str, help='Task description')
@click.option('--minify', is_flag=True, help='Minify JSON output (no pretty-printing)')
@click.option('--show', is_flag=True, help='Display JSON output to console')
def format_file(input_file, output, language, obfuscate, attack_type, task, minify, show):
    """
    Format a single source code file into noseeum JSON.

    Example:
        noseeum format file script.py -o output.json
        noseeum format file script.py --obfuscate -a bidi --show
    """
    # Auto-generate output path if not provided
    if not output and not show:
        input_path = Path(input_file)
        output = input_path.with_suffix('.noseeum.json')

    # Format the file
    result = format_code_file(
        file_path=input_file,
        output_path=output if not show else None,
        language=language,
        obfuscate=obfuscate,
        attack_type=attack_type,
        task=task,
        pretty=not minify
    )

    if show:
        click.echo(json.dumps(result, indent=2 if not minify else None, ensure_ascii=False))

    if output:
        click.secho(f"✓ Formatted file saved to: {output}", fg='green')
        click.echo(f"  Total payloads: {result['total_generated']}")
        click.echo(f"  Attack type: {result['attack_type']}")


@format_cli.command(name='dir')
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.argument('output', type=click.Path())
@click.option('-p', '--pattern', type=str, default='**/*.py', help='Glob pattern for files (default: **/*.py)')
@click.option('-l', '--language', type=str, help='Programming language (auto-detected if not provided)')
@click.option('--obfuscate', is_flag=True, help='Apply obfuscation techniques')
@click.option('-a', '--attack-type', type=click.Choice(['clean', 'bidi', 'homoglyph', 'normalization']),
              default='clean', help='Attack type to apply')
@click.option('-t', '--task', type=str, help='Task description')
@click.option('--minify', is_flag=True, help='Minify JSON output')
def format_directory(directory, output, pattern, language, obfuscate, attack_type, task, minify):
    """
    Format all code files in a directory into noseeum JSON.

    Example:
        noseeum format dir ./src output.json
        noseeum format dir ./src output.json -p "**/*.js" --obfuscate
    """
    result = format_code_directory(
        directory=directory,
        output_path=output,
        pattern=pattern,
        language=language,
        obfuscate=obfuscate,
        attack_type=attack_type,
        task=task,
        pretty=not minify
    )

    click.secho(f"✓ Batch formatting complete!", fg='green')
    click.echo(f"  Output saved to: {output}")
    click.echo(f"  Total files processed: {result['total_generated']}")
    click.echo(f"  Pattern used: {pattern}")
    click.echo(f"  Attack type: {result['attack_type']}")


@format_cli.command(name='string')
@click.argument('code', type=str)
@click.option('-l', '--language', type=str, required=True, help='Programming language')
@click.option('-o', '--output', type=click.Path(), help='Output JSON file path')
@click.option('--obfuscate', is_flag=True, help='Apply obfuscation techniques')
@click.option('-a', '--attack-type', type=click.Choice(['clean', 'bidi', 'homoglyph', 'normalization']),
              default='clean', help='Attack type to apply')
@click.option('-d', '--description', type=str, help='Code description')
@click.option('--minify', is_flag=True, help='Minify JSON output')
def format_string(code, language, output, obfuscate, attack_type, description, minify):
    """
    Format a code string directly into noseeum JSON.

    Example:
        noseeum format string "print('hello')" -l python --show
        noseeum format string "console.log('test')" -l javascript -o test.json
    """
    formatter = CodeFormatter(obfuscate=obfuscate, attack_type=attack_type)
    formatter.format_string(code, language=language, description=description)
    result = formatter.build_output(task="String formatting")

    if output:
        formatter.save_to_file(output, pretty=not minify)
        click.secho(f"✓ Formatted output saved to: {output}", fg='green')
    else:
        click.echo(json.dumps(result, indent=2 if not minify else None, ensure_ascii=False))


@format_cli.command(name='batch')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), required=True, help='Output JSON file path')
@click.option('-l', '--language', type=str, help='Programming language (auto-detected if not provided)')
@click.option('--obfuscate', is_flag=True, help='Apply obfuscation techniques')
@click.option('-a', '--attack-type', type=click.Choice(['clean', 'bidi', 'homoglyph', 'normalization']),
              default='clean', help='Attack type to apply')
@click.option('-t', '--task', type=str, help='Task description')
@click.option('--minify', is_flag=True, help='Minify JSON output')
def format_batch(files, output, language, obfuscate, attack_type, task, minify):
    """
    Format multiple specific files into noseeum JSON.

    Example:
        noseeum format batch file1.py file2.py file3.py -o output.json
        noseeum format batch *.js -o output.json --obfuscate -a bidi
    """
    if not files:
        click.secho("Error: No files provided", fg='red')
        return

    formatter = CodeFormatter(obfuscate=obfuscate, attack_type=attack_type)
    result = formatter.format_batch(list(files), language=language, task=task)
    formatter.save_to_file(output, task=task, pretty=not minify)

    click.secho(f"✓ Batch formatting complete!", fg='green')
    click.echo(f"  Output saved to: {output}")
    click.echo(f"  Total files processed: {result['total_generated']}")
    click.echo(f"  Attack type: {result['attack_type']}")


@format_cli.command(name='template')
@click.option('-l', '--language', type=click.Choice(['python', 'javascript', 'java', 'go', 'rust']),
              default='python', help='Programming language')
@click.option('-a', '--attack-type', type=click.Choice(['clean', 'bidi', 'homoglyph', 'normalization']),
              default='clean', help='Attack type')
@click.option('-o', '--output', type=click.Path(), help='Save template to file')
def show_template(language, attack_type, output):
    """
    Show a template JSON structure for noseeum ingestion.

    Example:
        noseeum format template
        noseeum format template -l javascript -a bidi -o template.json
    """
    template = {
        "task": "Example task description",
        "language": language,
        "attack_type": attack_type,
        "payloads": [
            {
                "id": 0,
                "payload": "# Your code here" if language == "python" else "// Your code here",
                "attack_type": attack_type,
                "language": language,
                "source_file": "example.py" if language == "python" else f"example.{language[:2]}",
                "naturalness_score": 0.8,
                "description": "Example payload",
                "metadata": {
                    "author": "your-name",
                    "timestamp": "2026-01-08T00:00:00",
                    "tags": ["example", "template"]
                }
            }
        ],
        "total_generated": 1,
        "status": "success",
        "agent": "Code Formatter"
    }

    if output:
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=2, ensure_ascii=False)
        click.secho(f"✓ Template saved to: {output}", fg='green')
    else:
        click.echo(json.dumps(template, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    format_cli()
