logo = """

███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████   █████  ███    ███ ███████ 
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██   ██ ████  ████ ██      
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ███████ ██ ████ ██ █████   
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██   ██ ██  ██  ██ ██      
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████  ██   ██ ██      ██ ███████ 
                                                                                                                                                                          
"""
import random
num_list = []
for num in range(1,101):
    num_list.append(num)

answer = random.choice(num_list)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
#print(f"Psst, the correct answer is {answer}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5

print(f"You have {guesses} attempts remaining to guess the number")
continue_game = True

while continue_game:
    guess = int(input("Make a guess: "))
    guesses -= 1
    if guesses == 0:
        continue_game = False
        print(f"You lose. The number was {answer}.")
    elif answer == guess:
        print(f"You got it! The number was {answer}.")
        continue_game = False
    elif answer > guess:
        print(f"Too low.\nGuess again.\nYou have {guesses} attempts remaining to guess the number")
    elif answer < guess:
        print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number")
