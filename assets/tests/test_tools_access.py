#!/usr/bin/env python3
"""Test script to verify that all security tools are accessible to agents."""

import subprocess
import sys
import os

def test_tool_access():
    """Test that all security tools can be accessed with the correct commands."""
    
    # Define the tools and their check commands
    tools = {
        "semgrep": "semgrep --version",
        "bandit": "bandit --version",
        "eslint": "eslint --version",
        "pylint": "pylint --version",
        "gosec": "gosec --version",
        "codeql": "gh codeql --version",  # Fixed command
        "sonarqube": "npx sonarqube-scanner --version",  # Fixed command
        "shellcheck": "shellcheck --version"
    }
    
    print("Testing security tool accessibility...")
    print("=" * 50)
    
    all_working = True
    
    for tool_name, command in tools.items():
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✓ {tool_name}: OK - {command}")
            else:
                print(f"✗ {tool_name}: FAILED - {command}")
                print(f"  Error: {result.stderr.strip()}")
                all_working = False
                
        except subprocess.TimeoutExpired:
            print(f"✗ {tool_name}: TIMEOUT - {command}")
            all_working = False
        except Exception as e:
            print(f"✗ {tool_name}: ERROR - {command}")
            print(f"  Exception: {str(e)}")
            all_working = False
    
    print("=" * 50)
    if all_working:
        print("✓ All tools are accessible!")
        return True
    else:
        print("✗ Some tools are not accessible!")
        return False

if __name__ == "__main__":
    success = test_tool_access()
    sys.exit(0 if success else 1)