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
  
# main driver function 
if __name__ == '__main__': 
    app.run(debug = True) # use for debugging
    # app,run() # for production
