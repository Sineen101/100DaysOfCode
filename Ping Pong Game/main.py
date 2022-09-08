from turtle import Screen
import turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


def line():
    for _ in range(10):
        center_line.penup()
        center_line.forward(20)
        center_line.pendown()
        center_line.forward(20)
    center_line.penup()
    center_line.goto(0, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("Black")
screen.tracer(0)


pad1_color = turtle.textinput("Player 1", "Enter the color of your pad:\n")
pad2_color = turtle.textinput("Player 2", "Enter the color of your pad:\n")
pad1 = Paddle((370, 0), pad1_color)
pad2 = Paddle((-370, 0), pad2_color)
ball = Ball()
score = Score()
center_line = turtle.Turtle()


center_line.color("white")
center_line.hideturtle()
center_line.left(90)
line()
center_line.right(180)
line()


screen.listen()
screen.onkey(fun=pad1.move_up, key="Up")
screen.onkey(fun=pad1.move_down, key="Down")
screen.onkey(fun=pad2.move_up, key="w")
screen.onkey(fun=pad2.move_down, key="s")


game_end = False
while not game_end:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(pad1) < 50 and ball.xcor() > 340 or ball.distance(pad2) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    # Detect collision with pad1
    if ball.xcor() > 400:
        score.user1_score()
        ball.reset()

    # Detect collision with pad2
    if ball.xcor() < -400:
        score.user2_score()
        ball.reset()


screen.exitonclick()
