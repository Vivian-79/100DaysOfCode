from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
def move_backward():
    t.setheading(270)
    t.forward(50)
def move_forward():
    t.setheading(90)
    t.forward(50)
def turn_left():
    t.setheading(180)
    t.forward(50)
def turn_right():
    t.setheading(0)
    t.forward(50)
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()