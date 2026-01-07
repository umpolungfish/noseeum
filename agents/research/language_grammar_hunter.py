"""Language Grammar Hunter - Analyzes language Unicode handling quirks."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class LanguageGrammarHunter(BaseAgent):
    """
    Agent specialized in discovering language-specific Unicode handling quirks.

    Capabilities:
    - Analyzes programming language specifications
    - Discovers parser Unicode edge cases
    - Tests compiler/interpreter behaviors
    - Documents exploitable language features
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="language_grammar_hunter",
            name="Language Grammar Hunter",
            description="Discovers language-specific Unicode handling quirks",
            capabilities=[AgentCapability.RESEARCH],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.target_languages = config.get("target_languages", [
            "python", "javascript", "java", "go", "kotlin", "swift", "rust", "c", "cpp"
        ])

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        base_tools = self.toolkit.get_noseeum_tools()
        custom_tools = [
            {
                "name": "analyze_language_spec",
                "description": "Analyze language specification for Unicode handling",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "language": {"type": "string"},
                        "spec_url": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["language"]
                }
            },
            {
                "name": "test_parser_behavior",
                "description": "Test language parser with Unicode edge cases",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "language": {"type": "string"},
                        "test_code": {"type": "string"},
                        "expected_behavior": {"type": "string"}
                    },
                    "required": ["language", "test_code"]
                }
            },
            {
                "name": "create_language_module",
                "description": "Create noseeum language-specific attack module",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "language": {"type": "string"},
                        "vulnerabilities": {"type": "array"},
                        "exploits": {"type": "array"}
                    },
                    "required": ["language", "vulnerabilities"]
                }
            }
        ]
        return base_tools + custom_tools

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute language grammar hunting task."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            self.logger.info(f"Starting language grammar hunt: {task}")

            # Determine target languages
            target_langs = context.get("languages", self.target_languages) if context else self.target_languages

            findings = []

            for language in target_langs:
                self.logger.info(f"Analyzing {language}...")
                lang_findings = self._analyze_language(language)
                findings.extend(lang_findings)

            # Generate comprehensive report
            report = self._generate_report(findings)

            # Save artifacts
            artifact_path = self.save_artifact(
                f"language_analysis",
                report,
                "json"
            )

            result = {
                "findings": findings,
                "report": report,
                "artifacts": [artifact_path],
                "languages_analyzed": len(target_langs)
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
            self.logger.error(f"Language grammar hunt failed: {e}")
            self.fail(str(e))
            return {
                "status": "error",
                "agent": self.name,
                "error": str(e)
            }

    def _analyze_language(self, language: str) -> List[Dict[str, Any]]:
        """Analyze a specific language for Unicode quirks."""
        findings = []

        # Known vulnerabilities database (in practice, would be researched dynamically)
        known_quirks = {
            "python": [
                {
                    "type": "identifier_normalization",
                    "description": "Python normalizes identifiers using NFKC",
                    "exploitable": True,
                    "example": "𝓪𝓫𝓬 = 1; print(abc)  # Different variable names that normalize to same",
                    "severity": "high"
                }
            ],
            "javascript": [
                {
                    "type": "unicode_escapes",
                    "description": "JavaScript allows Unicode escapes in identifiers",
                    "exploitable": True,
                    "example": "var \\u0061bc = 1; console.log(abc);  # Same variable",
                    "severity": "medium"
                }
            ],
            "go": [
                {
                    "type": "utf8_validation",
                    "description": "Go compiler strictly validates UTF-8 encoding",
                    "exploitable": True,
                    "example": "// Invalid UTF-8 can bypass source code scanners",
                    "severity": "medium"
                }
            ],
            "java": [
                {
                    "type": "unicode_escapes",
                    "description": "Java processes Unicode escapes before parsing",
                    "exploitable": True,
                    "example": "String s = \"\\u002f\\u002f not a comment\";  # Becomes //",
                    "severity": "high"
                }
            ],
            "kotlin": [
                {
                    "type": "unicode_identifiers",
                    "description": "Kotlin allows wide range of Unicode in identifiers",
                    "exploitable": True,
                    "example": "val 變數 = 1  # Chinese characters in identifiers",
                    "severity": "low"
                }
            ]
        }

        if language.lower() in known_quirks:
            findings.extend(known_quirks[language.lower()])
        else:
            findings.append({
                "type": "research_needed",
                "description": f"No known quirks documented for {language}",
                "exploitable": False,
                "action": "Requires manual research and testing"
            })

        # Store in memory for future reference
        self.memory.store(f"{language}_quirks", findings, "language_quirks")

        return findings

    def _generate_report(self, findings: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive analysis report."""
        return {
            "total_findings": len(findings),
            "high_severity": len([f for f in findings if f.get("severity") == "high"]),
            "exploitable": len([f for f in findings if f.get("exploitable")]),
            "findings": findings,
            "recommendations": [
                "Implement language-specific modules for high-severity findings",
                "Create test cases for each exploitable quirk",
                "Update grammar database with documented behaviors",
                "Generate YARA rules for detection"
            ]
        }

    def test_parser_quirk(self, language: str, test_code: str) -> Dict[str, Any]:
        """Test a specific parser quirk."""
        try:
            # Create temporary test file
            test_dir = "agents/artifacts/parser_tests"
            os.makedirs(test_dir, exist_ok=True)

            ext_map = {
                "python": ".py",
                "javascript": ".js",
                "java": ".java",
                "go": ".go",
                "kotlin": ".kt",
                "swift": ".swift",
                "rust": ".rs",
                "c": ".c",
                "cpp": ".cpp"
            }

            ext = ext_map.get(language.lower(), ".txt")
            test_file = f"{test_dir}/test_{language}{ext}"

            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_code)

            self.logger.info(f"Created test file: {test_file}")

            return {
                "status": "test_created",
                "test_file": test_file,
                "language": language,
                "note": "Manual testing required"
            }

        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }


def main():
    """Test the Language Grammar Hunter agent."""
    config = {
        "model": "claude-sonnet-4-5-20250929",
        "target_languages": ["python", "javascript", "go", "java"]
    }

    agent = LanguageGrammarHunter(config)

    # Test task
    task = "Analyze Python, JavaScript, Go, and Java for Unicode identifier vulnerabilities"
    result = agent.run(task)

    print("\n=== Language Grammar Hunter Results ===")
    print(f"Status: {result['status']}")
    print(f"Languages Analyzed: {result.get('languages_analyzed', 0)}")
    print(f"\nFindings:")
    for finding in result.get('findings', []):
        print(f"  [{finding.get('severity', 'N/A')}] {finding.get('type')}: {finding.get('description')}")


if __name__ == "__main__":
    main()
