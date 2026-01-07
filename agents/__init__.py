"""Noseeum Agent Menagerie - Autonomous security research agents."""

__version__ = "1.0.0"

# Lazy imports to avoid circular dependencies
def get_orchestrator(config_path: str = "agents/config.yaml"):
    """
    Get an orchestrator instance.

    Args:
        config_path: Path to configuration file

    Returns:
        AgentOrchestrator instance
    """
    from .orchestrator import AgentOrchestrator
    return AgentOrchestrator(config_path)


def list_available_agents() -> dict:
    """
    List all available agents with their descriptions.

    Returns:
        Dictionary of agent_id -> agent_info
    """
    orchestrator = get_orchestrator()
    return {agent['id']: agent for agent in orchestrator.list_agents()}


# Export commonly used items
__all__ = [
    'get_orchestrator',
    'list_available_agents',
]
