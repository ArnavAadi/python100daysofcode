from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"level: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"level: {self.score}", align="center", font=FONT)

    def GAME_OVER(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
