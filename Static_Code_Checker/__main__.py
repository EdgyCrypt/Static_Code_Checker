# getting errors?
# hit (Ctrl+Shift+P).and type Python: Select Interpreter
# the correct interpreter is Python 3.7.X 64 bit (./env/bin/python)
# if that is not an option call jake over

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
        self.landing_page = ''


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
    'index_css' : Bundle('css/main.css',  output='gen/index.css'),
    'student_js': Bundle('js/student.js',  output = 'gen/student.js'),
    'student_css': Bundle('css/student.css',  output = 'gen/student.css'),
    'teacher_js': Bundle('js/teacher.js',  output = 'gen/teacher.js'),
    'teacher_css': Bundle('css/teacher.css',  output = 'gen/teacher.css'),
    'interviewer_js': Bundle('js/interviewer.js',  output = 'gen/interviewer.js'),
    'interviewer_css': Bundle('css/interviewer.css',  output = 'gen/interviewer.css'),
    'interviewee_js': Bundle('js/interviewee.js',  output = 'gen/interviewee.js'),
    'interviewee_css': Bundle('css/interviewee.css',  output = 'gen/interviewee.css'),
})


"""
Routing:
Building the sitemap
"""

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def students():
    print(request.method)
    if request.method == 'POST':
        program = request.form['program']   
        print(request.form)
        if program:
            args = request.form['args']
            output = request.form['output']
            print(args)
            print(output)
            if not args:
                args = ''
            
            if not output:
                output = ''

            print(run_code(program, args, output))
    return render_template('student.html')

@app.route('/teacher')
def teachers():
    return render_template('teacher.html')

@app.route('/interviewer')
def interviewer():
    return render_template('interviewer.html')

@app.route('/interviewee')
def interviewee():
    return render_template('interviewee.html')

"""
Adding the POST Functions
"""
# Adds the ability to read in file using TK instead of JS
#       this enables us to read files as file paths and not as JS file objects
@app.route('/file')
def file():
    select = filedialog.askopenfilename()
    return select

# main driver function 
if __name__ == '__main__': 
    app.run(debug=True) # change this flag when moving into production
    
