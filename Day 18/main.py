from turtle import Turtle, Screen
#* is everything, can use but bad practice because can't see which class the method comes from
#usually is you use 3+ items can use from turtle import X
#otherwise it is best practice to just import the whole module

import turtle as t 
#Alias name for the module

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()

#Turtle Graphics Documentation: https://docs.python.org/3/library/turtle.html

# Challenge 2:
#  for i in range(15):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

#Challenge 3:
# import random
# screen.colormode(255)
# sides = 3
# while sides < 10: 
#      r = random.randint(0,255)
#      g = random.randint(0,255)
#      b = random.randint(0,255)
#      turtle.pencolor(r,g,b)
#      for _ in range(sides):
#         turtle.forward(100)
#         turtle.right(360/sides)
#      sides += 1

#Challenge 3: Angela's solution
# def draw_shape(sides):
#     for _ in range(sides):
#         turtle.forward(100)
#         turtle.right(360/sides)

# for shape_side_n in range (3,11):
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     turtle.pencolor(r,g,b)
#     draw_shape(shape_side_n)

#Challenge 4: Random Walk
# import random

# screen.colormode(255)
# turtle.pensize(10)
# turtle.speed(10)

# def random_walk():
#     directions = [0,90,180,270]
#     direction = random.choice(directions)
#     turtle.setheading(direction)
#     turtle.forward(30)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color

# for i in range(0,100):
#     turtle.pencolor(random_color())
#     random_walk()

#Challenge 5: Spirograph
import random
turtle.speed("fastest")
screen.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen.exitonclick()