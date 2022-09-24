from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(
            text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Helvetica", 10, "bold"))
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some Question Text", width=280, font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.b1 = Button(text="True", highlightthickness=0,
                         padx=20, pady=20, bg="green", font=("Helvetica", 10, "bold"), command=self.true_pressed)
        self.b2 = Button(text="False", highlightthickness=0,
                         padx=20, pady=20, bg="red", font=("Helvetica", 10, "bold"), command=self.false_pressed)
        self.b1.grid(row=2, column=0)
        self.b2.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.questions_remaining():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached the end of the quiz.")
            self.b1.config(state="disabled")
            self.b2.config(state="disabled")

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
