import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.onkey(key="w", fun=player.walk)

game_is_on = True
while game_is_on:
    if random.randint(1, 6) == 1:
        carManager.createCar()
    carManager.moveCars()

    # Collision with cars
    for car in carManager.carList:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameOver()

    # next level
    if player.ycor() > 280:
        carManager.clearCars()
        scoreboard.nextLevel()
        player.teleport(0, -280)
        carManager.nextLevel()

    time.sleep(0.1)
    screen.update()
screen.exitonclick()
