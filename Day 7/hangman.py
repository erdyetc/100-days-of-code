import os
from hangman_art import *
from hangman_words import *

#could also do import hangman_words and then use hangman_words.word_list

#Create word list and choose a random work
print(logo)
import random
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create word display
display = []
for letter in chosen_word:
    display.append("_")

#Play game
guesses = []
end_of_game = False
lives = 6
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    print(logo)
    #Check guessed letter
    if guess in guesses:
        print("\nYou have already guessed this letter.\n")
    else: 
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = guess
        if guess not in chosen_word:
            lives -= 1
            print(f"\nYou guessed the letter {guess}. That's not in the word. You lose a life. \n")
    guesses += guess
    print(f"{' '.join(display)}\n")
    print(stages[lives])
    print(f"You have guessed these letters: {' '.join(guesses)}")
    #Check if win
    if "_" not in display:
        end_of_game = True
        print("You win!")
    #Check if lose
    if lives == 0:
        end_of_game = True
        print(f"You lose. The correct word was {chosen_word}")