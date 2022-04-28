from flask import Flask,render_template
from WebReader import getJSON
app = Flask(__name__)

@app.route('/')
def index():
    data = getJSON()
    return render_template('index.html',database=data)

if __name__ == '__main__':
    app.run()