# hangman.py
# Hangman Game

import random

# create a list to use as the word bank for the game
word_bank = ["apple", "horror", "illusion", "obstacle", "conclusion"]

# randomly selects word from word bank
word_to_guess = random.choice(word_bank)