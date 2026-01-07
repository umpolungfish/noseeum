# Security Tools Installation Guide

This document provides instructions for installing the security tools used by the noseeum agent system, specifically `gosec` and `codeql-cli`.

## Prerequisites

Before installing the security tools, ensure you have:

- **Go** (for gosec): Version 1.17 or higher
- **Git**: For downloading codeql databases
- **curl** or **wget**: For downloading tools
- **Unzip**: For extracting archives

## Installation Methods

### Method 1: Using the Installation Script

The easiest way to install both tools is to use the provided installation script:

```bash
# Make the script executable
chmod +x install_security_tools.sh

# Run the installation script
./install_security_tools.sh
```

### Method 2: Manual Installation

#### Installing gosec

**Option A: Using Go (Recommended)**
```bash
go install github.com/securego/gosec/v2/cmd/gosec@latest
```

**Option B: Using Package Manager**

On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install golang-gosec
```

On macOS with Homebrew:
```bash
brew install gosec
```

On Windows with Chocolatey:
```bash
choco install gosec
```

#### Installing codeql-cli

**Option A: Using GitHub Releases**

1. Download the appropriate release for your OS from: https://github.com/github/codeql-cli-binaries/releases
2. Extract the archive
3. Add the `codeql` executable to your PATH

**Option B: Using Package Manager**

On macOS with Homebrew:
```bash
brew install codeql
```

## Verification

After installation, verify that both tools are properly installed:

```bash
# Check gosec
gosec --version

# Check codeql
codeql version
```

## Using with noseeum Agents

Once installed, the noseeum agents will automatically detect and use these tools when performing security analysis. You can test this by running:

```bash
python3 agents/cli.py run stealth_optimizer "Test tool detection" --context '{"payload":"test","tools":["gosec","codeql"]}'
```

## Troubleshooting

### PATH Issues
If the tools are not found after installation, ensure they are in your PATH:

```bash
# Check if tools are in PATH
which gosec
which codeql
```

If not found, add the installation directory to your PATH in your shell profile (`.bashrc`, `.zshrc`, etc.):

```bash
export PATH=$PATH:$GOPATH/bin  # For gosec
export PATH=$PATH:$HOME/.codeql  # For codeql (if installed in ~/.codeql)
```

### Go Installation Required for gosec
If you encounter issues with gosec installation, ensure Go is properly installed:

```bash
go version
```

### CodeQL Database Setup
For full CodeQL functionality, you may need to download query databases:

```bash
# Initialize a CodeQL database for a project
codeql database create my-database --language=go --source-root=.
```

## Notes

- The noseeum agent system will automatically detect these tools when they are available in the PATH
- If tools are not installed, the agents will report that they're not available but continue operation
- For best results with the agent system, ensure both tools are properly installed and accessible