from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = Snake()
snake_food = Food()
my_score = ScoreBoard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    # detect food
    if my_snake.segments[0].distance(snake_food) < 15:
        my_score.current_score += 1
        my_score.write_score()
        my_snake.extend()
        snake_food.refresh()

    # detect collision with wall
    if my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280 or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].ycor() < -280:
        my_score.reset()
        my_score.write_score()
        my_snake.reset()

    # detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            my_score.reset()
            my_score.write_score()
            my_snake.reset()

my_screen.exitonclick()
