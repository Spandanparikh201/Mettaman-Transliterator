LANGUAGE_MAPPINGS = {
    'ta': 'tamil', 'hi': 'hindi', 'te': 'telugu', 'kn': 'kannada',
    'ml': 'malayalam', 'bn': 'bengali', 'gu': 'gujarati', 'pa': 'punjabi',
    'or': 'odia', 'as': 'assamese'
}

STATEMENT_MAPPINGS = {
    'ta': {
        'அச்சிடு': 'print', 'ஆனால்': 'if', 'இல்லை': 'else', 'வரை': 'while',
        'உள்ளே': 'for', 'செயல்பாடு': 'def', 'திரும்பு': 'return', 'உள்': 'in',
        'மற்றும்': 'and', 'அல்லது': 'or', 'இல்லை': 'not', 'உண்மை': 'True',
        'பொய்': 'False', 'ஒன்றுமில்லை': 'None', 'முயற்சி': 'try', 'தவிர': 'except',
        'இறுதியாக': 'finally', 'உடன்': 'with', 'இறக்குமதி': 'import', 'இருந்து': 'from',
        'வகுப்பு': 'class', 'தொடர்': 'continue', 'உடைக்க': 'break', 'கடந்து': 'pass'
    },
    'hi': {
        'छापें': 'print', 'अगर': 'if', 'नहीं_तो': 'else', 'जब_तक': 'while',
        'के_लिए': 'for', 'कार्य': 'def', 'वापस': 'return', 'में': 'in',
        'और': 'and', 'या': 'or', 'नहीं': 'not', 'सच': 'True',
        'झूठ': 'False', 'कुछ_नहीं': 'None', 'कोशिश': 'try', 'सिवाय': 'except',
        'अंत_में': 'finally', 'के_साथ': 'with', 'आयात': 'import', 'से': 'from',
        'वर्ग': 'class', 'जारी': 'continue', 'तोड़': 'break', 'पास': 'pass'
    },
    'te': {
        'ముద్రించు': 'print', 'అయితే': 'if', 'లేకపోతే': 'else', 'వరకు': 'while',
        'కోసం': 'for', 'కార్యం': 'def', 'తిరిగి': 'return', 'లో': 'in',
        'మరియు': 'and', 'లేదా': 'or', 'కాదు': 'not', 'నిజం': 'True',
        'అబద్ధం': 'False', 'ఏమీలేదు': 'None', 'ప్రయత్నించు': 'try', 'తప్ప': 'except',
        'చివరకు': 'finally', 'తో': 'with', 'దిగుమతి': 'import', 'నుండి': 'from',
        'తరగతి': 'class', 'కొనసాగించు': 'continue', 'విరామం': 'break', 'దాటవేయి': 'pass'
    },
    'kn': {
        'ಮುದ್ರಿಸು': 'print', 'ಆದರೆ': 'if', 'ಇಲ್ಲದಿದ್ದರೆ': 'else', 'ವರೆಗೆ': 'while',
        'ಗಾಗಿ': 'for', 'ಕಾರ್ಯ': 'def', 'ಹಿಂತಿರುಗು': 'return', 'ನಲ್ಲಿ': 'in',
        'ಮತ್ತು': 'and', 'ಅಥವಾ': 'or', 'ಅಲ್ಲ': 'not', 'ನಿಜ': 'True',
        'ಸುಳ್ಳು': 'False', 'ಏನೂ_ಇಲ್ಲ': 'None', 'ಪ್ರಯತ್ನಿಸು': 'try', 'ಹೊರತು': 'except',
        'ಅಂತಿಮವಾಗಿ': 'finally', 'ಜೊತೆ': 'with', 'ಆಮದು': 'import', 'ಇಂದ': 'from',
        'ವರ್ಗ': 'class', 'ಮುಂದುವರಿಸು': 'continue', 'ಮುರಿ': 'break', 'ದಾಟು': 'pass'
    },
    'ml': {
        'അച്ചടിക്കുക': 'print', 'എങ്കിൽ': 'if', 'അല്ലെങ്കിൽ': 'else', 'വരെ': 'while',
        'വേണ്ടി': 'for', 'പ്രവർത്തനം': 'def', 'തിരികെ': 'return', 'ൽ': 'in',
        'ഒപ്പം': 'and', 'അല്ലെങ്കിൽ': 'or', 'അല്ല': 'not', 'സത്യം': 'True',
        'കള്ളം': 'False', 'ഒന്നുമില്ല': 'None', 'ശ്രമിക്കുക': 'try', 'ഒഴികെ': 'except',
        'അവസാനം': 'finally', 'കൂടെ': 'with', 'ഇറക്കുമതി': 'import', 'നിന്ന്': 'from',
        'ക്ലാസ്': 'class', 'തുടരുക': 'continue', 'തകർക്കുക': 'break', 'കടന്നുപോകുക': 'pass'
    },
    'bn': {
        'মুদ্রণ': 'print', 'যদি': 'if', 'নাহলে': 'else', 'যতক্ষণ': 'while',
        'জন্য': 'for', 'কাজ': 'def', 'ফিরে': 'return', 'মধ্যে': 'in',
        'এবং': 'and', 'অথবা': 'or', 'না': 'not', 'সত্য': 'True',
        'মিথ্যা': 'False', 'কিছুই_না': 'None', 'চেষ্টা': 'try', 'ছাড়া': 'except',
        'শেষে': 'finally', 'সাথে': 'with', 'আমদানি': 'import', 'থেকে': 'from',
        'শ্রেণী': 'class', 'চালিয়ে_যান': 'continue', 'ভাঙ্গুন': 'break', 'পাস': 'pass'
    },
    'gu': {
        'છાપો': 'print', 'જો': 'if', 'નહીં_તો': 'else', 'જ્યાં_સુધી': 'while',
        'માટે': 'for', 'કાર્ય': 'def', 'પાછા': 'return', 'માં': 'in',
        'અને': 'and', 'અથવા': 'or', 'નહીં': 'not', 'સાચું': 'True',
        'ખોટું': 'False', 'કંઈ_નહીં': 'None', 'પ્રયાસ': 'try', 'સિવાય': 'except',
        'અંતે': 'finally', 'સાથે': 'with', 'આયાત': 'import', 'થી': 'from',
        'વર્ગ': 'class', 'ચાલુ_રાખો': 'continue', 'તોડો': 'break', 'પાસ': 'pass'
    },
    'pa': {
        'ਛਾਪੋ': 'print', 'ਜੇ': 'if', 'ਨਹੀਂ_ਤਾਂ': 'else', 'ਜਦ_ਤੱਕ': 'while',
        'ਲਈ': 'for', 'ਕਾਰਜ': 'def', 'ਵਾਪਸ': 'return', 'ਵਿੱਚ': 'in',
        'ਅਤੇ': 'and', 'ਜਾਂ': 'or', 'ਨਹੀਂ': 'not', 'ਸੱਚ': 'True',
        'ਝੂਠ': 'False', 'ਕੁਝ_ਨਹੀਂ': 'None', 'ਕੋਸ਼ਿਸ਼': 'try', 'ਸਿਵਾਏ': 'except',
        'ਅੰਤ_ਵਿੱਚ': 'finally', 'ਨਾਲ': 'with', 'ਆਯਾਤ': 'import', 'ਤੋਂ': 'from',
        'ਸ਼੍ਰੇਣੀ': 'class', 'ਜਾਰੀ': 'continue', 'ਤੋੜੋ': 'break', 'ਪਾਸ': 'pass'
    },
    'gu': {
        'છાપો': 'print', 'જો': 'if', 'નહીં_તો': 'else', 'જ્યાં_સુધી': 'while',
        'માટે': 'for', 'કાર્ય': 'def', 'પાછા': 'return', 'માં': 'in',
        'અને': 'and', 'અથવા': 'or', 'નહીં': 'not', 'સાચું': 'True',
        'ખોટું': 'False', 'કંઈ_નહીં': 'None', 'પ્રયાસ': 'try', 'સિવાય': 'except',
        'અંતે': 'finally', 'સાથે': 'with', 'આયાત': 'import', 'થી': 'from',
        'વર્ગ': 'class', 'ચાલુ_રાખો': 'continue', 'તોડો': 'break', 'પાસ': 'pass'
    }
}

