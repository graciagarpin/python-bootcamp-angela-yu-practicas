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
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("Wrong")
