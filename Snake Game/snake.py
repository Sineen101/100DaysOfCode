from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
DIRECTIONS = {"UP": 90, "DOWN": 270, "LEFT": 180, "RIGHT": 0}


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle in POSITIONS:
            self.add_segment(turtle)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # range(start, stop, step)
        for snake_part in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[snake_part-1].xcor()
            new_y = self.segments[snake_part-1].ycor()
            self.segments[snake_part].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])

    def recenter(self):
        x_pos = self.head.xcor()
        x_neg = self.head.xcor()*-1
        y_pos = self.head.ycor()
        y_neg = self.head.ycor()*-1
        if x_pos > 300 or x_pos < -300:
            self.head.goto(x_neg, y_pos)
        elif y_pos > 300 or y_pos < -300:
            self.head.goto(x_pos, y_neg)
