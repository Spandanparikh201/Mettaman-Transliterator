import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compiler.indic_compiler import compile_indic, convert_to_velthuis
from replacer import convert_to_ezh

def handler(event, context):
    try:
        body = json.loads(event['body'])
        code = body['code']
        language = body['language']
        
        # Stage 1: Convert to Velthuis
        velthuis_output = convert_to_velthuis(code, language)
        
        # Stage 2: Transliterated (same as velthuis for now)
        transliterated_output = velthuis_output
        
        # Stage 3: Convert to Ezhil
        ezh_output = convert_to_ezh(transliterated_output)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps({
                'success': True,
                'velthuis': velthuis_output,
                'transliterated': transliterated_output,
                'ezh': ezh_output
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }