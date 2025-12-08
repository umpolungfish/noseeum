"""
Common error handling utilities for the Noseeum framework.
"""

import click
import os
from typing import Union, Optional


class NoseeumError(Exception):
    """Base exception class for Noseeum framework."""
    pass


class FileValidationError(NoseeumError):
    """Exception raised when file validation fails."""
    pass


def validate_file_path(file_path: str, check_exists: bool = True) -> str:
    """
    Validates a file path to prevent directory traversal and ensure it exists.
    
    Args:
        file_path: The file path to validate
        check_exists: Whether to check if the file exists (default True)
    
    Returns:
        The validated absolute file path
        
    Raises:
        FileValidationError: If the path is invalid or file doesn't exist
    """
    # Convert to absolute path
    abs_path = os.path.abspath(file_path)
    
    # Check for directory traversal
    current_dir = os.path.abspath('.')
    if not os.path.commonpath([abs_path, current_dir]) == current_dir:
        raise FileValidationError(f"File path '{file_path}' is outside the allowed directory.")
    
    # Check if file exists if requested
    if check_exists and not os.path.isfile(abs_path):
        raise FileValidationError(f"File '{file_path}' does not exist.")
    
    return abs_path


def handle_file_error(file_path: str, error: Exception, context: str = "processing") -> None:
    """
    Common error handler for file operations.
    
    Args:
        file_path: The file that caused the error
        error: The exception that occurred
        context: Context of the operation (e.g., "reading", "writing", "processing")
    """
    click.echo(f"Error {context} file '{file_path}': {str(error)}", err=True)


def handle_registry_load_error(registry_path: str, error: Exception) -> None:
    """
    Common error handler for registry loading operations.
    
    Args:
        registry_path: The registry file path that caused the error
        error: The exception that occurred
    """
    click.echo(f"Error: Could not load '{registry_path}'. Please run the registry creation script.", err=True)
    click.echo(f"Details: {str(error)}", err=True)


def validate_line_number(line_number: Optional[int], max_line: int) -> bool:
    """
    Validates a line number for file operations.
    
    Args:
        line_number: The line number to validate (1-indexed)
        max_line: The maximum valid line number
        
    Returns:
        True if the line number is valid, False otherwise
    """
    if line_number is None:
        return True  # None means append to end, which is always valid
    
    return 1 <= line_number <= max_line