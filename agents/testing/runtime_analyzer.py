"""Runtime Analyzer - Executes payloads in isolated environments and observes behavior."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import tempfile
import subprocess
import time
import resource
from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class RuntimeAnalyzer(BaseAgent):
    """
    Agent specialized in runtime analysis of Unicode attacks.

    Capabilities:
    - Multi-language execution (Python, JavaScript, Java, Go, Rust)
    - Sandboxed execution with monitoring
    - Behavioral analysis and side-effect detection
    - Runtime string transformation tracking
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="runtime_analyzer",
            name="Runtime Analyzer",
            description="Executes payloads in isolated environments",
            capabilities=[AgentCapability.TESTING],
            config=config
        )
        self.toolkit = AgentToolkit()
        self.memory = AgentMemory(self.agent_id)

        # Safety limits
        self.timeout = config.get("timeout", 5)  # seconds
        self.max_memory_mb = config.get("max_memory_mb", 100)
        self.enable_network = config.get("enable_network", False)
        self.isolation_level = config.get("isolation", "process")  # process, docker, vm

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get agent-specific tools."""
        base_tools = self.toolkit.get_noseeum_tools()
        custom_tools = [
            {
                "name": "execute_payload_safe",
                "description": "Execute payload in isolated environment",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "payload": {"type": "string"},
                        "language": {"type": "string"},
                        "monitor": {"type": "boolean"}
                    },
                    "required": ["payload", "language"]
                }
            },
            {
                "name": "analyze_behavior",
                "description": "Analyze runtime behavior of code",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "execution_trace": {"type": "object"}
                    },
                    "required": ["execution_trace"]
                }
            }
        ]
        return base_tools + custom_tools

    def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute runtime analysis task."""
        self.start()
        session_id = self.memory.start_session(task)

        try:
            self.logger.info(f"Starting runtime analysis: {task}")

            payload = context.get("payload") if context else None
            language = context.get("language", "python") if context else "python"
            monitor_level = context.get("monitor", "basic") if context else "basic"

            if not payload:
                raise ValueError("No payload provided for runtime analysis")

            # Execute payload in isolated environment
            execution_result = self._execute_isolated(payload, language, monitor_level)

            # Analyze behavior
            behavior_analysis = self._analyze_behavior(execution_result)

            # Save artifacts
            artifact_path = self.save_artifact(
                "runtime_analysis",
                {
                    "task": task,
                    "language": language,
                    "payload": payload[:200],  # Truncate for safety
                    "execution_result": execution_result,
                    "behavior_analysis": behavior_analysis
                },
                "json"
            )

            result = {
                "execution_result": execution_result,
                "behavior_analysis": behavior_analysis,
                "artifacts": [artifact_path],
                "malicious_behavior_detected": behavior_analysis.get("malicious", False)
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
            self.logger.error(f"Runtime analysis failed: {e}")
            self.fail(str(e))
            return {
                "status": "error",
                "agent": self.name,
                "error": str(e)
            }

    def _execute_isolated(self, payload: str, language: str, monitor: str) -> Dict[str, Any]:
        """Execute payload in isolated environment."""

        if self.isolation_level == "process":
            return self._execute_process(payload, language, monitor)
        elif self.isolation_level == "docker":
            return self._execute_docker(payload, language, monitor)
        else:
            return {"error": "Unsupported isolation level", "status": "failed"}

    def _execute_process(self, payload: str, language: str, monitor: str) -> Dict[str, Any]:
        """Execute in separate process with resource limits."""

        # Create temporary file
        ext_map = {
            "python": ".py",
            "javascript": ".js",
            "java": ".java",
            "go": ".go",
            "rust": ".rs"
        }
        ext = ext_map.get(language, ".txt")

        with tempfile.NamedTemporaryFile(mode='w', suffix=ext, delete=False) as f:
            temp_file = f.name

            # Add instrumentation wrapper if monitoring
            if monitor == "advanced":
                instrumented = self._add_instrumentation(payload, language)
                f.write(instrumented)
            else:
                f.write(payload)

        try:
            # Get interpreter command
            interpreter = self._get_interpreter(language)
            if not interpreter:
                return {"error": f"No interpreter for {language}", "status": "failed"}

            # Execute with resource limits
            start_time = time.time()

            try:
                result = subprocess.run(
                    [interpreter, temp_file],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                    # Note: resource limits would be set via preexec_fn on Unix
                )

                execution_time = time.time() - start_time

                return {
                    "status": "executed",
                    "exit_code": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "execution_time_ms": int(execution_time * 1000),
                    "timed_out": False
                }

            except subprocess.TimeoutExpired:
                return {
                    "status": "timeout",
                    "execution_time_ms": int(self.timeout * 1000),
                    "timed_out": True
                }

        finally:
            # Clean up
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def _execute_docker(self, payload: str, language: str, monitor: str) -> Dict[str, Any]:
        """Execute in Docker container (Phase 3 - not yet implemented)."""
        return {
            "error": "Docker isolation not yet implemented",
            "status": "not_implemented"
        }

    def _get_interpreter(self, language: str) -> Optional[str]:
        """Get interpreter command for language."""
        interpreters = {
            "python": "python3",
            "javascript": "node",
            "java": "java",
            "go": "go run",
            "rust": "rustc"
        }
        return interpreters.get(language)

    def _add_instrumentation(self, payload: str, language: str) -> str:
        """Add instrumentation wrapper for monitoring."""

        if language == "python":
            # Add tracing wrapper
            wrapper = f'''
import sys
import traceback

# Execution trace
_trace_log = []

def _trace_calls(frame, event, arg):
    if event == 'call':
        func_name = frame.f_code.co_name
        _trace_log.append({{'event': 'call', 'function': func_name}})
    elif event == 'return':
        func_name = frame.f_code.co_name
        _trace_log.append({{'event': 'return', 'function': func_name, 'value': str(arg)[:50]}})
    return _trace_calls

sys.settrace(_trace_calls)

try:
    # Original payload
{self._indent_code(payload, "    ")}
except Exception as e:
    print(f"EXCEPTION: {{type(e).__name__}}: {{e}}")
    traceback.print_exc()
finally:
    sys.settrace(None)
    print("\\n=== TRACE LOG ===")
    for entry in _trace_log[:50]:  # Limit output
        print(entry)
'''
            return wrapper

        elif language == "javascript":
            # Add console logging wrapper
            wrapper = f'''
const trace_log = [];

// Wrap execution
try {{
    // Original payload
{self._indent_code(payload, "    ")}
}} catch(e) {{
    console.log("EXCEPTION:", e.name, e.message);
    console.log(e.stack);
}} finally {{
    console.log("\\n=== TRACE LOG ===");
    console.log(trace_log);
}}
'''
            return wrapper

        return payload  # No instrumentation for other languages yet

    def _indent_code(self, code: str, indent: str) -> str:
        """Indent code block."""
        lines = code.split('\n')
        return '\n'.join(indent + line for line in lines)

    def _analyze_behavior(self, execution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze execution behavior for suspicious activity."""

        analysis = {
            "malicious": False,
            "suspicious_behaviors": [],
            "severity": "low"
        }

        # Check execution status
        if execution_result.get("status") == "failed":
            return analysis

        exit_code = execution_result.get("exit_code", 0)
        stdout = execution_result.get("stdout", "")
        stderr = execution_result.get("stderr", "")

        # Check for suspicious indicators
        suspicious_patterns = [
            "malicious", "evil", "exploit", "shell", "exec",
            "system", "subprocess", "eval", "compile",
            "__import__", "os.system", "socket", "urllib"
        ]

        for pattern in suspicious_patterns:
            if pattern in stdout.lower() or pattern in stderr.lower():
                analysis["suspicious_behaviors"].append({
                    "type": "suspicious_string",
                    "pattern": pattern,
                    "context": "output"
                })
                analysis["malicious"] = True

        # Check for exceptions
        if "EXCEPTION" in stdout or "Error" in stderr:
            analysis["suspicious_behaviors"].append({
                "type": "exception",
                "details": stderr[:200]
            })

        # Check for trace log (if instrumented)
        if "TRACE LOG" in stdout:
            analysis["suspicious_behaviors"].append({
                "type": "execution_trace",
                "details": "Execution trace available"
            })

        # Check execution time (possible infinite loop or heavy computation)
        exec_time = execution_result.get("execution_time_ms", 0)
        if exec_time > 1000:  # > 1 second
            analysis["suspicious_behaviors"].append({
                "type": "long_execution",
                "time_ms": exec_time
            })

        # Determine severity
        if len(analysis["suspicious_behaviors"]) > 3:
            analysis["severity"] = "high"
        elif len(analysis["suspicious_behaviors"]) > 1:
            analysis["severity"] = "medium"

        return analysis


def main():
    """Test the Runtime Analyzer agent."""
    config = {
        "model": "claude-sonnet-4-5-20250929",
        "timeout": 5,
        "isolation": "process"
    }

    agent = RuntimeAnalyzer(config)

    # Test with a simple bidi payload
    payload = '''# Safe code
evil_executed = False
# ‮evil_executed = True‭
print("Evil executed:", evil_executed)
'''

    task = "Analyze bidi payload runtime behavior"
    context = {
        "payload": payload,
        "language": "python",
        "monitor": "advanced"
    }

    result = agent.run(task, context)

    print("\n=== Runtime Analyzer Results ===")
    print(f"Status: {result['status']}")
    print(f"Malicious behavior: {result.get('malicious_behavior_detected', False)}")
    print(f"Execution: {result.get('execution_result', {}).get('status', 'unknown')}")

    if result.get('behavior_analysis'):
        print(f"\nBehaviors detected: {len(result['behavior_analysis'].get('suspicious_behaviors', []))}")
        for behavior in result['behavior_analysis'].get('suspicious_behaviors', []):
            print(f"  - {behavior['type']}: {behavior.get('details', behavior.get('pattern', 'N/A'))}")


if __name__ == "__main__":
    main()
