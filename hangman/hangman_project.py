import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
#remove then:
print(chosen_word)

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
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3:
    # print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.
    print(stages[lives])
else:
    print("You win.")

#Phrase to display on screen when the letter has not been guessed:
    #print(f'You guessed {letter}, that\'s not in the word. You lose a life')