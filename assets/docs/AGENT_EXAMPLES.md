# AGENT_EXAMPLES.md: Comprehensive Guide to Noseeum Agent Commands and Inquiries

This document provides a comprehensive collection of commands, inquiries, and combinations for the noseeum autonomous agent system. Each example demonstrates practical use cases for the 15 specialized Claude-powered agents.

## Table of Contents
1. [Basic Agent Commands](#basic-agent-commands)
2. [Research & Discovery Agents](#research--discovery-agents)
3. [Attack Development Agents](#attack-development-agents)
4. [Defense & Validation Agents](#defense--validation-agents)
5. [Analysis & Documentation Agents](#analysis--documentation-agents)
6. [Infrastructure Agents](#infrastructure-agents)
7. [Specialized Research Agents](#specialized-research-agents)
8. [Agent Swarms](#agent-swarms)
9. [Multi-Stage Pipelines](#multi-stage-pipelines)
10. [Context-Based Commands](#context-based-commands)
11. [Advanced Combinations](#advanced-combinations)

## Basic Agent Commands

### List All Available Agents
```bash
python3 agents/cli.py list
```

### Check Agent Status
```bash
python3 agents/cli.py status
```

### Check Specific Agent Status
```bash
python3 agents/cli.py status payload_artisan
```

### Get Agent System Information
```bash
python3 agents/cli.py info
```

## Research & Discovery Agents

### Unicode Archaeologist

#### Discover New Vulnerabilities
```bash
python3 agents/cli.py run unicode_archaeologist "Discover new Unicode control characters suitable for stealth attacks"
```

#### Analyze Specific Unicode Blocks
```bash
python3 agents/cli.py run unicode_archaeologist "Analyze Unicode blocks U+2000-U+206F for exploitable characters"
```

#### Research CVEs Related to Unicode
```bash
python3 agents/cli.py run unicode_archaeologist "Research CVEs related to bidirectional Unicode control characters"
```

#### Find New Homoglyph Opportunities
```bash
python3 agents/cli.py run unicode_archaeologist "Find visually similar characters in Cyrillic and Latin blocks"
```

#### Analyze Zero-Width Characters
```bash
python3 agents/cli.py run unicode_archaeologist "Analyze zero-width Unicode characters for steganographic use"
```

### Language Grammar Hunter

#### Analyze Python Unicode Handling
```bash
python3 agents/cli.py run language_grammar_hunter "Analyze Python's Unicode handling for parser vulnerabilities"
```

#### Compare Language Parsing Behaviors
```bash
python3 agents/cli.py run language_grammar_hunter "Compare Unicode parsing behaviors between Python, JavaScript, and Java"
```

#### Find Language-Specific Quirks
```bash
python3 agents/cli.py run language_grammar_hunter "Find Unicode handling quirks in Go's lexer"
```

#### Analyze Kotlin Vulnerabilities
```bash
python3 agents/cli.py run language_grammar_hunter "Analyze Kotlin's Unicode identifier handling for security issues"
```

#### Research Swift Unicode Support
```bash
python3 agents/cli.py run language_grammar_hunter "Research Swift's support for unassigned Unicode planes"
```

## Attack Development Agents

### Payload Artisan

#### Generate Context-Aware Bidi Attacks
```bash
python3 agents/cli.py run payload_artisan "Generate context-aware BIDI attacks for Python" --context '{"language":"python","attack_type":"bidi"}'
```

#### Create Kotlin-Specific Payloads
```bash
python3 agents/cli.py run payload_artisan "Generate Kotlin-specific Unicode payloads" --context '{"language":"kotlin","attack_type":"homoglyph"}'
```

#### Generate Polymorphic Variants
```bash
python3 agents/cli.py run payload_artisan "Generate polymorphic variants of BIDI attacks" --context '{"language":"javascript","attack_type":"bidi","variants":5}'
```

#### Create Language-Specific Payloads
```bash
python3 agents/cli.py run payload_artisan "Create Java-specific invisible character payloads" --context '{"language":"java","attack_type":"invisible"}'
```

#### Generate Obfuscated Payloads
```bash
python3 agents/cli.py run payload_artisan "Generate obfuscated payloads for C++" --context '{"language":"cpp","attack_type":"normalization"}'
```

### Stealth Optimizer

#### Optimize for Semgrep Evasion
```bash
python3 agents/cli.py run stealth_optimizer "Optimize payload for Semgrep evasion" --context '{"payload":"malicious_code_here","tools":["semgrep"]}'
```

#### Multi-Tool Evasion Optimization
```bash
python3 agents/cli.py run stealth_optimizer "Optimize payload for multiple security tools" --context '{"payload":"bidi_attack_here","tools":["semgrep","eslint","pylint","gosec"]}'
```

#### Test Against Static Analysis
```bash
python3 agents/cli.py run stealth_optimizer "Test payload against static analysis tools" --context '{"payload":"homoglyph_attack","tools":["bandit","eslint"]}'
```

#### Optimize for Specific Languages
```bash
python3 agents/cli.py run stealth_optimizer "Optimize JavaScript payload for tool evasion" --context '{"payload":"js_payload","language":"javascript","tools":["eslint","jshint"]}'
```

### Polyglot Specialist

#### Create Cross-Language Polyglots
```bash
python3 agents/cli.py run polyglot_specialist "Create polyglot that works in Python and JavaScript" --context '{"languages":["python","javascript"],"attack_type":"bidi"}'
```

#### Generate Multi-Environment Exploits
```bash
python3 agents/cli.py run polyglot_specialist "Generate multi-environment polyglot attacks" --context '{"languages":["python","java","javascript"],"environments":["web","desktop","mobile"]}'
```

#### Syntax Overlap Exploitation
```bash
python3 agents/cli.py run polyglot_specialist "Exploit syntax overlaps between C and C++" --context '{"languages":["c","cpp"],"attack_type":"comment_injection"}'
```

#### Create Tri-Language Polyglots
```bash
python3 agents/cli.py run polyglot_specialist "Create polyglot for Python, Ruby, and Perl" --context '{"languages":["python","ruby","perl"],"attack_type":"string_manipulation"}'
```

## Defense & Validation Agents

### Red Team Validator

#### Test Against Security Scanners
```bash
python3 agents/cli.py run red_team_validator "Test BIDI attacks against security scanners" --context '{"attacks":"bidi_payloads","tools":["semgrep","bandit","eslint"]}'
```

#### Validate Attack Effectiveness
```bash
python3 agents/cli.py run red_team_validator "Validate homoglyph attack effectiveness" --context '{"attacks":"homoglyph_payloads","targets":["python","javascript"]}'
```

#### Test Against Multiple Environments
```bash
python3 agents/cli.py run red_team_validator "Test payloads in Docker and CI/CD environments" --context '{"attacks":"unicode_payloads","environments":["docker","ci_cd","local"]}'
```

#### Effectiveness Metrics
```bash
python3 agents/cli.py run red_team_validator "Generate effectiveness metrics for invisible attacks" --context '{"attacks":"invisible_payloads","metrics":["detection_rate","false_positive","bypass_rate"]}'
```

### YARA Rule Smith

#### Generate BIDI Detection Rules
```bash
python3 agents/cli.py run yara_rule_smith "Generate YARA rules for BIDI attacks" --context '{"attack_type":"bidi","rule_quality":"high"}'
```

#### Create Homoglyph Detection Patterns
```bash
python3 agents/cli.py run yara_rule_smith "Create YARA patterns for homoglyph detection" --context '{"attack_type":"homoglyph","false_positive_tolerance":"low"}'
```

#### Generate IOC Signatures
```bash
python3 agents/cli.py run yara_rule_smith "Generate IOC signatures for invisible character attacks" --context '{"attack_type":"invisible","output_format":"ioc"}'
```

#### Update Detection Database
```bash
python3 agents/cli.py run yara_rule_smith "Update detection database with new Unicode patterns" --context '{"attack_type":"normalization","database":"unicode_db"}'
```

### Detector Adversary

#### Improve Scanner Through Adversarial Testing
```bash
python3 agents/cli.py run detector_adversary "Improve scanner through adversarial testing" --context '{"scanner":"noseeum_scanner","attacks":"unicode_payloads"}'
```

#### Analyze False Positives
```bash
python3 agents/cli.py run detector_adversary "Analyze false positives in detection" --context '{"scanner":"bidi_detector","files":"test_samples","analysis":"false_positive"}'
```

#### Continuous Improvement
```bash
python3 agents/cli.py run detector_adversary "Continuously improve detector performance" --context '{"scanner":"homoglyph_detector","feedback_loop":"enabled"}'
```

#### Vulnerability Assessment
```bash
python3 agents/cli.py run detector_adversary "Assess detector vulnerabilities" --context '{"scanner":"unicode_scanner","attack_methods":["bidi","homoglyph","invisible"]}'
```

## Analysis & Documentation Agents

### Vulnerability Cartographer

#### Map Python Attack Surface
```bash
python3 agents/cli.py run vulnerability_cartographer "Map Python Unicode attack surface" --context '{"language":"python","visualization":"enabled","output_formats":["markdown","html","json"]}'
```

#### Generate Attack Trees
```bash
python3 agents/cli.py run vulnerability_cartographer "Generate attack trees for JavaScript" --context '{"language":"javascript","tree_depth":"comprehensive","output_format":"graphviz"}'
```

#### Risk Assessment
```bash
python3 agents/cli.py run vulnerability_cartographer "Perform risk assessment for Java Unicode handling" --context '{"language":"java","risk_factors":["cvss","exploitability","impact"]}'
```

#### Cross-Language Comparison
```bash
python3 agents/cli.py run vulnerability_cartographer "Compare attack surfaces across Python and JavaScript" --context '{"languages":["python","javascript"],"comparison_type":"comprehensive"}'
```

### Report Synthesizer

#### Generate Technical Reports
```bash
python3 agents/cli.py run report_synthesizer "Generate technical security report" --context '{"report_type":"technical","topics":["bidi","homoglyph","invisible"]}'
```

#### Create Executive Summaries
```bash
python3 agents/cli.py run report_synthesizer "Create executive summary for Unicode vulnerabilities" --context '{"report_type":"executive","audience":"management","vulnerabilities":["trojan_source","homoglyph_substitution"]}'
```

#### Academic Papers
```bash
python3 agents/cli.py run report_synthesizer "Generate academic paper on Unicode attacks" --context '{"report_type":"academic","focus":"research","topics":["unicode_security","trojan_source","homoglyphs"]}'
```

#### CVE Submissions
```bash
python3 agents/cli.py run report_synthesizer "Prepare CVE submission for Unicode vulnerability" --context '{"report_type":"cve_submission","vulnerability":"bidi_attack","cvss_vector":"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H"}'
```

## Infrastructure Agents

### Test Oracle

#### Generate Comprehensive Test Coverage
```bash
python3 agents/cli.py run test_oracle "Generate tests for BIDI attack module" --context '{"module":"bidi_attack","coverage_target":"90","fuzzing":"enabled"}'
```

#### Create Edge Case Tests
```bash
python3 agents/cli.py run test_oracle "Generate edge case tests for homoglyph detection" --context '{"module":"homoglyph_detector","edge_cases":"aggressive","test_types":["unit","integration"]}'
```

#### Fuzzing Input Generation
```bash
python3 agents/cli.py run test_oracle "Generate fuzzing inputs for Unicode parser" --context '{"module":"unicode_parser","fuzzing":"enabled","input_types":["valid","invalid","boundary"]}'
```

#### Regression Testing
```bash
python3 agents/cli.py run test_oracle "Create regression tests for scanner improvements" --context '{"module":"unicode_scanner","regression":"enabled","test_suite":"comprehensive"}'
```

### Module Architect

#### Scaffold New Attack Modules
```bash
python3 agents/cli.py run module_architect "Create new attack module for Rust" --context '{"module_name":"rust_unicode_attack","language":"rust","patterns":["template","cli","test"]}'
```

#### Generate CLI Interfaces
```bash
python3 agents/cli.py run module_architect "Generate CLI interface for new attack" --context '{"module_name":"new_attack","patterns":["cli","click","options"]}'
```

#### Best Practices Enforcement
```bash
python3 agents/cli.py run module_architect "Create module following best practices" --context '{"module_name":"secure_attack","best_practices":"enforced","patterns":["security","logging","error_handling"]}'
```

#### Complete Module Scaffolding
```bash
python3 agents/cli.py run module_architect "Scaffold complete attack module" --context '{"module_name":"complete_attack","components":["module","cli","test","doc"]}'
```

## Specialized Research Agents

### Homoglyph Curator

#### Discover New Visually Similar Characters
```bash
python3 agents/cli.py run homoglyph_curator "Discover new visually similar characters" --context '{"unicode_blocks":["cyrillic","greek","latin"],"similarity_threshold":"0.8"}'
```

#### Update Homoglyph Registry
```bash
python3 agents/cli.py run homoglyph_curator "Update homoglyph registry with new findings" --context '{"registry_path":"homoglyph_registry.json","update_frequency":"weekly"}'
```

#### Font-Specific Analysis
```bash
python3 agents/cli.py run homoglyph_curator "Analyze font-specific homoglyphs" --context '{"fonts":["consolas","courier","monaco"],"character_sets":["ascii","extended"]}'
```

#### Visual Similarity Testing
```bash
python3 agents/cli.py run homoglyph_curator "Test visual similarity across fonts" --context '{"characters":["O","0","o"],"fonts":["default","monospace","serif"],"threshold":"0.9"}'
```

### Normalization Alchemist

#### Find NFC/NFD Collisions
```bash
python3 agents/cli.py run normalization_alchemist "Find NFC/NFD normalization collisions" --context '{"forms":["NFC","NFD"],"collision_detection":"enabled","test_strings":"comprehensive"}'
```

#### NFKC/NFKD Exploitation
```bash
python3 agents/cli.py run normalization_alchemist "Exploit NFKC/NFKD differences" --context '{"forms":["NFKC","NFKD"],"exploit_type":"collision","target_systems":["parser","scanner"]}'
```

#### Parser Behavior Analysis
```bash
python3 agents/cli.py run normalization_alchemist "Analyze parser normalization behaviors" --context '{"parsers":["python","javascript","java"],"normalization_forms":["NFC","NFD","NFKC","NFKD"]}'
```

#### Collision Detection
```bash
python3 agents/cli.py run normalization_alchemist "Detect normalization collisions in identifiers" --context '{"identifier_types":["variable","function","class"],"normalization_forms":["NFC","NFKC"]}'
```

### Bidirectional Puppeteer

#### Master Trojan Source Attacks
```bash
python3 agents/cli.py run bidirectional_puppeteer "Generate advanced Trojan Source attacks" --context '{"algorithms":["UAX9","custom"],"rendering_engines":["vscode","vim","emacs","github"]}'
```

#### RTL/LTR Control Character Testing
```bash
python3 agents/cli.py run bidirectional_puppeteer "Test RTL/LTR control character combinations" --context '{"directions":["rtl","ltr"],"control_characters":["RLO","LRO","RLM","LRM"]}'
```

#### Rendering Engine Validation
```bash
python3 agents/cli.py run bidirectional_puppeteer "Validate BIDI rendering across engines" --context '{"engines":["vscode","vim","emacs","github","gitlab"],"test_cases":"comprehensive"}'
```

#### Advanced BIDI Techniques
```bash
python3 agents/cli.py run bidirectional_puppeteer "Develop advanced BIDI obfuscation techniques" --context '{"techniques":["nested","overlapping","sequential"],"languages":["python","javascript","java"]}'
```

## Agent Swarms

### Comprehensive Security Analysis
```bash
python3 agents/cli.py swarm "Perform comprehensive Unicode security analysis for Python" --agents unicode_archaeologist,payload_artisan,red_team_validator,yara_rule_smith
```

### Multi-Language Research
```bash
python3 agents/cli.py swarm "Research Unicode vulnerabilities across multiple languages" --agents language_grammar_hunter,homoglyph_curator,normalization_alchemist,bidirectional_puppeteer
```

### Attack Development Pipeline
```bash
python3 agents/cli.py swarm "Develop and validate new attack payloads" --agents payload_artisan,stealth_optimizer,red_team_validator,vulnerability_cartographer
```

### Defense Enhancement
```bash
python3 agents/cli.py swarm "Enhance detection capabilities" --agents detector_adversary,yara_rule_smith,test_oracle,report_synthesizer
```

### Full Research Cycle
```bash
python3 agents/cli.py swarm "Complete research cycle: discover, develop, validate, document" --agents unicode_archaeologist,payload_artisan,red_team_validator,report_synthesizer
```

### Infrastructure Automation
```bash
python3 agents/cli.py swarm "Automate framework improvements" --agents test_oracle,module_architect,homoglyph_curator,normalization_alchemist
```

## Multi-Stage Pipelines

### Research → Weaponize → Validate → Document
```bash
# Stage 1: Research
python3 agents/cli.py run unicode_archaeologist "Discover new vulnerabilities" --output research_results.json

# Stage 2: Weaponize
python3 agents/cli.py run payload_artisan "Generate attacks" --context "{\"findings\":\"$(cat research_results.json)\",\"language\":\"python\"}" --output payloads.json

# Stage 3: Validate
python3 agents/cli.py run red_team_validator "Test attacks" --context "{\"payloads\":\"$(cat payloads.json)\",\"tools\":[\"semgrep\",\"bandit\"]}" --output validation.json

# Stage 4: Document
python3 agents/cli.py run report_synthesizer "Create report" --context "{\"results\":\"$(cat validation.json)\",\"report_type\":\"technical\"}" --output final_report.txt
```

### Continuous Improvement Loop
```bash
# Detect vulnerabilities → Improve scanner → Generate tests → Document
python3 agents/cli.py swarm "Continuous improvement loop" --agents unicode_archaeologist,detector_adversary,test_oracle,report_synthesizer
```

### Cross-Language Analysis Pipeline
```bash
# Analyze languages → Generate polyglots → Test → Optimize
python3 agents/cli.py run language_grammar_hunter "Analyze language differences" --context '{"languages":["python","javascript","java"]}' --output analysis.json
python3 agents/cli.py run polyglot_specialist "Create polyglots" --context "{\"analysis\":\"$(cat analysis.json)\",\"languages\":[\"python\",\"javascript\"]}" --output polyglots.json
python3 agents/cli.py run stealth_optimizer "Optimize polyglots" --context "{\"payloads\":\"$(cat polyglots.json)\",\"tools\":[\"semgrep\",\"eslint\"]}" --output optimized.json
```

## Context-Based Commands

### Language-Specific Context
```bash
python3 agents/cli.py run payload_artisan "Generate payloads" --context '{"language":"go","attack_type":"identifier","target_file":"/path/to/gofile.go"}'
```

### File-Based Context
```bash
python3 agents/cli.py run stealth_optimizer "Optimize for specific file" --context '{"payload":"bidi_attack","target_file":"/path/to/vulnerable.js","language":"javascript"}'
```

### Multi-Parameter Context
```bash
python3 agents/cli.py run vulnerability_cartographer "Detailed analysis" --context '{"language":"kotlin","attack_types":["bidi","homoglyph"],"visualization":"enabled","output_formats":["json","html"]}'
```

### Tool-Specific Context
```bash
python3 agents/cli.py run red_team_validator "Tool-specific testing" --context '{"attacks":"unicode_payloads","tools":["semgrep","eslint","pylint"],"environments":["local","docker"]}'
```

## Advanced Combinations

### Custom Agent Workflows
```python
from agents.orchestrator import AgentOrchestrator

# Create orchestrator
orchestrator = AgentOrchestrator()

# Research phase
research_result = orchestrator.run_agent('unicode_archaeologist', 
                                       'Find new exploitable Unicode characters', 
                                       {'focus_blocks': ['U+2000-U+206F'], 'categories': ['Cf', 'Cc']})

# Payload generation
payload_result = orchestrator.run_agent('payload_artisan', 
                                       'Generate context-aware payloads', 
                                       {'findings': research_result.get('findings', []), 
                                        'language': 'python', 
                                        'attack_type': 'bidi'})

# Validation
validation_result = orchestrator.run_agent('red_team_validator', 
                                          'Validate payload effectiveness', 
                                          {'payloads': payload_result.get('payloads', []), 
                                           'tools': ['semgrep', 'bandit']})

# Documentation
report_result = orchestrator.run_agent('report_synthesizer', 
                                      'Create comprehensive report', 
                                      {'research': research_result, 
                                       'payloads': payload_result, 
                                       'validation': validation_result, 
                                       'report_type': 'technical'})
```

### Conditional Agent Execution
```bash
# Run Unicode Archaeologist first
RESEARCH_RESULT=$(python3 agents/cli.py run unicode_archaeologist "Discover vulnerabilities" --output -)

# Conditionally run payload artisan based on findings
if [[ $(echo $RESEARCH_RESULT | jq '.findings | length') -gt 0 ]]; then
    python3 agents/cli.py run payload_artisan "Generate payloads" --context "{\"findings\":$(echo $RESEARCH_RESULT),\"language\":\"python\"}"
fi
```

### Parallel Agent Execution
```bash
# Run multiple research agents in parallel
python3 agents/cli.py run unicode_archaeologist "Find Unicode issues" &
PYTHON_PID=$!
python3 agents/cli.py run language_grammar_hunter "Analyze language quirks" --context '{"language":"javascript"}' &
JS_PID=$!
python3 agents/cli.py run homoglyph_curator "Discover homoglyphs" &
HOMOGLYPH_PID=$!

# Wait for all to complete
wait $PYTHON_PID $JS_PID $HOMOGLYPH_PID
echo "All research agents completed"
```

### Agent Result Aggregation
```bash
# Run multiple agents and aggregate results
RESULTS_DIR="agent_results_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RESULTS_DIR"

python3 agents/cli.py run unicode_archaeologist "Research" --output "$RESULTS_DIR/unicode_findings.json" &
UNICODE_PID=$!
python3 agents/cli.py run payload_artisan "Generate" --context '{"language":"python"}' --output "$RESULTS_DIR/payloads.json" &
PAYLOAD_PID=$!
python3 agents/cli.py run vulnerability_cartographer "Map" --context '{"language":"python"}' --output "$RESULTS_DIR/vulnerability_map.json" &
MAP_PID=$!

wait $UNICODE_PID $PAYLOAD_PID $MAP_PID

# Aggregate results
echo "{
  \"timestamp\": \"$(date -Iseconds)\",
  \"unicode_findings\": $(cat $RESULTS_DIR/unicode_findings.json),
  \"payloads\": $(cat $RESULTS_DIR/payloads.json),
  \"vulnerability_map\": $(cat $RESULTS_DIR/vulnerability_map.json)
}" > "$RESULTS_DIR/aggregated_results.json"

echo "Aggregated results saved to $RESULTS_DIR/aggregated_results.json"
```

## Troubleshooting and Debugging

### Enable Maximum Verbosity
```bash
# Set environment variable for maximum logging
export LOG_LEVEL=DEBUG
python3 agents/cli.py run payload_artisan "Generate payloads" --context '{"language":"python"}'
```

### Check Agent Logs
```bash
# View recent agent logs
tail -f agents/logs/payload_artisan.log
tail -f agents/logs/unicode_archaeologist.log
tail -f agents/logs/orchestrator.log
```

### Test Individual Agents
```bash
# Run individual agent with debug output
python3 agents/research/unicode_archaeologist.py
python3 agents/attack_dev/payload_artisan.py
python3 agents/defense/yara_rule_smith.py
```

### Validate Configuration
```bash
# Check if configuration is properly loaded
python3 agents/cli.py info
```

---

This comprehensive guide provides examples for all 15 noseeum agents, demonstrating their individual capabilities as well as their combined power when used in swarms and multi-stage pipelines. Each example is designed to showcase practical applications of the agent system for Unicode security research, attack development, and defense enhancement.