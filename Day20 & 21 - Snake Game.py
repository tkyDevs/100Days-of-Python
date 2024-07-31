from turtle import Screen
from Day20_snake import Snake
from Day20_food import Food
from Day20_scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game Loop ------------------------------------------------------------------
gameOver = False
while not gameOver:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food.
    if snake.segments[0].distance(food) < 15:
        scoreboard.pointUp()
        snake.grow()
        food.reappear()

    # collision with border.
    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280 or snake.segments[0].xcor() < -280:
        gameOver = True
        scoreboard.gameOver()

    # collision with tail.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            gameOver = True
            scoreboard.gameOver()

screen.exitonclick()

# Inheritance: A class gets the same attributes and methods from another class and a few of its own.
# How to inherit a class:
# class subClass(parentClass):
#   def __init__(self):
#       super().__init__()

# Now the class "subClass" will inherit everything from the "parentClass".
