import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")
imageShape = "blank_states_img.gif"
screen.addshape(imageShape)
turtle.shape(imageShape)
turtle.penup()

CORRECT_LIST = []


gameOn = True
stateTurtle = turtle.Turtle()
scoreTurtle = turtle.Turtle()
while len(CORRECT_LIST) < 50:
    userAnswer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if userAnswer in data["state"].tolist():
        CORRECT_LIST.append(userAnswer)
        stateTurtle.penup()
        stateTurtle.hideturtle()
        location = data[data["state"] == userAnswer]
        stateTurtle.teleport(location.iloc[0]['x'], location.iloc[0]['y'])
        stateTurtle.write(f"{userAnswer}", False, align='left', font=("Arial", 8, "normal"))

        scoreTurtle.clear()
        scoreTurtle.penup()
        scoreTurtle.hideturtle()
        scoreTurtle.goto(-240, 220)
        scoreTurtle.write(f"Score: {len(CORRECT_LIST)}", False, align="left", font=("Arial", 16, "normal"))

    if userAnswer == "Exit":
        break

result = {
    "states": []
}
for i in data["state"].tolist():
    if i not in CORRECT_LIST:
        result["states"].append(i)
pandas.DataFrame(result).to_csv("Day25_results")

screen.exitonclick()
