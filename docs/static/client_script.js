let pyodide;

async function initPyodide() {
    pyodide = await loadPyodide();
    await pyodide.loadPackage(['micropip']);
    
    // Load compiler code
    pyodide.runPython(`
STATEMENT_MAPPINGS = {
    'ta': {
        'அச்சிடு': 'print', 'ஆனால்': 'if', 'இல்லை': 'else', 'வரை': 'while',
        'உள்ளே': 'for', 'செயல்பாடு': 'def', 'திரும்பு': 'return'
    },
    'hi': {
        'छापें': 'print', 'अगर': 'if', 'नहीं_तो': 'else', 'जब_तक': 'while',
        'के_लिए': 'for', 'कार्य': 'def', 'वापस': 'return'
    },
    'te': {
        'ముద్రించు': 'print', 'అయితే': 'if', 'లేకపోతే': 'else', 'వరకు': 'while',
        'కోసం': 'for', 'కార్యం': 'def', 'తిరిగి': 'return'
    }
}

def get_char_mapping(lang_code):
    mappings = {
        'ta': {
            'అ': 'a', 'ஆ': 'aa', 'இ': 'i', 'ஈ': 'ii', 'உ': 'u', 'ஊ': 'uu', 'வ': 'va', 'ண': '.n', 'க': 'ka', 'ம': 'ma', 'ல': 'la', 'ங': 'Ga', 'ப': 'pa', 'ர': 'ra', 'ய': 'ya', 'த': 'ta', 'ன': 'na', 'ெ': 'e', 'ி': 'i', '்': '', 'ு': 'u', 'ா': 'aa', 'ே': 'ee', 'ை': 'ai', 'ோ': 'o', 'ௌ': 'au'
        },
        'hi': {
            'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'न': 'na', 'म': 'ma', 'स': 'sa', 'त': 'ta', 'े': 'e', 'ं': 'M', 'द': 'da', 'ु': 'u', 'ि': 'i', 'य': 'ya', 'ा': 'aa', 'र': 'ra', 'ल': 'la', 'क': 'ka', 'ग': 'ga', 'प': 'pa', 'ब': 'ba', 'छ': 'cha', 'ट': '.ta', 'ड': '.da', 'ण': '.na', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', '्': ''
        },
        'te': {
            'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ii', 'ఉ': 'u', 'ఊ': 'uu', 'న': 'na', 'మ': 'ma', 'స': 'sa', 'త': 'ta', 'ే': 'e', 'ం': 'M', 'ద': 'da', 'ు': 'u', 'ి': 'i', 'య': 'ya', 'ా': 'aa', 'ర': 'ra', 'ల': 'la', 'క': 'ka', 'గ': 'ga', 'ప': 'pa', 'బ': 'ba', 'చ': 'cha', 'ట': '.ta', 'డ': '.da', 'ణ': '.na', 'ై': 'ai', 'ొ': 'o', 'ౌ': 'au', '్': ''
        }
    }
    return mappings.get(lang_code, {})

def convert_statements_to_english(content, lang_code):
    if (lang_code in STATEMENT_MAPPINGS) {
        const statement_map = STATEMENT_MAPPINGS[lang_code];
        for (const [indic_stmt, eng_stmt] of Object.entries(statement_map)) {
            content = content.replaceAll(indic_stmt, eng_stmt);
        }
    }
    return content;
}

def compile_indic(content, lang_code):
    content = convert_statements_to_english(content, lang_code)
    char_map = get_char_mapping(lang_code)
    result = ""
    for char in content:
        result += char_map.get(char, char)
    return result

def convert_to_ezh(content):
    replacements = {
        'print': 'piriNTu', 'if': 'aaNaal', 'else': 'illai eNil',
        'while': 'vare', 'for': 'ullE', 'def': 'niyam', 'return': 'pirivu'
    }
    for eng, ezh in replacements.items():
        content = content.replace(eng, ezh)
    return content
    `);
}

document.addEventListener('DOMContentLoaded', async function() {
    await initPyodide();
    
    const compileBtn = document.getElementById('compile-btn');
    const codeInput = document.getElementById('code-input');
    const languageSelect = document.getElementById('language');
    
    const velthuisOutput = document.getElementById('velthuis-output');
    const transliteratedOutput = document.getElementById('transliterated-output');
    const ezhOutput = document.getElementById('ezh-output');
    
    compileBtn.addEventListener('click', function() {
        const code = codeInput.value;
        const language = languageSelect.value;
        
        if (!code.trim()) {
            alert('Please enter some code to compile!');
            return;
        }
        
        compileBtn.textContent = '⏳ Compiling...';
        compileBtn.disabled = true;
        
        try {
            // Stage 1: Compile to Velthuis
            pyodide.globals.set('input_code', code);
            pyodide.globals.set('lang_code', language);
            
            const velthuis = pyodide.runPython(`compile_indic(input_code, lang_code)`);
            velthuisOutput.textContent = velthuis;
            
            // Stage 2: Transliterated (simplified - same as velthuis for demo)
            transliteratedOutput.textContent = velthuis;
            
            // Stage 3: Convert to Ezhil
            pyodide.globals.set('velthuis_content', velthuis);
            const ezh = pyodide.runPython(`convert_to_ezh(velthuis_content)`);
            ezhOutput.textContent = ezh;
            
        } catch (error) {
            alert('Compilation failed: ' + error.message);
        } finally {
            compileBtn.textContent = '🚀 Compile';
            compileBtn.disabled = false;
        }
    });
    
    // Sample code for different languages
    const samples = {
        'ta': `print "வணக்கம் உலகம்"
if x > 5:
    print "பெரிய எண்"
else:
    print "சிறிய எண்"`,
        'hi': `print "नमस्ते दुनिया"
if x > 5:
    print "बड़ी संख्या"
else:
    print "छोटी संख्या"`,
        'te': `print "నమస్కారం ప్రపంచం"
if x > 5:
    print "పెద్ద సంఖ్య"
else:
    print "చిన్న సంఖ్య"`
    };
    
    languageSelect.addEventListener('change', function() {
        const lang = this.value;
        if (samples[lang]) {
            codeInput.value = samples[lang];
        }
    });
});