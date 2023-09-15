from turtle import Turtle, Screen
import random 

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
screen.setup(width=500,height=400)

#User makes a bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

#Make all the racing turtles
for color_t in colors:
    new_turtle = Turtle()
    new_turtle.color(color_t)
    new_turtle.shape("turtle")
    turtle_list.append(new_turtle)

#Starting position of race
y_position = -60
for turtle in turtle_list:
    turtle.penup()
    turtle.goto(x=-230, y=y_position)
    y_position += 30

game_on = True
while game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            game_on = False
        else:
            distance = random.randint(0,10)
            turtle.forward(distance)

if winning_turtle == user_bet:
    print(f"You've won! The {winning_turtle} turtle won the race!")
else:
    print(f"You've lost! The {winning_turtle} turtle won the race.")

screen.exitonclick()