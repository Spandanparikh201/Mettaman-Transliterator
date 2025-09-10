from flask import Flask, render_template, request, jsonify
import os
import tempfile
from main import compile_to_velthuis, transliterate_file, convert_to_ezh
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    try:
        data = request.json
        code = data['code']
        language = data['language']
        
        # Create temp files
        with tempfile.NamedTemporaryFile(mode='w', suffix=f'.{language}', delete=False, encoding='utf-8') as f:
            f.write(code)
            input_file = f.name
        
        base_name = os.path.splitext(input_file)[0]
        velthuis_file = f"{base_name}_velthuis.txt"
        transliterated_file = f"{base_name}_transliterated.txt"
        ezh_file = f"{base_name}.ezh"
        
        # Execute pipeline
        compile_to_velthuis(input_file, velthuis_file, language)
        
        subprocess.run([
            "venv\\Scripts\\python.exe", 
            "transliterator\\aksharamukha_converter.py", 
            velthuis_file, transliterated_file
        ])
        
        convert_to_ezh(transliterated_file, ezh_file)
        
        # Read results
        with open(velthuis_file, 'r', encoding='utf-8') as f:
            velthuis_output = f.read()
        
        with open(transliterated_file, 'r', encoding='utf-8') as f:
            transliterated_output = f.read()
            
        with open(ezh_file, 'r', encoding='utf-8') as f:
            ezh_output = f.read()
        
        # Cleanup
        for file in [input_file, velthuis_file, transliterated_file, ezh_file]:
            if os.path.exists(file):
                os.unlink(file)
        
        return jsonify({
            'success': True,
            'velthuis': velthuis_output,
            'transliterated': transliterated_output,
            'ezh': ezh_output
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)