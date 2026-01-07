# Noseeum Agents Configuration

## Overview

The agents system uses a YAML configuration file to manage settings for different agent types and their behavior.

## Configuration Files

- `config.yaml` - Main configuration file (not tracked in git)
- `config_sample.yaml` - Sample configuration file with default settings

## Setup

1. Copy the sample configuration:
   ```bash
   cp config_sample.yaml config.yaml
   ```

2. Edit `config.yaml` with your specific settings:
   - Add your Anthropic API key
   - Adjust agent settings as needed
   - Configure output directories

## Environment Variables

Some configuration values can be set via environment variables:

- `ANTHROPIC_API_KEY` - Your Anthropic API key

## Agent Types

The framework includes several specialized agents:

- **unicode_archaeologist**: Researches Unicode security issues
- **language_grammar_hunter**: Analyzes language-specific vulnerabilities
- **payload_artisan**: Creates obfuscation payloads
- **stealth_optimizer**: Optimizes for evasion
- And many more (see config_sample.yaml for full list)