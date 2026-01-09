"""
Noseeum Formatter API Examples
================================
Demonstrates how to use the formatter module programmatically.
"""

from noseeum.formatter import CodeFormatter, format_code_file, format_code_directory
import json


def example_1_basic_formatting():
    """Example 1: Basic file formatting."""
    print("=" * 60)
    print("Example 1: Basic File Formatting")
    print("=" * 60)

    # Format a single file
    result = format_code_file(
        file_path="test_sample.py",
        output_path="output1.json",
        task="Basic formatting example"
    )

    print(f"✓ Formatted {result['total_generated']} file(s)")
    print(f"  Output: output1.json")
    print()


def example_2_with_obfuscation():
    """Example 2: Formatting with obfuscation."""
    print("=" * 60)
    print("Example 2: Formatting with Obfuscation")
    print("=" * 60)

    # Format with bidi obfuscation
    result = format_code_file(
        file_path="test_sample.py",
        output_path="output2_obfuscated.json",
        obfuscate=True,
        attack_type="bidi",
        task="Bidi obfuscation example"
    )

    print(f"✓ Formatted with {result['attack_type']} attack")
    print(f"  Obfuscation applied: {result['obfuscation_applied']}")
    print(f"  Output: output2_obfuscated.json")
    print()


def example_3_formatter_class():
    """Example 3: Using the CodeFormatter class."""
    print("=" * 60)
    print("Example 3: Using CodeFormatter Class")
    print("=" * 60)

    # Create formatter instance
    formatter = CodeFormatter(obfuscate=True, attack_type="homoglyph")

    # Format multiple files
    formatter.format_file("test_sample.py", description="Sample Python file")

    # Add a string payload
    formatter.format_string(
        code='print("Hello, World!")',
        language="python",
        description="Hello world example",
        metadata={
            "author": "security-team",
            "tags": ["example", "test"]
        }
    )

    # Build output
    output = formatter.build_output(task="Multi-payload example")

    # Save to file
    formatter.save_to_file("output3_multi.json")

    print(f"✓ Created {len(formatter.payloads)} payloads")
    print(f"  Output: output3_multi.json")
    print()


def example_4_batch_processing():
    """Example 4: Batch processing multiple files."""
    print("=" * 60)
    print("Example 4: Batch Processing")
    print("=" * 60)

    formatter = CodeFormatter()

    # Process multiple files
    files = ["test_sample.py"]  # Add more files as needed

    result = formatter.format_batch(
        file_paths=files,
        task="Batch processing example"
    )

    formatter.save_to_file("output4_batch.json")

    print(f"✓ Processed {result['total_generated']} file(s)")
    print(f"  Output: output4_batch.json")
    print()


def example_5_custom_metadata():
    """Example 5: Adding custom metadata."""
    print("=" * 60)
    print("Example 5: Custom Metadata")
    print("=" * 60)

    formatter = CodeFormatter()

    # Format with custom metadata
    formatter.format_file(
        "test_sample.py",
        metadata={
            "campaign": "test-2026",
            "target_system": "linux",
            "technique": "T1027",  # MITRE ATT&CK technique
            "tags": ["python", "test", "research"],
            "severity": "medium"
        }
    )

    formatter.save_to_file("output5_metadata.json")

    print("✓ Added custom metadata to payload")
    print("  Output: output5_metadata.json")
    print()


def example_6_inline_display():
    """Example 6: Display output without saving."""
    print("=" * 60)
    print("Example 6: Display Output (No Save)")
    print("=" * 60)

    formatter = CodeFormatter()
    formatter.format_string(
        code="def hello(): print('Hi')",
        language="python"
    )

    output = formatter.build_output(task="Quick display")

    print(json.dumps(output, indent=2))
    print()


def example_7_directory_processing():
    """Example 7: Process entire directory."""
    print("=" * 60)
    print("Example 7: Directory Processing")
    print("=" * 60)

    # Format all Python files in examples directory (if it exists)
    try:
        result = format_code_directory(
            directory="examples",
            output_path="output7_directory.json",
            pattern="**/*.py",
            task="Directory processing example"
        )

        print(f"✓ Processed directory")
        print(f"  Files found: {result['total_generated']}")
        print(f"  Output: output7_directory.json")
    except Exception as e:
        print(f"⚠ Could not process directory: {e}")

    print()


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "Noseeum Formatter API Examples" + " " * 17 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    examples = [
        example_1_basic_formatting,
        example_2_with_obfuscation,
        example_3_formatter_class,
        example_4_batch_processing,
        example_5_custom_metadata,
        example_6_inline_display,
        # example_7_directory_processing,  # Commented out - may not have examples dir
    ]

    for i, example in enumerate(examples, 1):
        try:
            example()
        except Exception as e:
            print(f"⚠ Example {i} failed: {e}\n")

    print("=" * 60)
    print("✓ All examples completed!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  - output1.json")
    print("  - output2_obfuscated.json")
    print("  - output3_multi.json")
    print("  - output4_batch.json")
    print("  - output5_metadata.json")
    print()


if __name__ == "__main__":
    main()
