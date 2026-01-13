from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highscore = 0
        self.goto(-230, 270)
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
    def point(self):
        self.score += 1
        self.level_up()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
