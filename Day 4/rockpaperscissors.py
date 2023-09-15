#images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#game logic
#user move
options = [rock, paper, scissors]
user_move = int(input("Welcome to Rock, Paper, Scissors! What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
user_move_name = options[user_move]
print(user_move_name)

#computer move
import random
computer_move = random.choice(options)
print(f"Computer chose:\n{computer_move}")

#determine who wins
"""if user_move_name == rock:
    if computer_move == rock:
        print("It is a tie")
    elif computer_move == scissors:
        print("You win")
    else:
        print("You lose")

if user_move_name == scissors:
    if computer_move == scissors:
        print("It is a tie")
    elif computer_move == paper:
        print("You win")
    else:
        print("You lose")

if user_move_name == paper:
    if computer_move == paper:
        print("It is a tie")
    elif computer_move == rock:
        print("You win")
    else:
        print("You lose")"""

if user_move_name == rock and computer_move == scissors:
    print("You win")
elif user_move_name == rock and computer_move == paper:
    print("You lose")
elif user_move_name == scissors and computer_move == rock:
    print("You lose")
elif user_move_name == scissors and computer_move == paper:
    print("You win")
elif user_move_name == paper and computer_move == scissors:
    print("You lose")
elif user_move_name == paper and computer_move == rock:
    print("You win")
else:
    print("It is a tie")