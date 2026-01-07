"""YARA Rule Smith - Generates detection rules."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class YaraRuleSmith(BaseAgent):
    """Generates YARA rules for attack detection."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="yara_rule_smith",
            name="YARA Rule Smith",
            description="Generates detection rules",
            capabilities=[AgentCapability.DEFENSE],
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
            attack_type = context.get("attack_type", "bidi") if context else "bidi"
            rules = self._generate_yara_rules(attack_type)

            artifact_path = self.save_artifact(f"yara_rules_{attack_type}", rules, "text")

            result = {"rules": rules, "attack_type": attack_type, "artifacts": [artifact_path]}

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _generate_yara_rules(self, attack_type: str) -> str:
        templates = {
            "bidi": '''rule unicode_bidi_attack {
    meta:
        description = "Detects bidirectional Unicode control characters"
        author = "YARA Rule Smith"
    strings:
        $bidi1 = { E2 80 8E }  // LEFT-TO-RIGHT MARK
        $bidi2 = { E2 80 8F }  // RIGHT-TO-LEFT MARK
        $bidi3 = { E2 80 AA }  // LEFT-TO-RIGHT EMBEDDING
    condition:
        any of them
}''',
            "homoglyph": '''rule unicode_homoglyph_attack {
    meta:
        description = "Detects Cyrillic homoglyphs"
    strings:
        $cyrillic_a = { D0 B0 }  // Cyrillic 'a'
        $cyrillic_e = { D0 B5 }  // Cyrillic 'e'
    condition:
        any of them
}'''
        }
        return templates.get(attack_type, "# No template for " + attack_type)


if __name__ == "__main__":
    agent = YaraRuleSmith({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Generate YARA rules", {"attack_type": "bidi"})
    print(f"Generated: {result['status']}")
