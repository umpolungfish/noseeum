"""Payload Artisan - Creates context-aware malicious payloads."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class PayloadArtisan(BaseAgent):
    """
    Agent specialized in generating creative, context-aware payloads.

    Capabilities:
    - Analyzes codebase style and patterns
    - Generates payloads that blend naturally
    - Adapts to coding conventions
    - Creates polymorphic variants
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="payload_artisan",
            name="Payload Artisan",
            description="Creates context-aware malicious payloads",
            capabilities=[AgentCapability.ATTACK_DEV],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.creativity = config.get("creativity", "high")

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        base_tools = self.toolkit.get_noseeum_tools()
        custom_tools = [
            {
                "name": "analyze_codebase_style",
                "description": "Analyze codebase coding style and patterns",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "directory": {"type": "string"},
                        "language": {"type": "string"}
                    },
                    "required": ["directory", "language"]
                }
            },
            {
                "name": "generate_payload_variant",
                "description": "Generate payload variant with specific characteristics",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "base_payload": {"type": "string"},
                        "target_style": {"type": "string"},
                        "obfuscation_level": {"type": "string"}
                    },
                    "required": ["base_payload"]
                }
            },
            {
                "name": "test_payload_naturalness",
                "description": "Test how natural payload looks in context",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "payload": {"type": "string"},
                        "context": {"type": "string"}
                    },
                    "required": ["payload", "context"]
                }
            }
        ]
        return base_tools + custom_tools

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute payload generation task."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            self.logger.info(f"Starting payload generation: {task}")

            # Use intelligent context extraction
            target_language = self._extract_from_context(context, "language", "python")
            attack_type = self._extract_from_context(context, "attack_type", "bidi")
            target_file = self._extract_from_context(context, "target_file", None)

            # Log received context for debugging
            if context:
                self.logger.info(f"Context keys: {list(context.keys())}")
                if "findings" in context:
                    self.logger.info(f"Received {len(context['findings'])} findings from previous agent")

            # Analyze target if provided
            style_analysis = None
            if target_file and os.path.exists(target_file):
                style_analysis = self._analyze_code_style(target_file, target_language)

            # Generate payloads
            payloads = self._generate_payloads(attack_type, target_language, style_analysis)

            # Rank by naturalness
            ranked_payloads = self._rank_payloads(payloads, style_analysis)

            # Save artifacts
            artifact_path = self.save_artifact(
                "generated_payloads",
                {
                    "task": task,
                    "language": target_language,
                    "attack_type": attack_type,
                    "payloads": ranked_payloads
                },
                "json"
            )

            result = {
                "payloads": ranked_payloads[:5],  # Top 5
                "total_generated": len(payloads),
                "artifacts": [artifact_path],
                "style_analysis": style_analysis
            }

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {
                "status": "success",
                "agent": self.name,
                "task": task,
                **result
            }

        except Exception as e:
            self.logger.error(f"Payload generation failed: {e}")
            self.fail(str(e))
            return {
                "status": "error",
                "agent": self.name,
                "error": str(e)
            }

    def _analyze_code_style(self, filepath: str, language: str) -> Dict[str, Any]:
        """Analyze coding style of target file."""
        try:
            content = self.toolkit.file_read(filepath)

            analysis = {
                "indentation": self._detect_indentation(content),
                "naming_convention": self._detect_naming(content, language),
                "comment_style": self._detect_comments(content, language),
                "line_length": self._avg_line_length(content),
                "common_patterns": self._extract_patterns(content, language)
            }

            return analysis

        except Exception as e:
            self.logger.error(f"Style analysis failed: {e}")
            return {}

    def _detect_indentation(self, content: str) -> str:
        """Detect indentation style (spaces/tabs)."""
        lines = content.split('\n')
        space_count = sum(1 for line in lines if line.startswith('    '))
        tab_count = sum(1 for line in lines if line.startswith('\t'))
        return "tabs" if tab_count > space_count else "4spaces"

    def _detect_naming(self, content: str, language: str) -> str:
        """Detect naming convention."""
        import re
        # Simple heuristic - check variable patterns
        snake_case = len(re.findall(r'\b[a-z]+_[a-z]+\b', content))
        camel_case = len(re.findall(r'\b[a-z]+[A-Z][a-z]+\b', content))

        return "snake_case" if snake_case > camel_case else "camelCase"

    def _detect_comments(self, content: str, language: str) -> str:
        """Detect comment style."""
        comment_markers = {
            "python": "#",
            "javascript": "//",
            "java": "//",
            "c": "//",
            "cpp": "//"
        }
        marker = comment_markers.get(language, "#")
        return f"{marker} style"

    def _avg_line_length(self, content: str) -> int:
        """Calculate average line length."""
        lines = [l for l in content.split('\n') if l.strip()]
        return sum(len(l) for l in lines) // len(lines) if lines else 80

    def _extract_patterns(self, content: str, language: str) -> List[str]:
        """Extract common code patterns."""
        patterns = []

        if "import" in content:
            patterns.append("uses_imports")
        if "class " in content:
            patterns.append("object_oriented")
        if "def " in content or "function " in content:
            patterns.append("functional")

        return patterns

    def _generate_payloads(self, attack_type: str, language: str,
                           style: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate multiple payload variants."""
        payloads = []

        # Language-specific templates
        templates = {
            "python": {
                "bidi": [
                    '# Legitimate code\u202Eevil = "malicious"\u202D',
                    'safe = "ok"  # Comment\u202Eevil()\u202D',
                    'def test(): # \u202Eevil_code()\u202D\n    pass',
                ],
                "homoglyph": [
                    'admin = "safe"  # Using cyrillic а',
                    'uѕer = "data"  # Cyrillic s',
                    'арі_kеy = "xxx"  # Mixed Cyrillic',
                ],
                "invisible": [
                    'variable\u200B= "hidden zero-width"',
                    'user\u200Cdata = "hidden joiner"',
                    'api\u200Dkey = "zero-width joiner"',
                ]
            },
            "javascript": {
                "bidi": [
                    'var safe = "ok";  // Comment\u202Eevil();\u202D',
                    'function test() { /*\u202Eevil_code();\u202D*/ return true; }',
                    'const data = "safe"; // \u202Econsole.log("evil")\u202D',
                ],
                "homoglyph": [
                    'let admin = "safe";  // Using cyrillic а',
                    'let uѕer = "data";  // Cyrillic s',
                    'const арі_kеy = "xxx";  // Mixed Cyrillic',
                ],
                "invisible": [
                    'var variable\u200B= "hidden zero-width";',
                    'let user\u200Cdata = "hidden joiner";',
                    'const api\u200Dkey = "zero-width joiner";',
                ]
            },
            "java": {
                "bidi": [
                    'String safe = "ok";  // Comment\u202Eevil();\u202D',
                    'public void test() { /*\u202EevilCode();\u202D*/ return; }',
                    'private String data = "safe"; // \u202ESystem.out.println("evil");\u202D',
                ],
                "homoglyph": [
                    'String admin = "safe";  // Using cyrillic а',
                    'String uѕer = "data";  // Cyrillic s',
                    'final String арі_kеy = "xxx";  // Mixed Cyrillic',
                ],
                "invisible": [
                    'String variable\u200B= "hidden zero-width";',
                    'Object user\u200Cdata = "hidden joiner";',
                    'final String api\u200Dkey = "zero-width joiner";',
                ]
            },
            "go": {
                "bidi": [
                    'safe := "ok"  // Comment\u202Eevil()\u202D',
                    'func test() { /*\u202EevilCode()\u202D*/ return }',
                    'var data = "safe" // \u202Efmt.Println("evil")\u202D',
                ],
                "homoglyph": [
                    'admin := "safe"  // Using cyrillic а',
                    'uѕer := "data"  // Cyrillic s',
                    'const арі_kеy = "xxx"  // Mixed Cyrillic',
                ],
                "invisible": [
                    'var variable\u200B= "hidden zero-width"',
                    'user\u200Cdata := "hidden joiner"',
                    'api\u200Dkey := "zero-width joiner"',
                ]
            },
            "rust": {
                "bidi": [
                    'let safe = "ok";  // Comment\u202Eevil();\u202D',
                    'fn test() { /*\u202Eevil_code();\u202D*/ return; }',
                    'let data = "safe"; // \u202Eprintln!("evil");\u202D',
                ],
                "homoglyph": [
                    'let admin = "safe";  // Using cyrillic а',
                    'let uѕer = "data";  // Cyrillic s',
                    'const арі_kеy: &str = "xxx";  // Mixed Cyrillic',
                ],
                "invisible": [
                    'let variable\u200B= "hidden zero-width";',
                    'let user\u200Cdata = "hidden joiner";',
                    'let api\u200Dkey = "zero-width joiner";',
                ]
            }
        }

        # Normalize language names
        lang_normalized = language.lower()
        if lang_normalized not in templates:
            lang_normalized = "python"  # Default fallback

        # Get language-specific attack templates
        lang_templates = templates[lang_normalized]
        base_templates = lang_templates.get(attack_type, lang_templates.get("bidi", []))

        for i, template in enumerate(base_templates):
            payloads.append({
                "id": i,
                "payload": template,
                "attack_type": attack_type,
                "language": lang_normalized,
                "naturalness_score": 0  # Will be calculated
            })

        return payloads

    def _rank_payloads(self, payloads: List[Dict[str, Any]],
                      style: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rank payloads by naturalness score."""
        for payload in payloads:
            score = 0.5  # Base score

            # Bonus for matching style
            if style:
                if style.get("indentation") == "4spaces":
                    score += 0.1
                if style.get("naming_convention") == "snake_case":
                    score += 0.1

            payload["naturalness_score"] = min(score, 1.0)

        # Sort by score descending
        payloads.sort(key=lambda p: p["naturalness_score"], reverse=True)

        return payloads


def main():
    """Test the Payload Artisan agent."""
    config = {
        "model": "claude-sonnet-4-5-20250929",
        "creativity": "high"
    }

    agent = PayloadArtisan(config)

    task = "Generate stealthy bidirectional override payloads for Python"
    context = {
        "language": "python",
        "attack_type": "bidi"
    }

    result = agent.run(task, context)

    print("\n=== Payload Artisan Results ===")
    print(f"Status: {result['status']}")
    print(f"Generated: {result.get('total_generated', 0)} payloads")
    print(f"\nTop Payloads:")
    for p in result.get('payloads', []):
        print(f"  [{p['naturalness_score']:.2f}] {p['payload'][:60]}...")


if __name__ == "__main__":
    main()
