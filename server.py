from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

questions = {
    "1":{
        "id": 1,
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

modules = {
   "1":{
      'id': 1, 
      "title":"Letting Go",
      "image": "https://images.unsplash.com/photo-1610878180933-123728745d22?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2FuYWRhJTIwbmF0dXJlfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
      "audio": "/GitHub/UIproject/audio_files/tape_1.mp3", 
      "next": "2"
   },
   "2":{
      "id": "2",
      "title":"Box Breathing",  
      "image": "https://media.cntraveller.com/photos/611bf0b8f6bd8f17556db5e4/1:1/w_2000,h_2000,c_limit/gettyimages-1146431497.jpg", 
      "audio": "/GitHub/UIproject/audio_files/tape_2.mp3",
      "next": "3"
   }, 
   "3":{
      "id": "3",
      "title":"Blue Sky",
      "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Canyon_de_Chelly_panorama_of_valley_from_mountain.jpg", 
      "audio": "/GitHub/UIproject/audio_files/tape_3.mp3",
      "next": "4"
   },
   "4":{
      "id": "4",
      "title": "Your first meditation",
      "image":"https://www.rd.com/wp-content/uploads/2020/04/GettyImages-1093840488-5-scaled.jpg?resize=1536,1024",
      "audio": "/GitHub/UIproject/audio_files/tape_4.mp3",
      "next": "0"
   }
}


@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/learning/start')
def learning_start():
   return render_template('learning_start.html')

@app.route('/learning/<id>')
def learning(id=None):
   module = modules[id]
   return render_template('learning.html', module=module)

@app.route('/learning/end')
def learning_end():
   return render_template('learning_end.html')

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