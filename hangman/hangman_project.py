import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#remove then:
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    letter = "_ "
    placeholder += letter

print(f'Word to guess: {placeholder}')

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_ "

print(display)

#Phrase to display on screen when the letter has not been guessed:
    #print(f'You guessed {letter}, that\'s not in the word. You lose a life')