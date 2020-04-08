# getting errors?
# hit (Ctrl+Shift+P).and type Python: Select Interpreter
# the correct interpreter is Python 3.7.X 64 bit (./env/bin/python)
# if that is not an option call jake over

import os

from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from flask_assets import Environment, Bundle
from flask_bootstrap import Bootstrap

from tkinter import filedialog

try:
    from compiler import run_code # (program, in_file, out_file)
except:
    from Static_Code_Checker.compiler import run_code

class UserInstance:
    def __init__(self):
        self.code_files = ''
        self.input_file = ''
        self.output_file = ''
    def __repr__(self):
        return f'''
        Code file:  {self.code_files}
        Input file: {self.input_files}
        Output file: {self.output_file}
        '''


user = UserInstance()

app = Flask(__name__) 

"""
Applying JQuery and Bootstrap
"""
Bootstrap(app)
assets = Environment(app)

"""
Staticing the css and JS
"""

assets.register({
    'index_js' : Bundle('js/home.js', output='gen/index.js'),
    'index_css' : Bundle('css/main.css', 'css/animate.css',  output='gen/index.css'),
    'student_js': Bundle('js/student.js',  output = 'gen/student.js'),
    'student_css': Bundle('css/student.css',  'css/animate.css', output = 'gen/student.css'),
    'teacher_js': Bundle('js/teacher.js',  output = 'gen/teacher.js'),
    'teacher_css': Bundle('css/teacher.css',  'css/animate.css', output = 'gen/teacher.css'),
    'interviewer_js': Bundle('js/interviewer.js',  output = 'gen/interviewer.js'),
    'interviewer_css': Bundle('css/interviewer.css', 'css/animate.css',  output = 'gen/interviewer.css'),
    'interviewee_js': Bundle('js/interviewee.js',  output = 'gen/interviewee.js'),
    'interviewee_css': Bundle('css/interviewee.css', 'css/animate.css',  output = 'gen/interviewee.css'),
})


"""
Routing:
Building the sitemap
To get the button presses it will have to run back
"""
# request.args.get('<whatever>') - returns in safe mode ie avoiding not found exceptions

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def students():
    return render_template('student.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teachers():
    return render_template('teacher.html')

@app.route('/interviewer', methods=['GET', 'POST'])
def interviewer():
    return render_template('interviewer.html')

@app.route('/interviewee', methods=['GET', 'POST'])
def interviewee():
    return render_template('interviewee.html')

'''
Non-page routes
We use these to gather information for compilation
'''
# students
@app.route('/code_file_select_student' , methods=['POST', 'GET'])
def code_file_select_student():
    user.code = read_file()
    return students()

@app.route('/code_dir_select_student', methods=['POST', 'GET'])
def code_dir_select_student_student():
    user.code = read_file()
    return students()

@app.route('/input_file_select_student', methods=['POST', 'GET'])
def input_file_select_student():
    user.input_file = read_file()
    return students()

@app.route('/output_file_select_student', methods=['POST', 'GET'])
def output_file_select_student():
    user.output_file = read_file()
    return students()


# teachers
@app.route('/code_file_select_teacher' , methods=['POST', 'GET'])
def code_file_select_teacher():
    user.code = read_file()
    return teachers()

@app.route('/code_dir_select_teacher', methods=['POST', 'GET'])
def code_dir_select_teacher_teacher():
    user.code = read_file()
    return teachers()

@app.route('/input_file_select_teacher', methods=['POST', 'GET'])
def input_file_select_teacher():
    user.input_file = read_file()
    return teachers()

@app.route('/output_file_select_teacher', methods=['POST', 'GET'])
def output_file_select_teacher():
    user.output_file = read_file()
    return teachers()

# interviewer
@app.route('/code_file_select_interviewer' , methods=['POST', 'GET'])
def code_file_select_interviewer():
    user.code = read_file()
    return interviewer()

@app.route('/code_dir_select_interviewer', methods=['POST', 'GET'])
def code_dir_select_interviewer_interviewer():
    user.code = read_file()
    return interviewer()

@app.route('/input_file_select_interviewer', methods=['POST', 'GET'])
def input_file_select_interviewer():
    user.input_file = read_file()
    return interviewer()

@app.route('/output_file_select_interviewer', methods=['POST', 'GET'])
def output_file_select_interviewer():
    user.output_file = read_file()
    return interviewer()

# intervieee
@app.route('/code_file_select_interviewees' , methods=['POST', 'GET'])
def code_file_select_interviewees():
    user.code = read_file()
    return interviewee()

@app.route('/code_dir_select_interviewees', methods=['POST', 'GET'])
def code_dir_select_interviewees_interviewees():
    user.code = read_file()
    return interviewee()

@app.route('/input_file_select_interviewees', methods=['POST', 'GET'])
def input_file_select_interviewees():
    user.input_file = read_file()
    return interviewee()

@app.route('/output_file_select_interviewees', methods=['POST', 'GET'])
def output_file_select_interviewees():
    user.output_file = read_file()
    return interviewee()

def read_file():
    with open('file.py', 'w+') as f:
        f.write("from tkinter import filedialog as fd\nfile = filedialog.askopenfilename()\nwith open('_file_saver.mbnhwfjg', 'w+') as f:\nf.write(file)")

    run_code(program='file.py')
    filepath = open('_file_saver.mbnhwfjg', 'r').readline()

    tempFiles = ['_file_saver.mbnhwfjg', 'file.py', 'dummy.py']
    for i in tempFiles:
        os.remove(i)
    
    return filepath




# main driver function 
if __name__ == '__main__': 
    app.run(debug=True) # change this flag when moving into production
    
