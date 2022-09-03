from turtle import Turtle, Screen
from random import randint
import turtle


def random_colors():    # random color function
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tup = (r, g, b)
    return color_tup


t = Turtle()
s = Screen()
turtle.colormode(255)   # changing the color mode to RGB
t.speed("fastest")  # changing the speed of the turtle
t.shape("classic")  # changing the shape of the turtle


def spirograph(gap_between_circles):
    """This function draws a spirograph with the given gap between the circles"""
    for _ in range(int(360 / gap_between_circles)):    # creating a spirograph
        t.pencolor(random_colors())
        t.circle(100)   # drawing a circle
        # changing the direction of the turtle
        t.setheading(t.heading() + gap_between_circles)


spirograph(2)   # calling the function
s.exitonclick()
