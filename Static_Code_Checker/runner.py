from os import system
import subprocess
from Static_Code_Checker.checker import compare

code_languages = {
    'java': {
        'file_extension': ['.java', '.class'],
        'commands': ['javac', 'java'],
        'function': run_code_java
    },
    'python' : {
        'file_extension': ['.py', '.pyc'],
        'commands': ['python', 'python3'],
        'function': run_code_general
    }
}

def run_code(program, in_file, out_file):
    for language in code_languages:
        for ext in language['file_extension']:
            if ext in program:
                return language['function'](program, parseFile(in_file), parseFile(out_file))
    
    return 'No langauge found'

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

def run_code_java(program, args: list, results: list):
    # for this to work we will assume that len(args) = len(results)
    if type(program, enumerate):
        program_class = ''
        once = True
        for i in program:
            system(code_languages['java']['commands'][0] + ' ' + i) # javac's the file
            if 'driver' in i.lower() and once:
                program_class = i.split('.')[0] + '.class'
                once = False
        
    else:
        program_class = program.split('.')[0] + '.class'

    trial = []

    for i in range(len(args)):
        commandLine = [code_languages['java']['commands'][1], program_class]
        for arg in args[i]:
            commandLine.append(arg)
        
        output = subprocess.Popen(commandLine, stdout=subprocess.PIPE).communicate()[0]

        trial.append(compare(output, results[i]))
    
    return trial