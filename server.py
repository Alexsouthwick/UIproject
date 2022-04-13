from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

questions = {
    "1":{
        "id": "1",
        "question": "Letting go is about...",
        "answers": ["Judging Emotion", "Experiencing the here and now","Being openminded", "Perfecting meditation"],
        "correct": "Experiencing the here and now",
        "info": ["""Letting go is about releasing judgement on your thoughts 
        and emotions. Judgement only increases the emotion""", """Correct"""],
        "next": "2"
    },
    "2":{
        "id": "2",
        "question": "Box Breathing...",
        "answers": ["Is something to be forced", "Is the only way to meditate", "Is an important tool in meditation","Solves all problems"],
        "correct": "Is an important tool in meditation",
        "info": ["""There is no need to force anythign in meditation. Your body knows
        how to breath, just guide it to where you want it to go.""", """ There is no singular way
        to meditate""", """Correct"""],
        "next": "3"
    },
     "3":{
        "id": "3",
        "question": "Blue Sky...",
        "answers": ["Is about interrogating your emotions", "Is about identifying with your emotions", "Is about returning to a place of peace","Is about controlling your mind"],
        "correct": "Is about returning to a place of peace",
        "info": ["""There is no need to interrogate your emotions. Emotions are like clouds,
        just let them go, to return to your blue sky.""", """You don't need to identify your emotions""", """Correct"""],
        "next": "0"
    }
}




@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/quiz/start')
def quiz_start():
   return render_template('quiz_start.html')

@app.route('/quiz/<id>')
def quiz(id=None):
   question = questions[id]
   return render_template('quiz.html', question=question)

@app.route('/quiz/end')
def quiz_end():
   return render_template('quiz_end.html')


if __name__ == '__main__':
   app.run(debug = True)