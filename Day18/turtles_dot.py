from turtle import Screen, Turtle

screen = Screen()
screen.setup(400, 400)

t = Turtle()
t.penup()           # don’t draw lines
t.goto(0, 0)        # centre of the window
t.dot(50, "blue")   # a 50px blue dot
screen.exitonclick()