from turtle import Turtle, Screen
from random import randint
import turtle


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win?\nEnter a color:\n")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race = False
y_axis = -100
turtles_list = []


for color in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    turtles_list.append(new_turtle)
    y_axis += 40

if user_bet:
    race = True

while race:
    for turtle in turtles_list:
        if turtle.xcor() > 215:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You won!\nThe {winning_color} turtle is the winner of the race!")
            elif winning_color != user_bet:
                print(
                    f"You lost!\nThe {winning_color} turtle is the winner of the race!")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
