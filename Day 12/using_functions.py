logo = """

███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████   █████  ███    ███ ███████ 
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██   ██ ████  ████ ██      
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ███████ ██ ████ ██ █████   
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██   ██ ██  ██  ██ ██      
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████  ██   ██ ██      ██ ███████ 
                                                                                                                                                                          
"""
import random
EASY_GUESSES = 10
HARD_GUESSES = 5

num_list = []
for num in range(1,101):
    num_list.append(num)

answer = random.choice(num_list)

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_GUESSES
    elif difficulty == "hard":
        return HARD_GUESSES

def check_guess(guess, answer, guesses):
    if answer == guess:
        print(f"You got it! The number was {answer}.")
    elif answer > guess:
        print("Too low.")
        return guesses - 1
    elif answer < guess:
        print("Too high.")
        return guesses - 1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    #print(f"Psst, the correct answer is {answer}")

    guesses = set_difficulty()
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))
        guesses = check_guess(guess,answer,guesses)
        if guesses == 0:
            print(f"You lose. The number was {answer}.")
            return
        elif guess != answer: 
            print(f"Guess again.\nYou have {guesses} attempts remaining to guess the number")

game()