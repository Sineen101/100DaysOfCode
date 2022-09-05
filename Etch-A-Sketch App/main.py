from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


def forward():
    """This function moves the turtle forward by 10 pixels"""
    turtle.forward(10)


def backward():
    """This function moves the turtle backward by 10 pixels"""
    turtle.backward(10)


def clockwise():
    """This function turns the turtle clockwise by 10 degrees"""
    turtle.right(10)


def counter_clockwise():
    """This function turns the turtle counter clockwise by 10 degrees"""
    turtle.left(10)


def clear():
    """This function clears the screen and resets the turtle to the center"""
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()  # Listen for key presses
# When the user presses the "w" key, the forward function is called
screen.onkey(key="w", fun=forward)
# When the user presses the "s" key, the turtle moves backward
screen.onkey(key="s", fun=backward)
# When the user presses the "a" key, the turtle turns counter clockwise
screen.onkey(key="a", fun=counter_clockwise)
# When the user presses the "d" key, the turtle turns clockwise
screen.onkey(key="d", fun=clockwise)
# When the user presses the "c" key, the screen is cleared and the turtle is reset to the center
screen.onkey(key="c", fun=clear)


screen.exitonclick()    # When the user clicks on the screen, the program exits
