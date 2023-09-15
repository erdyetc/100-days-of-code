from turtle import Turtle

"""my original solution
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("blue")

    def ball_move(self):
        self.forward(30)
        # new_x = self.xcor()+ 10
        # new_y = self.ycor()+ 10
        # self.goto(new_x,new_y)

    def ball_bounce_right(self):
        self.right(90)
        self.ball_move()

    def ball_bounce_left(self):
        self.left(90)
        self.ball_move()
"""

#Angela's solution
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1 
    
    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_paddle()
        self.move()
        #Don't want to subtract because there is an error if speed <= 0
        self.move_speed *= 0.8
