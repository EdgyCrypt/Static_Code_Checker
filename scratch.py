import  subprocess

def find_python_command():
    possible_commnads = ['python', 'python3', 'py', 'py3']
    for command in possible_commnads:
        line = [command, '--version']
        
        try:
            output = subprocess.Popen(line, stdout=subprocess.PIPE).communicate()[0]
        except:
            continue

        print(output.decode("utf-8"))

        if '3' in output.decode("utf-8"):
            return command

print(find_python_command())