from turtle import Turtle, Screen
import random


def draw_shape(sides: str) -> None:
    """Draws a shape with the given number of sides"""
    angle = 360/sides   # Calculate the angle of the shape
    for _ in range(sides):  # Draw the shape
        timmy.forward(100)
        timmy.left(angle)


timmy = Turtle()  # object declaration
screen = Screen()


timmy.shape("turtle")  # changing the shape to turtle
timmy.color("PeachPuff")  # changing the color of the turtle
for _ in range(4):  # creating a square
    timmy.right(90)  # changing the direction of the turtle
    timmy.forward(100)  # moving the turtle forward
screen.clear()  # clearing the screen


timmy.shape("turtle")
timmy.pencolor("PaleGreen3")
for _ in range(15):  # creating a dotted line
    timmy.forward(10)
    timmy.penup()  # lifting the pen up from the screen
    timmy.forward(10)
    timmy.pendown()  # putting the pen down on screen
screen.clear()


colors = ["MediumPurple3", "tan2", "tomato1", "SkyBlue1", "plum",
          "PeachPuff2", "orange1", "LightSalmon2", "DarkSeaGreen3", "coral1"]
timmy.shape("turtle")
for shape_side in range(3, 10):  # creating a geometric shape
    # changing the color of the turtle to a random color from the list
    timmy.color(random.choices(colors))
    # changing the size of the pen to the number of sides of each shape
    timmy.pensize(shape_side)
    draw_shape(shape_side)  # calling the function to draw the shape


screen.exitonclick()
