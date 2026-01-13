from turtle import Turtle, Screen
import random
t = Turtle()
colours = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "brown", "gray", "black",
    "white", "cyan", "magenta", "lime", "maroon",
    "navy", "olive", "teal", "coral", "gold"
]
# draw angles
# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# # draw a square
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# # draw a pentagon
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# # draw a hexagon
# for _ in range(6):
#     t.forward(100)
#     t.left(60)
#
# # draw a heptagon
# for _ in range(7):
#     t.forward(100)
#     t.left(360 / 7)
#
# # draw a octagon
# for _ in range(8):
#     t.forward(100)
#     t.left(360 / 8)
#
# # draw a nonagon
# for _ in range(9):
#     t.forward(100)
#     t.left(360 / 9)
#
# # draw a decagon
# for _ in range(10):
#     t.forward(100)
#     t.left(360 / 10)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    t.color(random.choice(colours))
screen = Screen()
screen.exitonclick()