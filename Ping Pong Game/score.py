from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pad1_score = 0
        self.pad2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.pad1_score, align="center",
                   font=("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.pad2_score, align="center",
                   font=("Courier", 80, "bold"))

    def user1_score(self):
        self.pad1_score += 1
        self.update()

    def user2_score(self):
        self.pad2_score += 1
        self.update()
