from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape()
        self.penup()
        self.color("white")
        self.my_score = 0
        self.computer_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"Player A: {self.computer_score}", move = False, align = ALIGNMENT, font = FONT)
        self.goto(100,250)
        self.write(f"Player B: {self.my_score}", move = False, align = ALIGNMENT, font = FONT)
        
    def computer_point(self):
        self.computer_score += 1
        self.score_update()

    def my_point(self):
        self.my_score += 1
        self.score_update()

    def game_over(self,winning_player):
        self.goto(0,0)
        self.write(f"Game Over\n{winning_player} wins!", move = False, align = ALIGNMENT, font = FONT)