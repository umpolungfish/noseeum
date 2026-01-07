"""
Attack modules for the noseeum framework.
"""
from .bidi import bidi
from .homoglyph import homoglyph
from .invisible import invisible
from .language import language

# Import advanced attack modules
from .normalization import normalization, normalization_module
from .unassigned_planes import unassigned_planes, unassigned_planes_module
from .payload_injection import payload_injection, payload_injection_module
from .hangul_encoding import hangul_encoding, hangul_encoding_module

# Import language-specific modules
from .go_attack import go_attack, go_attack_module
from .kotlin_attack import kotlin_attack, kotlin_attack_module
from .javascript_attack import javascript_attack, javascript_attack_module
from .swift_attack import swift_attack, swift_attack_module