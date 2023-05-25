from flask import Flask

app = Flask(__name__)

"""
@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/')
def index():
    return "Hello World!"
   

if __name__ == "__main__":
    app.secret_key = "ThisisNotASecret:p"
    app.run(debug=True)