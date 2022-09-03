import turtle
from random import choice, randint


def random_colors():    # random color function
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tup = (r, g, b)
    return color_tup


def random_walk():  # random walk function
    t.color(random_colors())
    t.forward(randint(0, 100))
    t.setheading(choice(directions))


t = turtle.Turtle()
s = turtle.Screen()

directions = [0, 90, 180, 270]

t.shape("turtle")
t.pensize(20)   # changing the size of the pen
t.speed("fastest")  # changing the speed of the turtle
turtle.colormode(255)  # changing the color mode to RGB

while True:
    random_walk()   # calling the function
