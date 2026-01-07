"""Module Architect - Assists in developing new attack modules."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Dict, List, Any, Optional
from agents.base.agent import BaseAgent, AgentCapability
from agents.base.tools import AgentToolkit
from agents.base.memory import AgentMemory


class ModuleArchitect(BaseAgent):
    """Assists in developing new attack modules following project patterns."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            agent_id="module_architect",
            name="Module Architect",
            description="Develops new attack modules",
            capabilities=[AgentCapability.ATTACK_DEV],
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
            module_name = context.get("module_name", "new_attack") if context else "new_attack"
            attack_type = context.get("attack_type", "unicode") if context else "unicode"

            # Generate module scaffold
            module_code = self._scaffold_module(module_name, attack_type)

            # Generate CLI integration
            cli_code = self._scaffold_cli(module_name)

            # Generate tests
            test_code = self._scaffold_tests(module_name)

            # Generate registration code
            registration_code = self._scaffold_registration(module_name)

            result = {
                "module_name": module_name,
                "files_generated": 4,
                "module_code": module_code,
                "integration_complete": True
            }

            # Save artifacts
            self.save_artifact(f"module_{module_name}", module_code, "text")
            self.save_artifact(f"cli_{module_name}", cli_code, "text")
            self.save_artifact(f"test_{module_name}", test_code, "text")

            self.memory.end_session(session_id, result)
            self.complete(result)

            return {"status": "success", "agent": self.name, **result}

        except Exception as e:
            self.fail(str(e))
            return {"status": "error", "agent": self.name, "error": str(e)}

    def _scaffold_module(self, name: str, attack_type: str) -> str:
        return f'''"""
{name.replace("_", " ").title()} attack module.
"""

from noseeum.core.engine import ObfuscationModule, ObfuscationTechnique, LanguageSupport


class {name.title().replace("_", "")}Module(ObfuscationModule):
    """Implements {attack_type} attack."""

    def get_name(self) -> str:
        return "{name}"

    def get_description(self) -> str:
        return "{attack_type} based attack"

    def get_supported_languages(self) -> list:
        return [LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT]

    def obfuscate(self, code: str, **kwargs) -> str:
        # Implementation here
        return code


# Module instance
{name}_module = {name.title().replace("_", "")}Module()
'''

    def _scaffold_cli(self, name: str) -> str:
        return f'''import click

@click.command()
@click.option('--input', required=True)
def {name}(input):
    """Execute {name} attack."""
    from noseeum.attacks.{name} import {name}_module
    result = {name}_module.obfuscate(input)
    click.echo(result)
'''

    def _scaffold_tests(self, name: str) -> str:
        return f'''import pytest

def test_{name}_basic():
    """Test basic functionality."""
    from noseeum.attacks.{name} import {name}_module
    result = {name}_module.obfuscate("test")
    assert result is not None

def test_{name}_empty():
    """Test empty input."""
    from noseeum.attacks.{name} import {name}_module
    result = {name}_module.obfuscate("")
    assert result == ""
'''

    def _scaffold_registration(self, name: str) -> str:
        return f'''# Add to noseeum/core/__init__.py:
from noseeum.attacks.{name} import {name}_module
engine.register_module(ObfuscationTechnique.{name.upper()}, {name}_module)
'''


if __name__ == "__main__":
    agent = ModuleArchitect({"model": "claude-sonnet-4-5-20250929"})
    result = agent.run("Create module", {"module_name": "test_attack", "attack_type": "unicode"})
    print(f"Module: {result['status']}, Files: {result.get('files_generated', 0)}")
