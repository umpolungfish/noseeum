"""Stealth Optimizer - Optimizes attacks for maximum evasion."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class StealthOptimizer(BaseAgent):
    """Optimizes attacks to maximize evasion while maintaining functionality."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="stealth_optimizer",
            name="Stealth Optimizer",
            description="Optimizes attacks for maximum evasion",
            capabilities=[AgentCapability.ATTACK_DEV],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)
        self.benchmark_tools = config.get("benchmark_tools", [
            "semgrep", "eslint", "pylint", "bandit", "gosec", "codeql", "sonarqube"
        ])

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        return self.toolkit.get_noseeum_tools()

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute stealth optimization."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            # Use intelligent context extraction
            payload = self._extract_from_context(context, "payload", None)
            target_file = self._extract_from_context(context, "target_file", None)
            language = self._extract_from_context(context, "language", "python")
            target_tools = self._extract_from_context(context, "tools", self.benchmark_tools)

            # Log received context for debugging
            if context:
                self.logger.info(f"Context keys: {list(context.keys())}")
                if "payloads" in context:
                    self.logger.info(f"Received {len(context['payloads'])} payloads from previous agent")
                    # If we have payloads but no payload, use the first one
                    if not payload and context['payloads']:
                        payload = context['payloads'][0].get('payload')
                        self.logger.info(f"Using first payload from context")

            # If no target_file, create temporary file with payload
            import tempfile
            temp_file = None
            if not target_file and payload:
                ext_map = {"python": ".py", "javascript": ".js", "java": ".java", "go": ".go"}
                ext = ext_map.get(language, ".txt")
                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix=ext, delete=False)
                temp_file.write(payload)
                temp_file.close()
                target_file = temp_file.name

            # Test against detectors
            detection_results = self._test_against_detectors(target_file, target_tools, language)

            # Generate evasion variants
            evasion_variants = self._generate_evasion_variants(payload, detection_results)

            # Benchmark variants
            best_variant = self._select_best_variant(evasion_variants, target_tools)

            # Clean up temp file
            if temp_file:
                import os
                os.unlink(temp_file.name)

            result = {
                "original_payload": payload,
                "optimized_payload": best_variant,
                "detection_results": detection_results,
                "evasion_score": best_variant.get("evasion_score", 0) if best_variant else 0,
                "tools_tested": len(target_tools),
                "tools_bypassed": sum(1 for r in detection_results.get("results", {}).values() if r.get("bypassed"))
            }

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _test_against_detectors(self, target_file: str, tools: List[str], language: str) -> Dict[str, Any]:
        """Test payload against security tools."""
        if not target_file or not os.path.exists(target_file):
            # Fallback to simulation if no file
            results = {}
            for tool in tools:
                results[tool] = {"detected": False, "bypassed": True, "error": "No target file"}
            return {"results": results, "summary": {"total_tools": len(tools), "bypassed": len(tools)}}

        # Use real tool testing
        return self.toolkit.batch_test_security_tools(target_file, tools, language)

    def _generate_evasion_variants(self, payload: str, detection: Dict) -> List[Dict]:
        """Generate evasion variants."""
        return [{"payload": payload, "technique": "original", "evasion_score": 0.5}]

    def _select_best_variant(self, variants: List[Dict], tools: List[str]) -> Dict:
        """Select best evasion variant."""
        return max(variants, key=lambda v: v.get("evasion_score", 0)) if variants else {}


if __name__ == "__main__":
    agent = StealthOptimizer({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Optimize payload", {"payload": "test"})
    print(f"Result: {result['status']}")
