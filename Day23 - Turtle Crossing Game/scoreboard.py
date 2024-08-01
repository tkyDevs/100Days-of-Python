from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.teleport(-280, 270)
        self.showScore()

    def showScore(self):
        self.write(f"Level: {self.score}", False, align="left", font=("Arial", 12, "normal"))

    def nextLevel(self):
        self.clear()
        self.score += 1
        self.showScore()

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Your score was {self.score}!", False, align="center", font=FONT)
