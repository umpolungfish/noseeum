"""
Stealth Metrics Engine for the noseeum framework.
This module calculates various metrics to measure the stealthiness of obfuscated code.
"""
import math
from typing import Dict, List, Any
from collections import Counter


class StealthMetricsEngine:
    """Engine for calculating stealth metrics of obfuscated code."""
    
    def __init__(self):
        # Empirical entropy baselines for different file types
        self.entropy_baselines = {
            "python": 4.5,
            "javascript": 5.0,
            "java": 4.8,
            "go": 4.2,
            "kotlin": 4.7,
            "swift": 4.6,
            "rust": 4.4,
            "c": 4.1,
            "cpp": 4.3,
            "html": 3.8,
            "txt": 3.2
        }
    
    def calculate_shannon_entropy(self, content: str) -> float:
        """
        Calculate the Shannon entropy of the given content.
        Higher entropy indicates more randomness.
        """
        if not content:
            return 0.0
            
        # Count frequency of each character
        char_counts = Counter(content)
        content_length = len(content)
        
        # Calculate entropy using Shannon's formula
        entropy = 0.0
        for count in char_counts.values():
            probability = count / content_length
            if probability > 0:
                entropy -= probability * math.log2(probability)
                
        return entropy
    
    def calculate_file_entropy(self, file_content: str, file_type: str) -> Dict[str, Any]:
        """
        Calculate entropy metrics for a file, comparing to baseline for the file type.
        """
        entropy = self.calculate_shannon_entropy(file_content)
        baseline = self.entropy_baselines.get(file_type.lower(), 4.5)
        
        # Determine if the entropy is within acceptable bounds
        is_suspicious = entropy > baseline + 1.0  # Threshold could be adjusted
        
        return {
            "entropy": entropy,
            "baseline": baseline,
            "is_suspicious": is_suspicious,
            "stealth_score": max(0, 100 - ((entropy - baseline) * 10))  # Simple scoring
        }
    
    def calculate_obfuscation_metrics(self, original: str, obfuscated: str) -> Dict[str, Any]:
        """
        Compare metrics between original and obfuscated code.
        """
        original_entropy = self.calculate_shannon_entropy(original)
        obfuscated_entropy = self.calculate_shannon_entropy(obfuscated)
        
        return {
            "original_entropy": original_entropy,
            "obfuscated_entropy": obfuscated_entropy,
            "entropy_increase": obfuscated_entropy - original_entropy,
            "size_increase": len(obfuscated) - len(original),
            "size_ratio": len(obfuscated) / len(original) if original else 0
        }


# Global instance of the engine
stealth_engine = StealthMetricsEngine()