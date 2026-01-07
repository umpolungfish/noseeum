"""Polyglot Specialist - Creates cross-language polyglot attacks."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class PolyglotSpecialist(BaseAgent):
    """Creates polyglot attacks exploiting multiple languages simultaneously."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="polyglot_specialist",
            name="Polyglot Specialist",
            description="Creates cross-language polyglot attacks",
            capabilities=[AgentCapability.ATTACK_DEV],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute polyglot creation."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            languages = context.get("languages", ["python", "javascript"]) if context else ["python", "javascript"]

            # Find syntax overlaps
            overlaps = self._find_syntax_overlaps(languages)

            # Generate polyglot payload
            polyglot = self._generate_polyglot(languages, overlaps)

            result = {
                "languages": languages,
                "overlaps": overlaps,
                "polyglot_payload": polyglot,
                "compatibility_score": 0.8
            }

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _find_syntax_overlaps(self, languages: List[str]) -> List[Dict[str, Any]]:
        """Find syntax overlaps between languages."""
        overlaps = [
            {"feature": "comments", "syntax": "//", "languages": ["javascript", "java", "c", "cpp", "go"]},
            {"feature": "strings", "syntax": "\"\"", "languages": ["python", "javascript", "java", "c", "cpp"]},
        ]
        return overlaps

    def _generate_polyglot(self, languages: List[str], overlaps: List[Dict]) -> str:
        """Generate polyglot payload."""
        return f"/* Polyglot for {', '.join(languages)} */ // Valid in both"


if __name__ == "__main__":
    agent = PolyglotSpecialist({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Create Python/JS polyglot", {"languages": ["python", "javascript"]})
    print(f"Result: {result['status']}")
