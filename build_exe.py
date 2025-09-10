import PyInstaller.__main__
import os

def build_executable():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--name=MetammanTransliterator',
        '--add-data=compiler;compiler',
        '--add-data=transliterator;transliterator',
        '--add-data=venv/Lib/site-packages/aksharamukha;aksharamukha',
        '--hidden-import=aksharamukha',
        '--console'
    ])

if __name__ == "__main__":
    build_executable()