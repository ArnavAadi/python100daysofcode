from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    ques = Question(question["question"], question["correct_answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You have completed the quiz \n your final score is {quiz.score}/{quiz.question_number}")
