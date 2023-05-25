from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/page2')
def page2():
    from script.test import test
    x = test()
    return render_template('page2.html')    
"""
@app.route('/')
def index():
    return "Hello World!"
"""
   

if __name__ == "__main__":
    app.secret_key = "ThisisNotASecret:p"
    app.run(debug=True)