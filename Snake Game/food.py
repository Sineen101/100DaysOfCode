from turtle import Turtle
import random


class Food(Turtle):     # Inherit from Turtle class(superclass)

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x, y=rand_y)
