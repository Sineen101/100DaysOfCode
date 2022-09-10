from time import sleep
from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open(".\high_score.txt", "r") as file:
            self.high_scores = int(file.read())
        self.color("Yellow")
        self.penup()
        self.goto(x=0, y=290)
        self.hideturtle()
        self.update()

    def increment(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score}          High Score: {self.high_scores}", move=False, align='center', font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_scores:
            with open(".\high_score.txt", "w") as file:
                file.write(str(self.score))
                self.high_scores = self.score
        self.score = 0
        self.update()
