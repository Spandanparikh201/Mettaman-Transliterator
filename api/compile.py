from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compiler.indic_compiler import convert_to_velthuis
from replacer import convert_to_ezh_string
import re

def execute_ezh_code(ezh_code):
    """Simple interpreter for basic Ezhil commands"""
    output = []
    lines = ezh_code.strip().split('\n')
    variables = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Handle piriNTu (print) statements
        if line.startswith('piriNTu'):
            # Extract string content
            match = re.search(r'piriNTu\s+"([^"]+)"', line)
            if match:
                output.append(match.group(1))
            else:
                # Handle variable printing
                var_match = re.search(r'piriNTu\s+([a-zA-Z_][a-zA-Z0-9_]*)', line)
                if var_match:
                    var_name = var_match.group(1)
                    if var_name in variables:
                        output.append(str(variables[var_name]))
                    else:
                        output.append(f"undefined: {var_name}")
        
        # Handle simple variable assignments
        elif '=' in line and not any(op in line for op in ['>', '<', '==', '!=']):
            parts = line.split('=', 1)
            if len(parts) == 2:
                var_name = parts[0].strip()
                value = parts[1].strip()
                # Try to evaluate as number
                try:
                    variables[var_name] = int(value)
                except ValueError:
                    # Store as string (remove quotes if present)
                    if value.startswith('"') and value.endswith('"'):
                        variables[var_name] = value[1:-1]
                    else:
                        variables[var_name] = value
    
    return '\n'.join(output) if output else 'No output generated'

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            code = data['code']
            language = data['language']
            
            # Stage 1: Convert to Velthuis
            velthuis_output = convert_to_velthuis(code, language)
            
            # Stage 2: Transliterated (same as velthuis)
            transliterated_output = velthuis_output
            
            # Stage 3: Convert to Ezhil
            ezh_output = convert_to_ezh_string(transliterated_output)
            
            # Stage 4: Execute code and get output
            execution_output = execute_ezh_code(ezh_output)
            
            response = {
                'success': True,
                'velthuis': velthuis_output,
                'transliterated': transliterated_output,
                'ezh': ezh_output,
                'output': execution_output
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_response = {
                'success': False,
                'error': str(e)
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()