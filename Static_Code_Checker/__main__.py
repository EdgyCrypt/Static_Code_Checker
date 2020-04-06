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
To get the button presses it will have to run back
"""
# request.args.get('<whatever>') - returns in safe mode ie avoiding not found exceptions

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def students():
    return render_template('student.html', input_file= user.input_file, output_file= user.output_file, code_file= user.code_files)

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
We use these to gather information for compliation
'''


re_routes = {'index': index, 'students': students, 'teacher': teachers, 'interviewer': interviewer, 'interviewee': interviewee}

@app.route('/code_file_select' , methods=['POST', 'GET'])
def code_file_select():
    user.landing_page = request.args.get('page_url')
    print(f"from {user.landing_page}")
    if user.landing_page != 'teacher':
        run_code(program='files.py')
    else:
        run_code(program='dir.py')
    
    return re_routes[user.landing_page]()

@app.route('/code_dir_select', methods=['POST', 'GET'])
def code_dir_select():
    user.landing_page = request.args.get('page_url')
    print(f"from {user.landing_page}")
    run_code(program='files.py')
    return re_routes[user.landing_page]()

@app.route('/input_file_select', methods=['POST', 'GET'])
def input_file_select():
    print("We are in the input file")
    user.landing_page = request.args.get('page_url')
    print(f"from {user.landing_page}")
    run_code(program='files.py')
    redirect('/' + user.landing_page)

@app.route('/output_file_select', methods=['POST', 'GET'])
def output_file_select():
    user.landing_page = request.args.get('page_url')
    print(f"from {user.landing_page}")
    run_code(program='files.py')
    return re_routes[user.landing_page]()
    

# main driver function 
if __name__ == '__main__': 
    app.run(debug=True) # change this flag when moving into production
    
