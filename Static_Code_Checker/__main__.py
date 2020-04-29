# Standard Library Imports
import os
import subprocess
import webbrowser
import sys

# Flask
from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from flask_assets import Environment, Bundle
from flask_bootstrap import Bootstrap

# Other third party
from tkinter import filedialog


# START: Compile


def run_code(program, in_file=None, out_file=None):
    for language in code_languages:
        for ext in language['file_extension']:
            if ext in program:
                if in_file and out_file:
                    return language['function'](program, parse_file(in_file), parse_file(out_file))
                elif in_file and not out_file:
                    return language['function'](program, parse_file(in_file), [])
                elif not in_file and out_file:
                    return language['function'](program, [], parse_file(out_file))
                elif not in_file and not out_file:
                    return language['function'](program, [], [])

    return 'No langauge found'


def parse_file(file):
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
            exec_bit = code_languages['java']['commands'][0] + ' ' + i
            os.system(exec_bit)
            if 'driver' in i.lower() and once:
                program_class = i.split('.')[0] + '.class'
                once = False

    else:
        exec_bit = code_languages['java']['commands'][0] + ' ' + program
        os.system(exec_bit)
        program_class = program.split('.')[0] + '.class'

    trial = []

    for i in range(len(args)):
        command_line = [code_languages['java']['commands'][1], program_class]
        for arg in args[i]:
            command_line.append(arg)

        output = subprocess.Popen(command_line, stdout=subprocess.PIPE).communicate()[0]

        trial.append(compare(output, results[i]))

    return trial


def run_code_python(program, args: list, results: list):
    return None


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


# START: Compare


def prep_html(text: str, expression: bool):
    """
    Returns the match or miss for each character while already moving it to html
    text: the actual character
    expression: matching status
    """
    if expression:
        return f'<div class="__g__"> {text} </div>'
    else:
        return f'<div class="__r__"> {text} </div>'


def compare(original_text: str, generated_text: str):
    """
    Compares 2 strings and returns html to be served to the models
    original_text - The text from the example
    generated_text - The text from the
    """
    comparison = ""

    # we will assume that this is the actual text
    for i in range(len(generated_text)):
        try:
            comparison += prep_html(generated_text[i], generated_text[i] == original_text[i])
        except IndexError:
            comparison += prep_html(generated_text[i], False)

    if len(original_text) > len(generated_text):
        comparison += prep_html(original_text[len(generated_text):len(original_text)], False)

    percent_match = comparison.count("__g__") / (comparison.count("__g__") + comparison.count("__r__"))

    return comparison, percent_match


# START: Routes, FLASK


class UserInstance:
    def __init__(self):
        self.code_files = ''
        self.input_file = ''
        self.output_file = ''

    def __repr__(self):
        return f'Code file:  {self.code_files}\nInput file: {self.input_file}\nOutput file: {self.output_file}'


user = UserInstance()

app = Flask(__name__)

"""
Applying JQuery and Bootstrap
"""
Bootstrap(app)
assets = Environment(app)

"""
Static-ing the css and JS
"""

assets.register({
    'index_js': Bundle('js/home.js', output='gen/index.js'),
    'index_css': Bundle('css/main.css', 'css/animate.css', output='gen/index.css'),
    'student_js': Bundle('js/student.js', output='gen/student.js'),
    'student_css': Bundle('css/student.css', 'css/animate.css', output='gen/student.css'),
    'teacher_js': Bundle('js/teacher.js', output='gen/teacher.js'),
    'teacher_css': Bundle('css/teacher.css', 'css/animate.css', output='gen/teacher.css'),
    'interviewer_js': Bundle('js/interviewer.js', output='gen/interviewer.js'),
    'interviewer_css': Bundle('css/interviewer.css', 'css/animate.css', output='gen/interviewer.css'),
    'interviewee_js': Bundle('js/interviewee.js', output='gen/interviewee.js'),
    'interviewee_css': Bundle('css/interviewee.css', 'css/animate.css', output='gen/interviewee.css'),
})

"""
file finding functions
"""


def read_file():
    with open('file.py', 'w+') as f:
        f.write(
            "from tkinter import Tk\nfrom tkinter.filedialog import askopenfilename\nroot = Tk()\nfile = "
            "askopenfilename()\nroot.destroy()\nwith open('_file_saver.mbnhwfjg', 'w+') as f:\n\tf.write(file)\ninput("
            ")")

    os.system(find_python_command() + ' file.py')

    with open('../_file_saver.mbnhwfjg', 'r') as f:
        filepath = f.readline()

    temp_files = ['_file_saver.mbnhwfjg', 'file.py']
    for i in temp_files:
        os.remove(i)

    return filepath


