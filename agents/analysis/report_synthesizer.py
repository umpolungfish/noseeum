"""Report Synthesizer - Generates security reports."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory
from datetime import datetime


class ReportSynthesizer(BaseAgent):
    """Generates professional security research reports."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="report_synthesizer",
            name="Report Synthesizer",
            description="Generates security reports",
            capabilities=[AgentCapability.DOCUMENTATION],
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
            report_type = context.get("report_type", "technical") if context else "technical"
            findings = context.get("findings", []) if context else []

            report = self._generate_report(report_type, findings)

            report_path = self.save_artifact(f"report_{report_type}", report, "text")

            result = {"report_type": report_type, "report_path": report_path}

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _generate_report(self, report_type: str, findings: List) -> str:
        report = f"""# Security Research Report
## {report_type.capitalize()} Analysis

Generated: {datetime.now().isoformat()}

### Executive Summary
This report documents Unicode-based security vulnerabilities discovered by the noseeum framework.

### Findings
"""
        for i, finding in enumerate(findings, 1):
            report += f"{i}. {finding}\n"

        report += "\n### Recommendations\n"
        report += "- Implement detection mechanisms\n"
        report += "- Update security policies\n"
        report += "- Train developers on Unicode security\n"

        return report


if __name__ == "__main__":
    agent = ReportSynthesizer({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Generate report", {"report_type": "technical", "findings": ["Finding 1", "Finding 2"]})
    print(f"Report: {result['status']}")
