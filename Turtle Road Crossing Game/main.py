import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()


screen.listen()
screen.onkey(fun=player.move, key="Up")

game_end = False
while not game_end:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_end = True

    # Detect successful crossing
    if player.ycor() > 280:
        player.reset()
        car_manager.level_up()
        score.level_up()

screen.exitonclick()
