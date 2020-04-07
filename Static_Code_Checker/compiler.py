from os import system
import subprocess
try:
    from comparer import compare
except:
    from Static_Code_Checker.comparer import compare
    
def run_code(program, in_file=None, out_file=None):
    for language in code_languages:
        for ext in language['file_extension']:
            if ext in program:
                if in_file and out_file:
                    return language['function'](program, parseFile(in_file), parseFile(out_file))
                elif in_file and not out_file:
                    return language['function'](program, parseFile(in_file), [])
                elif not in_file and out_file:
                    return language['function'](program, [], parseFile(out_file))
                elif not in_file and not out_file:
                    return language['function'](program, [], [])
    
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

def run_code_python(program, args: list, results: list):
    info = code_languages[python_loc]
    command = -1
    trial = []

    for i in info['commands']:
        if subprocess.Popen([i, 'dummy.py'], stdout=subprocess.PIPE).communicate()[0] == 0 and command == -1:
            command = i
        else:
            continue
    if not isinstance(program, enumerate):
        for arg in args:
            commandLine = [command, program]

            for arg in args[i]:
                commandLine.append(arg)

            output = subprocess.Popen(commandLine, stdout=subprocess.PIPE).communicate()[0]
        
            trial.append(compare(output, results[i]))
    
    else:
        for script in program:
            for arg in args:
                commandLine = [command, script]

                for arg in args[i]:
                    commandLine.append(arg)

                output = subprocess.Popen(commandLine, stdout=subprocess.PIPE).communicate()[0]
                
                if output != '':
                    trial.append(compare(output, results[i]))

code_languages = [
    {
        # Java
        'file_extension': ['.java', '.class'],
        'commands': ['javac', 'java'],
        'function': run_code_java
    },
    {
        # Python
        'file_extension': ['.py', '.pyc'],
        'commands': ['python3', 'python'],
        'function': run_code_python
    }
]

java_loc = 0
python_loc = 1

