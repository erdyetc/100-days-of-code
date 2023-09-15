import turtle
import time
import food
import scoreboard
file = open("my_file.txt")
contents = file.read()

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
difficulty = screen.textinput("Difficulty Level", "Set the level at 'easy', 'medium', or 'hard': ")

speed = 0 

if difficulty == "easy":
    speed = 0.13
elif difficulty == "medium":
    speed = 0.1
elif difficulty == "hard":
    speed = 0.06

START_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, speed):
        self.snakes = []
        self.speed = speed
        self.create_snake()
        self.head = self.snakes[0]

    def reset_snake(self):
        for segment in self.snakes:
            segment.goto(400,400)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in START_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new = turtle.Turtle()
        new.shape("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.snakes.append(new)
    
    def extend(self):
        self.add_segment(self.snakes[-1].position())
        #Count from end of list using -1
    
    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # def check_tail(self):
    #     for snake_num in range(1,len(self.snakes)-1):
    #         if self.head.position() == self.snakes[snake_num].position():
    #             return True

    def check_tail(self):
        for snake_num in self.snakes[1:]:
            if self.head.distance(snake_num) < 10:
                return True
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        self.snakes.clear()
        self.create_snake()

snake = Snake(speed)
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun=snake.move_up)
screen.onkey(key = "Down", fun=snake.move_down)
screen.onkey(key = "Right", fun=snake.move_right)
screen.onkey(key = "Left", fun=snake.move_left)

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.score_increase()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()
        # for original version with no high score:
        # scoreboard.game_over()
        # game_is_on = False

    #Detect collision with snake tail
    if snake.check_tail() == True:
        scoreboard.reset()
        snake.reset_snake()
        # for original version with no high score:
        # scoreboard.game_over()
        # game_is_on = False
    
"""OR: for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""

screen.exitonclick()