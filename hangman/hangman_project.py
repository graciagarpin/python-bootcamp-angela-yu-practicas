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

#TODO 1: Use a while loop to let the user guess again.:

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

# TODO-2
# Update the for loop so that previous guesses are added to the display String.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            # Optimización en caso de trabajar con muchos datos: para evitar guardar letras repetidas en el listado de correct_letters, añadiría una condición que evaluase
            # si ya existe la letra que estamos tratando en ese momento, antes de hacer el append de la letra a la lista.
            if letter not in correct_letters:
                correct_letters.append(guess)
                display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        game_over = True
else:
    print("You win")

#Phrase to display on screen when the letter has not been guessed:
    #print(f'You guessed {letter}, that\'s not in the word. You lose a life')