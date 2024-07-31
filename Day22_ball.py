from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moveSpeed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounceY(self):
        self.y_move *= -1

    def bounceX(self):
        self.x_move *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self):
        self.x_move *= -1
        self.moveSpeed = 0.1
        self.teleport(0, 0)
