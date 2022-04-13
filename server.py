from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

questions = {
    "1":{
        "id": "1",
        "question": "Letting go is about...",
        "answers": ["Judging Emotion", "Experiencing the here and now","Being openminded", "Perfecting meditation"]
    }
}




@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/quiz/<id>')
def quiz(id=None):
   question = questions[id]
   return render_template('quiz.html', question=question)


if __name__ == '__main__':
   app.run(debug = True)