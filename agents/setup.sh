#!/bin/bash
# Setup script for noseeum agent system

set -e

echo "=================================================="
echo "Noseeum Agent System Setup"
echo "=================================================="
echo ""

# Check Python version
echo "[1] Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "    Python version: $python_version"

# Create necessary directories
echo ""
echo "[2] Creating directories..."
mkdir -p agents/logs
mkdir -p agents/artifacts
mkdir -p agents/memory
mkdir -p agents/communication
mkdir -p agents/results
echo "    ✓ Directories created"

# Install dependencies
echo ""
echo "[3] Installing dependencies..."
if [ -f "agents/requirements.txt" ]; then
    pip3 install -r agents/requirements.txt
    echo "    ✓ Dependencies installed"
else
    echo "    ✗ requirements.txt not found"
    exit 1
fi

# Check for Anthropic API key
echo ""
echo "[4] Checking Anthropic API key..."
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "    ⚠ ANTHROPIC_API_KEY not set"
    echo "    Please set it with: export ANTHROPIC_API_KEY='your-key'"
else
    echo "    ✓ API key found"
fi

# Install YAML dependency
echo ""
echo "[5] Installing PyYAML..."
pip3 install pyyaml
echo "    ✓ PyYAML installed"

# Make CLI executable
echo ""
echo "[6] Making CLI executable..."
chmod +x agents/cli.py
chmod +x agents/orchestrator.py
chmod +x agents/examples/*.py
echo "    ✓ Scripts are executable"

# Test import
echo ""
echo "[7] Testing agent imports..."
python3 -c "
import sys
sys.path.insert(0, 'agents')
from base.agent import BaseAgent
from orchestrator import AgentOrchestrator
print('    ✓ Imports successful')
" || echo "    ✗ Import failed"

# Create symlink for easy access
echo ""
echo "[8] Creating convenience symlink..."
ln -sf agents/cli.py agents-cli 2>/dev/null || true
echo "    ✓ Symlink created (optional)"

echo ""
echo "=================================================="
echo "Setup Complete!"
echo "=================================================="
echo ""
echo "Quick Start:"
echo "  1. Set API key: export ANTHROPIC_API_KEY='your-key'"
echo "  2. List agents: python3 agents/cli.py list"
echo "  3. Run agent:   python3 agents/cli.py run unicode_archaeologist 'Find new vulnerabilities'"
echo "  4. Run swarm:   python3 agents/cli.py swarm 'Comprehensive analysis'"
echo ""
echo "Examples:"
echo "  - python3 agents/examples/example_single_agent.py"
echo "  - python3 agents/examples/example_swarm.py"
echo "  - python3 agents/examples/example_pipeline.py"
echo ""
echo "Documentation:"
echo "  - agents/README.md"
echo "  - agents/USAGE.md"
echo ""
echo "=================================================="
