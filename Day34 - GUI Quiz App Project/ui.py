import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = tkinter.Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tkinter.Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.questionText = self.canvas.create_text(150, 125, text="fasdfa", fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"),
                                                    width=280)
        self.canvas.grid(columnspan=2, row=1, pady=50)

        self.rightImage = tkinter.PhotoImage(file="images/true.png")
        self.rightAnswer = tkinter.Button(image=self.rightImage, highlightthickness=0, command=self.guessTrue)
        self.rightAnswer.grid(column=0, row=2)
        self.wrongImage = tkinter.PhotoImage(file="images/false.png")
        self.wrongAnswer = tkinter.Button(image=self.wrongImage, highlightthickness=0, command=self.guessFalse)
        self.wrongAnswer.grid(column=1, row=2)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        self.score.config(text=f"score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=qText)
        else:
            self.canvas.itemconfig(self.questionText, text="You have completed the quiz!")
            self.rightAnswer.config(state="disabled")
            self.wrongAnswer.config(state="disabled")

    def guessTrue(self):
        self.giveFeedback(self.quiz.check_answer("True"))

    def guessFalse(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self, isRight):
        if isRight:
            self.canvas.config(bg="green")
            self.window.after(1000, self.newQuestion)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.newQuestion)

    def newQuestion(self):
        self.canvas.config(bg="white")
        self.getNextQuestion()
