import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    letter = "_ "
    placeholder += letter

print(placeholder)

guess = input("Guess a letter: ").lower()
#Create an empty string called "display".
#Loop through each letter in the chosen_word
#If the letter at that position matches guess then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
#Print display and you should see the guessed letter in the correct position.
#But every letter that is not a match is represented with a "_".

display = ""

for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("_")
