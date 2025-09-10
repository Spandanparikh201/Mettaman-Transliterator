import sys
import os
import subprocess
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <language_code>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    lang_code = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    
    base_name = Path(input_file).stem
    
    # Stage 1: Compile to Roman Velthuis
    velthuis_file = f"{base_name}_velthuis.txt"
    compile_to_velthuis(input_file, velthuis_file, lang_code)
    
    # Stage 2: Transliterate using Aksharamukha
    transliterated_file = f"{base_name}_transliterated.txt"
    transliterate_file(velthuis_file, transliterated_file)
    
    # Stage 3: Convert to .ezh
    ezh_file = f"{base_name}.ezh"
    convert_to_ezh(transliterated_file, ezh_file)
    
    # Stage 4: Execute with Ezhil
    execute_ezh(ezh_file)

def compile_to_velthuis(input_file, output_file, lang_code):
    from compiler.indic_compiler import compile_indic
    compile_indic(input_file, output_file, lang_code)

def transliterate_file(input_file, output_file):
    subprocess.run([
        "venv\\Scripts\\python.exe", 
        "transliterator\\aksharamukha_converter.py", 
        input_file, output_file
    ])

def convert_to_ezh(input_file, output_file):
    from replacer import convert_to_ezh
    convert_to_ezh(input_file, output_file)

def execute_ezh(ezh_file):
    print(f"Generated {ezh_file} - Execute manually with Ezhil interpreter")
    with open(ezh_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print("\nGenerated Ezhil code:")
        try:
            print(content)
        except UnicodeEncodeError:
            print(content.encode('utf-8', errors='replace').decode('utf-8'))

if __name__ == "__main__":
    main()