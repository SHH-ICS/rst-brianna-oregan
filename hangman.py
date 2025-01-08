# hangman.py
# Hangman Game

import random

# create a list to use as the word bank for the game
word_bank = ["apple", "horror", "illusion", "vehicle", "obstacle", "conclusion"]

# randomly selects word from word bank
word_to_guess = random.choice(word_bank)

# displays word as a string of blanks
display_word = ""
for _ in word_to_guess:
    display_word += "_ "

print("Your word:", display_word)

# list to track guessed letters
guessed_letters = []
wrong_guesses = []

#Set the # of attempts
attempts_remaining = 6

# Game loop
while attempts_remaining > 0 and "_" in display_word:
    # Display the current state of the word & the game info
    print("Your word: " + )
    print()
    print()





#asks the user for a guess + validates it
while True:
    # prompts user to guess a letter
    guess = input("Enter your guess: ").lower()

    # validates input. if invalid it'll loop until a valid guess is entered
    if len(guess) != 1 or not guess.isalpha():
        print("Error: Guess must be a single letter.")
    elif guess in guessed_letters:
        print("You've already guessed " + str(guess) + ". Try a different letter.")
    else:
        #add guess to list of guessed letters
        guessed_letters = guessed_letters + [guess]
        break #exit the loop once a valid guess is entered
