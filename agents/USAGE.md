# Noseeum Agent System - Usage Guide

## Quick Start

### Installation

```bash
# Install agent dependencies
cd agents
pip install -r requirements.txt

# Set your API key (supports Anthropic, DeepSeek, Mistral, Qwen)
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Basic Usage

#### List Available Agents

```bash
python orchestrator.py list
python cli.py list
```

#### Run a Single Agent

```bash
# Using orchestrator directly
python orchestrator.py run --agent unicode_archaeologist --task "Discover new control characters"

# Using CLI
python cli.py run unicode_archaeologist "Discover new control characters"
```

#### Run Agent Swarm (Parallel)

```bash
# Run all agents against a task
python cli.py swarm "Analyze Python Unicode security"

# Run specific agents
python cli.py swarm "Generate attacks" --agents payload_artisan,stealth_optimizer
```

#### Check Agent Status

```bash
python cli.py status                        # all agents
python cli.py status unicode_archaeologist  # specific agent
```

---

## Agent Descriptions

### Research & Discovery

#### Unicode Archaeologist
Discovers new Unicode vulnerabilities and control characters.

```bash
python cli.py run unicode_archaeologist "Find zero-width characters in Unicode blocks U+2000-U+206F"
```

Use cases: discovering exploitable Unicode characters, tracking CVEs, updating the vulnerability database.

#### Language Grammar Hunter
Analyzes programming language specifications for Unicode handling quirks.

```bash
python cli.py run language_grammar_hunter "Analyze Go and Rust identifier normalization" \
  --context '{"languages": ["go", "rust"]}'
```

Use cases: language-specific Unicode vulnerabilities, parser edge cases, language-specific attack modules.

### Attack Development

#### Payload Artisan
Generates context-aware malicious payloads that blend with codebases.

```bash
python cli.py run payload_artisan "Generate stealthy Bidi payloads for Python" \
  --context '{"language": "python", "attack_type": "bidi", "target_file": "sample.py"}'
```

#### Stealth Optimizer
Optimizes attacks to maximize evasion while maintaining functionality.

```bash
python cli.py run stealth_optimizer "Optimize payload against Semgrep" \
  --context '{"payload": "admin = true", "tools": ["semgrep", "bandit"]}'
```

#### Polyglot Specialist
Creates polyglot attacks that exploit multiple languages simultaneously.

```bash
python cli.py run polyglot_specialist "Create Python/JavaScript polyglot" \
  --context '{"languages": ["python", "javascript"]}'
```

### Defense & Validation

#### Red Team Validator
Tests attack effectiveness against real-world security tools.

```bash
python cli.py run red_team_validator "Test Bidi attack against IDE linters" \
  --context '{"attack": "bidi_payload.py", "tools": ["pylint", "mypy"]}'
```

#### YARA Rule Smith
Generates YARA rules and detection signatures for attacks.

```bash
python cli.py run yara_rule_smith "Generate rules for homoglyph attacks" \
  --context '{"attack_type": "homoglyph"}'
```

#### Detector Adversary
Improves the noseeum scanner through adversarial testing.

```bash
python cli.py run detector_adversary "Improve scanner false positive rate"
```

### Analysis & Documentation

#### Vulnerability Cartographer
Maps and visualizes attack surfaces across languages and ecosystems.

```bash
python cli.py run vulnerability_cartographer "Map Python ecosystem Unicode attack surface" \
  --output vulnerability_map.json
```

#### Report Synthesizer
Generates professional security research reports and advisories.

```bash
python cli.py run report_synthesizer "Generate CVE submission" \
  --context '{"report_type": "cve_submission", "findings": ["..."]}'
```

### Infrastructure

#### Test Oracle
Maintains comprehensive test coverage and generates test cases.

```bash
python cli.py run test_oracle "Generate tests for bidi module" \
  --context '{"module": "bidi"}'
```

#### Module Architect
Assists in developing new attack modules following project patterns.

```bash
python cli.py run module_architect "Create RTL injection module" \
  --context '{"module_name": "rtl_injection", "attack_type": "directional"}'
```

### Specialized Research

#### Homoglyph Curator
Maintains and expands the homoglyph registry with visual confusables.

```bash
python cli.py run homoglyph_curator "Discover Arabic homoglyphs" \
  --context '{"unicode_blocks": ["arabic"]}'
```

#### Normalization Alchemist
Exploits Unicode normalization (NFC, NFD, NFKC, NFKD) edge cases.

```bash
python cli.py run normalization_alchemist "Find NFKC collisions"
```

#### Bidirectional Puppeteer
Masters Trojan Source attacks using bidirectional control characters.

```bash
python cli.py run bidirectional_puppeteer "Generate advanced Bidi attacks" \
  --context '{"rendering_engines": ["vscode", "vim", "github"]}'
```

### Testing & Runtime Analysis

#### Runtime Analyzer
Analyzes code at runtime for security vulnerabilities and execution patterns.

```bash
python cli.py run runtime_analyzer "Monitor Python script for suspicious behavior" \
  --context '{"script": "suspicious.py", "monitor": ["network", "filesystem", "processes"]}'
