from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: tuple, paddle_color: str):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=position[0], y=position[1])

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)
