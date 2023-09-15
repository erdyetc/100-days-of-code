from turtle import Turtle
import time
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")
        
    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        self.setheading(90)
        self.backward(MOVE_DISTANCE)
    
    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
    
    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    def get_speed(self):
        t_end = time.time() + 10
        while time.time() < t_end:
            self.speed("fastest")

class Power_Up(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.power_ups = []
    
    def generate_power_shape(self, position):
        new_power = Turtle()
        new_power.penup()
        new_power.shape("triangle")
        new_power.color("gold")
        new_power.goto(position)
        new_power.showturtle()
        self.power_ups.append(new_power)
    
    def generate_power_up(self):
        random_y = random.randint(-250,250)
        random_x = random.randint(-300,300)
        position = (random_x, random_y)
        self.generate_power_shape(position)