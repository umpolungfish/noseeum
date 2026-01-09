"""
Noseeum Code Formatter Module
==============================
Converts source code files into properly formatted JSON for noseeum ingestion.

Features:
- Auto-detect language from file extension
- Apply obfuscation techniques (homoglyph, bidi, normalization, etc.)
- Batch processing of multiple files
- Template support for different attack types
- Metadata extraction and enrichment
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from datetime import datetime


# Language detection based on file extension
LANGUAGE_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.java': 'java',
    '.go': 'go',
    '.rs': 'rust',
    '.c': 'c',
    '.cpp': 'cpp',
    '.cs': 'csharp',
    '.rb': 'ruby',
    '.php': 'php',
    '.kt': 'kotlin',
    '.swift': 'swift',
    '.sh': 'bash',
    '.sql': 'sql',
    '.html': 'html',
    '.css': 'css',
}


class CodeFormatter:
    """Formats source code into noseeum-compatible JSON structures."""

    def __init__(self, obfuscate: bool = False, attack_type: Optional[str] = None):
        """
        Initialize the formatter.

        Args:
            obfuscate: Whether to apply obfuscation techniques
            attack_type: Attack type to use (bidi, homoglyph, normalization, etc.)
        """
        self.obfuscate = obfuscate
        self.attack_type = attack_type or "clean"
        self.payloads = []

    def format_file(
        self,
        file_path: Union[str, Path],
        language: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Format a single source code file into noseeum JSON.

        Args:
            file_path: Path to source code file
            language: Programming language (auto-detected if not provided)
            description: Description of the code
            metadata: Additional metadata to include

        Returns:
            Formatted JSON dictionary
        """
        file_path = Path(file_path)

        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
        except UnicodeDecodeError:
            # Try with different encodings
            for encoding in ['latin-1', 'cp1252', 'iso-8859-1']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        code = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            else:
                raise ValueError(f"Could not decode file: {file_path}")

        # Detect language if not provided
        if not language:
            language = self._detect_language(file_path)

        # Apply obfuscation if enabled
        if self.obfuscate:
            code = self._apply_obfuscation(code, language)

        # Build payload
        payload = {
            "id": len(self.payloads),
            "payload": code,
            "attack_type": self.attack_type,
            "language": language,
            "source_file": str(file_path.name),
            "naturalness_score": 0.8 if not self.obfuscate else 0.5,
        }

        # Add optional fields
        if description:
            payload["description"] = description

        if metadata:
            payload["metadata"] = metadata

        self.payloads.append(payload)
        return payload

    def format_batch(
        self,
        file_paths: List[Union[str, Path]],
        language: Optional[str] = None,
        task: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Format multiple files into a batch payload.

        Args:
            file_paths: List of file paths to process
            language: Programming language (auto-detected if not provided)
            task: Task description

        Returns:
            Complete noseeum JSON structure with multiple payloads
        """
        self.payloads = []

        for file_path in file_paths:
            try:
                self.format_file(file_path, language=language)
            except Exception as e:
                print(f"Warning: Failed to process {file_path}: {e}")
                continue

        return self.build_output(task=task or "Code ingestion batch")

    def format_string(
        self,
        code: str,
        language: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Format a code string directly into noseeum JSON.

        Args:
            code: Source code string
            language: Programming language
            description: Description of the code
            metadata: Additional metadata

        Returns:
            Formatted JSON dictionary
        """
        # Apply obfuscation if enabled
        if self.obfuscate:
            code = self._apply_obfuscation(code, language)

        # Build payload
        payload = {
            "id": len(self.payloads),
            "payload": code,
            "attack_type": self.attack_type,
            "language": language,
            "naturalness_score": 0.8 if not self.obfuscate else 0.5,
        }

        if description:
            payload["description"] = description

        if metadata:
            payload["metadata"] = metadata

        self.payloads.append(payload)
        return payload

    def build_output(
        self,
        task: Optional[str] = None,
        include_metadata: bool = True
    ) -> Dict[str, Any]:
        """
        Build the final noseeum-compatible JSON structure.

        Args:
            task: Task description
            include_metadata: Whether to include metadata fields

        Returns:
            Complete JSON structure ready for noseeum ingestion
        """
        output = {
            "task": task or "Code formatting",
            "payloads": self.payloads,
            "total_generated": len(self.payloads),
        }

        if include_metadata:
            output.update({
                "status": "success",
                "agent": "Code Formatter",
                "timestamp": datetime.now().isoformat(),
                "obfuscation_applied": self.obfuscate,
                "attack_type": self.attack_type,
            })

        return output

    def save_to_file(
        self,
        output_path: Union[str, Path],
        task: Optional[str] = None,
        pretty: bool = True
    ) -> Path:
        """
        Save formatted output to a JSON file.

        Args:
            output_path: Path to save JSON file
            task: Task description
            pretty: Whether to pretty-print the JSON

        Returns:
            Path to saved file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        output = self.build_output(task=task)

        with open(output_path, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(output, f, indent=2, ensure_ascii=False)
            else:
                json.dump(output, f, ensure_ascii=False)

        return output_path

    def _detect_language(self, file_path: Path) -> str:
        """
        Detect programming language from file extension.

        Args:
            file_path: Path to file

        Returns:
            Detected language name
        """
        ext = file_path.suffix.lower()
        return LANGUAGE_MAP.get(ext, "unknown")

    def _apply_obfuscation(self, code: str, language: str) -> str:
        """
        Apply basic obfuscation techniques to code.

        Args:
            code: Source code
            language: Programming language

        Returns:
            Obfuscated code

        Note:
            For full obfuscation, use the noseeum agent system.
            This is a lightweight version for the formatter.
        """
        if self.attack_type == "bidi":
            # Apply bidirectional text attacks
            return self._apply_bidi(code)
        elif self.attack_type == "homoglyph":
            # Apply homoglyph substitution
            return self._apply_homoglyph(code)
        elif self.attack_type == "normalization":
            # Apply normalization attacks
            return self._apply_normalization(code)
        else:
            # No obfuscation
            return code

    def _apply_bidi(self, code: str) -> str:
        """Apply bidirectional text attack."""
        # Insert RLO/LRO marks in comments
        # This is a simple example - use agents for full capability
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if '#' in line or '//' in line:
                # Add RLO before comment content
                lines[i] = line.replace('#', '#\u202e').replace('//', '//\u202e')
        return '\n'.join(lines)

    def _apply_homoglyph(self, code: str) -> str:
        """Apply homoglyph substitution."""
        # Basic homoglyph substitution
        # For full capability, use the homoglyph_curator agent
        homoglyphs = {
            'a': 'а',  # Cyrillic a
            'e': 'е',  # Cyrillic e
            'o': 'о',  # Cyrillic o
            'p': 'р',  # Cyrillic p
        }

        # Only substitute in identifiers, not strings
        # This is a simplified version
        for original, substitute in homoglyphs.items():
            # Replace in variable names (very basic)
            code = re.sub(rf'\b(\w*){original}(\w*)\b', rf'\1{substitute}\2', code)

        return code

    def _apply_normalization(self, code: str) -> str:
        """Apply normalization attacks."""
        # Use composed/decomposed forms
        # For full capability, use the normalization_alchemist agent
        return code  # Placeholder


def format_code_file(
    file_path: str,
    output_path: Optional[str] = None,
    language: Optional[str] = None,
    obfuscate: bool = False,
    attack_type: Optional[str] = None,
    task: Optional[str] = None,
    pretty: bool = True
) -> Dict[str, Any]:
    """
    Convenience function to format a single code file.

    Args:
        file_path: Path to source code file
        output_path: Path to save JSON (optional)
        language: Programming language (auto-detected if not provided)
        obfuscate: Whether to apply obfuscation
        attack_type: Attack type (bidi, homoglyph, etc.)
        task: Task description
        pretty: Pretty-print JSON

    Returns:
        Formatted JSON dictionary
    """
    formatter = CodeFormatter(obfuscate=obfuscate, attack_type=attack_type)
    formatter.format_file(file_path, language=language)
    output = formatter.build_output(task=task)

    if output_path:
        formatter.save_to_file(output_path, task=task, pretty=pretty)

    return output


def format_code_directory(
    directory: str,
    output_path: str,
    pattern: str = "**/*.py",
    language: Optional[str] = None,
    obfuscate: bool = False,
    attack_type: Optional[str] = None,
    task: Optional[str] = None,
    pretty: bool = True
) -> Dict[str, Any]:
    """
    Format all code files in a directory matching a pattern.

    Args:
        directory: Directory to search
        output_path: Path to save JSON
        pattern: Glob pattern for files (default: **/*.py)
        language: Programming language
        obfuscate: Whether to apply obfuscation
        attack_type: Attack type
        task: Task description
        pretty: Pretty-print JSON

    Returns:
        Formatted JSON dictionary with all files
    """
    directory = Path(directory)
    file_paths = list(directory.glob(pattern))

    formatter = CodeFormatter(obfuscate=obfuscate, attack_type=attack_type)
    output = formatter.format_batch(
        file_paths,
        language=language,
        task=task or f"Batch import from {directory}"
    )

    formatter.save_to_file(output_path, task=task, pretty=pretty)

    return output
