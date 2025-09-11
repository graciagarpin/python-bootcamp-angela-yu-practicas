# TODO LIST
# ✔ TODO 1: print: Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100
# ✔ TODO 2: generate a random number between 1 and 100 and store in the variable "number". This will be the number to guess.
# ✔ TODO 3: Choose a difficulty. Type 'easy' or 'hard':
    # ✔ TODO - select the LEVEL OF DIFFICULTY -: easy: You have 10 attemps remaining to guess the number. hard: You have 5 attemps remaining to guess the number.
# TODO 4: Compare the guess with the number.
    # ✔ TODO 4.1: print input: Make a guess:
    # ✔  TODO 4.2: if the guess is higher than the number, print: Too high. n/Guess again. n/You have {lives} attemps remaining to guess the number.
    # ✔  TODO 4.3: if the guess is lower than the number, print: Too low. n/Guess again. n/You have {lives} attemps remaining to guess the number.
    # ✔ TODO : after each failed attempt, you lose a life.
# TODO 5 : While the number is not guessed, a new attempt will be requested, until all lives are lost.
# TODO : You lose when you run out guesses. You win when you guess the number.
    # You've run out of guesses. Refresh the page to run again.
    # You got it! The answer was {number}
# TODO : print LOGO
# while you remain lives, you can play.

import random

print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)

print(number)

def select_difficulty_level(lives):
    level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level_of_difficulty == "easy":
        print("You have 10 attemps remaining to guess the number.")
        return lives + 10
    elif level_of_difficulty == "hard":
        print("You have 5 attemps remaining to guess the number.")
        return lives + 5
    else:
        return "type again" #cambiar más adelante


def compare_the_guess(guess, number, lives):
    if guess > number:
        lives -= 1
        print(f"Too high.\nGuess again. \nYou have {lives} attemps remaining to guess the number.")
        return lives
    elif guess < number:
        lives -= 1
        print(f"Too low.\nGuess again. \nYou have {lives} attemps remaining to guess the number.")
        return lives
    else:
        print(f"You got it! The answer was {number}")
        return lives

lives = 0

lives = select_difficulty_level(lives)

guess = int(input("Make a guess: "))

lives = compare_the_guess(guess, number, lives)

print(lives)