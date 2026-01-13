from turtle import Turtle, Screen

t = Turtle()

# draw dashed line
for _ in range(50):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

screen = Screen()
screen.exitonclick()