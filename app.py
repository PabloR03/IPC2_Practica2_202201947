#http://localhost:5000/ 
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('curriculum_202201947.html')

if __name__ == '__main__':
    app.run(debug=True)
