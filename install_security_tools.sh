#!/bin/bash

set -e  # Exit on any error

echo "Installing security tools: gosec and codeql-cli"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install gosec
install_gosec() {
    echo "Installing gosec..."
    
    if command_exists gosec; then
        echo "gosec is already installed. Skipping installation."
        return
    fi
    
    # Check if Go is installed
    if ! command_exists go; then
        echo "Go is required to install gosec but is not installed."
        echo "Please install Go first, then run this script again."
        exit 1
    fi
    
    # Install gosec using Go
    # Use a specific version compatible with Go 1.24
    go install github.com/securego/gosec/v2/cmd/gosec@v2.19.0
    
    # Add GOPATH bin to PATH if not already present
    GOPATH_BIN=$(go env GOPATH)/bin
    if [[ ":$PATH:" != *":$GOPATH_BIN:"* ]]; then
        echo "Adding $GOPATH_BIN to PATH"
        export PATH="$PATH:$GOPATH_BIN"
        # Also add to shell profile for persistence
        if [[ -n "$BASH_VERSION" ]]; then
            echo 'export PATH="$PATH:$(go env GOPATH)/bin"' >> ~/.bashrc
        elif [[ -n "$ZSH_VERSION" ]]; then
            echo 'export PATH="$PATH:$(go env GOPATH)/bin"' >> ~/.zshrc
        fi
    fi
    
    if command_exists gosec; then
        echo "gosec installed successfully!"
        gosec --version
    else
        echo "Failed to install gosec"
        exit 1
    fi
}

# Install codeql-cli
install_codeql() {
    echo "Installing codeql-cli..."
    
    if command_exists codeql; then
        echo "codeql is already installed. Skipping installation."
        return
    fi
    
    # Determine OS
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    ARCH=$(uname -m)
    
    # Map architecture to GitHub release format
    case $ARCH in
        x86_64)
            ARCH="x64"
            ;;
        aarch64|arm64)
            ARCH="arm64"
            ;;
        *)
            echo "Unsupported architecture: $ARCH"
            exit 1
            ;;
    esac
    
    # Create temporary directory
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    # Download the appropriate release based on OS and architecture
    if [[ "$OS" == "linux" ]]; then
        CODEQL_URL="https://github.com/github/codeql-cli-binaries/releases/latest/download/codeql-linux64.zip"
    elif [[ "$OS" == "darwin" ]]; then
        if [[ "$ARCH" == "arm64" ]]; then
            CODEQL_URL="https://github.com/github/codeql-cli-binaries/releases/latest/download/codeql-darwin.arm64.zip"
        else
            CODEQL_URL="https://github.com/github/codeql-cli-binaries/releases/latest/download/codeql-darwin64.zip"
        fi
    else
        echo "Unsupported OS: $OS"
        exit 1
    fi
    
    echo "Downloading CodeQL CLI from: $CODEQL_URL"
    curl -L -o codeql.zip "$CODEQL_URL"
    
    # Extract the archive
    unzip codeql.zip
    
    # Move codeql to a standard location
    CODEQL_DIR="$HOME/.codeql"
    mkdir -p "$CODEQL_DIR"
    mv codeql "$CODEQL_DIR/"
    
    # Add to PATH
    if [[ ":$PATH:" != *":$CODEQL_DIR:"* ]]; then
        echo "Adding $CODEQL_DIR to PATH"
        export PATH="$PATH:$CODEQL_DIR"
        # Also add to shell profile for persistence
        if [[ -n "$BASH_VERSION" ]]; then
            echo "export PATH=\"\$PATH:$CODEQL_DIR\"" >> ~/.bashrc
        elif [[ -n "$ZSH_VERSION" ]]; then
            echo "export PATH=\"\$PATH:$CODEQL_DIR\"" >> ~/.zshrc
        fi
    fi
    
    # Clean up
    rm -rf "$TEMP_DIR"
    
    if command_exists codeql; then
        echo "codeql installed successfully!"
        codeql version
    else
        echo "Failed to install codeql"
        exit 1
    fi
}

# Main execution
echo "Checking for existing installations..."

if command_exists gosec; then
    echo "✓ gosec is already installed:"
    gosec --version
else
    install_gosec
fi

if command_exists codeql; then
    echo "✓ codeql is already installed:"
    codeql version
else
    install_codeql
fi

echo "Both gosec and codeql have been installed successfully!"
echo "Please restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to update your PATH."