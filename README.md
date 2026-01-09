<div align="center">
  <h1>noseeum</h1>
  <p><b>A FRAMEWORK FOR UNICODE-BASED EXPLOITATION</b></p>

![glasswurm](https://imgur.com/pUsCMHQ.png)

</div>

<div align="center">

  ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
  &nbsp;
  ![Unicode](https://img.shields.io/badge/Unicode-%23000000.svg?style=for-the-badge&logo=unicode&logoColor=white)
  &nbsp;
  ![Security](https://img.shields.io/badge/Security-Offensive-%23FF0000.svg?style=for-the-badge)
  &nbsp;
  ![Cross-Platform](https://img.shields.io/badge/Cross--Platform-Windows%20%7C%20Linux%20%7C%20macOS-%230071C5.svg?style=for-the-badge)

</div>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#agent-menagerie">Agents</a> •
  <a href="#installation">Installation</a> •
  <a href="#basic-usage">Usage</a> •
  <a href="#development">Development</a> •
  <a href="#package-structure">Structure</a>
</p>

<hr>

## OVERVIEW

**Primary Function:** Execute Unicode smuggling attacks including Trojan Source, homoglyph substitution, and invisible character encoding to hide malicious code in plain sight

`noseeum` is a modular offensive security framework for executing Unicode-based attacks  

`noseeum` encodes their payload in the same/similar fashion as exhibited in the "GlassWorm" malware of late 2025  

`noseeum` employs a range of obfuscation and encoding techniques into an extensible CLI  

## NOSEEUM IN ACTION

Below is a screencap of the VirusTotal analysis of the unencoded powershell malware (BEFORE processing with `noseeum`) as well as its "MITRE ATT&CK Tactics and Techniques" Chart  

+ **NOTE THE `8/62` DETECTION RATE**
+ HASH = `f6adc7db3ce7e756bcfd995c6bfeae1480e4626ab4c049644754903e2610a104`

![before](https://imgur.com/XmbiBPH.png)
</div>

![before MITRE](https://imgur.com/nWcx747.png)
</div>

Below is a screencap of the VirusTotal analysis of the `Zero Width Character`-encoded powershell malware (AFTER processing with `noseeum`) as well as its "MITRE ATT&CK Tactics and Techniques" Chart 

+ **NOTE THE `0/62` DETECTION RATE**
+ HASH = `b700553732b9c8c2843885dc4f1122d2471beac47d682e67863f81cbb6d9a55f`

![after](https://imgur.com/P3j33GT.png)
</div>

![after MITRE](https://imgur.com/jQIisUN.png)
</div>  

## FEATURES

### Unified Command-Line Interface
Noseeum provides a single, clean command-line interface powered by Python's `click` library

- **Modular Architecture**: Each attack vector is a self-contained module, allowing for rapid development and integration of new exploits  

- **Multiple Attack Vectors**:  

    - **`Bidi (Trojan Source)`**: Make malicious code appear as harmless comments
    - **`Homoglyph`**: Evade signature-based detection and confuse human analysts by substituting characters with visually identical ones
    - **`Invisible Ink`**: Hide payloads steganographically within benign text or generate imperceptible prompts to jailbreak LLMs
    - **`File Steganography`**: Encode entire files as zero-width character sequences and decode them back
    - **`Language-Specific Exploits`**: Target unique weaknesses in Python, JavaScript, and Java
    - **`Normalization Exploitation`**: Craft payloads that normalize differently across system components (parser vs. scanner)
    - **`Unassigned Planes / Variation Selectors`**: Generate syntactically valid identifiers using characters from unassigned Unicode planes (U+20000–U+2FFFD)
    - **`Payload-injection via Identifier Characters`**: Encode malicious data within language constructs like object properties, class names, or function names  

- **Advanced Language Modules**:

    - **`Go`**: Exploits Go's configurable lexer and permissive Unicode handling
    - **`Kotlin`**: Uses permissive frontend with restrictive backend to create compilation-failing code
    - **`JavaScript`**: Performs AST-level manipulations and low-entropy payload generation
    - **`Swift`**: Leverages ambiguous identifier handling and unassigned planes support

- **Code Formatting & Preprocessing**: Convert source code to noseeum-compatible JSON format
    - Auto-detect 17 programming languages (Python, JavaScript, TypeScript, Java, Go, Rust, C, C++, C#, Ruby, PHP, Kotlin, Swift, Bash, SQL, HTML, CSS)
    - Batch processing for multiple files
    - Template system for custom workflows
    - Direct integration with attack modules
    - Metadata extraction and enrichment

- **Globally Installable`**: Can be installed as a system-wide command-line tool using pip

### Detection and Scanning Module

Includes a scanner to identify the presence of these same Unicode smuggling vulnerabilities in source code

- **File Vulnerability Scanning**: Scan individual files for Unicode smuggling vulnerabilities
- **Multi-Language Support**: Detect vulnerabilities across Python, JavaScript, Java, and other languages
- **Comprehensive Detection**: Identifies various types of Unicode exploits including Bidi, homoglyphs, and invisible characters

## AGENT MENAGERIE

<div align="center">

![AI Agents](https://img.shields.io/badge/AI_Agents-16_Autonomous-%23FF6B6B.svg?style=for-the-badge&logo=openai&logoColor=white)
&nbsp;
![Claude](https://img.shields.io/badge/Claude-Powered-%238B5CF6.svg?style=for-the-badge&logo=anthropic&logoColor=white)
&nbsp;
![Swarm](https://img.shields.io/badge/Swarm-Capable-%2300D9FF.svg?style=for-the-badge)

</div>

**New in 2026**: `noseeum` now includes a complete autonomous agent system powered by Claude AI, featuring **16 specialized agents** that can operate independently or as coordinated swarms for comprehensive Unicode security research, attack development, and defense.

### Agent Categories

#### 🔬 Research & Discovery
- **Unicode Archaeologist**: Discovers new Unicode vulnerabilities, mines CVE databases, tracks exploitable control characters
- **Language Grammar Hunter**: Analyzes programming language specifications for Unicode handling quirks and parser edge cases

#### ⚔️ Attack Development
- **Payload Artisan**: Generates context-aware malicious payloads that blend naturally with target codebases
- **Stealth Optimizer**: Optimizes attacks for maximum evasion against security tools (Semgrep, Bandit, ESLint)
- **Polyglot Specialist**: Creates sophisticated cross-language polyglot attacks exploiting syntax overlaps

#### 🛡️ Defense & Validation
- **Red Team Validator**: Tests attack effectiveness against real-world security scanners and linters
- **YARA Rule Smith**: Generates YARA detection rules and IOC signatures for Unicode attacks
- **Detector Adversary**: Continuously improves noseeum's scanner through adversarial testing

#### 📊 Analysis & Documentation
- **Vulnerability Cartographer**: Maps attack surfaces, generates visualization, creates comprehensive attack trees
- **Report Synthesizer**: Produces technical reports, CVE submissions, and security advisories

#### 🔧 Infrastructure
- **Test Oracle**: Maintains comprehensive test coverage, generates fuzzing inputs, ensures code quality
- **Module Architect**: Scaffolds new attack modules following framework patterns and best practices

#### 🎯 Specialized Research
- **Homoglyph Curator**: Discovers and maintains registry of visually similar Unicode characters
- **Normalization Alchemist**: Exploits Unicode normalization (NFC, NFD, NFKC, NFKD) edge cases and collisions
- **Bidirectional Puppeteer**: Masters Trojan Source attacks using RTL/LTR control characters

#### 🧪 Testing & Runtime Analysis
- **Runtime Analyzer**: Analyzes code at runtime for vulnerabilities, monitors execution patterns, detects security issues during execution

### Agent System Features

- **Autonomous Operation**: Each agent operates independently with minimal supervision
- **Swarm Intelligence**: Coordinate multiple agents for complex multi-stage attacks
- **Persistent Memory**: Agents maintain state and learnings across sessions
- **Inter-Agent Communication**: Agents collaborate and share findings
- **Tool Integration**: Native integration with noseeum framework modules
- **Artifact Generation**: All agents produce structured outputs and actionable results
- **Multi-Provider LLM Support**: Choose from 4 providers or combine them intelligently
  - **Anthropic Claude** (default) - Latest Claude models
  - **DeepSeek** - Cost-effective, code-focused
  - **Mistral AI** - Creative, multilingual tasks
  - **Mixture of Experts (MoE)** - Ensemble with 5 intelligent routing strategies (task_based, voting, cascade, best_of_n, specialist)
- **Enhanced Logging**: Comprehensive logging with configurable verbosity levels (DEBUG/INFO/WARNING/ERROR)
- **Detailed Output**: Rich console output with timestamps, status updates, and execution metrics
- **File-based Logging**: All agent activities logged to individual files in `agents/logs/` directory

### Quick Start with Agents

```bash
# Setup agent system
./agents/setup.sh
export ANTHROPIC_API_KEY="your-key"

# List all available agents
python3 agents/cli.py list

# Run single agent
python3 agents/cli.py run unicode_archaeologist "Discover new vulnerabilities"

# Run coordinated swarm
python3 agents/cli.py swarm "Comprehensive Python Unicode analysis"

# Run specific agents as swarm
python3 agents/cli.py swarm "Generate and validate attacks" \
  --agents payload_artisan,red_team_validator,yara_rule_smith
```

### Agent Usage Examples

**Discover new Unicode vulnerabilities:**
```bash
python3 agents/cli.py run unicode_archaeologist \
  "Find exploitable format characters in Unicode blocks U+2000-U+206F"
```

**Generate stealthy attack payloads:**
```bash
python3 agents/cli.py run payload_artisan \
  "Generate context-aware Bidi attacks for Python" \
  --context '{"language":"python","attack_type":"bidi"}'
```

**Test and validate attacks:**
```bash
python3 agents/cli.py run red_team_validator \
  "Validate attacks against Semgrep and Bandit" \
  --context '{"attack":"payload.py","tools":["semgrep","bandit"]}'
```

**Create detection rules:**
```bash
python3 agents/cli.py run yara_rule_smith \
  "Generate YARA rules for invisible character attacks" \
  --context '{"attack_type":"invisible"}'
```

**Multi-stage research pipeline:**
```python
from agents import AgentOrchestrator

orchestrator = AgentOrchestrator()

# Stage 1: Research
research = orchestrator.run_agent('unicode_archaeologist', 'Find vulnerabilities')

# Stage 2: Weaponize
attacks = orchestrator.run_agent('payload_artisan', 'Generate attacks',
                                 context={'findings': research['findings']})

# Stage 3: Validate
results = orchestrator.run_agent('red_team_validator', 'Test attacks',
                                 context={'attacks': attacks['payloads']})

# Stage 4: Document
report = orchestrator.run_agent('report_synthesizer', 'Create report',
                                context={'results': results})
```

### Agent Documentation

For comprehensive agent documentation, see:
- **[AGENT_QUICKSTART.md](./AGENT_QUICKSTART.md)** - Quick start guide
- **[agents/README.md](./agents/README.md)** - Architecture overview
- **[agents/USAGE.md](./agents/USAGE.md)** - Detailed usage guide
- **[AGENTS_IMPLEMENTATION.md](./AGENTS_IMPLEMENTATION.md)** - Implementation details
- **[MULTI_PROVIDER_SUMMARY.md](./MULTI_PROVIDER_SUMMARY.md)** - Multi-provider LLM support guide
- **[FORMATTER_README.md](./FORMATTER_README.md)** - Code formatter documentation

### Agent System Architecture

The agent system is built on a modular architecture with:
- **Base Framework**: Shared tools, memory, and communication systems
- **Orchestrator**: Swarm coordination with thread-pool execution
- **CLI Interface**: Comprehensive command-line tools
- **Python API**: Programmatic agent control
- **Test Suite**: Comprehensive integration tests
- **Examples**: Working examples for all use cases

## INSTALLATION

### Global Installation (Recommended)

`noseeum` can be installed as a globally accessible command-line tool:

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd noseeum
    ```

2. **Install required data files:**
    Before using the framework, you need to generate the required registry files:
    ```bash
    python3 create_registry.py      # Creates homoglyph_registry.json
    python3 create_nfkc_map.py      # Creates nfkc_map.json
    ```

3. **Install the package:**
    ```bash
    pip install .
    ```
    or using the Makefile:
    ```bash
    make install
    ```

This will install the `noseeum` command globally on your system, making it accessible from any directory

### Uninstallation

To remove the globally installed package:
```bash
make uninstall
```

## BASIC USAGE

All functionality is accessed through the `noseeum` command

**View all available commands:**
```bash
noseeum --help
```

**View attack-specific commands:**
```bash
noseeum attack --help
```

**Scan a file for vulnerabilities:**
```bash
noseeum detect --file /path/to/your/file.js
```

**Format source code for noseeum:**
```bash
noseeum format file /path/to/code.py
noseeum format dir /path/to/project
noseeum format batch file1.js file2.py file3.go
```

For a complete breakdown of every command, option, and argument, refer to the [**USAGE.md**](./docs/USAGE.md) document
 
## DEVELOPMENT

This project uses a `Makefile` to streamline common development tasks.

-   **`make install`**: Sets up the development environment, installs dependencies from `requirements.txt`, creates required data files, and installs the `noseeum` package in editable mode
-   **`make uninstall`**: Removes the `noseeum` package from your system
-   **`make clean`**: Deletes all build artifacts, such as `build/`, `dist/`, and `.egg-info/` directories

## PACKAGE STRUCTURE

The framework is organized as follows:
- `noseeum/`: Main Python package containing:
  - `attacks/`: Individual modules for each attack vector
  - `core/`: Core engine, grammar database, and integration components
  - `detector/`: Scanning and detection functionality
  - `utils/`: Helper utilities and error handling
  - `data/`: Embedded data files (homoglyph_registry.json, nfkc_map.json)
  - `formatter.py`: Code formatting module (converts source to JSON)
  - `cli_format.py`: Formatter CLI interface
- `agents/`: **NEW** Autonomous agent system:
  - `base/`: Base agent framework (agent, tools, memory, communication)
  - `research/`: Research agents (Unicode Archaeologist, Language Grammar Hunter)
  - `attack_dev/`: Attack development agents (Payload Artisan, Stealth Optimizer, Polyglot Specialist)
  - `defense/`: Defense agents (Red Team Validator, YARA Rule Smith, Detector Adversary)
  - `analysis/`: Analysis agents (Vulnerability Cartographer, Report Synthesizer)
  - `infrastructure/`: Infrastructure agents (Test Oracle, Module Architect)
  - `specialized/`: Specialized research agents (Homoglyph Curator, Normalization Alchemist, Bidi Puppeteer)
  - `testing/`: Testing agents (Runtime Analyzer)
  - `llm_providers/`: Multi-provider LLM support (Anthropic, DeepSeek, Mistral, MoE)
  - `orchestrator.py`: Swarm coordination system
  - `cli.py`: Agent CLI interface
  - `tests/`: Agent integration tests
  - `examples/`: Usage examples and tutorials
- `create_registry.py`: Script to generate the homoglyph registry
- `create_nfkc_map.py`: Script to generate the NFKC mapping

## RECENT IMPROVEMENTS

### Autonomous Agent System (2026 - Latest)
- **🚀 NEW: Complete Agent Menagerie** - Added 15 autonomous Claude-powered agents for Unicode security research
- **Agent Categories**: Research, Attack Development, Defense, Analysis, Infrastructure, Specialized Research
- **Swarm Intelligence**: Coordinate multiple agents for complex multi-stage operations
- **Orchestration System**: Thread-pool based swarm coordinator with intelligent task distribution
- **CLI & API**: Comprehensive command-line interface and Python API for agent control
- **Persistent Memory**: Agents maintain state and learnings across sessions
- **Inter-Agent Communication**: Collaboration and information sharing between agents
- **Complete Documentation**: 4 comprehensive docs (7,000+ lines), 4 working examples, full test suite
- **Production Ready**: 41 files, 36 Python modules, comprehensive integration tests

### Code Quality & Reliability
- **Fixed critical logic bug** in homoglyph identifier replacement that could cause incorrect output
- **Added Python 3.8+ compatibility** by replacing Python 3.9+ type annotations
- **Improved error handling** by replacing bare except clauses with proper exception types
- **Consolidated duplicate code** by moving file encoding logic to shared utilities
- **Enhanced CLI consistency** by standardizing error output with click.echo()
- **Completed language support** by adding grammar definitions for Java, Rust, C, and C++
- **Improved path validation** with more reliable directory traversal prevention
- **Added pytest dependency** to requirements for proper test execution

### Testing
Run the test suite with:
```bash
pip install -e ".[dev]"  # Install with dev dependencies
pytest tests/
```

## LICENSE

`noseeum` is sicced upon the Whyrld under the ![UNLICENSE](./UNLICENSE)