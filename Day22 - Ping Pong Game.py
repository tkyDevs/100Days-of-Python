from turtle import Turtle, Screen
from Day22_paddle import Paddle
from Day22_ball import Ball
from Day22_scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

rightPaddle = Paddle((350, 0))
rightScore = Scoreboard((320, 260))
screen.onkey(key="Up", fun=rightPaddle.goUp)
screen.onkey(key="Down", fun=rightPaddle.goDown)

leftPaddle = Paddle(position=(-350, 0))
leftScore = Scoreboard((-320, 260))
screen.onkey(key="w", fun=leftPaddle.goUp)
screen.onkey(key="s", fun=leftPaddle.goDown)
ball = Ball()

gameOver = False
while not gameOver:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Collision with paddle
    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
        ball.bounceX()

    # Collision with goal
    if ball.xcor() < -385:
        rightScore.pointUp()
        ball.resetPosition()
    elif ball.xcor() > 385:
        leftScore.pointUp()
        ball.resetPosition()

    # Detect game over
    if rightScore.score == 5:
        gameOver = True
        rightScore.winner("rightPaddle")
    elif leftScore.score == 5:
        gameOver = True
        leftScore.winner("leftPaddle")

screen.exitonclick()
