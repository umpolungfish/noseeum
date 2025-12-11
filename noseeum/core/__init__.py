"""
Core components for the noseeum framework.
"""
from .engine import engine, ObfuscationTechnique, LanguageSupport
from .grammar_db import grammar_db
from .stealth_engine import stealth_engine
from .evasion_library import evasion_library
from .linguistic_generator import linguistic_generator
from .yara_generator import yara_generator
from .integration import integration_engine

# Import and register all modules
from noseeum.attacks.normalization import normalization_module
from noseeum.attacks.unassigned_planes import unassigned_planes_module
from noseeum.attacks.payload_injection import payload_injection_module
from noseeum.attacks.hangul_encoding import hangul_encoding_module
from noseeum.attacks.go_attack import go_attack_module
from noseeum.attacks.kotlin_attack import kotlin_attack_module
from noseeum.attacks.javascript_attack import javascript_attack_module
from noseeum.attacks.swift_attack import swift_attack_module
from .language_dispatcher import language_dispatcher_module

# Register the new modules with the engine
engine.register_module(ObfuscationTechnique.NORMALIZATION, normalization_module)
engine.register_module(ObfuscationTechnique.UNASSIGNED_PLANES, unassigned_planes_module)
engine.register_module(ObfuscationTechnique.PAYLOAD_INJECTION, payload_injection_module)
engine.register_module(ObfuscationTechnique.HANGUL_ENCODING, hangul_encoding_module)

# Register language-specific modules with the dispatcher
language_dispatcher_module.register_language_module(LanguageSupport.GO, go_attack_module)
language_dispatcher_module.register_language_module(LanguageSupport.KOTLIN, kotlin_attack_module)
language_dispatcher_module.register_language_module(LanguageSupport.JAVASCRIPT, javascript_attack_module)
language_dispatcher_module.register_language_module(LanguageSupport.SWIFT, swift_attack_module)

# Register the language dispatcher under the LANGUAGE_SPECIFIC technique
engine.register_module(ObfuscationTechnique.LANGUAGE_SPECIFIC, language_dispatcher_module)