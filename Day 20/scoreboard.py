from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = ALIGNMENT, font = FONT)

# Removing for Day 24 activity to include high score
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move = False, align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()