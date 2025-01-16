# hangman.py
# ICD2O Final Project - Hangman Game

import random

def play_hangman():
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
        print("Your word: " + " ".join(display_word))
        #for char in display_word:
          #  print(char, end = "")
       # print()
        print("You have " + str(attempts_remaining) + " attemps remaining.")
        print("Incorrect guesses: ", end = "")
        if wrong_guesses:
            # Loop thru the indices of the wrong_guesses list
            for i in range(len(wrong_guesses)):
                # Check if the current index is not the last index in the list
                if i < len(wrong_guesses) - 1:
                    # Prints current wrong guess followed by a comma
                    # Uses end to avoid moving to a new line after printing
                    print(wrong_guesses[i] + ", ", end = "")
                else:
                    # If it's the last index then it prints without a comma after
                    print(wrong_guesses[i], end="")
    
        # Ask user to guess a letter
        print() # Move to next line for input prompt
        guess = input("Enter your guess: ").lower()
        
        # Validates input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            print()
            continue
        if guess in guessed_letters or guess in wrong_guesses:
            print("You have already guessed ''" + guess + "' Try a different letter.")
            print()
            continue
        print()
    
        # Add guess to guessed letters list
        guessed_letters.append(guess)
    
        # Check if the guess is in the word
        if guess in word_to_guess:
            print("Good guess! '" + guess + "' is in the word.")
            # Reveal the letter in its correct position(s)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
                    
        else:
            print("Sorry, '" + guess + "' is not in the word.")
            # Add to wrong_guesses and subtract an attempt
            wrong_guesses.append(guess)
            attempts_remaining -= 1
    
    # Stage 4: end of game win / lose conditions
    if "_" not in display_word:
        print("Congrats! You guessed the word: '" + word_to_guess + "', with " + str(attempts_remaining) + " attempts remaining!")
    else:
        print("Game over! The word was: " + word_to_guess)
    
    # Ask if user wants to play again
    play_again = input("Play again? (Y/N): ").lower()
    
    if play_again == "y":
        play_hangman()
    elif play_again == "n":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid input. Exiting the game.")

# Starts the game
play_hangman()