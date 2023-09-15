from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

#SCREENLINE
screen.tracer(0)
turtle = Turtle()
turtle.hideturtle()
turtle.pencolor("white")
turtle.penup()
turtle.goto(0,580)
turtle.pendown()
turtle.setheading(270)

while not turtle.ycor() == -300:
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen.update()

STARTING_POSITIONS = [(350,0),(-350,0)]
my_paddle = Paddle(STARTING_POSITIONS[0])
computer_paddle = Paddle(STARTING_POSITIONS[1])

WINNING_SCORE = 5

ball = Ball()
game_is_on = True
winner = ""
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun=my_paddle.move_paddle_up)
screen.onkey(key = "Down", fun=my_paddle.move_paddle_down)
screen.onkey(key = "w", fun=computer_paddle.move_paddle_up)
screen.onkey(key = "s", fun=computer_paddle.move_paddle_down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #Bounce on paddle
    if ball.distance(my_paddle) < 50 and ball.xcor() >= 330 or ball.distance(computer_paddle) < 50 and ball.xcor() <= -330:
       ball.bounce_paddle()
       ball.move()
    #Bounce on top and bottom walls
    elif ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce()
       ball.move()
    #Point
    elif ball.xcor() > 380:
       scoreboard.computer_point()
       ball.reset_position()
    elif ball.xcor() < -380:
       scoreboard.my_point()
       ball.reset_position()
    #Game over
    elif scoreboard.computer_score == WINNING_SCORE or scoreboard.my_score == WINNING_SCORE:
       if scoreboard.computer_score == WINNING_SCORE:
          winner = "Player A"
       elif scoreboard.my_score == WINNING_SCORE:
          winner = "Player B"
       turtle.clear()
       scoreboard.game_over(winner)
       game_is_on = False
    else:
       ball.move()

screen.exitonclick()