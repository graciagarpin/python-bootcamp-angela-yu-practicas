import random

import hangman_art
import hangman_words

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""

for letter in chosen_word:
    letter = "_ "
    placeholder += letter

print(f'Word to guess: {placeholder}')

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if letter not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(hangman_art.stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")
else:
    print("You win.")