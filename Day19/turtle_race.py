import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for num in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colours[num])
    t.penup()
    t.goto(x = -230, y = y_position[num])
    all_turtle.append(t)

if user_bet:
    is_race_on = True
while is_race_on:
    for t in all_turtle:
        if t.xcor() > 230:
            is_race_on = False
            winning_colour = t.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)
screen.exitonclick()