from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.highScore = self.getHighScore()
        self.drawScoreBoard()


    def getHighScore(self):
        with open('data.txt') as file:
            return int(file.read())

    def drawScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", False, font=("Arial", 16, "normal"), align="center")

    def pointUp(self):
        self.clear()
        self.score += 1
        self.drawScoreBoard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.drawScoreBoard()

    # def gameOver(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"YOU LOST!\nYOUR SCORE WAS: {self.score}", font=("Arial", 28, "normal"), align="center")
