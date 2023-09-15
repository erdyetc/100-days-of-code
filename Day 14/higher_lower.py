import higher_lower_art
import higher_lower_game_data
import random
import os

def play_game():
    is_correct = True
    current_score = 0
    A = random.choice(higher_lower_game_data.data)

    while is_correct:
        def generate_B(other_list):
            computer_choice = random.choice(higher_lower_game_data.data)
            while computer_choice == other_list:
                computer_choice = random.choice(higher_lower_game_data.data) 
            return computer_choice
        
        def print_score():
            if is_correct and current_score >= 1:
                print(f"You're right! Current score: {current_score}")

        A_name = A["name"]
        A_followers = A["follower_count"]
        A_description = A["description"]
        A_country = A["country"]
        
        B = generate_B(A)
        B_name = B["name"]
        B_followers = B["follower_count"]
        B_description = B["description"]
        B_country = B["country"]

        os.system("clear")
        print(higher_lower_art.logo)
        print_score()
        print(f"Compare A: {A_name}, a {A_description} from {A_country}")
        print(higher_lower_art.vs)
        print(f"Against B: {B_name}, a {B_description} from {B_country}")
        guess = input("Who has more followers? Type 'A' or B' ").upper()

        if guess == "A":
            if A_followers >= B_followers:
                current_score += 1
                generate_B(A)
            else:
                is_correct = False
        elif guess == "B":
            if B_followers >= A_followers:
                current_score += 1
                A = B
                generate_B(A)
            else:
                is_correct = False

    os.system("clear")
    print(higher_lower_art.logo)
    print(f"Sorry, that's wrong. Final score: {current_score}")
    
play = input("Do you want to play Higher/Lower? Input 'y' or 'n': ").lower()

while play == "y":
    play_game()
    play = input("Do you want to play Higher/Lower? Input 'y' or 'n': ").lower()