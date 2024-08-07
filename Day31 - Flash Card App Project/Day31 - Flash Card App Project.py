from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
WORD = ""

# WINDOW/CANVAS SETTINGS ----------------------------------------------------------
window = Tk()
window.title("Flash Card App Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
imageFront = PhotoImage(file="images/card_front.png")
imageBack = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
image_id = canvas.create_image(400, 263, image=imageFront)
canvas.grid(columnspan=2)

# LOGIC ---------------------------------------------------------------------------
data = pandas.read_csv("data/french_words.csv")
myDict = data.to_dict(orient="records")
print(myDict)


def knowWord():
    global WORD, myDict
    if len(WORD) != 0:
        if 'French' in WORD:
            word_to_remove = WORD['French']
            # Remove the entire dictionary where the 'French' key matches
            myDict = [word for word in myDict if word['French'] != word_to_remove]
            print(f"Number of words after removal: {len(myDict)}")
            pickRandomWord()
        else:
            print(f"{WORD} does not have a 'French' key")
    else:
        pickRandomWord()


def doNotKnowWord():
    global WORD, myDict
    if len(WORD) != 0:
        with open("data/wordsToLearn.csv", "a+") as file:
            file.write(f"{WORD}\n")
            file.seek(0)
            lines = file.readlines()
            print(f"# of words to learn later: {len(lines)}")
        pickRandomWord()
    else:
        pickRandomWord()


def pickRandomWord():
    global WORD, timer
    window.after_cancel(timer)
    canvas.itemconfig(image_id, image=imageFront)
    canvas.itemconfig(languageLabel, text="French")
    WORD = random.choice(myDict)
    canvas.itemconfig(wordLabel, text=WORD['French'])
    timer = window.after(3000, flip)


def flip():
    global WORD
    canvas.itemconfig(image_id, image=imageBack)
    canvas.itemconfig(languageLabel, text="English")
    canvas.itemconfig(wordLabel, text=WORD['English'])


timer = window.after(3000, flip)
# CARD ----------------------------------------------------------------------------
languageLabel = canvas.create_text(400, 140, text="French", font=("Ariel", 40, "italic"))
wordLabel = canvas.create_text(400, 263, text=WORD, font=("Ariel", 60, "bold"))

# BUTTONS -------------------------------------------------------------------------
wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongImage, highlightthickness=0, command=doNotKnowWord)
wrongButton.grid(row=1, column=0)
rightImage = PhotoImage(file="images/right.png")
rightButton = Button(image=rightImage, highlightthickness=0, command=knowWord)
rightButton.grid(row=1, column=1)

window.mainloop()
