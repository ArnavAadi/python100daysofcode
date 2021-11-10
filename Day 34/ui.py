from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.user_answer = None

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.canvas = Canvas(height=250, width=300, )
        self.ques_text = self.canvas.create_text(
            150, 125, text="ques", fill=THEME_COLOR, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        self.score_label = Label(
            text=f"score: {self.quiz_brain.score}", bg=THEME_COLOR, fg="#FFFFFF")
        self.score_label.grid(column=1, row=0)

        self.true_img = PhotoImage(file="images/true.png")

        self.true_button = Button(
            image=self.true_img, highlightthickness=0.3, command=self.true)
        self.true_button.grid(column=0, row=2,)

        self.false_img = PhotoImage(file="images/false.png")

        self.false_button = Button(
            image=self.false_img, highlightthickness=0.3, command=self.false)
        self.false_button.grid(column=1, row=2,)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        if self.quiz_brain.still_has_questions():
            score = self.quiz_brain.score
            self.score_label.config(text=f"score: {score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.ques_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(bg="white")

    def true(self):
        self.user_answer = "True"
        ans = self.quiz_brain.check_answer(self.user_answer)
        self.check_ans(ans)

    def false(self):
        self.user_answer = "False"
        ans = self.quiz_brain.check_answer(self.user_answer)
        self.check_ans(ans)

    def check_ans(self, cor_ans):
        if cor_ans == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)
