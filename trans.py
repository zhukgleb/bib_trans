import re

# Translate string
def transliterate(text):
    translit_rules = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 
        'ь': '’', 'ы': 'y', 'ъ': '”', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    
    # Translator
    for cyrillic_char, latin_char in translit_rules.items():
        text = text.replace(cyrillic_char, latin_char)
        text = text.replace(cyrillic_char.upper(), latin_char.upper())
    
    return text

# Translitirate all fields in .bib file
def transliterate_bib_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    transliterated_content = []
    
    for line in content:
        if re.match(r'^\s*[a-zA-Z]+\s*=\s*{', line):
            field_name, field_value = re.split(r'\s*=\s*{', line, maxsplit=1)
            field_value = field_value.rstrip(',\n}')
            transliterated_value = transliterate(field_value)
            transliterated_line = f"{field_name} = {{{transliterated_value}}},\n"
            transliterated_content.append(transliterated_line)
        else:
            transliterated_content.append(line)
    
    output_file_path = file_path.replace('.bib', '_transliterated.bib')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(transliterated_content)


if __name__ == "__main__":
    bib_file_path = '/mnt/data/BIBLIOGRAPHY.bib'
    transliterate_bib_file(bib_file_path)
