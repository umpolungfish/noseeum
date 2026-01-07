"""Tests for agent orchestrator."""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator import AgentOrchestrator


@pytest.fixture
def orchestrator():
    """Create orchestrator instance."""
    return AgentOrchestrator()


def test_orchestrator_initialization(orchestrator):
    """Test orchestrator initialization."""
    assert orchestrator is not None
    assert len(orchestrator.agents) > 0


def test_list_agents(orchestrator):
    """Test listing agents."""
    agents = orchestrator.list_agents()
    assert len(agents) > 0
    assert all('id' in agent for agent in agents)
    assert all('name' in agent for agent in agents)


def test_run_single_agent(orchestrator):
    """Test running a single agent."""
    result = orchestrator.run_agent(
        "unicode_archaeologist",
        "Test task"
    )
    assert "status" in result


def test_run_invalid_agent(orchestrator):
    """Test running invalid agent."""
    result = orchestrator.run_agent("invalid_agent", "Test")
    assert result["status"] == "error"


def test_run_swarm(orchestrator):
    """Test running agent swarm."""
    result = orchestrator.run_swarm(
        "Test task",
        agent_ids=["unicode_archaeologist", "payload_artisan"]
    )

    assert result["status"] == "completed"
    assert result["agents_run"] == 2
    assert "results" in result


def test_get_agent_status(orchestrator):
    """Test getting agent status."""
    status = orchestrator.get_agent_status("unicode_archaeologist")
    assert status is not None
    assert "agent_id" in status
    assert "status" in status


def test_get_all_status(orchestrator):
    """Test getting all agent statuses."""
    all_status = orchestrator.get_all_status()
    assert len(all_status) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
