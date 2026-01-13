from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed("fastest")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_colour())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
draw_spirograph(5)
screen = Screen()
screen.exitonclick()