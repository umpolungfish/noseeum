# Helper script to create a comprehensive map of Unicode characters
# that normalize to specific ASCII characters under NFKC.
import unicodedata
import json

def create_nfkc_map():
    """
    Iterates through a large portion of the Unicode space to find all
    characters that normalize to a specific set of ASCII characters under NFKC.
    """
    # The set of ASCII characters we want to find equivalents for
    target_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    nfkc_map = {char: [] for char in target_chars}

    # We iterate up to a high code point to cover most common scripts.
    # The full Unicode range is up to 0x10FFFF, but this is slow.
    # 0xFFFF covers the Basic Multilingual Plane, which is sufficient.
    max_codepoint = 0xFFFF 
    
    print(f"Building NFKC map by checking Unicode points up to {max_codepoint:X}...")
    
    for i in range(max_codepoint + 1):
        try:
            char = chr(i)
            # Normalize the character using NFKC
            normalized_char = unicodedata.normalize('NFKC', char)
            
            # Check if the normalized form is one of our target characters
            if normalized_char in nfkc_map:
                # Don't map the character to itself
                if char != normalized_char:
                    nfkc_map[normalized_char].append(char)
        except UnicodeEncodeError:
            # Some code points are not valid characters (e.g., surrogates)
            continue
            
    output_path = 'nfkc_map.json'
    print(f"Writing NFKC map to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nfkc_map, f, ensure_ascii=False, indent=2)

    print("NFKC map creation complete.")
    print(f"Found {sum(len(v) for v in nfkc_map.values())} total NFKC-equivalent characters.")

if __name__ == '__main__':
    create_nfkc_map()
