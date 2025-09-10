def convert_to_ezh(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert Roman Velthuis to Ezhil syntax
    ezh_content = velthuis_to_ezh(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(ezh_content)

def velthuis_to_ezh(content):
    # Basic replacements for Ezhil syntax
    replacements = {
        'print': 'piriNTu',
        'if': 'aaNaal',
        'else': 'illai eNil',
        'while': 'vare',
        'for': 'ullE',
        'def': 'niyam',
        'return': 'pirivu'
    }
    
    lines = content.split('\n')
    converted_lines = []
    
    for line in lines:
        converted_line = line
        for eng, ezh in replacements.items():
            converted_line = converted_line.replace(eng, ezh)
        converted_lines.append(converted_line)
    
    return '\n'.join(converted_lines)

def convert_to_ezh_string(content):
    return velthuis_to_ezh(content)