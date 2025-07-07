import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_art
import hangman_words

lives = 6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#from hangman_words import logo

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

# TODO-2:
# If guess is not a letter in the chosen_word, Then reduce lives by 1.
# If lives goes down to 0 then the game should end, and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")
else:
    print("You win.")

#Phrase to display on screen when the letter has not been guessed:
    #print(f'You guessed {letter}, that\'s not in the word. You lose a life')