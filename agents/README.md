# Noseeum Agent Menagerie

This directory contains autonomous Claude agents that enhance the noseeum framework with specialized capabilities.

## Architecture

The agent system is built on a multi-provider async-capable framework and provides:

- **Base Agent Framework**: Common tools, utilities, and LLM abstraction for all agents
- **Orchestration Layer**: Single-agent, parallel swarm, and sequential pipeline execution
- **Pipeline Presets**: Named reusable workflows declared in YAML or code
- **Dynamic Tool Registry**: Runtime tool registration without subclassing
- **16 Specialized Agents**: Domain-specific agents for research, attack development, defense, and analysis

### Framework Layers

```
agents/
├── base/
│   ├── agent.py          # BaseAgent — persona, clean_response, extract_json_blocks, execute_with_tools
│   ├── tools.py          # AgentToolkit (static) + ToolRegistry / ToolDefinitions / ToolExecutor
│   ├── memory.py         # AgentMemory — sync + async (atomic writes, asyncio.Lock)
│   ├── communication.py  # AgentCommunication — Message dataclass, MessageType, sync + async
│   └── config_loader.py  # YAML config helpers + register_presets_from_config()
├── llm_providers/        # Anthropic, DeepSeek, Mistral, MoE (Mixture of Experts)
├── orchestrator.py       # AgentOrchestrator + PipelineContext
└── cli.py                # Command-line interface
```

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

### Testing & Runtime Analysis
- **Runtime Analyzer**: Analyzes code at runtime for security vulnerabilities and execution patterns

## Orchestration Modes

### Swarm (parallel)
All selected agents run concurrently against the same task, results collected.

### Pipeline (sequential, with full context accumulation)
Agents run in order; each stage receives outputs from **all prior stages** via `PipelineContext` — not just the previous one. This lets the Report Synthesizer, for example, see raw findings from the Archaeologist and intermediate payloads from the Artisan simultaneously.

### Presets
Named pipelines registered once and run by name:

```python
orchestrator.register_preset("full_analysis", [
    "unicode_archaeologist",
    "payload_artisan",
    "red_team_validator",
    "report_synthesizer",
])
result = orchestrator.run_preset("full_analysis", task="Audit CVE-2023-1234")
```

Presets can also be declared in `config.yaml`:

```yaml
presets:
  full_analysis:  [unicode_archaeologist, payload_artisan, red_team_validator, report_synthesizer]
  quick_scan:     [unicode_archaeologist, report_synthesizer]
  red_team:       [payload_artisan, stealth_optimizer, red_team_validator]
```

Then loaded with:

```python
from base.config_loader import load_config, register_presets_from_config
cfg = load_config("agents/config.yaml")
register_presets_from_config(orchestrator, cfg)
```

## Base Agent Capabilities

All agents inherit from `BaseAgent` which provides:

| Method | Description |
|--------|-------------|
| `clean_response(text)` | Strips `<think>` tags, code fences, `FINAL ANSWER:` prefix |
| `extract_json_blocks(text)` | Parses JSON from ` ```json ` fenced blocks or bare objects |
| `execute_with_tools(task)` | Autonomous thinking/acting loop using available tools |
| `save_artifact(name, content, type)` | Saves to disk and tracks in `self.artifacts` list |
| `persona` | Optional identity shaping system prompt (defaults to `name`) |

## Dynamic Tool Registry

Tools can be registered at runtime without modifying `AgentToolkit`:

```python
from base.tools import global_registry

async def fetch_cve(inp):
    # custom CVE lookup
    ...

global_registry.register(
    name="fetch_cve",
    handler=fetch_cve,
    description="Look up a CVE by ID",
    input_schema={"type": "object", "properties": {"cve_id": {"type": "string"}}, "required": ["cve_id"]},
)
```

The `ToolExecutor` checks `global_registry` first before falling back to `AgentToolkit`.

## Usage

```bash
# List all agents
python cli.py list

# Run individual agent
python cli.py run unicode_archaeologist "Find zero-width characters"

# Run agent swarm (parallel)
python cli.py swarm "Analyze Python Unicode security"

# Run specific agents in a swarm
python cli.py swarm "Generate attacks" --agents payload_artisan,stealth_optimizer

# Agent status
python cli.py status
python cli.py status unicode_archaeologist
```

## Configuration

Edit `agents/config.yaml` to customize:
- LLM provider and model per-agent (supports Anthropic, DeepSeek, Mistral, MoE)
- Swarm concurrency (`max_concurrent_agents`)
- Pipeline presets
- Output preferences and log levels

## Adding New Agents

1. Subclass `BaseAgent` from `agents/base/agent.py`
2. Implement `run(task, context)` and `get_tools()`
3. Register in `orchestrator.py`'s `_get_agent_classes()`
4. Add config entry to `config.yaml`

See `agents/base/` for full framework API.