def compile_indic(input_file, output_file, lang_code):
    if lang_code not in LANGUAGE_MAPPINGS:
        raise ValueError(f"Unsupported language: {lang_code}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    velthuis_content = convert_to_velthuis(content, lang_code)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(velthuis_content)

def convert_to_velthuis(content, lang_code):
    content = convert_statements_to_english(content, lang_code)
    
    lines = content.split('\n')
    converted_lines = []
    
    for line in lines:
        if line.strip():
            converted_lines.append(transliterate_line(line, lang_code))
        else:
            converted_lines.append(line)
    
    return '\n'.join(converted_lines)

def convert_statements_to_english(content, lang_code):
    if lang_code not in STATEMENT_MAPPINGS:
        return content
    
    statement_map = STATEMENT_MAPPINGS[lang_code]
    
    for indic_stmt, eng_stmt in sorted(statement_map.items(), key=lambda x: len(x[0]), reverse=True):
        content = content.replace(indic_stmt, eng_stmt)
    
    return content

def transliterate_line(line, lang_code):
    char_map = get_char_mapping(lang_code)
    result = ""
    
    i = 0
    while i < len(line):
        if i < len(line) - 1:
            two_char = line[i:i+2]
            if two_char in char_map:
                result += char_map[two_char]
                i += 2
                continue
        
        char = line[i]
        result += char_map.get(char, char)
        i += 1
    
    return result

def get_char_mapping(lang_code):
    mappings = {
        'ta': {
            'அ': 'a', 'ஆ': 'aa', 'இ': 'i', 'ஈ': 'ii', 'உ': 'u', 'ஊ': 'uu', 'எ': 'e', 'ஏ': 'ee', 'ஐ': 'ai', 'ஒ': 'o', 'ஓ': 'oo', 'ஔ': 'au',
            'க': 'ka', 'ங': 'Ga', 'ச': 'ca', 'ஞ': 'Ja', 'ட': '.ta', 'ண': '.na', 'த': 'ta', 'ன': 'na', 'ப': 'pa', 'ம': 'ma', 'ய': 'ya', 'ர': 'ra', 'ல': 'la', 'வ': 'va', 'ழ': '.la', 'ள': '.la', 'ற': 'Ra', 'ன்': 'n',
            'ா': 'aa', 'ி': 'i', 'ீ': 'ii', 'ு': 'u', 'ூ': 'uu', 'ெ': 'e', 'ே': 'ee', 'ை': 'ai', 'ொ': 'o', 'ோ': 'oo', 'ௌ': 'au', '்': ''
        },
        'hi': {
            'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
            'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'ङ': 'Ga', 'च': 'ca', 'छ': 'cha', 'ज': 'ja', 'झ': 'jha', 'ञ': 'Ja',
            'ट': '.ta', 'ठ': '.tha', 'ड': '.da', 'ढ': '.dha', 'ण': '.na', 'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na',
            'प': 'pa', 'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma', 'य': 'ya', 'र': 'ra', 'ल': 'la', 'व': 'va', 'श': 'za', 'ष': '.sa', 'स': 'sa', 'ह': 'ha',
            'ा': 'aa', 'ि': 'i', 'ी': 'ii', 'ु': 'u', 'ू': 'uu', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', '्': '', 'ं': 'M', 'ः': 'H'
        },
        'te': {
            'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ii', 'ఉ': 'u', 'ఊ': 'uu', 'ఎ': 'e', 'ఏ': 'ee', 'ఐ': 'ai', 'ఒ': 'o', 'ఓ': 'oo', 'ఔ': 'au',
            'క': 'ka', 'ఖ': 'kha', 'గ': 'ga', 'ఘ': 'gha', 'ఙ': 'Ga', 'చ': 'ca', 'ఛ': 'cha', 'జ': 'ja', 'ఝ': 'jha', 'ఞ': 'Ja',
            'ట': '.ta', 'ఠ': '.tha', 'డ': '.da', 'ఢ': '.dha', 'ణ': '.na', 'త': 'ta', 'థ': 'tha', 'ద': 'da', 'ధ': 'dha', 'న': 'na',
            'ప': 'pa', 'ఫ': 'pha', 'బ': 'ba', 'భ': 'bha', 'మ': 'ma', 'య': 'ya', 'ర': 'ra', 'ల': 'la', 'వ': 'va', 'శ': 'za', 'ష': '.sa', 'స': 'sa', 'హ': 'ha',
            'ా': 'aa', 'ి': 'i', 'ీ': 'ii', 'ు': 'u', 'ూ': 'uu', 'ె': 'e', 'ే': 'ee', 'ై': 'ai', 'ొ': 'o', 'ో': 'oo', 'ౌ': 'au', '్': '', 'ం': 'M', 'ః': 'H'
        },
        'gu': {
            'અ': 'a', 'આ': 'aa', 'ઇ': 'i', 'ઈ': 'ii', 'ઉ': 'u', 'ઊ': 'uu', 'એ': 'e', 'ઐ': 'ai', 'ઓ': 'o', 'ઔ': 'au',
            'ક': 'ka', 'ખ': 'kha', 'ગ': 'ga', 'ઘ': 'gha', 'ઙ': 'Ga', 'ચ': 'ca', 'છ': 'cha', 'જ': 'ja', 'ઝ': 'jha', 'ઞ': 'Ja',
            'ટ': '.ta', 'ઠ': '.tha', 'ડ': '.da', 'ઢ': '.dha', 'ણ': '.na', 'ત': 'ta', 'થ': 'tha', 'દ': 'da', 'ધ': 'dha', 'ન': 'na',
            'પ': 'pa', 'ફ': 'pha', 'બ': 'ba', 'ભ': 'bha', 'મ': 'ma', 'ય': 'ya', 'ર': 'ra', 'લ': 'la', 'વ': 'va', 'શ': 'za', 'ષ': '.sa', 'સ': 'sa', 'હ': 'ha',
            'ા': 'aa', 'િ': 'i', 'ી': 'ii', 'ુ': 'u', 'ૂ': 'uu', 'ે': 'e', 'ૈ': 'ai', 'ો': 'o', 'ૌ': 'au', '્': '', 'ં': 'M', 'ઃ': 'H'
        }
    }
    return mappings.get(lang_code, {})