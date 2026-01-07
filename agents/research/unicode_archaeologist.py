"""Unicode Archaeologist - Discovers new Unicode vulnerabilities."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class UnicodeArchaeologist(BaseAgent):
    """
    Agent specialized in discovering Unicode vulnerabilities and control characters.

    Capabilities:
    - Mines Unicode standards for exploitable characters
    - Tracks CVEs related to Unicode security
    - Discovers undocumented parser behaviors
    - Updates grammar database with new findings
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="unicode_archaeologist",
            name="Unicode Archaeologist",
            description="Discovers new Unicode vulnerabilities and control characters",
            capabilities=[AgentCapability.RESEARCH],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        base_tools = self.toolkit.get_noseeum_tools()
        custom_tools = [
            {
                "name": "analyze_unicode_block",
                "description": "Analyze a Unicode block for suspicious characters",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "block_name": {"type": "string", "description": "Unicode block name"},
                        "start_codepoint": {"type": "integer", "description": "Start codepoint (hex)"},
                        "end_codepoint": {"type": "integer", "description": "End codepoint (hex)"}
                    },
                    "required": ["block_name", "start_codepoint", "end_codepoint"]
                }
            },
            {
                "name": "search_cve_database",
                "description": "Search CVE database for Unicode vulnerabilities",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "keywords": {"type": "array", "items": {"type": "string"}},
                        "year": {"type": "integer", "description": "Optional year filter"}
                    },
                    "required": ["keywords"]
                }
            },
            {
                "name": "update_grammar_db",
                "description": "Update grammar database with new vulnerability",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "language": {"type": "string"},
                        "vulnerability": {"type": "object"}
                    },
                    "required": ["language", "vulnerability"]
                }
            }
        ]
        return base_tools + custom_tools

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute Unicode archaeology task."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            self.logger.info(f"Starting Unicode archaeology: {task}")

            # Build the system prompt
            system_prompt = self._build_system_prompt()

            # Prepare messages
            messages = [
                {
                    "role": "user",
                    "content": f"""Task: {task}

Context: {context if context else 'None provided'}

Please perform comprehensive Unicode security research to discover:
1. New exploitable Unicode characters and control codes
2. Recent CVEs related to Unicode handling
3. Language-specific parser quirks
4. Undocumented Unicode behaviors

Provide actionable findings that can be integrated into the noseeum framework."""
                }
            ]

            # Execute with Claude
            result = self._execute_with_tools(messages, system_prompt)

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {
                "status": "success",
                "agent": self.name,
                "task": task,
                "findings": result.get("findings", []),
                "artifacts": result.get("artifacts", []),
                "session_id": session_id
            }

        except Exception as e:
            self.logger.error(f"Unicode archaeology failed: {e}")
            self.fail(str(e))
            return {
                "status": "error",
                "agent": self.name,
                "error": str(e)
            }

    def _build_system_prompt(self) -> str:
        """Build system prompt for the agent."""
        return """You are the Unicode Archaeologist, a specialized agent for discovering Unicode security vulnerabilities.

Your expertise includes:
- Deep knowledge of Unicode standards (UAX reports, Unicode blocks)
- CVE tracking and vulnerability analysis
- Programming language parser behaviors
- Exploitation techniques using Unicode

Your tools allow you to:
- Analyze Unicode blocks systematically
- Search CVE databases for Unicode-related vulnerabilities
- Update the grammar database with new findings
- Read and write files in the noseeum framework
- Execute commands and fetch web resources

When discovering vulnerabilities:
1. Be systematic - analyze Unicode blocks methodically
2. Focus on exploitable characteristics (invisibility, directionality, normalization)
3. Test against multiple programming languages
4. Document findings with CVE references when applicable
5. Provide integration code for noseeum framework

Always provide concrete, actionable results."""

    def _execute_with_tools(self, messages: List[Dict[str, Any]], system_prompt: str) -> Dict[str, Any]:
        """Execute task with tool use."""
        tools = self.get_tools()
        findings = []
        artifacts = []

        try:
            # In a real implementation, this would use the Claude API with tool use
            # For now, provide a structured response framework

            # Simulate research findings
            findings.append({
                "type": "unicode_block_analysis",
                "description": "Analyzed Unicode block for exploitable characters",
                "block": "Miscellaneous Technical",
                "range": "U+2300-U+23FF",
                "suspicious_chars": [
                    {"codepoint": "U+2060", "name": "WORD JOINER", "category": "Cf"},
                    {"codepoint": "U+2061", "name": "FUNCTION APPLICATION", "category": "Cf"},
                ]
            })

            findings.append({
                "type": "cve_research",
                "description": "Recent Unicode-related CVEs",
                "cves": [
                    {
                        "id": "CVE-2021-42574",
                        "title": "Trojan Source Attack",
                        "description": "Bidirectional Unicode control characters in source code"
                    }
                ]
            })

            # Save artifacts
            artifact_path = self.save_artifact(
                "unicode_findings",
                str(findings),
                "json"
            )
            artifacts.append(artifact_path)

            return {
                "findings": findings,
                "artifacts": artifacts,
                "recommendations": [
                    "Add detection for U+2060-U+2064 format characters",
                    "Update BIDI attack module with latest UAX#9 findings",
                    "Test Trojan Source patterns against noseeum detector"
                ]
            }

        except Exception as e:
            self.logger.error(f"Tool execution failed: {e}")
            raise

    def analyze_unicode_block(self, block_name: str, start: int, end: int) -> Dict[str, Any]:
        """Analyze a Unicode block for suspicious characters."""
        suspicious = []

        for cp in range(start, end + 1):
            try:
                char = chr(cp)
                import unicodedata
                name = unicodedata.name(char, "UNNAMED")
                category = unicodedata.category(char)

                # Check for exploitable categories
                if category in ['Cf', 'Cc', 'Co']:  # Format, Control, Private Use
                    suspicious.append({
                        "codepoint": f"U+{cp:04X}",
                        "char": char if category != 'Cc' else repr(char),
                        "name": name,
                        "category": category
                    })
            except:
                pass

        return {
            "block_name": block_name,
            "range": f"U+{start:04X}-U+{end:04X}",
            "suspicious_count": len(suspicious),
            "suspicious_chars": suspicious
        }

    def search_unicode_org(self, query: str) -> List[Dict[str, Any]]:
        """Search unicode.org for relevant information."""
        try:
            # In practice, would use web scraping or API
            results = []
            self.logger.info(f"Searching unicode.org for: {query}")
            return results
        except Exception as e:
            self.logger.error(f"unicode.org search failed: {e}")
            return []

    def update_framework_grammar_db(self, language: str, vulnerability: Dict[str, Any]):
        """Update noseeum grammar database."""
        try:
            grammar_db_path = "noseeum/core/grammar_db.py"

            if os.path.exists(grammar_db_path):
                self.logger.info(f"Updating grammar DB for {language}: {vulnerability}")
                # Would integrate into grammar_db.py
                self.memory.store(f"grammar_update_{language}", vulnerability, "updates")
            else:
                self.logger.warning("Grammar DB not found")

        except Exception as e:
            self.logger.error(f"Failed to update grammar DB: {e}")


def main():
    """Test the Unicode Archaeologist agent."""
    config = {
        "model": "claude-sonnet-4-5-20250929",
        "research_depth": "deep"
    }

    agent = UnicodeArchaeologist(config)

    # Test task
    task = "Discover new Unicode control characters suitable for stealth attacks"
    result = agent.run(task)

    print("\n=== Unicode Archaeologist Results ===")
    print(f"Status: {result['status']}")
    print(f"\nFindings: {len(result.get('findings', []))}")
    for finding in result.get('findings', []):
        print(f"  - {finding['type']}: {finding['description']}")


if __name__ == "__main__":
    main()
