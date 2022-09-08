from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("Coral")
        self.penup()
        self.goto(x=0, y=290)
        self.hideturtle()
        self.write(
            f"Score: {self.score} ", move=False, align='center', font=('Courier', 15, 'normal'))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score} ", move=False, align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.color("Yellow")
        self.goto(x=0, y=0)
        self.write(
            "GAME OVER!", move=False, align='center', font=('Courier', 40, 'bold'))