```

---

## Programmatic Usage

### Single Agent

```python
from agents.orchestrator import AgentOrchestrator

orchestrator = AgentOrchestrator("agents/config.yaml")

result = orchestrator.run_agent(
    "unicode_archaeologist",
    "Discover new Unicode vulnerabilities",
    context={"focus": "format_characters"},
)
print(result["status"])
print(result.get("findings", []))
```

### Parallel Swarm

```python
swarm_result = orchestrator.run_swarm(
    "Comprehensive Unicode security analysis",
    agent_ids=["unicode_archaeologist", "language_grammar_hunter", "vulnerability_cartographer"],
)
print(f"Agents run: {swarm_result['agents_run']}")
print(f"Successful: {swarm_result['successful']}")
```

### Sequential Pipeline with Full Context Accumulation

Each stage receives the outputs of **all prior stages** — not just the previous one — so downstream agents can build on the full history.

```python
result = orchestrator.run_pipeline(
    task="Audit CVE-2023-1234",
    agent_ids=[
        "unicode_archaeologist",   # stage 1: research
        "payload_artisan",         # stage 2: sees stage 1 findings
        "red_team_validator",      # stage 3: sees stages 1+2
        "report_synthesizer",      # stage 4: sees stages 1+2+3
    ],
    initial_context={"target": "CVE-2023-1234", "language": "python"},
)

print(result["status"])
for stage in result["pipeline_results"]:
    print(f"Stage {stage['stage']} ({stage['agent_id']}): {stage['result']['status']}")
```

The `PipelineContext` accumulated context is available at `result["final_context"]`:

```python
ctx = result["final_context"]
print(ctx["pipeline_stages"])   # all stage results
print(ctx["all_artifacts"])     # artifacts from all stages
print(ctx["previous_stage"])    # last stage result (convenience key)
```

### Pipeline Presets

Register named pipelines once, run by name:

```python
orchestrator.register_preset("full_analysis", [
    "unicode_archaeologist",
    "payload_artisan",
    "red_team_validator",
    "report_synthesizer",
])
orchestrator.register_preset("quick_scan", [
    "unicode_archaeologist",
    "report_synthesizer",
])

result = orchestrator.run_preset("full_analysis", task="Audit CVE-2023-1234")
```

Or declare presets in `config.yaml` and load them automatically:

```yaml
presets:
  full_analysis:  [unicode_archaeologist, payload_artisan, red_team_validator, report_synthesizer]
  quick_scan:     [unicode_archaeologist, report_synthesizer]
  red_team:       [payload_artisan, stealth_optimizer, red_team_validator]
```

```python
from base.config_loader import load_config, register_presets_from_config

cfg = load_config("agents/config.yaml")
register_presets_from_config(orchestrator, cfg)

result = orchestrator.run_preset("red_team", task="Test bidi injection")
```

### Async Execution

For async contexts (FastAPI, scripts using `asyncio.run`, etc.):

```python
import asyncio

async def main():
    # Parallel swarm — asyncio.gather + Semaphore (more efficient than ThreadPoolExecutor)
    result = await orchestrator.run_swarm_async(
        "Analyze Unicode security",
        agent_ids=["unicode_archaeologist", "language_grammar_hunter"],
    )

    # Sequential pipeline, async
    pipeline = await orchestrator.run_pipeline_async(
        task="Full audit",
        agent_ids=["unicode_archaeologist", "payload_artisan", "report_synthesizer"],
    )

    # Named preset, async
    preset = await orchestrator.run_preset_async("quick_scan", task="Fast check")

asyncio.run(main())
```

### Agent Introspection

```python
# Get info on all registered agents (name, description, capabilities, status)
info = orchestrator.get_all_agents()
for agent_id, details in info.items():
    print(f"{agent_id}: {details['status']}")

# List all presets
presets = orchestrator.list_presets()
for name, ids in presets.items():
    print(f"{name}: {' -> '.join(ids)}")
```

### Dynamic Tool Registration

Register custom tools that any agent's `execute_with_tools()` or `ToolExecutor` can call:

```python
from base.tools import global_registry

async def fetch_cve(inp):
    import httpx
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://cveawg.mitre.org/api/cve/{inp['cve_id']}")
        return r.text

global_registry.register(
    name="fetch_cve",
    handler=fetch_cve,
    description="Fetch CVE details by ID",
    input_schema={
        "type": "object",
        "properties": {"cve_id": {"type": "string"}},
        "required": ["cve_id"],
    },
)
```

### Async Memory

Agent memory has async equivalents of all operations (atomic writes, `asyncio.Lock`):

```python
from base.memory import AgentMemory

mem = AgentMemory("my_agent")

# Async
session_id = await mem.start_session_async("Analyze bidi")
await mem.store_async("findings", ["U+202E", "U+200F"])
await mem.log_event_async(session_id, "scan_complete", {"count": 2})
await mem.end_session_async(session_id)

