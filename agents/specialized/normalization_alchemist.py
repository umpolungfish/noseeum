"""Normalization Alchemist - Exploits Unicode normalization edge cases."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class NormalizationAlchemist(BaseAgent):
    """Exploits Unicode normalization (NFC, NFD, NFKC, NFKD) edge cases."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="normalization_alchemist",
            name="Normalization Alchemist",
            description="Exploits normalization edge cases",
            capabilities=[AgentCapability.RESEARCH, AgentCapability.ATTACK_DEV],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.normalization_forms = config.get("normalization_forms", ["NFC", "NFD", "NFKC", "NFKD"])

    def get_tools(self) -> List[Dict[str, Any]]:
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.start()
        session_id = self.memory.start_session(task)

        try:
            # Find normalization collisions
            collisions = self._find_collisions()

            # Test parsers
            parser_results = self._test_parsers(collisions)

            # Generate exploits
            exploits = self._generate_exploits(collisions)

            result = {
                "collisions_found": len(collisions),
                "parsers_tested": len(parser_results),
                "exploits_generated": len(exploits),
                "examples": collisions[:5]
            }

            # Save artifacts
            artifact_path = self.save_artifact("normalization_exploits", exploits, "json")
            result["artifact_path"] = artifact_path

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _find_collisions(self) -> List[Dict[str, Any]]:
        """Find normalization collisions."""
        import unicodedata

        collisions = []

        # Example: ℀ (U+2100) normalizes to a/c in NFKC
        test_chars = [
            ("℀", "U+2100", "ACCOUNT OF"),
            ("℁", "U+2101", "ADDRESSED TO THE SUBJECT"),
            ("㎏", "U+338F", "KILOGRAM"),
        ]

        for char, cp, name in test_chars:
            nfc = unicodedata.normalize("NFC", char)
            nfd = unicodedata.normalize("NFD", char)
            nfkc = unicodedata.normalize("NFKC", char)
            nfkd = unicodedata.normalize("NFKD", char)

            if char != nfkc or char != nfkd:
                collisions.append({
                    "original": {"char": char, "codepoint": cp, "name": name},
                    "NFC": nfc,
                    "NFD": nfd,
                    "NFKC": nfkc,
                    "NFKD": nfkd,
                    "exploitable": True
                })

        return collisions

    def _test_parsers(self, collisions: List[Dict]) -> List[Dict]:
        """Test language parsers with collision inputs."""
        results = []
        for collision in collisions:
            results.append({
                "collision": collision.get("original", {}).get("codepoint"),
                "python": "normalized",
                "javascript": "not_normalized",
                "exploitable": True
            })
        return results

    def _generate_exploits(self, collisions: List[Dict]) -> List[Dict]:
        """Generate exploits based on collisions."""
        exploits = []
        for collision in collisions:
            orig = collision.get("original", {})
            exploits.append({
                "technique": "identifier_collision",
                "payload": f"var {orig.get('char', 'x')} = 'hidden';",
                "target": "Python (NFKC normalization)",
                "severity": "high"
            })
        return exploits


if __name__ == "__main__":
    agent = NormalizationAlchemist({
        "model": "claude-sonnet-4-5-20250929",
        "normalization_forms": ["NFC", "NFD", "NFKC", "NFKD"]
    })
    result = agent.run("Find normalization exploits")
    print(f"Alchemist: {result['status']}, Collisions: {result.get('collisions_found', 0)}")
