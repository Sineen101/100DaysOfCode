from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=700, height=700)  # Set the screen size
screen.bgcolor("black")        # Set the background color
screen.title("My Snake Game")   # Set the title of the game
screen.tracer(0)       # Turn off the screen updates


snake = Snake()
food = Food()
score = Score()

screen.listen()  # Listen for key presses
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_end = False
while not game_end:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Delay the screen updates

    snake.move()    # Move the snake

    if snake.head.distance(food) < 15:    # Snake head collision with the food
        score.increment()              # Increment the score
        food.refresh()  # Move the food to a random position
        snake.extend()  # Add a new segment to the snake

    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        snake.recenter()    # Snake head collision with the wall

    for part in snake.segments[1:]:
        # Snake head collision with its tail
        if snake.head.distance(part) < 10:
            score.reset()   # Reset the score
            snake.reset()   # Reset the snake


screen.exitonclick()
