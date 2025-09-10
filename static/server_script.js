document.addEventListener('DOMContentLoaded', function() {
    const compileBtn = document.getElementById('compile-btn');
    const codeInput = document.getElementById('code-input');
    const languageSelect = document.getElementById('language');
    
    const programOutput = document.getElementById('program-output');
    const ezhOutput = document.getElementById('ezh-output');
    const velthuisOutput = document.getElementById('velthuis-output');
    const transliteratedOutput = document.getElementById('transliterated-output');
    
    compileBtn.addEventListener('click', async function() {
        const code = codeInput.value;
        const language = languageSelect.value;
        
        if (!code.trim()) {
            alert('Please enter some code to compile!');
            return;
        }
        
        compileBtn.textContent = '⏳ Compiling...';
        compileBtn.disabled = true;
        
        try {
            const response = await fetch('/api/compile', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    code: code,
                    language: language
                })
            });
            
            const result = await response.json();
            
            if (result.success) {
                programOutput.textContent = result.output;
                ezhOutput.textContent = result.ezh;
                velthuisOutput.textContent = result.velthuis;
                transliteratedOutput.textContent = result.transliterated;
            } else {
                alert('Compilation failed: ' + result.error);
            }
        } catch (error) {
            alert('Error: ' + error.message);
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