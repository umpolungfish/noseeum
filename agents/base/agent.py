"""Base agent class for all noseeum agents."""

import os
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Any, Optional
from datetime import datetime
import anthropic


class AgentStatus(Enum):
    """Agent execution status."""
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"


class AgentCapability(Enum):
    """Agent capabilities."""
    RESEARCH = "research"
    ATTACK_DEV = "attack_development"
    DEFENSE = "defense"
    ANALYSIS = "analysis"
    TESTING = "testing"
    DOCUMENTATION = "documentation"


class BaseAgent(ABC):
    """Base class for all noseeum agents."""

    def __init__(self, agent_id: str, name: str, description: str,
                 capabilities: List[AgentCapability], config: Dict[str, Any]):
        """
        Initialize base agent.

        Args:
            agent_id: Unique identifier for agent
            name: Human-readable agent name
            description: Agent description
            capabilities: List of agent capabilities
            config: Agent configuration dictionary
        """
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.capabilities = capabilities
        self.config = config
        self.status = AgentStatus.IDLE
        self.logger = self._setup_logger()
        self.client = self._setup_anthropic_client()
        self.memory: Dict[str, Any] = {}
        self.results: List[Dict[str, Any]] = []
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def _setup_logger(self) -> logging.Logger:
        """Set up agent logger."""
        # Get log level from config, default to DEBUG for verbose output
        log_level_str = self.config.get('log_level', 'DEBUG')
        log_level = getattr(logging, log_level_str.upper(), logging.DEBUG)

        logger = logging.getLogger(f"noseeum.agent.{self.agent_id}")
        logger.setLevel(log_level)

        # Console handler - use the same level as configured
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter(
            f'[%(asctime)s] [{self.name}] %(levelname)s: %(message)s'
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler
        os.makedirs("agents/logs", exist_ok=True)
        file_handler = logging.FileHandler(f"agents/logs/{self.agent_id}.log")
        file_handler.setLevel(logging.DEBUG)  # Always log DEBUG to file for detailed records
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    def _setup_anthropic_client(self) -> anthropic.Anthropic:
        """Set up Anthropic API client."""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            self.logger.warning("ANTHROPIC_API_KEY not set, using demo mode")
            return None
        return anthropic.Anthropic(api_key=api_key)

    @abstractmethod
    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute agent task.

        Args:
            task: Task description
            context: Optional context dictionary

        Returns:
            Result dictionary
        """
        pass

    @abstractmethod
    def get_tools(self) -> List[Dict[str, Any]]:
        """
        Get agent-specific tools.

        Returns:
            List of tool definitions for Claude API
        """
        pass

    def start(self):
        """Start agent execution."""
        self.status = AgentStatus.RUNNING
        self.start_time = datetime.now()
        self.logger.info(f"Agent {self.name} started")

    def complete(self, result: Dict[str, Any]):
        """Mark agent as completed."""
        self.status = AgentStatus.COMPLETED
        self.end_time = datetime.now()
        self.results.append(result)
        duration = (self.end_time - self.start_time).total_seconds()
        self.logger.info(f"Agent {self.name} completed in {duration:.2f}s")

    def fail(self, error: str):
        """Mark agent as failed."""
        self.status = AgentStatus.FAILED
        self.end_time = datetime.now()
        self.logger.error(f"Agent {self.name} failed: {error}")

    def pause(self):
        """Pause agent execution."""
        self.status = AgentStatus.PAUSED
        self.logger.info(f"Agent {self.name} paused")

    def resume(self):
        """Resume agent execution."""
        self.status = AgentStatus.RUNNING
        self.logger.info(f"Agent {self.name} resumed")

    def save_artifact(self, artifact_name: str, content: Any,
                      artifact_type: str = "text") -> str:
        """
        Save agent artifact.

        Args:
            artifact_name: Name of artifact
            content: Artifact content
            artifact_type: Type of artifact (text, json, binary)

        Returns:
            Path to saved artifact
        """
        os.makedirs("agents/artifacts", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.agent_id}_{artifact_name}_{timestamp}"

        if artifact_type == "json":
            import json
            filepath = f"agents/artifacts/{filename}.json"
            with open(filepath, 'w') as f:
                json.dump(content, f, indent=2)
        elif artifact_type == "binary":
            filepath = f"agents/artifacts/{filename}.bin"
            with open(filepath, 'wb') as f:
                f.write(content)
        else:
            filepath = f"agents/artifacts/{filename}.txt"
            with open(filepath, 'w') as f:
                f.write(str(content))

        self.logger.info(f"Artifact saved: {filepath}")
        return filepath

    def store_in_memory(self, key: str, value: Any):
        """Store data in agent memory."""
        self.memory[key] = value
        self.logger.debug(f"Stored in memory: {key}")

    def retrieve_from_memory(self, key: str) -> Optional[Any]:
        """Retrieve data from agent memory."""
        return self.memory.get(key)

    def get_status_report(self) -> Dict[str, Any]:
        """Get agent status report."""
        duration = None
        if self.start_time:
            end = self.end_time or datetime.now()
            duration = (end - self.start_time).total_seconds()

        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "status": self.status.value,
            "capabilities": [c.value for c in self.capabilities],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "duration_seconds": duration,
            "results_count": len(self.results),
            "memory_size": len(self.memory),
        }

    def call_claude(self, messages: List[Dict[str, Any]],
                    tools: Optional[List[Dict[str, Any]]] = None,
                    max_tokens: int = 4000) -> Any:
        """
        Call Claude API with messages and tools.

        Args:
            messages: List of message dictionaries
            tools: Optional list of tool definitions
            max_tokens: Maximum tokens in response

        Returns:
            API response
        """
        if not self.client:
            self.logger.warning("Claude API client not available (demo mode)")
            return {"type": "text", "text": "Demo mode - no API call made"}

        try:
            kwargs = {
                "model": self.config.get("model", "claude-sonnet-4-5-20250929"),
                "max_tokens": max_tokens,
                "messages": messages,
            }

            if tools:
                kwargs["tools"] = tools

            response = self.client.messages.create(**kwargs)
            return response
        except Exception as e:
            self.logger.error(f"Claude API call failed: {e}")
            raise
