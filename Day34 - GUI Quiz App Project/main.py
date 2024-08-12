from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


def getQuestions():
    myParams = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get("https://opentdb.com/api.php", params=myParams)
    data = response.json()
    with open("data.py", "w") as file:
        file.write("question_data = ")
    with open("data.py", "a") as file:
        file.write(str(data['results']))


getQuestions()
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quizUi = QuizInterface(quiz)
#while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
