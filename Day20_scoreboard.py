from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.drawScoreBoard()

    def drawScoreBoard(self):
        self.write(f"Score: {self.score}", False, font=("Arial", 16, "normal"), align="center")

    def pointUp(self):
        self.clear()
        self.score += 1
        self.drawScoreBoard()

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"YOU LOST!\nYOUR SCORE WAS: {self.score}", font=("Arial", 28, "normal"), align="center")
