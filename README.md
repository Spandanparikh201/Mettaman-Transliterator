# Metamman Transliterator

Multi-stage compiler for Indic languages to Ezhil execution.

## Prerequisites
- Python 3.6.0 (with PATH) for Ezhil
- Python 3.13.0 (no PATH) for Aksharamukha

## Usage
```cmd
python main.py <input_file> <language_code>
```

## Workflow
1. Indic language code → Roman Velthuis (compiler)
2. Roman Velthuis → transliteration (Aksharamukha)
3. Transliteration → .ezh file (replacer.py)
4. Execute .ezh file (Ezhil)