#1. Move the turtle with keypress
#2. Create and move the cars
#3. Detect collision with car
#4. Detect when turtle reaches the other side
#5. Create a scoreboard



import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #detect collision with wall
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.speed_up()
        scoreboard.point()

screen.exitonclick()