"""Agent swarm orchestrator for coordinating multiple agents."""

import os
import sys
import yaml
import logging
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add agents to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from base.agent import BaseAgent, AgentStatus
from research.unicode_archaeologist import UnicodeArchaeologist
from research.language_grammar_hunter import LanguageGrammarHunter
from attack_dev.payload_artisan import PayloadArtisan
from attack_dev.stealth_optimizer import StealthOptimizer
from attack_dev.polyglot_specialist import PolyglotSpecialist
from defense.red_team_validator import RedTeamValidator
from defense.yara_rule_smith import YaraRuleSmith
from defense.detector_adversary import DetectorAdversary
from analysis.vulnerability_cartographer import VulnerabilityCartographer
from analysis.report_synthesizer import ReportSynthesizer
from infrastructure.test_oracle import TestOracle
from infrastructure.module_architect import ModuleArchitect
from specialized.homoglyph_curator import HomoglyphCurator
from specialized.normalization_alchemist import NormalizationAlchemist
from specialized.bidirectional_puppeteer import BidirectionalPuppeteer
from testing.runtime_analyzer import RuntimeAnalyzer


class AgentOrchestrator:
    """Orchestrates and coordinates multiple agents."""

    def __init__(self, config_path: str = "agents/config.yaml"):
        """Initialize orchestrator."""
        self.config = self._load_config(config_path)
        self.logger = self._setup_logger()
        self.agents: Dict[str, BaseAgent] = {}
        self.agent_classes = self._get_agent_classes()
        self._initialize_agents()

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logging.warning(f"Config not found: {config_path}, using defaults")
            return self._default_config()

    def _default_config(self) -> Dict[str, Any]:
        """Default configuration."""
        return {
            "api": {"model": "claude-sonnet-4-5-20250929"},
            "agents": {},
            "swarm": {"max_concurrent_agents": 5}
        }

    def _setup_logger(self) -> logging.Logger:
        """Set up orchestrator logger."""
        # Get log level from config, default to DEBUG for verbose output
        log_level_str = self.config.get('output', {}).get('log_level', 'DEBUG')
        log_level = getattr(logging, log_level_str.upper(), logging.DEBUG)

        logger = logging.getLogger("noseeum.orchestrator")
        logger.setLevel(log_level)

        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        formatter = logging.Formatter('[%(asctime)s] [Orchestrator] %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def _get_agent_classes(self) -> Dict[str, type]:
        """Get all available agent classes."""
        return {
            "unicode_archaeologist": UnicodeArchaeologist,
            "language_grammar_hunter": LanguageGrammarHunter,
            "payload_artisan": PayloadArtisan,
            "stealth_optimizer": StealthOptimizer,
            "polyglot_specialist": PolyglotSpecialist,
            "red_team_validator": RedTeamValidator,
            "yara_rule_smith": YaraRuleSmith,
            "detector_adversary": DetectorAdversary,
            "vulnerability_cartographer": VulnerabilityCartographer,
            "report_synthesizer": ReportSynthesizer,
            "test_oracle": TestOracle,
            "module_architect": ModuleArchitect,
            "homoglyph_curator": HomoglyphCurator,
            "normalization_alchemist": NormalizationAlchemist,
            "bidirectional_puppeteer": BidirectionalPuppeteer,
            "runtime_analyzer": RuntimeAnalyzer,
        }

    def _initialize_agents(self):
        """Initialize all enabled agents."""
        agent_configs = self.config.get("agents", {})
        api_config = self.config.get("api", {})
        output_config = self.config.get("output", {})
        llm_provider_config = self.config.get("llm_provider", {})

        for agent_id, agent_class in self.agent_classes.items():
            agent_config = agent_configs.get(agent_id, {})

            if agent_config.get("enabled", True):
                try:
                    # Start with base config
                    full_config = {**api_config, **output_config}

                    # Determine which provider to use
                    # Agent-specific overrides global default
                    if 'llm_provider' in agent_config:
                        provider_name = agent_config['llm_provider']
                    elif 'provider' in llm_provider_config:
                        provider_name = llm_provider_config.get('provider', 'anthropic')
                    else:
                        provider_name = 'anthropic'

                    # Set the provider name in config
                    full_config['llm_provider'] = provider_name

                    # Copy provider-specific configs to top level
                    # This allows BaseAgent to access api_key, model, etc. directly
                    if provider_name in llm_provider_config:
                        provider_specific = llm_provider_config.get(provider_name, {})
                        for key, value in provider_specific.items():
                            if key not in full_config:
                                full_config[key] = value

                    # For MoE provider, add MoE-specific configs
                    if provider_name == 'moe' and 'moe' in llm_provider_config:
                        moe_config = llm_provider_config.get('moe', {})
                        for key, value in moe_config.items():
                            if key not in full_config:
                                full_config[key] = value
                        # Pass the full llm_provider config so MoE can access sub-provider API keys
                        full_config['llm_provider_config'] = llm_provider_config

                    # Finally, merge agent-specific config (highest priority)
                    full_config.update(agent_config)

                    self.agents[agent_id] = agent_class(full_config)
                    self.logger.info(f"Initialized agent: {agent_id}")
                except Exception as e:
                    self.logger.error(f"Failed to initialize {agent_id}: {e}")

    def list_agents(self) -> List[Dict[str, Any]]:
        """List all available agents."""
        return [
            {
                "id": agent_id,
                "name": agent.name,
                "description": agent.description,
                "status": agent.status.value,
                "capabilities": [c.value for c in agent.capabilities]
            }
            for agent_id, agent in self.agents.items()
        ]

    def run_agent(self, agent_id: str, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run a single agent."""
        if agent_id not in self.agents:
            return {"status": "error", "error": f"Agent {agent_id} not found"}

        agent = self.agents[agent_id]
        self.logger.info(f"Running agent: {agent.name}")

        try:
            result = agent.run(task, context)
            self.logger.info(f"Agent {agent.name} completed: {result.get('status')}")
            return result
        except Exception as e:
            self.logger.error(f"Agent {agent.name} failed: {e}")
            return {"status": "error", "agent": agent_id, "error": str(e)}

    def run_swarm(self, task: str, agent_ids: Optional[List[str]] = None,
                  context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run multiple agents as a coordinated swarm."""
        if agent_ids is None:
            agent_ids = list(self.agents.keys())

        # Filter to valid agent IDs
        agent_ids = [aid for aid in agent_ids if aid in self.agents]

        if not agent_ids:
            return {"status": "error", "error": "No valid agents specified"}

        self.logger.info(f"Starting swarm with {len(agent_ids)} agents")

        max_concurrent = self.config.get("swarm", {}).get("max_concurrent_agents", 5)

        results = {}
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            # Submit all agent tasks
            future_to_agent = {
                executor.submit(self.run_agent, agent_id, task, context): agent_id
                for agent_id in agent_ids
            }

            # Collect results as they complete
            for future in as_completed(future_to_agent):
                agent_id = future_to_agent[future]
                try:
                    result = future.result()
                    results[agent_id] = result
                    self.logger.info(f"Agent {agent_id} completed in swarm")
                except Exception as e:
                    self.logger.error(f"Agent {agent_id} failed in swarm: {e}")
                    results[agent_id] = {"status": "error", "error": str(e)}

        # Aggregate results
        successful = sum(1 for r in results.values() if r.get("status") == "success")
        failed = len(results) - successful

        return {
            "status": "completed",
            "task": task,
            "agents_run": len(agent_ids),
            "successful": successful,
            "failed": failed,
            "results": results
        }

    def get_agent_status(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific agent."""
        if agent_id not in self.agents:
            return None

        return self.agents[agent_id].get_status_report()

    def get_all_status(self) -> Dict[str, Any]:
        """Get status of all agents."""
        return {
            agent_id: agent.get_status_report()
            for agent_id, agent in self.agents.items()
        }


def main():
    """Test the orchestrator."""
    import argparse

    parser = argparse.ArgumentParser(description="Noseeum Agent Orchestrator")
    parser.add_argument("command", choices=["list", "run", "swarm", "status"])
    parser.add_argument("--agent", help="Agent ID to run")
    parser.add_argument("--task", help="Task description")
    parser.add_argument("--agents", help="Comma-separated agent IDs for swarm")

    args = parser.parse_args()

    orchestrator = AgentOrchestrator()

    if args.command == "list":
        agents = orchestrator.list_agents()
        print("\n=== Available Agents ===")
        for agent in agents:
            print(f"\n{agent['id']}")
            print(f"  Name: {agent['name']}")
            print(f"  Description: {agent['description']}")
            print(f"  Capabilities: {', '.join(agent['capabilities'])}")

    elif args.command == "run":
        if not args.agent or not args.task:
            print("Error: --agent and --task required")
            return

        result = orchestrator.run_agent(args.agent, args.task)
        print(f"\n=== Agent Result ===")
        print(f"Status: {result.get('status')}")
        print(f"Agent: {result.get('agent', args.agent)}")

    elif args.command == "swarm":
        if not args.task:
            print("Error: --task required")
            return

        agent_ids = args.agents.split(",") if args.agents else None
        result = orchestrator.run_swarm(args.task, agent_ids)

        print(f"\n=== Swarm Results ===")
        print(f"Task: {result['task']}")
        print(f"Agents Run: {result['agents_run']}")
        print(f"Successful: {result['successful']}")
        print(f"Failed: {result['failed']}")

    elif args.command == "status":
        if args.agent:
            status = orchestrator.get_agent_status(args.agent)
            if status:
                print(f"\n=== Agent Status: {args.agent} ===")
                for key, value in status.items():
                    print(f"{key}: {value}")
        else:
            all_status = orchestrator.get_all_status()
            print(f"\n=== All Agents Status ===")
            for agent_id, status in all_status.items():
                print(f"\n{agent_id}: {status['status']}")


if __name__ == "__main__":
    main()