def find_python_command():
    possible_commands = ['python', 'python3', 'py', 'py3']
    for command in possible_commands:
        line = [command, '--version']

        try:
            output = subprocess.Popen(line, stdout=subprocess.PIPE).communicate()[0]
        except:
            continue

        if '3' in output.decode("utf-8"):
            return command


"""
Routing:
Building the sitemap
To get the button presses it will have to run back
"""


# request.args.get('<whatever>') - returns in safe mode ie avoiding not found exceptions


@app.route('/')
def index():
    print(user)
    return render_template('index.html')


@app.route('/student', methods=['GET', 'POST'])
def students(out=None):
    print(user)
    return render_template('student.html')


@app.route('/teacher', methods=['GET', 'POST'])
def teachers(out=None):
    print(user)
    return render_template('teacher.html')


@app.route('/interviewer', methods=['GET', 'POST'])
def interviewer(out=None):
    print(user)
    return render_template('interviewer.html')


@app.route('/interviewee', methods=['GET', 'POST'])
def interviewee(out=None):
    print(user)
    return render_template('interviewee.html')


'''
Non-page routes
We use these to gather information for compilation
'''


# students


@app.route('/code_file_select_student', methods=['POST', 'GET'])
def code_file_select_student():
    global user
    user.code = read_file()
    return redirect(url_for('student'))


@app.route('/code_dir_select_student', methods=['POST', 'GET'])
def code_dir_select_student_student():
    global user
    user.code = read_file()
    return redirect(url_for('student'))


@app.route('/input_file_select_student', methods=['POST', 'GET'])
def input_file_select_student():
    global user
    user.input_file = read_file()
    return redirect(url_for('student'))


@app.route('/output_file_select_student', methods=['POST', 'GET'])
def output_file_select_student():
    global user
    user.output_file = read_file()
    return redirect(url_for('student'))


@app.route('/submit_student')
def submit_student():
    print('yeet')


# teachers


@app.route('/code_file_select_teacher', methods=['POST', 'GET'])
def code_file_select_teacher():
    global user
    user.code = read_file()
    return redirect(url_for('teachers'))


@app.route('/code_dir_select_teacher', methods=['POST', 'GET'])
def code_dir_select_teacher_teacher():
    global user
    user.code = read_file()
    return redirect(url_for('teachers'))


@app.route('/input_file_select_teacher', methods=['POST', 'GET'])
def input_file_select_teacher():
    global user
    user.input_file = read_file()
    return redirect(url_for('teachers'))


@app.route('/output_file_select_teacher', methods=['POST', 'GET'])
def output_file_select_teacher():
    global user
    user.output_file = read_file()
    return redirect(url_for('teachers'))


@app.route('/submit_teachers')
def submit_teachers():
    global user
    print('yeet')


# interviewer


@app.route('/code_file_select_interviewer', methods=['POST', 'GET'])
def code_file_select_interviewer():
    global user
    user.code = read_file()
    return redirect(url_for('interviewer'))


@app.route('/code_dir_select_interviewer', methods=['POST', 'GET'])
def code_dir_select_interviewer_interviewer():
    global user
    user.code = read_file()
    return redirect(url_for('interviewer'))


@app.route('/input_file_select_interviewer', methods=['POST', 'GET'])
def input_file_select_interviewer():
    global user
    user.input_file = read_file()
    return redirect(url_for('interviewer'))


@app.route('/output_file_select_interviewer', methods=['POST', 'GET'])
def output_file_select_interviewer():
    global user
    user.output_file = read_file()
    return redirect(url_for('interviewer'))


@app.route('/submit_interviewer')
def submit_interviewer():
    print('yeet')


# interviewee


@app.route('/code_file_select_interviewees', methods=['POST', 'GET'])
def code_file_select_interviewees():
    global user
    user.code = read_file()
    return redirect(url_for('interviewee'))


@app.route('/code_dir_select_interviewees', methods=['POST', 'GET'])
def code_dir_select_interviewees_interviewees():
    global user
    user.code = read_file()
    return redirect(url_for('interviewee'))


@app.route('/input_file_select_interviewees', methods=['POST', 'GET'])
def input_file_select_interviewees():
    global user
    user.input_file = read_file()
    return redirect(url_for('interviewee'))


@app.route('/output_file_select_interviewees', methods=['POST', 'GET'])
def output_file_select_interviewees():
    global user
    user.output_file = read_file()
    return redirect(url_for('interviewee'))


@app.route('/submit_interviewees')
def submit_interviewees():
    print('yeet')


# main driver function


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')  # Auto opens up browser
    app.run(debug=True)  # change this flag when moving into production
