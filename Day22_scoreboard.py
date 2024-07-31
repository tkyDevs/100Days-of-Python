from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.position = position
        self.hideturtle()
        self.teleport(position[0], position[1])
        self.drawScoreBoard()

    def drawScoreBoard(self):
        self.write(f"Score: {self.score}", False, font=("Arial", 16, "normal"), align="center")

    def pointUp(self):
        self.clear()
        self.score += 1
        self.drawScoreBoard()

    def winner(self, name):
        self.clear()
        self.goto(0, 0)
        self.write(f"The winner is {name}!", False, font=("Arial", 24, "normal"), align="center")
