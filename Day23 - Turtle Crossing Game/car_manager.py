from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.carList = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        newCar = Turtle()
        newCar.penup()
        newCar.shape("square")
        newCar.shapesize(stretch_wid=1, stretch_len=2)
        newCar.color(random.choice(COLORS))
        newCar.teleport(320, random.randrange(-250, 250))
        self.carList.append(newCar)

    def moveCars(self):
        for car in self.carList:
            car.forward(-self.carSpeed)

    def nextLevel(self):
        self.carSpeed += MOVE_INCREMENT

    def clearCars(self):
        for car in self.carList:
            car.hideturtle()
            car.clear()
        self.carList.clear()
