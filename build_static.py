import os
import shutil
from pathlib import Path

def build_static_site():
    # Create docs directory for GitHub Pages
    docs_dir = Path('docs')
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir()
    
    # Copy static files
    shutil.copytree('static', docs_dir / 'static')
    
    # Create client-side only version
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metamman Transliterator IDE</title>
    <link rel="stylesheet" href="static/style.css">
    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔤 Metamman Transliterator IDE</h1>
            <p>Multi-stage compiler for Indic languages to Ezhil execution</p>
        </header>
        
        <div class="editor-section">
            <div class="controls">
                <select id="language">
                    <option value="ta">Tamil (ta)</option>
                    <option value="hi">Hindi (hi)</option>
                    <option value="te">Telugu (te)</option>
                    <option value="kn">Kannada (kn)</option>
                    <option value="ml">Malayalam (ml)</option>
                    <option value="bn">Bengali (bn)</option>
                    <option value="gu">Gujarati (gu)</option>
                    <option value="pa">Punjabi (pa)</option>
                </select>
                <button id="compile-btn">🚀 Compile</button>
            </div>
            
            <div class="editor-container">
                <div class="editor-panel">
                    <h3>📝 Input Code</h3>
                    <textarea id="code-input">print "வணக்கம் உலகம்"
if x > 5:
    print "பெரிய எண்"
else:
    print "சிறிய எண்"</textarea>
                </div>
            </div>
        </div>
        
        <div class="output-section">
            <div class="output-panel">
                <h3>🔄 Roman Velthuis</h3>
                <pre id="velthuis-output"></pre>
            </div>
            <div class="output-panel">
                <h3>🌐 Transliterated</h3>
                <pre id="transliterated-output"></pre>
            </div>
            <div class="output-panel">
                <h3>⚡ Ezhil Code</h3>
                <pre id="ezh-output"></pre>
            </div>
        </div>
        
        <div class="workflow">
            <div class="stage">Stage 1<br>Indic → Velthuis</div>
            <div class="arrow">→</div>
            <div class="stage">Stage 2<br>Aksharamukha</div>
            <div class="arrow">→</div>
            <div class="stage">Stage 3<br>Replacer</div>
            <div class="arrow">→</div>
            <div class="stage">Stage 4<br>Ezhil</div>
        </div>
    </div>
    
    <script src="static/client_script.js"></script>
</body>
</html>'''
    
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    build_static_site()
    print("Static site built in docs/ directory")