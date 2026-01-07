# Noseeum Agent System - Usage Guide

## Quick Start

### Installation

```bash
# Install agent dependencies
cd agents
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Basic Usage

#### List Available Agents

```bash
python orchestrator.py list
```

Or using the CLI:

```bash
python cli.py list
```

#### Run a Single Agent

```bash
# Using orchestrator directly
python orchestrator.py run --agent unicode_archaeologist --task "Discover new control characters"

# Using CLI
python cli.py run unicode_archaeologist "Discover new control characters"
```

#### Run Agent Swarm

```bash
# Run all agents
python cli.py swarm "Analyze Python Unicode security"

# Run specific agents
python cli.py swarm "Generate attacks" --agents payload_artisan,stealth_optimizer
```

#### Check Agent Status

```bash
# All agents
python cli.py status

# Specific agent
python cli.py status unicode_archaeologist
```

## Agent Descriptions

### Research & Discovery

#### Unicode Archaeologist
Discovers new Unicode vulnerabilities and control characters.

**Example:**
```bash
python cli.py run unicode_archaeologist "Find zero-width characters in Unicode blocks U+2000-U+206F"
```

**Use Cases:**
- Discovering new exploitable Unicode characters
- Tracking CVEs related to Unicode
- Updating the framework's vulnerability database

#### Language Grammar Hunter
Analyzes programming language specifications for Unicode handling quirks.

**Example:**
```bash
python cli.py run language_grammar_hunter "Analyze Go and Rust identifier normalization" \
  --context '{"languages": ["go", "rust"]}'
```

**Use Cases:**
- Finding language-specific Unicode vulnerabilities
- Documenting parser edge cases
- Creating language-specific attack modules

### Attack Development

#### Payload Artisan
Generates context-aware malicious payloads that blend with codebases.

**Example:**
```bash
python cli.py run payload_artisan "Generate stealthy Bidi payloads for Python" \
  --context '{"language": "python", "attack_type": "bidi", "target_file": "sample.py"}'
```

**Use Cases:**
- Creating natural-looking malicious code
- Generating polymorphic attack variants
- Adapting attacks to coding styles

#### Stealth Optimizer
Optimizes attacks to maximize evasion while maintaining functionality.

**Example:**
```bash
python cli.py run stealth_optimizer "Optimize payload against Semgrep" \
  --context '{"payload": "admin = true", "tools": ["semgrep", "bandit"]}'
```

**Use Cases:**
- Evading static analysis tools
- A/B testing attack variants
- Reducing detection signatures

#### Polyglot Specialist
Creates polyglot attacks that exploit multiple languages simultaneously.

**Example:**
```bash
python cli.py run polyglot_specialist "Create Python/JavaScript polyglot" \
  --context '{"languages": ["python", "javascript"]}'
```

**Use Cases:**
- Cross-language exploitation
- Finding syntax overlaps
- Multi-environment attacks

### Defense & Validation

#### Red Team Validator
Tests attack effectiveness against real-world security tools.

**Example:**
```bash
python cli.py run red_team_validator "Test Bidi attack against IDE linters" \
  --context '{"attack": "bidi_payload.py", "tools": ["pylint", "mypy"]}'
```

**Use Cases:**
- Validating attack effectiveness
- Testing against security scanners
- Benchmarking evasion techniques

#### YARA Rule Smith
Generates YARA rules and detection signatures for attacks.

**Example:**
```bash
python cli.py run yara_rule_smith "Generate rules for homoglyph attacks" \
  --context '{"attack_type": "homoglyph"}'
```

**Use Cases:**
- Creating detection rules
- Defensive signature generation
- Threat intelligence creation

#### Detector Adversary
Improves the noseeum scanner through adversarial testing.

**Example:**
```bash
python cli.py run detector_adversary "Improve scanner false positive rate"
```

**Use Cases:**
- Enhancing detection capabilities
- Analyzing scanner weaknesses
- Reducing false positives

### Analysis & Documentation

#### Vulnerability Cartographer
Maps and visualizes attack surfaces across languages and ecosystems.

**Example:**
```bash
python cli.py run vulnerability_cartographer "Map Python ecosystem Unicode attack surface" \
  --output vulnerability_map.json
```

**Use Cases:**
- Creating attack surface maps
- Visualizing vulnerability relationships
- Risk assessment

#### Report Synthesizer
Generates professional security research reports and advisories.

**Example:**
```bash
python cli.py run report_synthesizer "Generate CVE submission" \
  --context '{"report_type": "cve_submission", "findings": ["..."]}'
```

**Use Cases:**
- Creating technical reports
- Writing CVE disclosures
- Generating executive summaries

### Infrastructure

#### Test Oracle
Maintains comprehensive test coverage and generates test cases.

**Example:**
```bash
python cli.py run test_oracle "Generate tests for bidi module" \
  --context '{"module": "bidi"}'
