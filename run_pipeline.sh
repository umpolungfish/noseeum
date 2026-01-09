#!/bin/bash
# Noseeum Agent Pipeline
set -e  # Exit on any error

CONFIG="agents/config.yaml"
CLI="python3 agents/cli.py --config $CONFIG"

echo "=== Step 1: Unicode Research ==="
$CLI run unicode_archaeologist "Discover new vulnerabilities" --output research_results.json

echo -e "\n=== Step 2: Payload Generation ==="
$CLI run payload_artisan "Generate attacks" --context-file research_results.json --output payloads.json

echo -e "\n=== Step 3: Red Team Validation ==="
$CLI run red_team_validator "Test attacks" --context-file payloads.json --output validation.json

echo -e "\n=== Step 4: Report Synthesis ==="
$CLI run report_synthesizer "Create report" --context-file validation.json --output final_report.txt

echo -e "\n✓ Pipeline complete! Check final_report.txt"