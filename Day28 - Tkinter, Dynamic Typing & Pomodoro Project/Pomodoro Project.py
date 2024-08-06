from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    window.after_cancel(timer)
    titleLabel.config(text="Pomodoro")
    canvas.itemconfig(timerText, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    if reps == 7:
        titleLabel.config(text="Break", bg=RED)
        countDown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        titleLabel.config(text="Break", bg=PINK)
        countDown(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 0:
        titleLabel.config(text="Work", bg=GREEN)
        countDown(WORK_MIN * 60)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countSec = count % 60
    if countSec < 10:
        countSec = "0" + str(countSec)
    countMin = f"{count//60}:{countSec}"
    canvas.itemconfig(timerText, text=countMin)
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=100, bg=YELLOW, highlightcolor=YELLOW)

titleLabel = Label(text="Pomodoro", font=("Arial", 24, "normal"), bg=YELLOW, fg=RED)
titleLabel.grid(column=1, row=0)

# Canvas is a Tkinter class used to integrate images in GUIs.
canvas = Canvas(width=200, height=224, bg=YELLOW)
bgImage = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=bgImage)
canvas.grid(column=1, row=1)
timerText = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

startTimer = Button(text="Start", command=startTimer)
startTimer.grid(column=0, row=2)

resetTimer = Button(text="Reset", command=resetTimer)
resetTimer.grid(column=2, row=2)

mainloop()
