from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random
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
        "next": "4"
    },
       "4":
       {
         "id": "4",
         "question": "To let go I must: ",
         "answers": ["Let go of everything forever","Think about what to let go","Direct my focus on something","Letting go will solve all of my problems."],
         "correct": "Direct my focus on something",
         "info":["There is no need to let go of everything forever, it is an impossible task. Letting go just means giving your mind a break so you can enjoy the present moment.",
         "When letting, you do not need to actively think about anything. Thinking is often the cause of mental suffering, so to let go, just allow your mind to focus on your breathing, or at nothing at all.",
         "Letting go does not mean to fogo perception. Letting go means observing the present, and not ruminating on the past or future.",
         "No act in mediation will solve all of your problems. Letting go allows your mind to rest and allows you to reorient yourself To better solve your problems. "],
         "next": "5"
       },
       "5":
       {
         "id": "5",
         "question": "Meditation …  ",
         "answers": ["Involves only letting go","constistes Techniques that must be mastered","Is a cure for all your problems","Meditation allows you to step back and observe"],
         "correct": "Meditation allows you to step back and observe",
         "info":["Meddition involves lots of different techniques, not only letting go. ",
         "Nothing in meditation needs to be mastered, all one needs to do is begin.",
         " No act in mediation will solve all of your problems. Letting go allows your mind to rest and allows you to reorient yourself.",
         "The purpose of meditation is to give your mind a break, the core of meditation is observing the present moment."],
         "next": "6"
       }
   }

score = len(questions) * [0]
not_answered = len(questions)* [True]

modules = {
   "1":{
      "id": "1", 
      "title":"Letting Go",
      "image": "https://images.unsplash.com/photo-1610878180933-123728745d22?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2FuYWRhJTIwbmF0dXJlfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
      "audio": "/static/audio_files/tape_1.mp3",
      "next": "2"
   },
   "2":{
      "id": "2",
      "title":"Box Breathing",  
      "image": "https://media.cntraveller.com/photos/611bf0b8f6bd8f17556db5e4/1:1/w_2000,h_2000,c_limit/gettyimages-1146431497.jpg", 
      "audio": "/static/audio_files/tape_2.mp3",
      "next": "3"
   }, 
   "3":{
      "id": "3",
      "title":"Blue Sky",
      "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Canyon_de_Chelly_panorama_of_valley_from_mountain.jpg", 
      "audio": "/static/audio_files/tape_3.mp3",
      "next": "4"
   },
   "4":{
      "id": "4",
      "title": "Your first meditation",
      "image":"https://www.rd.com/wp-content/uploads/2020/04/GettyImages-1093840488-5-scaled.jpg?resize=1536,1024",
      "audio": "/static/audio_files/tape_4.mp3",
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
   global score 
   global not_answered
   score = len(questions) * [0]
   not_answered = len(questions)* [True]
   shuffel_question()
   return render_template('quiz_start.html')

@app.route('/quiz/<id>', methods=['GET', 'POST'])
def quiz(id=None):
   question = questions[id]
   total_questions = len(questions)
   total_score = sum (score)
   return render_template('quiz.html',total_num = len(questions), question_num = id, question=question,total_score = total_score)

@app.route('/quiz/update_score', methods=['GET', 'POST'])
def update_score():
   global score 
   global not_answered
   answer = request.get_json()
   correct = answer["correct"]
   question_num = int(answer["id"]) - 1

   if correct == "true" and not_answered[question_num] == True:

      score[question_num] = 1
   elif not_answered[question_num]:

      not_answered[question_num] = False

   total_score = sum(score)

   return jsonify(total_score = total_score)

@app.route('/quiz/end')
def quiz_end():
   total_score = sum (score)
   return render_template('quiz_end.html',total_score = total_score)
def shuffel_question():
   print("in shuffel")
   global questions
   new_question_list = {}
   questions_list = list(questions.items())
   random.shuffle(questions_list)
   for i in range(1,len(questions)):# not going to reset the next value for the last question
      new_id = str(i)
      question = questions_list.pop()[1]
      question["id"] = new_id
      question["next"] = str(i+1)
      new_question_list[new_id] =question #add the question to the dictionary
   #deal with the last question
   last_question_id = str(len(questions))
   last_question = questions_list.pop()[1]
   last_question["id"] = last_question_id
   last_question["next"] = "0"
   new_question_list[last_question_id] = last_question
   questions = new_question_list
   return questions

@app.route('/report/<id>')
def report(id=None):
   module = modules[id]
   return render_template('report.html', module=module)
   





if __name__ == '__main__':
   shuffel_question()
   app.run(debug = True)
   


