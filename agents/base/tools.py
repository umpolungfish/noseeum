"""Agent toolkit with common tools for all agents."""

import os
import re
import json
import subprocess
from typing import Dict, List, Any, Optional
import requests


class AgentToolkit:
    """Common tools for noseeum agents."""

    @staticmethod
    def file_read(filepath: str, encoding: str = 'utf-8') -> str:
        """Read file contents."""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    def file_write(filepath: str, content: str, encoding: str = 'utf-8') -> str:
        """Write content to file."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(content)
            return f"Successfully wrote to {filepath}"
        except Exception as e:
            return f"Error writing file: {e}"

    @staticmethod
    def file_search(directory: str, pattern: str, file_extension: Optional[str] = None) -> List[str]:
        """Search for files matching pattern."""
        results = []
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file_extension and not file.endswith(file_extension):
                        continue
                    if re.search(pattern, file):
                        results.append(os.path.join(root, file))
        except Exception as e:
            return [f"Error searching files: {e}"]
        return results

    @staticmethod
    def grep_code(directory: str, pattern: str, file_extension: Optional[str] = None) -> List[Dict[str, Any]]:
        """Grep for pattern in code files."""
        results = []
        try:
            for root, dirs, files in os.walk(directory):
                # Skip venv and build directories
                dirs[:] = [d for d in dirs if d not in ['venv', 'build', '__pycache__', '.git']]

                for file in files:
                    if file_extension and not file.endswith(file_extension):
                        continue

                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            for line_num, line in enumerate(f, 1):
                                if re.search(pattern, line):
                                    results.append({
                                        'file': filepath,
                                        'line': line_num,
                                        'content': line.strip()
                                    })
                    except:
                        continue
        except Exception as e:
            return [{'error': str(e)}]
        return results

    @staticmethod
    def run_command(command: str, cwd: Optional[str] = None) -> Dict[str, Any]:
        """Run shell command."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr
            }
        except subprocess.TimeoutExpired:
            return {'error': 'Command timeout'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def web_fetch(url: str) -> Dict[str, Any]:
        """Fetch content from URL."""
        try:
            response = requests.get(url, timeout=10)
            return {
                'status_code': response.status_code,
                'content': response.text,
                'headers': dict(response.headers)
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def json_load(filepath: str) -> Dict[str, Any]:
        """Load JSON file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def json_save(filepath: str, data: Dict[str, Any]) -> str:
        """Save data as JSON."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            return f"Saved to {filepath}"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def unicode_analyze(text: str) -> Dict[str, Any]:
        """Analyze Unicode properties of text."""
        results = {
            'length': len(text),
            'codepoints': [],
            'categories': {},
            'suspicious': []
        }

        for char in text:
            codepoint = ord(char)
            cp_info = {
                'char': char,
                'codepoint': f"U+{codepoint:04X}",
                'name': None,
                'category': None
            }

            try:
                import unicodedata
                cp_info['name'] = unicodedata.name(char, 'UNKNOWN')
                cp_info['category'] = unicodedata.category(char)

                category = cp_info['category']
                results['categories'][category] = results['categories'].get(category, 0) + 1

                # Check for suspicious characters
                if category in ['Cf', 'Cc']:  # Format or Control
                    results['suspicious'].append(cp_info)
                elif 0x200B <= codepoint <= 0x200F:  # Zero-width
                    results['suspicious'].append(cp_info)
                elif 0x202A <= codepoint <= 0x202E:  # Bidi
                    results['suspicious'].append(cp_info)

            except:
                pass

            results['codepoints'].append(cp_info)

        return results

    @staticmethod
    def test_with_security_tool(tool: str, target_file: str, language: str = "python") -> Dict[str, Any]:
        """Test a file with a security tool."""
        tool_configs = {
            "semgrep": {
                "cmd": f"semgrep --config=auto --json {target_file}",
                "check_installed": "semgrep --version"
            },
            "bandit": {
                "cmd": f"bandit -r {target_file} -f json",
                "check_installed": "bandit --version"
            },
            "eslint": {
                "cmd": f"eslint {target_file} --format json",
                "check_installed": "eslint --version"
            },
            "pylint": {
                "cmd": f"pylint {target_file} --output-format=json",
                "check_installed": "pylint --version"
            },
            "gosec": {
                "cmd": f"gosec -fmt=json {target_file}",
                "check_installed": "gosec --version"
            },
            "codeql": {
                "cmd": f"gh codeql database analyze --format=json {target_file}",
                "check_installed": "gh codeql --version"
            },
            "sonarqube": {
                "cmd": f"npx sonarqube-scanner -Dsonar.sources={target_file} -Dsonar.projectKey=test",
                "check_installed": "npx sonarqube-scanner --version"
            }
        }

        if tool not in tool_configs:
            return {"error": f"Unknown tool: {tool}", "detected": False}

        config = tool_configs[tool]

        # Check if tool is installed
        check_result = subprocess.run(
            config["check_installed"],
            shell=True,
            capture_output=True,
            text=True
        )

        if check_result.returncode != 0:
            return {
                "tool": tool,
                "detected": False,
                "bypassed": True,
                "error": f"Tool not installed: {tool}",
                "findings": []
            }

        # Run the tool
        try:
            result = subprocess.run(
                config["cmd"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Parse results based on tool
            findings = AgentToolkit._parse_tool_output(tool, result.stdout, result.stderr)

            return {
                "tool": tool,
                "detected": len(findings) > 0,
                "bypassed": len(findings) == 0,
                "returncode": result.returncode,
                "findings": findings,
                "raw_output": result.stdout[:1000]  # Truncate for safety
            }

        except subprocess.TimeoutExpired:
            return {"tool": tool, "error": "Tool timeout", "detected": False, "bypassed": True}
        except Exception as e:
            return {"tool": tool, "error": str(e), "detected": False, "bypassed": True}

    @staticmethod
    def _parse_tool_output(tool: str, stdout: str, stderr: str) -> List[Dict[str, Any]]:
        """Parse security tool output."""
        findings = []

        try:
            if tool in ["semgrep", "bandit", "eslint", "pylint"]:
                # These tools output JSON
                try:
                    data = json.loads(stdout)
                    if tool == "semgrep":
                        findings = data.get("results", [])
                    elif tool == "bandit":
                        findings = data.get("results", [])
                    elif tool == "eslint":
                        for file_result in data:
                            findings.extend(file_result.get("messages", []))
                    elif tool == "pylint":
                        findings = data if isinstance(data, list) else []
                except json.JSONDecodeError:
                    pass

            elif tool in ["gosec", "codeql", "sonarqube"]:
                # Try to parse JSON output
                try:
                    data = json.loads(stdout)
                    if tool == "gosec":
                        findings = data.get("Issues", [])
                    elif tool == "codeql":
                        findings = data.get("results", [])
                    elif tool == "sonarqube":
                        # SonarQube typically uses server API
                        pass
                except json.JSONDecodeError:
                    pass

        except Exception as e:
            findings.append({"error": f"Failed to parse output: {e}"})

        return findings

    @staticmethod
    def batch_test_security_tools(target_file: str, tools: List[str], language: str = "python") -> Dict[str, Any]:
        """Test a file against multiple security tools."""
        results = {}
        total_detected = 0
        total_bypassed = 0

        for tool in tools:
            result = AgentToolkit.test_with_security_tool(tool, target_file, language)
            results[tool] = result

            if result.get("detected"):
                total_detected += 1
            elif result.get("bypassed"):
                total_bypassed += 1

        return {
            "results": results,
            "summary": {
                "total_tools": len(tools),
                "detected": total_detected,
                "bypassed": total_bypassed,
                "evasion_rate": total_bypassed / len(tools) if tools else 0
            }
        }

    @staticmethod
    def get_noseeum_tools() -> List[Dict[str, Any]]:
        """Get tool definitions for Claude API."""
        return [
            {
                "name": "file_read",
                "description": "Read contents of a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "filepath": {"type": "string", "description": "Path to file"},
                        "encoding": {"type": "string", "description": "File encoding", "default": "utf-8"}
                    },
                    "required": ["filepath"]
                }
            },
            {
                "name": "file_write",
                "description": "Write content to a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "filepath": {"type": "string", "description": "Path to file"},
                        "content": {"type": "string", "description": "Content to write"},
                        "encoding": {"type": "string", "description": "File encoding", "default": "utf-8"}
                    },
                    "required": ["filepath", "content"]
                }
            },
            {
                "name": "file_search",
                "description": "Search for files matching a pattern",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "directory": {"type": "string", "description": "Directory to search"},
                        "pattern": {"type": "string", "description": "Regex pattern to match"},
                        "file_extension": {"type": "string", "description": "Optional file extension filter"}
                    },
                    "required": ["directory", "pattern"]
                }
            },
            {
                "name": "grep_code",
                "description": "Search for pattern in code files",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "directory": {"type": "string", "description": "Directory to search"},
                        "pattern": {"type": "string", "description": "Regex pattern to match"},
                        "file_extension": {"type": "string", "description": "Optional file extension"}
                    },
                    "required": ["directory", "pattern"]
                }
            },
            {
                "name": "run_command",
                "description": "Execute a shell command",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Command to execute"},
                        "cwd": {"type": "string", "description": "Working directory"}
                    },
                    "required": ["command"]
                }
            },
            {
                "name": "web_fetch",
                "description": "Fetch content from a URL",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "description": "URL to fetch"}
                    },
                    "required": ["url"]
                }
            },
            {
                "name": "unicode_analyze",
                "description": "Analyze Unicode properties of text",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "Text to analyze"}
                    },
                    "required": ["text"]
                }
            }
        ]
