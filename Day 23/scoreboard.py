from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.color("black")
        self.level = 0
        self.level_update()

    def level_update(self):
        self.level += 1
        self.clear()
        self.goto(-250,250)
        self.write(f"Level: {self.level}", move = False, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move = False, font = FONT, align = "center")