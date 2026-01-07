"""
Testing and Validation Framework for the noseeum framework.
This module provides validation tests for all obfuscation techniques.
"""
import unittest
from typing import Dict, Any
from noseeum.core.engine import engine, ObfuscationTechnique, LanguageSupport
from noseeum.core.stealth_engine import stealth_engine
from noseeum.core.grammar_db import grammar_db


class TestObfuscationTechniques(unittest.TestCase):
    """Test class for validating obfuscation techniques."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_content = "def sample_function():\n    return 'Hello, World!'"
        self.js_content = "function sampleFunction() {\n    return 'Hello, World!';\n}"
        self.swift_content = "func sampleFunction() {\n    return \"Hello, World!\"\n}"
    
    def test_normalization_obfuscation(self):
        """Test normalization-based obfuscation."""
        try:
            result = engine.apply_obfuscation(
                self.test_content,
                ObfuscationTechnique.NORMALIZATION,
                LanguageSupport.PYTHON
            )
            
            # Check that the result is different from the original
            self.assertNotEqual(result, self.test_content)
            
            # Check that it's still valid Python syntactically (just basic check)
            self.assertIn("def", result)  # Should still contain function definition
            
            print("Normalization obfuscation test passed")
        except Exception as e:
            print(f"Normalization obfuscation test failed: {e}")
            self.fail(f"Normalization obfuscation failed: {e}")
    
    def test_unassigned_planes_obfuscation(self):
        """Test unassigned planes obfuscation."""
        try:
            result = engine.apply_obfuscation(
                self.swift_content,
                ObfuscationTechnique.UNASSIGNED_PLANES,
                LanguageSupport.SWIFT
            )
            
            # Check that the result is different from the original
            self.assertNotEqual(result, self.swift_content)
            
            # Check that it still contains Swift syntax elements
            self.assertIn("func", result)
            
            print("Unassigned planes obfuscation test passed")
        except Exception as e:
            print(f"Unassigned planes obfuscation test failed: {e}")
            self.fail(f"Unassigned planes obfuscation failed: {e}")
    
    def test_payload_injection_obfuscation(self):
        """Test payload injection obfuscation."""
        try:
            result = engine.apply_obfuscation(
                self.js_content,
                ObfuscationTechnique.PAYLOAD_INJECTION,
                LanguageSupport.JAVASCRIPT
            )
            
            # Check that the result is different from the original
            self.assertNotEqual(result, self.js_content)
            
            # Check that it still contains JavaScript syntax elements
            self.assertIn("function", result)
            
            print("Payload injection obfuscation test passed")
        except Exception as e:
            print(f"Payload injection obfuscation test failed: {e}")
            self.fail(f"Payload injection obfuscation failed: {e}")
    
    def test_hangul_encoding_obfuscation(self):
        """Test Hangul encoding obfuscation."""
        try:
            result = engine.apply_obfuscation(
                self.js_content,
                ObfuscationTechnique.HANGUL_ENCODING,
                LanguageSupport.JAVASCRIPT
            )
            
            # Check that the result is different from the original
            self.assertNotEqual(result, self.js_content)
            
            # Check that it still contains JavaScript syntax elements
            self.assertIn("function", result)
            
            print("Hangul encoding obfuscation test passed")
        except Exception as e:
            print(f"Hangul encoding obfuscation test failed: {e}")
            self.fail(f"Hangul encoding obfuscation failed: {e}")
    
    def test_language_specific_obfuscation(self):
        """Test language-specific obfuscation."""
        # Test each language-specific module individually
        test_cases = [
            (LanguageSupport.GO, "func test() { }"),
            (LanguageSupport.KOTLIN, "fun test() { }"),
            (LanguageSupport.JAVASCRIPT, "function test() { }"),
            (LanguageSupport.SWIFT, "func test() { }"),
        ]

        for lang, content in test_cases:
            with self.subTest(lang=lang.value):
                try:
                    result = engine.apply_obfuscation(
                        content,
                        ObfuscationTechnique.LANGUAGE_SPECIFIC,
                        lang
                    )
                    self.assertNotEqual(result, content, f"Language {lang.value} obfuscation did not modify content")
                    print(f"Language-specific obfuscation test passed for {lang.value}")
                except Exception as e:
                    self.fail(f"Language-specific obfuscation test failed for {lang.value}: {e}")
    
    def test_stealth_metrics(self):
        """Test stealth metrics calculation."""
        entropy_result = stealth_engine.calculate_file_entropy(self.test_content, "python")
        
        # Check that entropy calculation returns expected structure
        self.assertIn("entropy", entropy_result)
        self.assertIn("baseline", entropy_result)
        self.assertIn("is_suspicious", entropy_result)
        
        # Entropy should be a reasonable value
        self.assertIsInstance(entropy_result["entropy"], float)
        
        print("Stealth metrics test passed")
    
    def test_language_grammar_access(self):
        """Test access to language grammar information."""
        python_info = grammar_db.get_language_info(LanguageSupport.PYTHON)
        
        # Check that we get some information about Python
        self.assertIsInstance(python_info, dict)
        self.assertIn("name", python_info)
        self.assertEqual(python_info["name"], "Python")
        
        print("Language grammar access test passed")


def run_all_tests():
    """Run all tests in the validation framework."""
    print("Starting noseeum validation tests...")
    
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestObfuscationTechniques)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
