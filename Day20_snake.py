from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.createSnake()
        self.screen.onkey(key="a", fun=self.turnLeft)
        self.screen.onkey(key="w", fun=self.turnUp)
        self.screen.onkey(key="s", fun=self.turnDown)
        self.screen.onkey(key="d", fun=self.turnRight)

    def createSnake(self):
        for pos in STARTING_POSITIONS:
            self.addSegment(pos)

    def turnLeft(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turnRight(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turnUp(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turnDown(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segment - 1].xcor()
            newY = self.segments[segment - 1].ycor()
            self.segments[segment].goto(newX, newY)
        self.segments[0].forward(SNAKE_SPEED)

    def addSegment(self, position):
        newSegment = Turtle(shape="square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def grow(self):
        self.addSegment(self.segments[-1].position())
