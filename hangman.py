# hangman.py
# Hangman Game

import random

# create a list to use as the word bank for the game
word_bank = ["apple", "horror", "illusion", "obstacle", "conclusion"]

# randomly selects word from word bank
word_to_guess = random.choice(word_bank)

# displays word as a string of blanks
display_word = ""
for _ in word_to_guess:
    display_word += "_ "

# displays the blanks
print("Word to guess:", display_word)