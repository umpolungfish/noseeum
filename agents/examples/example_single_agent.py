#!/usr/bin/env python3
"""Example: Running a single agent."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from research.unicode_archaeologist import UnicodeArchaeologist


def main():
    """Run Unicode Archaeologist agent example."""

    print("=" * 70)
    print("Example: Running Unicode Archaeologist Agent")
    print("=" * 70)

    # Configure agent
    config = {
        "model": "claude-sonnet-4-5-20250929",
        "research_depth": "deep",
        "sources": ["unicode.org", "cve.mitre.org"]
    }

    # Initialize agent
    print("\n[1] Initializing agent...")
    agent = UnicodeArchaeologist(config)
    print(f"    Agent: {agent.name}")
    print(f"    Status: {agent.status.value}")

    # Run agent task
    print("\n[2] Running agent task...")
    task = "Discover new Unicode control characters suitable for stealth attacks"
    context = {
        "focus_blocks": ["U+2000-U+206F", "U+FE00-U+FE0F"],
        "categories": ["Cf", "Cc"]  # Format and Control characters
    }

    result = agent.run(task, context)

    # Display results
    print(f"\n[3] Results:")
    print(f"    Status: {result['status']}")

    if result['status'] == 'success':
        print(f"    Findings: {len(result.get('findings', []))}")

        # Show sample findings
        for i, finding in enumerate(result.get('findings', [])[:3], 1):
            print(f"\n    Finding {i}:")
            print(f"      Type: {finding.get('type')}")
            print(f"      Description: {finding.get('description')}")

        # Show artifacts
        artifacts = result.get('artifacts', [])
        if artifacts:
            print(f"\n    Artifacts saved:")
            for artifact in artifacts:
                print(f"      - {artifact}")

    else:
        print(f"    Error: {result.get('error')}")

    # Agent status report
    print(f"\n[4] Agent Status Report:")
    status_report = agent.get_status_report()
    for key, value in status_report.items():
        print(f"    {key}: {value}")

    print("\n" + "=" * 70)
    print("Example completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
