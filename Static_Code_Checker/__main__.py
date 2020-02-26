# getting errors?
# hit (Ctrl+Shift+P).and type Python: Select Interpreter
# the correct interpreter is Python 3.7.X 64 bit (./env/bin/python)
# if that is not an option call jake over

from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/student')
def students():
    return render_template('students.html')

@app.route('/teacher')
def teachers():
    return render_template('teacher.html')

@app.route('/interviewer')
def interviewer():
    return render_template('teacher.html')

@app.route('/interviewee')
def interviewee():
    return render_template('interviewee.html')

# main driver function 
if __name__ == '__main__': 
    app.run(debug = True) # change this flag when moving into production
    
