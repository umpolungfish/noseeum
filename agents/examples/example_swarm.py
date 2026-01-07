#!/usr/bin/env python3
"""Example: Running a coordinated agent swarm."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator import AgentOrchestrator


def main():
    """Run agent swarm example."""

    print("=" * 70)
    print("Example: Coordinated Agent Swarm Attack")
    print("=" * 70)

    # Initialize orchestrator
    print("\n[1] Initializing orchestrator...")
    orchestrator = AgentOrchestrator()
    print(f"    Loaded agents: {len(orchestrator.agents)}")

    # Define comprehensive task
    task = """
    Perform comprehensive Unicode security analysis of Python codebases:
    1. Discover new exploitable Unicode characters
    2. Analyze Python's Unicode handling quirks
    3. Generate stealthy attack payloads
    4. Create detection rules
    5. Generate comprehensive report
    """

    # Select agents for swarm
    swarm_agents = [
        "unicode_archaeologist",      # Research new vulnerabilities
        "language_grammar_hunter",    # Analyze Python specifics
        "payload_artisan",            # Generate attacks
        "yara_rule_smith",            # Create detections
        "report_synthesizer"          # Document findings
    ]

    print(f"\n[2] Swarm composition:")
    for agent_id in swarm_agents:
        agent = orchestrator.agents.get(agent_id)
        if agent:
            print(f"    - {agent.name}")

    # Run swarm
    print(f"\n[3] Executing swarm...")
    context = {
        "target_language": "python",
        "attack_types": ["bidi", "homoglyph", "invisible"],
        "generate_report": True
    }

    result = orchestrator.run_swarm(task, swarm_agents, context)

    # Display results
    print(f"\n[4] Swarm Results:")
    print(f"    Status: {result['status']}")
    print(f"    Agents run: {result['agents_run']}")
    print(f"    Successful: {result['successful']}")
    print(f"    Failed: {result['failed']}")

    # Individual agent results
    print(f"\n[5] Individual Agent Results:")
    for agent_id, agent_result in result['results'].items():
        status = agent_result.get('status', 'unknown')
        status_symbol = "✓" if status == "success" else "✗"
        print(f"    {status_symbol} {agent_id}: {status}")

        if status == "success":
            # Show key metrics
            for key in ['findings', 'payloads', 'rules', 'report_path']:
                if key in agent_result:
                    value = agent_result[key]
                    if isinstance(value, list):
                        print(f"        {key}: {len(value)} items")
                    else:
                        print(f"        {key}: {value}")

    print("\n" + "=" * 70)
    print("Swarm attack completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
