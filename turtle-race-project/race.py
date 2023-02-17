from turtle import Screen, Turtle
import random

my_screen = Screen()
start_race = False
my_screen.setup(500, 400)
user_bet = my_screen.textinput("Make your bet", "Which turtle might win the race? Enter a colour:")
print("Your bet: "+user_bet)

colours = ["red", "orange", "black", "blue", "green", "purple"]
y_coords = [-70, -40, -10, 20, 50, 80]
my_turtles = []

for colour in colours:
    my_turtle = Turtle("turtle")
    my_turtle.penup()
    my_turtle.color(colour)
    my_turtle.goto(-230, y_coords[colours.index(colour)])
    my_turtles.append(my_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            start_race = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winning_turtle == user_bet:
    print("Congrats! You won!")
else:
    print("Oops! You lost!" + winning_turtle + " won the race!")


my_screen.exitonclick()
