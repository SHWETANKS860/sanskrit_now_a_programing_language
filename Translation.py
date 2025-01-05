#!/usr/bin/env python3
import sys
import os

def translate_to_python(sanskrit_code):
    translations = {
        "वद": "print",
        "यदि": "if",
        "अन्यथा": "else",
        "चक्र": "for",
        "में": "in",
        "क्रम": "range",
        "सत्यं": "True",
        "मिथ्या": "False",
        "कृतिः": "def",
        "प्रत्यावर्तनम्": "return",
    }
    for sanskrit, python in translations.items():
        sanskrit_code = sanskrit_code.replace(sanskrit, python)
    sanskrit_code = sanskrit_code.replace(";", "")
    return sanskrit_code

def execute_sanskrit_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sanskrit_code = file.read()
        python_code = translate_to_python(sanskrit_code)
        exec(python_code)
    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./file.sanskrit or sanskrit_interpreter.py <filename.sanskrit>")
        sys.exit(1)
    file_path = sys.argv[1]
    execute_sanskrit_file(file_path)
