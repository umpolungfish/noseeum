"""
YAML-Based Configuration Loader for Noseeum Agent Orchestration.

Ported from AjintK framework. Allows entire orchestration setups —
providers, agents, presets — to be declared in a single YAML file.

Minimal example config.yaml
----------------------------
provider: anthropic
model: claude-sonnet-4-6
max_tokens: 4000
temperature: 0.7
max_concurrent_agents: 5

presets:
  full_analysis:   [unicode_archaeologist, payload_artisan, report_synthesizer]
  quick_scan:      [unicode_archaeologist, report_synthesizer]
  red_team:        [payload_artisan, stealth_optimizer, red_team_validator]
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)


def load_config(path: str | Path) -> Dict[str, Any]:
    """
    Load a YAML config file and return it as a plain dict.

    Raises FileNotFoundError if the file doesn't exist.
    Raises yaml.YAMLError on parse errors.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as f:
        cfg = yaml.safe_load(f)

    if not isinstance(cfg, dict):
        raise ValueError(
            f"Config file must contain a YAML mapping at the top level: {path}"
        )

    logger.info(f"Loaded config from {path}")
    return cfg


def agent_config_from(
    cfg: Dict[str, Any],
    overrides: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Extract the agent-level config dict from a top-level config,
    with optional per-agent overrides.

    This is the dict passed to BaseAgent.__init__(config=...).
    """
    base = {
        "llm_provider": cfg.get("provider", cfg.get("llm_provider", "anthropic")),
        "model":        cfg.get("model", "claude-sonnet-4-6"),
        "max_tokens":   cfg.get("max_tokens", 4000),
        "temperature":  cfg.get("temperature", 0.7),
    }
    if overrides:
        base.update(overrides)
    return base


def orchestrator_config_from(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Extract the orchestrator-level config dict from a top-level config."""
    return {
        "max_concurrent_agents": cfg.get(
            "max_concurrent_agents",
            cfg.get("swarm", {}).get("max_concurrent_agents", 5)
        ),
        "timeout": cfg.get("timeout", 300),
    }


def register_presets_from_config(
    orchestrator,
    cfg: Dict[str, Any],
) -> List[str]:
    """
    Read the ``presets`` block from a config dict and register each preset on
    the given AgentOrchestrator instance.

    Returns the list of preset names registered.

    Config format::

        presets:
          full_analysis: [unicode_archaeologist, payload_artisan, report_synthesizer]
          quick_scan:    [unicode_archaeologist, report_synthesizer]
    """
    presets_cfg = cfg.get("presets", {})
    registered: List[str] = []
    for name, agent_ids in presets_cfg.items():
        if not isinstance(agent_ids, list):
            logger.warning(f"Preset '{name}' must be a list of agent IDs; skipping.")
            continue
        orchestrator.register_preset(name, agent_ids)
        registered.append(name)

    if registered:
        logger.info(f"Registered {len(registered)} presets from config: {registered}")
    return registered
