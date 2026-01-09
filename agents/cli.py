#!/usr/bin/env python3
"""CLI interface for noseeum agent management."""

import click
import json
import sys
import os

# Add agents to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from orchestrator import AgentOrchestrator


@click.group()
@click.option('--config', default='agents/config.yaml', help='Path to config file')
@click.pass_context
def cli(ctx, config):
    """Noseeum Agent Management CLI."""
    ctx.ensure_object(dict)
    try:
        ctx.obj['orchestrator'] = AgentOrchestrator(config)
    except Exception as e:
        click.echo(f"Error initializing orchestrator: {e}", err=True)
        sys.exit(1)


@cli.command(name='list')
@click.pass_context
def list_agents(ctx):
    """List all available agents."""
    orchestrator = ctx.obj['orchestrator']
    agents = orchestrator.list_agents()

    click.echo("\n" + "=" * 70)
    click.echo("NOSEEUM AGENT MENAGERIE")
    click.echo("=" * 70)

    # Group by category
    categories = {
        "research": [],
        "attack_development": [],
        "defense": [],
        "analysis": [],
        "testing": [],
        "documentation": []
    }

    for agent in agents:
        caps = agent['capabilities']
        if 'research' in caps:
            categories['research'].append(agent)
        elif 'attack_development' in caps:
            categories['attack_development'].append(agent)
        elif 'defense' in caps:
            categories['defense'].append(agent)
        elif 'analysis' in caps:
            categories['analysis'].append(agent)
        elif 'testing' in caps:
            categories['testing'].append(agent)
        elif 'documentation' in caps:
            categories['documentation'].append(agent)

    for category, agents_list in categories.items():
        if agents_list:
            click.echo(f"\n{category.upper().replace('_', ' ')}")
            click.echo("-" * 70)
            for agent in agents_list:
                click.echo(f"  {agent['id']}")
                click.echo(f"    Name: {agent['name']}")
                click.echo(f"    Description: {agent['description']}")
                click.echo(f"    Status: {agent['status']}")

    click.echo("\n" + "=" * 70)
    click.echo(f"Total agents: {len(agents)}")
    click.echo()


@cli.command()
@click.argument('agent_id')
@click.argument('task')
@click.option('--context', help='JSON context for the task')
@click.option('--context-file', type=click.Path(exists=True), help='JSON file containing context')
@click.option('--output', '-o', help='Output file for results')
@click.pass_context
def run(ctx, agent_id, task, context, context_file, output):
    """Run a single agent."""
    orchestrator = ctx.obj['orchestrator']

    # Parse context if provided
    context_dict = None
    if context_file:
        try:
            with open(context_file, 'r') as f:
                context_dict = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            click.echo(f"Error: Failed to load context file: {e}", err=True)
            sys.exit(1)
    elif context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            click.echo("Error: Invalid JSON context", err=True)
            sys.exit(1)

    click.echo(f"\nRunning agent: {agent_id}")
    click.echo(f"Task: {task}\n")

    result = orchestrator.run_agent(agent_id, task, context_dict)

    if result.get('status') == 'success':
        click.secho("✓ Success", fg='green', bold=True)
        click.echo(f"\nAgent: {result.get('agent', agent_id)}")

        # Display relevant result fields
        for key, value in result.items():
            if key not in ['status', 'agent', 'task']:
                if isinstance(value, (list, dict)):
                    click.echo(f"{key}: {len(value)} items" if isinstance(value, (list, dict)) else value)
                else:
                    click.echo(f"{key}: {value}")

    else:
        click.secho("✗ Failed", fg='red', bold=True)
        click.echo(f"Error: {result.get('error', 'Unknown error')}")

    # Save to file if requested
    if output:
        with open(output, 'w') as f:
            json.dump(result, f, indent=2)
        click.echo(f"\nResults saved to: {output}")


