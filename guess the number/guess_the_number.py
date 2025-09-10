# TODO LIST
#  ✔ TODO 1: print: Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100
#  ✔ TODO : generate a random number between 1 and 100 and store in the variable "number". This will be the number to guess.
# TODO : print input: Choose a difficulty. Type 'easy' or 'hard':
# TODO  - LEVEL OF DIFFICULTY -: easy: You have 10 attemps remaining to guess the number. hard: You have 5 attemps remaining to guess the number.
# TODO : print input: Make a guess:
# TODO : Compare the guess with the number.
    # TODO .1: if the guess is higher than the number, print: Too high. n/Guess again. n/You have {lives} attemps remaining to guess the number.
    # TODO .2: if the guess is lower than the number, print: Too low. n/Guess again. n/You have {lives} attemps remaining to guess the number.
# TODO : after each failed attempt, you lose a life.
# TODO : You lose when you run out guesses. You win when you guess the number.
    # You've run out of guesses. Refresh the page to run again.
    # You got it! The answer was {number}
# TODO : print LOGO
# while you remain lives, you can play.

import random
from symbol import return_stmt

print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)

print(number)

lives = 0

def apply_difficulty_level(lives):
    level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    print(level_of_difficulty)

    if level_of_difficulty == "easy":
        return lives + 10
    elif level_of_difficulty == "hard":
        return lives + 5
    else:
        return "type again" #cambiar más adelante

lives = apply_difficulty_level(lives)
print(lives)