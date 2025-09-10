const STATEMENT_MAPPINGS = {
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
    },
    'gu': {
        'છાપો': 'print', 'જો': 'if', 'નહીં_તો': 'else', 'જ્યાં_સુધી': 'while',
        'માટે': 'for', 'કાર્ય': 'def', 'પાછા': 'return'
    }
};

function get_char_mapping(lang_code) {
    const mappings = {
        'ta': {
            'அ': 'a', 'ஆ': 'aa', 'இ': 'i', 'ஈ': 'ii', 'உ': 'u', 'ஊ': 'uu', 'வ': 'va', 'ண': '.n', 'க': 'ka', 'ம': 'ma', 'ல': 'la', 'ங': 'Ga', 'ப': 'pa', 'ர': 'ra', 'ய': 'ya', 'த': 'ta', 'ன': 'na', 'ெ': 'e', 'ி': 'i', '்': '', 'ு': 'u', 'ா': 'aa', 'ே': 'ee', 'ை': 'ai', 'ோ': 'o', 'ௌ': 'au'
        },
        'hi': {
            'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'न': 'na', 'म': 'ma', 'स': 'sa', 'त': 'ta', 'े': 'e', 'ं': 'M', 'द': 'da', 'ु': 'u', 'ि': 'i', 'य': 'ya', 'ा': 'aa', 'र': 'ra', 'ल': 'la', 'क': 'ka', 'ग': 'ga', 'प': 'pa', 'ब': 'ba', 'छ': 'cha', 'ट': '.ta', 'ड': '.da', 'ण': '.na', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', '्': ''
        },
        'te': {
            'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ii', 'ఉ': 'u', 'ఊ': 'uu', 'న': 'na', 'మ': 'ma', 'స': 'sa', 'త': 'ta', 'ే': 'e', 'ం': 'M', 'ద': 'da', 'ు': 'u', 'ి': 'i', 'య': 'ya', 'ా': 'aa', 'ర': 'ra', 'ల': 'la', 'క': 'ka', 'గ': 'ga', 'ప': 'pa', 'బ': 'ba', 'చ': 'cha', 'ట': '.ta', 'డ': '.da', 'ణ': '.na', 'ై': 'ai', 'ొ': 'o', 'ౌ': 'au', '్': ''
        },
        'gu': {
            'અ': 'a', 'આ': 'aa', 'ઇ': 'i', 'ઈ': 'ii', 'ઉ': 'u', 'ઊ': 'uu', 'ન': 'na', 'મ': 'ma', 'સ': 'sa', 'ત': 'ta', 'ે': 'e', 'ં': 'M', 'દ': 'da', 'ુ': 'u', 'િ': 'i', 'ય': 'ya', 'ા': 'aa', 'ર': 'ra', 'લ': 'la', 'ક': 'ka', 'ગ': 'ga', 'પ': 'pa', 'બ': 'ba', 'છ': 'cha', 'ટ': '.ta', 'ડ': '.da', 'ણ': '.na', 'ૈ': 'ai', 'ો': 'o', 'ૌ': 'au', '્': ''
        }
    };
    return mappings[lang_code] || {};
}

function convert_statements_to_english(content, lang_code) {
    if (lang_code in STATEMENT_MAPPINGS) {
        const statement_map = STATEMENT_MAPPINGS[lang_code];
        for (const [indic_stmt, eng_stmt] of Object.entries(statement_map)) {
            content = content.replaceAll(indic_stmt, eng_stmt);
        }
    }
    return content;
}

function compile_indic(content, lang_code) {
    content = convert_statements_to_english(content, lang_code);
    const char_map = get_char_mapping(lang_code);
    let result = "";
    for (const char of content) {
        result += char_map[char] || char;
    }
    return result;
}

function convert_to_ezh(content) {
    const replacements = {
        'print': 'piriNTu', 'if': 'aaNaal', 'else': 'illai eNil',
        'while': 'vare', 'for': 'ullE', 'def': 'niyam', 'return': 'pirivu'
    };
    for (const [eng, ezh] of Object.entries(replacements)) {
        content = content.replaceAll(eng, ezh);
    }
    return content;
}

document.addEventListener('DOMContentLoaded', function() {
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
            const velthuis = compile_indic(code, language);
            velthuisOutput.textContent = velthuis;
            
            transliteratedOutput.textContent = velthuis;
            
            const ezh = convert_to_ezh(velthuis);
            ezhOutput.textContent = ezh;
            
        } catch (error) {
            alert('Compilation failed: ' + error.message);
        } finally {
            compileBtn.textContent = '🚀 Compile';
            compileBtn.disabled = false;
        }
    });
    
    const samples = {
        'ta': `அச்சிடு "வணக்கம் உலகம்"
ஆனால் x > 5:
    அச்சிடு "பெரிய எண்"
இல்லை:
    அச்சிடு "சிறிய எண்"`,
        'hi': `छापें "नमस्ते दुनिया"
अगर x > 5:
    छापें "बड़ी संख्या"
नहीं_तो:
    छापें "छोटी संख्या"`,
        'te': `ముద్రించు "నమస్కారం ప్రపంచం"
అయితే x > 5:
    ముద్రించు "పెద్ద సంఖ్య"
లేకపోతే:
    ముద్రించు "చిన్న సంఖ్య"`,
        'gu': `છાપો "નમસ્તે દુનિયા"
જો x > 5:
    છાપો "મોટી સંખ્યા"
નહીં_તો:
    છાપો "નાની સંખ્યા"`
    };
    
    languageSelect.addEventListener('change', function() {
        const lang = this.value;
        if (samples[lang]) {
            codeInput.value = samples[lang];
        }
    });
});