from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.pensize(15)
t.speed("fastest")

direction = [0, 90, 180, 270]
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for _ in range(200):
    t.forward(30)
    t.setheading(random.choice(direction))
    t.color(random_colour())


screen.exitonclick()