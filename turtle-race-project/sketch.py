from turtle import Screen, Turtle

my_turtle = Turtle()
my_screen = Screen()


def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def clear_screen():
    my_turtle.reset()

def move_right():
    my_turtle.right(10)

def move_left():
    my_turtle.left(10)


my_screen.listen()
my_screen.onkey(move_forward, "f")
my_screen.onkey(move_backward, "b")
my_screen.onkey(move_right, "r")
my_screen.onkey(move_left, "l")
my_screen.onkey(clear_screen, "c")

my_screen.exitonclick()