```

**Use Cases:**
- Generating test cases
- Fuzzing input generation
- Coverage analysis

#### Module Architect
Assists in developing new attack modules following project patterns.

**Example:**
```bash
python cli.py run module_architect "Create RTL injection module" \
  --context '{"module_name": "rtl_injection", "attack_type": "directional"}'
```

**Use Cases:**
- Scaffolding new modules
- Ensuring best practices
- Module integration

### Specialized Research

#### Homoglyph Curator
Maintains and expands the homoglyph registry with visual confusables.

**Example:**
```bash
python cli.py run homoglyph_curator "Discover Arabic homoglyphs" \
  --context '{"unicode_blocks": ["arabic"]}'
```

**Use Cases:**
- Finding new homoglyphs
- Testing visual similarity
- Updating homoglyph registry

#### Normalization Alchemist
Exploits Unicode normalization (NFC, NFD, NFKC, NFKD) edge cases.

**Example:**
```bash
python cli.py run normalization_alchemist "Find NFKC collisions"
```

**Use Cases:**
- Finding normalization collisions
- Exploiting parser normalization
- Creating identifier collision attacks

#### Bidirectional Puppeteer
Masters Trojan Source attacks using bidirectional control characters.

**Example:**
```bash
python cli.py run bidirectional_puppeteer "Generate advanced Bidi attacks" \
  --context '{"rendering_engines": ["vscode", "vim", "github"]}'
```

**Use Cases:**
- Crafting sophisticated Bidi attacks
- Testing rendering engines
- Trojan Source research

## Programmatic Usage

### Python API

```python
from agents import AgentOrchestrator

# Initialize orchestrator
orchestrator = AgentOrchestrator('agents/config.yaml')

# Run a single agent
result = orchestrator.run_agent(
    'unicode_archaeologist',
    'Discover new Unicode vulnerabilities',
    context={'focus': 'format_characters'}
)

print(f"Status: {result['status']}")
print(f"Findings: {result.get('findings', [])}")

# Run agent swarm
swarm_result = orchestrator.run_swarm(
    'Comprehensive Unicode security analysis',
    agent_ids=['unicode_archaeologist', 'language_grammar_hunter', 'vulnerability_cartographer']
)

print(f"Agents run: {swarm_result['agents_run']}")
print(f"Successful: {swarm_result['successful']}")
```

### Using Individual Agents

```python
from agents.research import UnicodeArchaeologist
from agents.attack_dev import PayloadArtisan

# Initialize agents with config
config = {
    "model": "claude-sonnet-4-5-20250929",
    "research_depth": "deep"
}

archaeologist = UnicodeArchaeologist(config)
artisan = PayloadArtisan(config)

# Run Unicode research
result1 = archaeologist.run(
    "Find zero-width characters",
    context={"blocks": ["U+2000-U+206F"]}
)

# Generate payloads based on findings
result2 = artisan.run(
    "Generate payloads using discovered characters",
    context={
        "language": "python",
        "findings": result1.get("findings", [])
    }
)
```

## Configuration

Edit `agents/config.yaml` to customize agent behavior:

```yaml
api:
  anthropic_api_key: ${ANTHROPIC_API_KEY}
  model: claude-sonnet-4-5-20250929
  max_tokens: 8000

agents:
  unicode_archaeologist:
    enabled: true
    research_depth: deep
    update_frequency: daily

  payload_artisan:
    enabled: true
    creativity: high
    context_awareness: true

swarm:
  max_concurrent_agents: 5
  coordination: enabled
```

## Best Practices

1. **Start with single agents** before running swarms
2. **Use context parameters** to provide specific guidance
3. **Save results to files** for later analysis
4. **Review agent artifacts** in `agents/artifacts/`
5. **Check agent logs** in `agents/logs/` for debugging
6. **Use swarms for comprehensive analysis** tasks
7. **Test attacks in isolated environments** only

## Troubleshooting

### Agent fails to initialize
- Check `ANTHROPIC_API_KEY` environment variable
- Verify `config.yaml` syntax
- Ensure all dependencies are installed

### Swarm runs slowly
- Reduce `max_concurrent_agents` in config
- Run specific agents instead of all
- Check system resources

### Missing artifacts
- Verify `agents/artifacts/` directory exists
- Check file permissions
- Review agent logs for errors

## Examples

See `agents/examples/` directory for complete working examples:
- `example_single_agent.py` - Running individual agents
- `example_swarm.py` - Coordinated swarm attacks
- `example_pipeline.py` - Multi-stage agent pipelines
- `example_integration.py` - Integrating with noseeum framework
