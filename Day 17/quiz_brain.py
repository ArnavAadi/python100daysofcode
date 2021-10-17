class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {cur_question.text} (True/False): ")
        self.check_answer(answer, cur_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("thats wrong")
        print(f"the answer was : {correct_answer}")
        print(f"your current score is: {self.score}/{self.question_number}\n")
