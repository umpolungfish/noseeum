"""
Integration Module for the noseeum framework.
This module orchestrates all components to provide a unified obfuscation pipeline.
"""
import click
from typing import Dict, Any, List
from .engine import engine, ObfuscationTechnique, LanguageSupport
from .grammar_db import grammar_db
from .stealth_engine import stealth_engine
from .evasion_library import evasion_library
from .linguistic_generator import linguistic_generator
from .yara_generator import yara_generator


class IntegrationEngine:
    """Main integration engine that orchestrates all noseeum components."""
    
    def __init__(self):
        self.pipeline_steps = [
            self.apply_language_specific_obfuscation,
            self.apply_advanced_techniques,
            self.apply_evasion_tactics,
            self.apply_linguistic_noise,
            self.validate_stealth_metrics,
            self.generate_yara_resilient_payloads
        ]
    
    def full_obfuscation_pipeline(self, content: str, target_language: LanguageSupport, 
                                 config: Dict[str, Any] = None) -> str:
        """
        Execute the complete obfuscation pipeline.
        
        Args:
            content: The original content to obfuscate
            target_language: The target programming language
            config: Configuration options for the pipeline
        
        Returns:
            Obfuscated content that has passed through all pipeline steps
        """
        if config is None:
            config = {}
        
        result = content
        
        # Execute each step in the pipeline
        for step in self.pipeline_steps:
            try:
                result = step(result, target_language, config)
            except Exception as e:
                click.echo(f"Error in pipeline step {step.__name__}: {e}", err=True)
                # Continue to next step even if one fails
                continue
        
        return result
    
    def apply_language_specific_obfuscation(self, content: str, target_language: LanguageSupport, 
                                           config: Dict[str, Any]) -> str:
        """Apply language-specific obfuscation techniques using the dispatcher."""
        try:
            return engine.apply_obfuscation(
                content,
                ObfuscationTechnique.LANGUAGE_SPECIFIC,
                target_language
            )
        except ValueError:
            # This language doesn't have a specific module registered in the dispatcher.
            return content
    
    def apply_advanced_techniques(self, content: str, target_language: LanguageSupport, 
                                 config: Dict[str, Any]) -> str:
        """Apply advanced obfuscation techniques like normalization and unassigned planes."""
        result = content
        
        # Apply normalization-based obfuscation
        try:
            result = engine.apply_obfuscation(
                result,
                ObfuscationTechnique.NORMALIZATION,
                target_language
            )
        except Exception:
            # If normalization fails, continue with original content
            pass
        
        # Apply unassigned planes if appropriate for the language
        if target_language in [LanguageSupport.SWIFT, LanguageSupport.PYTHON, LanguageSupport.JAVASCRIPT]:
            try:
                result = engine.apply_obfuscation(
                    result,
                    ObfuscationTechnique.UNASSIGNED_PLANES,
                    target_language
                )
            except Exception:
                # If unassigned planes fail, continue with original content
                pass
        
        return result
    
    def apply_evasion_tactics(self, content: str, target_language: LanguageSupport, 
                             config: Dict[str, Any]) -> str:
        """Apply general evasion tactics."""
        result = content
        
        # Apply all available evasion tactics
        for tactic_name in evasion_library.get_available_tactics():
            try:
                result = evasion_library.apply_tactic(tactic_name, result)
            except Exception:
                # If a tactic fails, continue with the next
                continue
        
        return result
    
    def apply_linguistic_noise(self, content: str, target_language: LanguageSupport, 
                              config: Dict[str, Any]) -> str:
        """Apply linguistic noise to make the code blend in."""
        result = content
        
        # Generate contextual noise for the target language
        noise = linguistic_generator.generate_contextual_noise(target_language)
        
        # Add the noise to the content (at the beginning or end)
        if config.get('add_noise_at_end', True):
            result = result + "\n\n" + noise
        else:
            result = noise + "\n\n" + result
        
        return result
    
    def validate_stealth_metrics(self, content: str, target_language: LanguageSupport, 
                                config: Dict[str, Any]) -> str:
        """Validate that the obfuscated content meets stealth requirements."""
        result = content
        
        # Calculate entropy metrics
        metrics = stealth_engine.calculate_file_entropy(result, target_language.value)
        
        # If entropy is too high, apply additional obfuscation to reduce it
        if metrics['is_suspicious'] and config.get('optimize_for_stealth', True):
            # Apply more low-entropy obfuscation techniques
            result = evasion_library.apply_tactic("create_low_entropy_payloads", result)
        
        return result
    
    def generate_yara_resilient_payloads(self, content: str, target_language: LanguageSupport, 
                                        config: Dict[str, Any]) -> str:
        """Generate YARA-resilient versions of any payloads."""
        result = content
        
        # Apply YARA-resilient payload generation
        result = yara_generator.generate_yara_resilient_payload(result, "printable_ascii")
        
        return result


# Global instance of the integration engine
integration_engine = IntegrationEngine()
