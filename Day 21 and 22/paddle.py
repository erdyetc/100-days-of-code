from turtle import Turtle
#PADDLES
# USING THE SAME METHOD AS SNAKE
# MY_START_POSITIONS = [(350,0),(350,20),(350,40),(350,-20),(350,-40)]

# class Paddle(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.paddle = []
#         self.create_paddle(MY_START_POSITIONS)

#     def create_paddle(self, positions):
#         for coor in positions:
#             new = Turtle()
#             self.paddle.append(new)
#             new.penup()
#             new.goto(coor)
#             new.shape("square")
#             new.color("white")
#             new.shapesize(1,1)
        
#     def move_paddle_up(self):
#         for block in self.paddle:
#             block.setheading(90)
#             block.forward(20)
    
#     def move_paddle_down(self):
#         for block in self.paddle:
#             block.setheading(270)
#             block.forward(20)

# USING STRETCH
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 5,stretch_wid = 1)
        self.penup()
        self.goto(position)
        self.setheading(90)
    
    def move_paddle_up(self):
        self.setheading(90)
        self.forward(20)
    
    def move_paddle_down(self):
        self.setheading(270)
        self.forward(20)