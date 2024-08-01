from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])
        self.shape("turtle")
        self.left(90)

    def walk(self):
        self.forward(MOVE_DISTANCE)
