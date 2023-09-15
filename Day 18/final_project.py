# import colorgram
# from PIL import Image
# image = Image.open("/Users/edwinaliu/Documents/Coding/100 Days of Coding/Day 18/image.jpg")
# colors = colorgram.extract(image,126)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

final_rgb_colors = [
    (232, 251, 242),
    (198, 13, 32),
    (250, 237, 19),
    (39, 76, 189),
    (39, 217, 68),
    (238, 227, 5),
    (229, 159, 47),
    (28, 40, 156),
    (214, 75, 13),
    (242, 246, 252),
    (16, 154, 16),
    (198, 15, 11),
    (243, 34, 165),
    (68, 10, 30),
    (228, 18, 120),
    (60, 15, 8),
    (223, 141, 209),
    (11, 97, 62),
    (221, 161, 9),
    (50, 212, 231),
    (18, 20, 47),
    (11, 227, 239),
    (238, 156, 217),
    (84, 74, 211),
    (78, 210, 163),
    (82, 234, 200),
    (61, 233, 241),
    (5, 68, 42),
    (216, 90, 52),
    (173, 178, 231),
    (235, 170, 164),
    (8, 244, 224),
    (248, 9, 44),
    (10, 77, 114),
    (20, 53, 243),
]

from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.speed("fastest")

def random_color():
    random_color = random.choice(final_rgb_colors)
    return random_color

def new_line():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.backward(500)
    turtle.pendown()

print(random_color())

dots = 0
while dots < 100:
    turtle.dot(20,random_color())
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    dots += 1
    if dots % 10 == 0:
        new_line()

screen.exitonclick()