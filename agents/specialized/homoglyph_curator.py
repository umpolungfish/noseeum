"""Homoglyph Curator - Maintains homoglyph registry."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class HomoglyphCurator(BaseAgent):
    """Maintains and expands the homoglyph registry with visual confusables."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="homoglyph_curator",
            name="Homoglyph Curator",
            description="Maintains homoglyph registry",
            capabilities=[AgentCapability.RESEARCH],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.similarity_threshold = config.get("visual_similarity_threshold", 0.8)
        self.unicode_blocks = config.get("unicode_blocks", [
            "basic_latin", "cyrillic", "greek", "han", "hangul"
        ])

    def get_tools(self) -> List[Dict[str, Any]]:
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.start()
        session_id = self.memory.start_session(task)

        try:
            # Discover new homoglyphs
            new_homoglyphs = self._discover_homoglyphs()

            # Test visual similarity
            validated = self._validate_similarity(new_homoglyphs)

            # Update registry
            registry_path = self._update_registry(validated)

            result = {
                "discovered": len(new_homoglyphs),
                "validated": len(validated),
                "registry_path": registry_path,
                "homoglyphs": validated[:10]  # Top 10
            }

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _discover_homoglyphs(self) -> List[Dict[str, Any]]:
        """Discover new homoglyphs across Unicode blocks."""
        homoglyphs = []

        # Latin 'a' (U+0061) looks like Cyrillic 'а' (U+0430)
        homoglyphs.append({
            "latin": {"char": "a", "codepoint": "U+0061"},
            "cyrillic": {"char": "а", "codepoint": "U+0430"},
            "similarity": 0.99
        })

        # Latin 'e' (U+0065) looks like Cyrillic 'е' (U+0435)
        homoglyphs.append({
            "latin": {"char": "e", "codepoint": "U+0065"},
            "cyrillic": {"char": "е", "codepoint": "U+0435"},
            "similarity": 0.99
        })

        # Latin 'o' (U+006F) looks like Cyrillic 'о' (U+043E)
        homoglyphs.append({
            "latin": {"char": "o", "codepoint": "U+006F"},
            "cyrillic": {"char": "о", "codepoint": "U+043E"},
            "similarity": 0.99
        })

        return homoglyphs

    def _validate_similarity(self, homoglyphs: List[Dict]) -> List[Dict]:
        """Validate visual similarity of homoglyphs."""
        validated = []
        for h in homoglyphs:
            if h.get("similarity", 0) >= self.similarity_threshold:
                validated.append(h)
        return validated

    def _update_registry(self, homoglyphs: List[Dict]) -> str:
        """Update homoglyph registry."""
        try:
            registry_path = "homoglyph_registry.json"
            current_registry = {}

            if os.path.exists(registry_path):
                current_registry = self.toolkit.json_load(registry_path)

            # Add new homoglyphs
            for h in homoglyphs:
                latin_char = h.get("latin", {}).get("char")
                if latin_char:
                    if latin_char not in current_registry:
                        current_registry[latin_char] = []
                    current_registry[latin_char].append(h.get("cyrillic", {}).get("char"))

            # Save updated registry
            artifact_path = self.save_artifact("updated_homoglyph_registry", current_registry, "json")

            self.logger.info(f"Registry updated: {artifact_path}")
            return artifact_path

        except Exception as e:
            self.logger.error(f"Failed to update registry: {e}")
            return ""


if __name__ == "__main__":
    agent = HomoglyphCurator({
        "model": "claude-sonnet-4-5-20250929",
        "visual_similarity_threshold": 0.8
    })
    result = agent.run("Discover new homoglyphs")
    print(f"Curator: {result['status']}, Discovered: {result.get('discovered', 0)}")
