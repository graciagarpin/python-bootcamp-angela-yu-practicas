import random
from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_drawing = [rock, paper, scissors]

# Recoger la elección del user:
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
if my_choice > 2 or my_choice < 0:
    print("You are type an invalid number. You lose!")
else:
    # pintar la elección del user:
    print(hand_drawing[my_choice])
    #generar la elección aleatoria de computer:
    computer_choice = random.randint(0, 2)
    # pintar la elección de computer:
    print(f"Computer Choose: {hand_drawing[computer_choice]}")

#Lógica del juego:

# rock against ...
if my_choice == 0 and computer_choice == 0:
    print("This is a tie")
elif my_choice == 0 and computer_choice == 1:
    print("You loose")
elif my_choice == 0 and  computer_choice == 2:
    print("You win")
# paper against...
elif my_choice == 1 and computer_choice == 0:
    print("You win")
elif my_choice == 1 and computer_choice == 1:
    print("This is a tie")
elif my_choice == 1 and computer_choice == 2:
    print("You loose")
# scissors against...
elif my_choice == 2 and computer_choice == 0:
    print("You loose")
elif my_choice == 2 and computer_choice == 1:
    print("You win")
elif my_choice == 2 and computer_choice == 2:
    print("This is a tie")