@cli.command()
@click.argument('task')
@click.option('--agents', help='Comma-separated agent IDs')
@click.option('--context', help='JSON context for the task')
@click.option('--context-file', type=click.Path(exists=True), help='JSON file containing context')
@click.option('--output', '-o', help='Output file for results')
@click.pass_context
def swarm(ctx, task, agents, context, context_file, output):
    """Run multiple agents as a coordinated swarm."""
    orchestrator = ctx.obj['orchestrator']

    # Parse agent IDs
    agent_ids = agents.split(',') if agents else None

    # Parse context
    context_dict = None
    if context_file:
        try:
            with open(context_file, 'r') as f:
                context_dict = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            click.echo(f"Error: Failed to load context file: {e}", err=True)
            sys.exit(1)
    elif context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            click.echo("Error: Invalid JSON context", err=True)
            sys.exit(1)

    click.echo(f"\nStarting swarm")
    click.echo(f"Task: {task}")
    click.echo(f"Agents: {agents if agents else 'all'}\n")

    with click.progressbar(length=100, label='Running swarm') as bar:
        result = orchestrator.run_swarm(task, agent_ids, context_dict)
        bar.update(100)

    click.echo(f"\n\nSwarm completed!")
    click.echo(f"Agents run: {result['agents_run']}")
    click.secho(f"Successful: {result['successful']}", fg='green')
    if result['failed'] > 0:
        click.secho(f"Failed: {result['failed']}", fg='red')

    # Display individual results
    click.echo("\nIndividual Results:")
    for agent_id, agent_result in result['results'].items():
        status = agent_result.get('status', 'unknown')
        if status == 'success':
            click.secho(f"  ✓ {agent_id}", fg='green')
        else:
            click.secho(f"  ✗ {agent_id}: {agent_result.get('error', 'unknown')}", fg='red')

    # Save to file if requested
    if output:
        with open(output, 'w') as f:
            json.dump(result, f, indent=2)
        click.echo(f"\nResults saved to: {output}")


@cli.command()
@click.argument('agent_id', required=False)
@click.pass_context
def status(ctx, agent_id):
    """Get status of agents."""
    orchestrator = ctx.obj['orchestrator']

    if agent_id:
        # Single agent status
        status_report = orchestrator.get_agent_status(agent_id)
        if not status_report:
            click.echo(f"Agent not found: {agent_id}", err=True)
            sys.exit(1)

        click.echo(f"\n=== Status: {agent_id} ===")
        for key, value in status_report.items():
            click.echo(f"{key}: {value}")
    else:
        # All agents status
        all_status = orchestrator.get_all_status()

        click.echo("\n=== All Agents Status ===\n")
        for aid, status_report in all_status.items():
            status_val = status_report['status']
            color = 'green' if status_val == 'idle' else 'yellow' if status_val == 'running' else 'red'
            click.secho(f"{aid}: {status_val}", fg=color)


@cli.command()
@click.pass_context
def info(ctx):
    """Display information about the agent system."""
    click.echo("\n" + "=" * 70)
    click.echo("NOSEEUM AGENT MENAGERIE")
    click.echo("=" * 70)
    click.echo("\nAutonomous security research agents for Unicode-based exploitation.\n")
    click.echo("Agent Categories:")
    click.echo("  • Research & Discovery: Unicode vulnerability research")
    click.echo("  • Attack Development: Payload and exploit generation")
    click.echo("  • Defense & Validation: Testing and detection")
    click.echo("  • Analysis & Documentation: Reporting and visualization")
    click.echo("  • Infrastructure: Testing and module development")
    click.echo("  • Specialized Research: Domain-specific experts")
    click.echo("\nCommands:")
    click.echo("  list    - List all available agents")
    click.echo("  run     - Run a single agent")
    click.echo("  swarm   - Run multiple agents as a swarm")
    click.echo("  status  - Check agent status")
    click.echo("  info    - Display this information")
    click.echo("\nExamples:")
    click.echo("  agents list")
    click.echo('  agents run unicode_archaeologist "Discover new control characters"')
    click.echo('  agents swarm "Analyze Python Unicode security"')
    click.echo("\n" + "=" * 70 + "\n")


if __name__ == '__main__':
    cli(obj={})
