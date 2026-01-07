# Noseeum Agent System - Quick Start

## 🚀 Instant Setup

```bash
# 1. Navigate to noseeum directory
cd /home/mrnob0dy666/noseeum

# 2. Run setup script
./agents/setup.sh

# 3. Set your API key
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# 4. Verify installation
python3 agents/cli.py list
```

## ⚡ Quick Examples

### List All Agents
```bash
python3 agents/cli.py list
```

### Run Single Agent
```bash
python3 agents/cli.py run unicode_archaeologist "Discover new Unicode control characters"
```

### Run Agent Swarm
```bash
python3 agents/cli.py swarm "Analyze Python Unicode security"
```

### Run Specific Agents
```bash
python3 agents/cli.py swarm "Generate and validate attacks" \
  --agents payload_artisan,red_team_validator,yara_rule_smith
```

### Save Results
```bash
python3 agents/cli.py run payload_artisan "Generate Bidi payloads" \
  --context '{"language":"python","attack_type":"bidi"}' \
  --output results.json
```

## 📚 Example Scripts

```bash
# Single agent example
python3 agents/examples/example_single_agent.py

# Coordinated swarm
python3 agents/examples/example_swarm.py

# Multi-stage pipeline
python3 agents/examples/example_pipeline.py

# Framework integration
python3 agents/examples/example_integration.py
```

## 🎯 Common Use Cases

### 1. Discover New Vulnerabilities
```bash
python3 agents/cli.py run unicode_archaeologist \
  "Find exploitable format characters in Unicode blocks U+2000-U+206F"
```

### 2. Generate Stealthy Attacks
```bash
python3 agents/cli.py run payload_artisan \
  "Generate context-aware homoglyph attacks for Python" \
  --context '{"language":"python","attack_type":"homoglyph"}'
```

### 3. Test Attack Effectiveness
```bash
python3 agents/cli.py run red_team_validator \
  "Validate Bidi attacks against security tools" \
  --context '{"attack":"payload.py","tools":["semgrep","bandit"]}'
```

### 4. Create Detection Rules
```bash
python3 agents/cli.py run yara_rule_smith \
  "Generate YARA rules for invisible character attacks" \
  --context '{"attack_type":"invisible"}'
```

### 5. Comprehensive Analysis
```bash
python3 agents/cli.py swarm \
  "Perform comprehensive Unicode security analysis for Go language" \
  --agents unicode_archaeologist,language_grammar_hunter,vulnerability_cartographer,report_synthesizer
```

## 🔧 Configuration

Edit `agents/config.yaml`:

```yaml
api:
  model: claude-sonnet-4-5-20250929
  max_tokens: 8000

agents:
  unicode_archaeologist:
    enabled: true
    research_depth: deep

swarm:
  max_concurrent_agents: 5
```

## 📊 Agent Overview

| Category | Agents | Purpose |
|----------|--------|---------|
| Research | Unicode Archaeologist, Language Grammar Hunter | Discover vulnerabilities |
| Attack Dev | Payload Artisan, Stealth Optimizer, Polyglot Specialist | Generate exploits |
| Defense | Red Team Validator, YARA Rule Smith, Detector Adversary | Test and detect |
| Analysis | Vulnerability Cartographer, Report Synthesizer | Analyze and document |
| Infrastructure | Test Oracle, Module Architect | Maintain framework |
| Specialized | Homoglyph Curator, Normalization Alchemist, Bidi Puppeteer | Expert research |

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not set"
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

### "Agent not found"
```bash
# List available agents
python3 agents/cli.py list
```

### "Module import error"
```bash
# Reinstall dependencies
pip3 install -r agents/requirements.txt
```

## 📖 Documentation

- **Full Documentation**: `agents/README.md`
- **Usage Guide**: `agents/USAGE.md`
- **Implementation Details**: `AGENTS_IMPLEMENTATION.md`

## 💡 Pro Tips

1. **Start small**: Run single agents before swarms
2. **Use context**: Provide detailed context for better results
3. **Save artifacts**: Check `agents/artifacts/` for generated content
4. **Review logs**: Monitor `agents/logs/` for debugging
5. **Chain agents**: Use output from one agent as input to another

## 🎓 Learning Path

1. ✅ Run `example_single_agent.py` to understand individual agents
2. ✅ Run `example_swarm.py` to see coordination
3. ✅ Run `example_pipeline.py` to learn multi-stage workflows
4. ✅ Run `example_integration.py` to integrate with noseeum
5. ✅ Create your own agent workflows!

---

**Ready to start?** Run: `python3 agents/cli.py info`
