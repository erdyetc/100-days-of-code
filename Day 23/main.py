import time
from turtle import Screen
from player import Player, Power_Up
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)

game_on = False
play = True
start_game = "y"

def new_game():
    global start_game
    screen.clearscreen()
    screen.tracer(0)

    level = Scoreboard()
    player = Player()
    car = CarManager()
    powerup = Power_Up()
 
    car.start_game()
    game_on = True
    screen.listen()
    screen.onkey(key= "Up",fun=player.move_up)
    screen.onkey(key= "Down",fun=player.move_down)
    screen.onkey(key= "Right",fun=player.move_right)
    screen.onkey(key= "Left",fun=player.move_left)

    while game_on == True:
        time.sleep(0.1)
        screen.update()
        car.move_cars()
        car.game_continue()

        #Level up
        if player.ycor() > 280:
            player.reset_position()
            level.level_update()
            car.level_up_car()
        
        #Power up
        random_chance_power = random.randint(1,20)
        if random_chance_power == 1:
            powerup.generate_power_up()

        for x in powerup.power_ups:
            if powerup.distance(player) < 15:
                player.get_speed()

        #Game over
        """Angela's solution
        for car in car.cars:
            if car.distance(player) < 20:
                game_is_on = False
        She looped through cars touching player, instead of player touching cars
        """
        for i in range(len(car.cars)):
            if player.distance(car.cars[i]) < 20:
                level.game_over()
                start_game = screen.textinput("Start Game", "Would you like to start a new game? Type 'y' or 'n': ").lower()
                game_on = False
            
while play == True:
    new_game()
    if start_game == "y":
        play = True
    else:
        play = False

screen.exitonclick()