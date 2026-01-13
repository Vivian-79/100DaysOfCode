from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
#Extract colours from an image
# import colorgram
#
# colours = colorgram.extract('hirst_dots.jpg', 30)
# rgb = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colours = (r, g, b)
#     rgb.append(new_colours)
# print(rgb)
colour_list = [(225, 232, 226), (199, 158, 92), (63, 87, 125), (137, 90, 51), (218, 205, 120), (133, 170, 194), (145, 53, 83), (124, 36, 49), (46, 53, 101), (139, 185, 144), (77, 26, 44), (41, 42, 60), (175, 99, 110), (148, 170, 66), (179, 142, 171), (56, 40, 32), (183, 87, 77), (104, 154, 97), (94, 124, 176), (77, 72, 48), (77, 128, 126), (170, 206, 156), (50, 71, 74), (176, 189, 213), (213, 178, 188), (97, 145, 152), (168, 200, 212)]

t = Turtle()
t.hideturtle()  # hide the cursor
t.penup()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):                           # not strictly needed for .dot(), but good habit
    t.dot(20, random.choice(colour_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)#up
        t.forward(50)
        t.setheading(180)#left
        t.forward(500)
        t.setheading(0)#right

screen.exitonclick()