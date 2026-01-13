from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
def move_backward():
    t.forward(10)
def move_forward():
    t.backward(10)
def turn_left():#the cursor
    new_heading = t.heading() + 10
    t.setheading(new_heading)
def turn_right():#the cursor
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward, "s")
screen.onkey(move_backward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()