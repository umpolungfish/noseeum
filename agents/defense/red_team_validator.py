"""Red Team Validator - Tests attack effectiveness."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class RedTeamValidator(BaseAgent):
    """Tests attack effectiveness against real-world security tools."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="red_team_validator",
            name="Red Team Validator",
            description="Tests attack effectiveness",
            capabilities=[AgentCapability.DEFENSE, AgentCapability.TESTING],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)

    def get_tools(self) -> List[Dict[str, Any]]:
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.start()
        session_id = self.memory.start_session(task)

        try:
            attack = context.get("attack") if context else None
            target_file = context.get("target_file") if context else None
            language = context.get("language", "python") if context else "python"
            tools = context.get("test_tools", [
                "semgrep", "bandit", "eslint", "pylint", "gosec", "codeql", "sonarqube"
            ]) if context else ["semgrep", "bandit"]

            # Create temp file if needed
            import tempfile
            import os
            temp_file = None
            if not target_file and attack:
                ext_map = {"python": ".py", "javascript": ".js", "java": ".java", "go": ".go"}
                ext = ext_map.get(language, ".txt")
                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix=ext, delete=False)
                temp_file.write(attack)
                temp_file.close()
                target_file = temp_file.name

            # Test with all tools
            batch_results = self.toolkit.batch_test_security_tools(target_file, tools, language)

            # Clean up
            if temp_file:
                os.unlink(temp_file.name)

            test_results = {
                "tools_tested": batch_results["summary"]["total_tools"],
                "bypassed": batch_results["summary"]["bypassed"],
                "detected": batch_results["summary"]["detected"],
                "details": batch_results["results"]
            }

            result = {
                "test_results": test_results,
                "effectiveness_score": batch_results["summary"]["evasion_rate"]
            }

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}


if __name__ == "__main__":
    agent = RedTeamValidator({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Test attack", {"attack": "test_payload"})
    print(f"Validated: {result['status']}")
