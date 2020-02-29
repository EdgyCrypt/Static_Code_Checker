from os import system as terminal

code_languages = {
    'java': {
        'file_extension': ['.java', '.class'],
        'commands': ['javac', 'java'],
        'function': run_code_java
    },
    'python' : {
        'file_extension': ['.py', '.pyc'],
        'commands': ['python', 'python3'],
        'function': run_code_python
    }
}

def run_code(program, in_file, out_file):
    for language in code_languages:
        for ext in language['file_extension']:
            if ext in program:
                return language['function'](program, parseFile(in_file), parseFile(out_file))
    
    return 'No langauge dected'

def parseFile(file):
    try:
        file = open(file).readlines()
        
    finally:
        temp = ''
        runs = []
        for line in file:
            if '^^^' not in line:
                temp += line
            else:
                runs.append(temp)
                temp = ''
    
    return runs