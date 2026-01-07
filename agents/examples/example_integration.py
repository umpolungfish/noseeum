#!/usr/bin/env python3
"""Example: Integrating agents with noseeum framework."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator import AgentOrchestrator


def main():
    """Demonstrate agent integration with noseeum framework."""

    print("=" * 70)
    print("Example: Agent Integration with Noseeum Framework")
    print("=" * 70)

    orchestrator = AgentOrchestrator()

    # Scenario: Enhance noseeum with agent-generated content

    # 1. Discover new Unicode vulnerabilities
    print("\n[1] Discovering new Unicode vulnerabilities...")
    discovery_result = orchestrator.run_agent(
        "unicode_archaeologist",
        "Find unexploited Unicode characters in mathematical blocks",
        context={"blocks": ["U+2100-U+214F", "U+2200-U+22FF"]}
    )

    # 2. Create new attack module using Module Architect
    print("\n[2] Creating new attack module...")
    module_result = orchestrator.run_agent(
        "module_architect",
        "Create mathematical Unicode attack module",
        context={
            "module_name": "math_unicode_attack",
            "attack_type": "unicode",
            "vulnerabilities": discovery_result.get('findings', [])
        }
    )

    print(f"    Module files generated: {module_result.get('files_generated', 0)}")

    # 3. Generate test cases for new module
    print("\n[3] Generating test cases...")
    test_result = orchestrator.run_agent(
        "test_oracle",
        "Generate comprehensive tests for math_unicode_attack module",
        context={"module": "math_unicode_attack"}
    )

    print(f"    Test cases generated: {test_result.get('generated_tests', 0)}")

    # 4. Update grammar database
    print("\n[4] Updating grammar database...")
    print("    Simulating grammar database update with new findings...")

    for finding in discovery_result.get('findings', [])[:3]:
        print(f"      - Adding: {finding.get('type', 'unknown')}")

    # 5. Enhance detector capabilities
    print("\n[5] Enhancing detector...")
    detector_result = orchestrator.run_agent(
        "detector_adversary",
        "Improve scanner to detect new mathematical Unicode attacks"
    )

    improvements = detector_result.get('improvements', [])
    print(f"    Scanner improvements: {len(improvements)}")
    for improvement in improvements[:3]:
        print(f"      - {improvement}")

    # 6. Generate YARA rules
    print("\n[6] Generating detection rules...")
    yara_result = orchestrator.run_agent(
        "yara_rule_smith",
        "Create YARA rules for mathematical Unicode attacks",
        context={"attack_type": "math_unicode"}
    )

    print(f"    YARA rules generated: {yara_result.get('artifacts', ['N/A'])[0]}")

    # 7. Create documentation
    print("\n[7] Generating documentation...")
    doc_result = orchestrator.run_agent(
        "report_synthesizer",
        "Document new mathematical Unicode attack module",
        context={
            "report_type": "technical",
            "findings": [
                "New attack module: math_unicode_attack",
                f"Tests generated: {test_result.get('generated_tests', 0)}",
                f"Detector improvements: {len(improvements)}",
                "YARA rules created"
            ]
        }
    )

    print(f"    Documentation: {doc_result.get('report_path', 'N/A')}")

    # Integration summary
    print("\n" + "=" * 70)
    print("Integration Complete!")
    print("=" * 70)
    print("\nFramework Enhancements:")
    print(f"  ✓ New vulnerabilities discovered: {len(discovery_result.get('findings', []))}")
    print(f"  ✓ New attack module created: math_unicode_attack")
    print(f"  ✓ Test coverage added: {test_result.get('generated_tests', 0)} tests")
    print(f"  ✓ Scanner improvements: {len(improvements)}")
    print(f"  ✓ Detection rules: YARA rules generated")
    print(f"  ✓ Documentation: Technical report created")
    print("\nNext Steps:")
    print("  1. Review generated module in agents/artifacts/")
    print("  2. Integrate module into noseeum/attacks/")
    print("  3. Run generated tests with pytest")
    print("  4. Update noseeum/core/__init__.py to register module")
    print("  5. Add YARA rules to noseeum detector")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
