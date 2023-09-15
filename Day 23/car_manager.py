from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.cars = []
        self.hideturtle()
        
    def generate_car(self, a_position):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1,2)
        new_car.goto(a_position)
        new_car.setheading(180)
        self.cars.append(new_car)

    def start_game(self):
        for i in range(10):
            random_x = random.randint(-300,300)
            random_y = random.randint(-250,250)
            position = (random_x, random_y)
            self.generate_car(position)
        self.move_cars()

    def game_continue(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            random_y = random.randint(-250,250)
            position = (300, random_y)
            self.generate_car(position)
            self.move_cars()

    def move_cars(self):
        for car_num in range(0,len(self.cars)):
            self.cars[car_num].forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level))

    def level_up_car(self):
        self.level += 1
