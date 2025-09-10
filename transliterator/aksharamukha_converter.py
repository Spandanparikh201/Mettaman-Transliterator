import sys
from aksharamukha import transliterate

def convert_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert to Roman Velthuis encoding
    converted = transliterate.process('autodetect', 'Velthuis', content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python aksharamukha_converter.py <input_file> <output_file>")
        sys.exit(1)
    
    convert_file(sys.argv[1], sys.argv[2])