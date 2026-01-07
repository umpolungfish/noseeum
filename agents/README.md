# Noseeum Agent Menagerie

This directory contains autonomous Claude agents that enhance the noseeum framework with specialized capabilities.

## Architecture

The agent system is built on the Claude Agent SDK and provides:

- **Base Agent Framework**: Common tools and utilities for all agents
- **Orchestration Layer**: Swarm coordination and task distribution
- **Specialized Agents**: 15 domain-specific agents for research, attack development, defense, and analysis

## Agent Categories

### Research & Discovery
- **Unicode Archaeologist**: Discovers new Unicode vulnerabilities and control characters
- **Language Grammar Hunter**: Analyzes programming language Unicode handling quirks

### Attack Development
- **Payload Artisan**: Generates context-aware malicious payloads
- **Stealth Optimizer**: Optimizes attacks for maximum evasion
- **Polyglot Specialist**: Creates cross-language polyglot attacks

### Defense & Validation
- **Red Team Validator**: Tests attack effectiveness against security tools
- **YARA Rule Smith**: Generates detection rules and signatures
- **Detector Adversary**: Improves scanner detection capabilities

### Analysis & Documentation
- **Vulnerability Cartographer**: Maps and visualizes attack surfaces
- **Report Synthesizer**: Generates security research reports

### Infrastructure
- **Test Oracle**: Maintains comprehensive test coverage
- **Module Architect**: Assists in developing new attack modules

### Specialized Research
- **Homoglyph Curator**: Maintains homoglyph registry
- **Normalization Alchemist**: Exploits Unicode normalization edge cases
- **Bidirectional Puppeteer**: Masters RTL/LTR control character exploitation

## Usage

```bash
# Run individual agent
python -m agents.orchestrator run unicode-archaeologist

# Run agent swarm on task
python -m agents.orchestrator swarm --task "discover new homoglyphs"

# List all agents
python -m agents.orchestrator list

# Agent status
python -m agents.orchestrator status
```

## Configuration

Edit `agents/config.yaml` to customize:
- Agent parameters
- API keys and endpoints
- Swarm behavior
- Output preferences

## Adding New Agents

See `agents/base/agent_template.py` for a template to create new agents.
