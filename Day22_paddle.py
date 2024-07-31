from turtle import Turtle

SPEED = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.teleport(self.position[0], self.position[1])
        self.shapesize(stretch_wid=5, stretch_len=1)

    def goUp(self):
        self.goto(self.xcor(), self.ycor() + SPEED)

    def goDown(self):
        self.goto(self.xcor(), self.ycor() - SPEED)
