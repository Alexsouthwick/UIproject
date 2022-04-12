from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('homepage.html')


if __name__ == '__main__':
   app.run(debug = True)