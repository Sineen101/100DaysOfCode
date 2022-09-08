from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(x=self.xcor()+self.x_move, y=self.ycor()+self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(x=0, y=0)
        self.ball_speed = 0.1
        self.x_bounce()