findings = await mem.retrieve_async("findings")
```

### Async Communication

```python
from base.communication import AgentCommunication, MessageType

comm = AgentCommunication("unicode_archaeologist")

# Send typed message
msg_id = await comm.send_message_async(
    to_agent="payload_artisan",
    message_type=MessageType.COLLABORATION,
    content="Found U+202E — please generate a bidi payload",
    priority=8,
)

# Convenience wrapper for collaboration requests
req_id = await comm.send_collaboration_request_async(
    target_agent="payload_artisan",
    task="Generate bidi payload for U+202E",
    context={"char": "\u202e", "language": "python"},
)

# Receive and process
messages = await comm.receive_messages_async(unread_only=True)
for msg in messages:
    print(f"[{msg['message_type']}] {msg['content']}")
    await comm.mark_as_read_async(msg["message_id"])
```

### Response Utilities

`BaseAgent` exposes static utilities useful outside the agent loop:

```python
from base.agent import BaseAgent

# Strip <think> tags (DeepSeek-R1 / Qwen), code fences, FINAL ANSWER prefix
clean = BaseAgent.clean_response(raw_llm_output)

# Extract all JSON objects from LLM text
blocks = BaseAgent.extract_json_blocks(response_text)
tool_call = next((b for b in blocks if "tool" in b), None)
```

### Using Individual Agents

```python
from agents.research.unicode_archaeologist import UnicodeArchaeologist
from agents.attack_dev.payload_artisan import PayloadArtisan

config = {"llm_provider": "anthropic", "model": "claude-sonnet-4-6"}

archaeologist = UnicodeArchaeologist(config)
artisan = PayloadArtisan(config)

result1 = archaeologist.run(
    "Find zero-width characters",
    context={"blocks": ["U+2000-U+206F"]},
)

result2 = artisan.run(
    "Generate payloads using discovered characters",
    context={
        "language": "python",
        "findings": result1.get("findings", []),
        # pipeline_stages is populated automatically when run via orchestrator
    },
)
```

---

## Configuration

`agents/config.yaml` structure:

```yaml
# LLM provider defaults
llm_provider:
  provider: anthropic          # or deepseek, mistral, moe
  anthropic:
    model: claude-sonnet-4-6
  deepseek:
    model: deepseek-chat
  mistral:
    model: codestral-2508
  moe:
    providers: [anthropic, deepseek, mistral]
    strategy: task_based       # task_based | voting | specialist

# Per-agent overrides
agents:
  unicode_archaeologist:
    enabled: true
    research_depth: deep
  payload_artisan:
    enabled: true
    llm_provider: deepseek     # override for this agent only

# Orchestration
swarm:
  max_concurrent_agents: 5

# Named pipelines (loaded by register_presets_from_config)
presets:
  full_analysis:  [unicode_archaeologist, payload_artisan, red_team_validator, report_synthesizer]
  quick_scan:     [unicode_archaeologist, report_synthesizer]
  red_team:       [payload_artisan, stealth_optimizer, red_team_validator]

# Logging
output:
  log_level: INFO
```

---

## Best Practices

1. **Start with single agents** before running swarms or pipelines
2. **Use pipelines over swarms** when results need to build on each other (`run_pipeline` vs `run_swarm`)
3. **Define presets in config.yaml** so workflows are reproducible and version-controlled
4. **Use context parameters** to provide specific guidance; downstream pipeline agents inherit all prior context automatically
5. **Register custom tools** via `global_registry` rather than subclassing `AgentToolkit`
6. **Prefer async swarm** (`run_swarm_async`) in production — it uses `asyncio.gather` with a semaphore instead of `ThreadPoolExecutor`
7. **Review agent artifacts** in `agents/artifacts/` and agent logs in `agents/logs/`
8. **Test attacks in isolated environments** only

## Troubleshooting

### Agent fails to initialize
- Check that the relevant `*_API_KEY` environment variable is set
- Verify `config.yaml` syntax
- Ensure all dependencies are installed (`pip install -r requirements.txt`)

### Pipeline stops early
- Check `result["failed_at_stage"]` and `result["failed_agent"]`
- Review `agents/logs/<agent_id>.log` for the failing stage
- Ensure agent `run()` returns `{"status": "success", ...}` on success

### Swarm runs slowly
- Prefer `run_swarm_async()` over `run_swarm()` for I/O-bound LLM calls
- Reduce `max_concurrent_agents` in config if hitting rate limits
- Run specific agents instead of all 16

### Missing artifacts
- Verify `agents/artifacts/` directory exists and is writable
- Check `self.artifacts` list on the agent object after running
- Review agent logs for errors

## Examples

See `agents/examples/` for complete working examples:
- `example_single_agent.py` — Running individual agents
- `example_swarm.py` — Coordinated parallel swarm
- `example_pipeline.py` — Multi-stage sequential pipeline with PipelineContext
- `example_integration.py` — Integrating with the noseeum core framework
