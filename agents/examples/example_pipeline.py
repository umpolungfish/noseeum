#!/usr/bin/env python3
"""Example: Multi-stage agent pipeline."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator import AgentOrchestrator


def main():
    """Run multi-stage agent pipeline."""

    print("=" * 70)
    print("Example: Multi-Stage Agent Pipeline")
    print("=" * 70)

    orchestrator = AgentOrchestrator()

    # Stage 1: Research
    print("\n[Stage 1] Research Phase")
    print("-" * 70)

    research_result = orchestrator.run_agent(
        "unicode_archaeologist",
        "Discover new homoglyph candidates in Cyrillic and Greek blocks"
    )

    print(f"Research status: {research_result['status']}")
    findings = research_result.get('findings', [])
    print(f"Discoveries: {len(findings)}")

    # Stage 2: Curation
    print("\n[Stage 2] Curation Phase")
    print("-" * 70)

    curator_result = orchestrator.run_agent(
        "homoglyph_curator",
        "Validate and curate discovered homoglyphs",
        context={"discoveries": findings}
    )

    print(f"Curation status: {curator_result['status']}")
    validated = curator_result.get('validated', 0)
    print(f"Validated homoglyphs: {validated}")

    # Stage 3: Attack Generation
    print("\n[Stage 3] Attack Generation Phase")
    print("-" * 70)

    payload_result = orchestrator.run_agent(
        "payload_artisan",
        "Generate sophisticated homoglyph attack payloads",
        context={
            "homoglyphs": curator_result.get('homoglyphs', []),
            "language": "python",
            "attack_type": "homoglyph"
        }
    )

    print(f"Generation status: {payload_result['status']}")
    payloads = payload_result.get('payloads', [])
    print(f"Generated payloads: {len(payloads)}")

    # Stage 4: Runtime Analysis
    print("\n[Stage 4] Runtime Analysis Phase")
    print("-" * 70)

    runtime_results = []
    for i, payload in enumerate(payloads[:3], 1):
        print(f"\n  Analyzing payload {i} runtime behavior...")

        runtime_result = orchestrator.run_agent(
            "runtime_analyzer",
            f"Analyze runtime behavior of payload {i}",
            context={
                "payload": payload.get('payload'),
                "language": "python",
                "monitor": "advanced"
            }
        )

        runtime_results.append(runtime_result)
        malicious = runtime_result.get('malicious_behavior_detected', False)
        print(f"  Malicious behavior detected: {malicious}")

    # Stage 5: Optimization
    print("\n[Stage 5] Optimization Phase")
    print("-" * 70)

    for i, payload in enumerate(payloads[:3], 1):
        print(f"\n  Optimizing payload {i}...")

        opt_result = orchestrator.run_agent(
            "stealth_optimizer",
            f"Optimize payload {i} for maximum evasion",
            context={
                "payload": payload.get('payload'),
                "tools": ["semgrep", "bandit", "pylint"]
            }
        )

        evasion_score = opt_result.get('evasion_score', 0)
        print(f"  Evasion score: {evasion_score:.2f}")

    # Stage 6: Validation
    print("\n[Stage 6] Validation Phase")
    print("-" * 70)

    validator_result = orchestrator.run_agent(
        "red_team_validator",
        "Validate optimized attacks against security tools",
        context={
            "attacks": payloads,
            "test_tools": ["semgrep", "bandit", "pyflakes"]
        }
    )

    print(f"Validation status: {validator_result['status']}")
    test_results = validator_result.get('test_results', {})
    print(f"Tools tested: {test_results.get('tools_tested', 0)}")
    print(f"Bypassed: {test_results.get('bypassed', 0)}")

    # Stage 7: Defense
    print("\n[Stage 7] Defense Generation Phase")
    print("-" * 70)

    yara_result = orchestrator.run_agent(
        "yara_rule_smith",
        "Generate YARA rules for homoglyph detection",
        context={"attack_type": "homoglyph"}
    )

    print(f"YARA generation status: {yara_result['status']}")
    rules_path = yara_result.get('artifacts', [None])[0]
    if rules_path:
        print(f"YARA rules saved: {rules_path}")

    # Stage 8: Documentation
    print("\n[Stage 8] Documentation Phase")
    print("-" * 70)

    report_result = orchestrator.run_agent(
        "report_synthesizer",
        "Generate comprehensive research report",
        context={
            "report_type": "technical",
            "findings": [
                f"Discovered {len(findings)} new homoglyph candidates",
                f"Validated {validated} high-confidence homoglyphs",
                f"Generated {len(payloads)} attack payloads",
                f"Runtime analyzed {len(runtime_results)} payloads",
                f"Achieved evasion against {test_results.get('bypassed', 0)} tools"
            ]
        }
    )

    print(f"Report status: {report_result['status']}")
    report_path = report_result.get('report_path')
    if report_path:
        print(f"Report saved: {report_path}")

    # Pipeline summary
    print("\n" + "=" * 70)
    print("Pipeline Summary")
    print("=" * 70)
    print(f"Stages completed: 8")
    print(f"Total discoveries: {len(findings)}")
    print(f"Validated items: {validated}")
    print(f"Generated payloads: {len(payloads)}")
    print(f"Tests passed: {test_results.get('bypassed', 0)}/{test_results.get('tools_tested', 0)}")
    print(f"Final report: {report_path or 'N/A'}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
