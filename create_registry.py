# Helper script to create the homoglyph registry from the Unicode standard.
import requests
import json

def create_homoglyph_registry():
    """
    Fetches the confusables.txt file from unicode.org, parses it,
    and creates a JSON registry of homoglyph mappings.
    """
    url = "https://www.unicode.org/Public/security/latest/confusables.txt"
    print(f"Fetching data from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    print("Parsing data and building registry...")
    lines = response.text.splitlines()
    registry = {}

    for line in lines:
        if line.startswith('#') or not line.strip():
            continue

        try:
            parts = line.split(';')
            if len(parts) < 3:
                continue

            source_hex_str = parts[0].strip()
            target_hex_str = parts[1].strip()
            type_str = parts[2].strip().split('#')[0].strip()

            if type_str in ('MA', 'SA'):
                # Handle multi-codepoint characters by taking the first one
                source_char = chr(int(source_hex_str.split()[0], 16))
                target_char = chr(int(target_hex_str.split()[0], 16))
                
                # We only care about single character substitutions for this tool
                if len(source_char) == 1 and len(target_char) == 1:
                    if source_char in registry:
                        if target_char not in registry[source_char]:
                            registry[source_char].append(target_char)
                    else:
                        registry[source_char] = [target_char]

        except (ValueError, IndexError) as e:
            # Ignore lines that don't parse correctly
            # print(f"Skipping malformed line: {line} ({e})")
            continue
            
    output_path = 'homoglyph_registry.json'
    print(f"Writing registry to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    print("Registry creation complete.")

if __name__ == '__main__':
    create_homoglyph_registry()
