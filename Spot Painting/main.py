import colorgram
import turtle
from random import choice

colors = colorgram.extract("painting.jpg", 8)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# Incase colorgram doesn't work, use a list of each color rgb value tuples

t = turtle.Turtle()
s = turtle.Screen()

turtle.mode(255)
t.speed("faster")
t.penup()
t.hideturtle()
t.setheading(300)
t.forward(250)
t.setheading(0)
dots = 100
for dot_count in range(dots):
    t.dot(20, choice(rgb_colors))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
