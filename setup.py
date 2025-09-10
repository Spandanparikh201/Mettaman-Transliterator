import subprocess
import sys
import os

def setup_project():
    print("Setting up Metamman Transliterator...")
    
    # Create virtual environment for Python 3.13.0
    print("Creating virtual environment...")
    subprocess.run([
        r"C:\Users\Spandan\AppData\Local\Programs\Python\Python313\python.exe",
        "-m", "venv", "venv"
    ])
    
    # Install Aksharamukha in virtual environment
    print("Installing Aksharamukha...")
    subprocess.run([
        "venv\\Scripts\\pip.exe", 
        "install", "aksharamukha"
    ])
    
    print("Setup complete!")
    print("Usage: python main.py <input_file> <language_code>")

if __name__ == "__main__":
    setup_project()