import blackjack_art
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def new_game():
    your_cards = []
    your_current_score = 0
    computer_cards = []
    computer_current_score = 0
    game_over = False
    
    start_game = False
    start_first_game = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if start_first_game == "y":
        start_game = True
        os.system("clear")
        print(blackjack_art.logo)
        continue_drawing_cards = True

    while start_game:
        def game_outcome(your_final_score, computer_final_score):
            print(f"Your final hand: {your_cards}, final score: {your_final_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_final_score}")
            if your_final_score > 21:
                print("You went over. You lose.")
            elif your_final_score <= 21 and computer_final_score <= 21:
                if your_final_score > computer_final_score:
                    print("You win!")
                elif your_final_score == computer_final_score:
                    print("You draw.")
                elif your_final_score < computer_final_score:
                    print("You lose.")
            elif your_final_score <= 21 and computer_final_score > 21:
                print("Computer went over. You win!")

        #Computer's cards
        while computer_current_score < 17:
            computer_new_card = random.choice(cards)
            computer_cards.append(computer_new_card)
            computer_current_score = sum(computer_cards)

        #Your cards
        your_new_card = random.choice(cards)
        your_cards.append(your_new_card)
        your_current_score = sum(your_cards)

        while continue_drawing_cards:
            your_new_card = random.choice(cards)
            your_cards.append(your_new_card)
            your_current_score = sum(your_cards)

            if 11 in your_cards:
                if your_current_score > 21:
                    index = your_cards.index(11)
                    your_cards[index] = 1
                    your_current_score = sum(your_cards)
                    
            #If you go over 21
            if your_current_score > 21:
                continue_drawing_cards = False
                game_outcome(your_current_score, computer_current_score)
                game_over = True
            #If your score not over 21
            else:
                print(f"Your cards: {your_cards}, current score: {your_current_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                draw = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw == "n":
                    continue_drawing_cards = False
                    game_outcome(your_current_score, computer_current_score)
                    game_over = True
        
        if game_over == True:
            play_again = input("Do you want to play again? Type 'y' or 'n': ")
            if play_again == "n":
                start_game = False
            else:
                os.system("clear")
                print(blackjack_art.logo)
                your_cards = []
                your_current_score = 0
                computer_cards = []
                computer_current_score = 0
                game_over = False
                continue_drawing_cards = True
new_game()