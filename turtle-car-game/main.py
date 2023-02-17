import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(turtle.move_up, "Up")
game_is_on = True

car_manager = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect if turtle has reached the top
    if turtle.check_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()