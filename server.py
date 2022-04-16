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
        and emotions. Judgement only increases the emotion""","""Correct""","Not really, try again","There is no perfect way to meditate"],
        "next": "2"
    },
    "2":{
        "id": "2",
        "question": "Box Breathing...",
        "answers": ["Is something to be forced", "Is the only way to meditate", "Is an important tool in meditation","Solves all problems"],
        "correct": "Is an important tool in meditation",
        "info": ["""There is no need to force anythign in meditation. Your body knows
        how to breath, just guide it to where you want it to go.""", """ There is no singular way
        to meditate""", """Correct""","""Nothing will solve all problem , but box breathing may facilitate it !"""],
        "next": "3"
    },
     "3":{
        "id": "3",
        "question": "Blue Sky...",
        "answers": ["Is about interrogating your emotions", "Is about identifying with your emotions", "Is about returning to a place of peace","Is about controlling your mind"],
        "correct": "Is about returning to a place of peace",
        "info": ["""There is no need to interrogate your emotions. Emotions are like clouds,
        just let them go, to return to your blue sky.""", """You don't need to identify your emotions""", """Correct""","Nope blue sky is never about this"],
        "next": "0"
    }
}
score = len(questions) * [0]
not_answered = len(questions)* [True]




@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/quiz/start')
def quiz_start():
   global score 
   global not_answered
   score = len(questions) * [0]
   not_answered = len(questions)* [True]
   return render_template('quiz_start.html')

@app.route('/quiz/<id>', methods=['GET', 'POST'])
def quiz(id=None):
   print(id)
   question = questions[id]
   total_score = sum (score)
   return render_template('quiz.html', question_num = id, question=question,total_score = total_score)
@app.route('/quiz/update_score', methods=['GET', 'POST'])
def update_score():
   global score 
   global not_answered
   answer = request.get_json()
   correct = answer["correct"]
   question_num = int(answer["id"]) - 1
   print( question_num)
   if correct == "true" and not_answered[question_num] == True:
      print(not_answered[question_num])
      score[question_num] = 1
   elif not_answered[question_num]:
      print("wrong")
      not_answered[question_num] = False
      print(not_answered)
   total_score = sum(score)
   print("put of if loop",not_answered)
   return jsonify(total_score = total_score)

@app.route('/quiz/end')
def quiz_end():
   total_score = sum (score)
   return render_template('quiz_end.html',total_score = total_score)


if __name__ == '__main__':
   app.run(debug = True)