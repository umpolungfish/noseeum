"""Integration tests for all agents."""

import pytest
import sys
import os

# Add agents to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


@pytest.fixture
def config():
    """Test configuration."""
    return {
        "model": "claude-sonnet-4-5-20250929",
        "api_key": "test_key"
    }


class TestResearchAgents:
    """Test research agents."""

    def test_unicode_archaeologist(self, config):
        agent = UnicodeArchaeologist(config)
        assert agent.agent_id == "unicode_archaeologist"
        assert agent.name == "Unicode Archaeologist"

        result = agent.run("Test task")
        assert "status" in result

    def test_language_grammar_hunter(self, config):
        agent = LanguageGrammarHunter(config)
        assert agent.agent_id == "language_grammar_hunter"

        result = agent.run("Analyze Python")
        assert "status" in result


class TestAttackDevAgents:
    """Test attack development agents."""

    def test_payload_artisan(self, config):
        agent = PayloadArtisan(config)
        assert agent.agent_id == "payload_artisan"

        result = agent.run("Generate payloads", {"language": "python"})
        assert "status" in result

    def test_stealth_optimizer(self, config):
        agent = StealthOptimizer(config)
        assert agent.agent_id == "stealth_optimizer"

        result = agent.run("Optimize attack", {"payload": "test"})
        assert "status" in result

    def test_polyglot_specialist(self, config):
        agent = PolyglotSpecialist(config)
        assert agent.agent_id == "polyglot_specialist"

        result = agent.run("Create polyglot", {"languages": ["python", "js"]})
        assert "status" in result


class TestDefenseAgents:
    """Test defense agents."""

    def test_red_team_validator(self, config):
        agent = RedTeamValidator(config)
        assert agent.agent_id == "red_team_validator"

        result = agent.run("Validate attack", {"attack": "test"})
        assert "status" in result

    def test_yara_rule_smith(self, config):
        agent = YaraRuleSmith(config)
        assert agent.agent_id == "yara_rule_smith"

        result = agent.run("Generate YARA rules", {"attack_type": "bidi"})
        assert "status" in result

    def test_detector_adversary(self, config):
        agent = DetectorAdversary(config)
        assert agent.agent_id == "detector_adversary"

        result = agent.run("Improve scanner")
        assert "status" in result


class TestAnalysisAgents:
    """Test analysis agents."""

    def test_vulnerability_cartographer(self, config):
        agent = VulnerabilityCartographer(config)
        assert agent.agent_id == "vulnerability_cartographer"

        result = agent.run("Map vulnerabilities")
        assert "status" in result

    def test_report_synthesizer(self, config):
        agent = ReportSynthesizer(config)
        assert agent.agent_id == "report_synthesizer"

        result = agent.run("Generate report", {"report_type": "technical"})
        assert "status" in result


class TestInfrastructureAgents:
    """Test infrastructure agents."""

    def test_test_oracle(self, config):
        agent = TestOracle(config)
        assert agent.agent_id == "test_oracle"

        result = agent.run("Generate tests", {"module": "bidi"})
        assert "status" in result

    def test_module_architect(self, config):
        agent = ModuleArchitect(config)
        assert agent.agent_id == "module_architect"

        result = agent.run("Create module", {"module_name": "test_attack"})
        assert "status" in result


class TestSpecializedAgents:
    """Test specialized research agents."""

    def test_homoglyph_curator(self, config):
        agent = HomoglyphCurator(config)
        assert agent.agent_id == "homoglyph_curator"

        result = agent.run("Discover homoglyphs")
        assert "status" in result

    def test_normalization_alchemist(self, config):
        agent = NormalizationAlchemist(config)
        assert agent.agent_id == "normalization_alchemist"

        result = agent.run("Find collisions")
        assert "status" in result

    def test_bidirectional_puppeteer(self, config):
        agent = BidirectionalPuppeteer(config)
        assert agent.agent_id == "bidirectional_puppeteer"

        result = agent.run("Generate Bidi attacks")
        assert "status" in result


class TestAgentIntegration:
    """Test agent integration and communication."""

    def test_agent_memory(self, config):
        """Test agent memory persistence."""
        agent = UnicodeArchaeologist(config)

        # Store in memory using AgentMemory methods
        agent.memory.store("test_key", "test_value")

        # Retrieve from memory
        value = agent.memory.retrieve("test_key")
        assert value == "test_value"

    def test_agent_artifacts(self, config):
        """Test agent artifact saving."""
        agent = PayloadArtisan(config)

        # Save artifact
        path = agent.save_artifact("test", "content", "text")
        assert os.path.exists(path)

    def test_agent_status_transitions(self, config):
        """Test agent status transitions."""
        agent = StealthOptimizer(config)

        assert agent.status.value == "idle"

        agent.start()
        assert agent.status.value == "running"

        agent.pause()
        assert agent.status.value == "paused"

        agent.resume()
        assert agent.status.value == "running"

        agent.complete({"result": "test"})
        assert agent.status.value == "completed"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
