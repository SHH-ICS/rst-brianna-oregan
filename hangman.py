# hangman.py
# ICD2O Final Project - Hangman Game

import random

# Stage 1: setup for the game
# Word bank for the game
word_bank = ["apple", "horror", "illusion", "vehicle", "obstacle", "conclusion"]

# Randomly select a word from the word bank
word_to_guess = random.choice(word_bank)

# List of blanks to represent the word
display_word = ["_"] * len(word_to_guess)

# List to track guessed letters
guessed_letters = []
wrong_guesses = []

#Set the # of attempts
attempts_remaining = 6

# Welcome message
print("Welcome to Hangman! :)")

# Stages 2: user input
# Game loop
while attempts_remaining > 0 and "_" in display_word:
    # Stage 3: game logic
    # DIsplay the current state of the word + game info
    print("Your word: ", end = "")
    for char in display_word:
        print(char, end = "")
    print()
    print("You have " + str(attempts_remaining) + " attemps remaining.")
    print("Incorrect guesses: ", end = "")
    # Loop thru the indices of the wrong_guesses list
    for i in range(len(wrong_guesses)):
        # Check if the current index is not the last index in the list
        if i < len(wrong_guesses) - 1:
            # Prints current wrong guess followed by a comma
            # Uses end to avoid moving to a new line after printing
            print(wrong_guesses[i] + ", ", end = "")
        else:
            # If it's the last index then it prints without a comma after
            print(wrong_guesses[i])
    print() # new line

    # Ask user to guess a letter
    guess = input("Enter your guess: ").lower()
    
    # Validates input
    #
    