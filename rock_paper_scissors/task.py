import random

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

# Rules of the logic:
# Rock wins against scissors
# Paper wins against rock
# Scissors wins against paper

# first request for the input: the user enter "rock", "scissors" or "paper"
# and take the result in each variable
# then, the computer enter a random choice and take the result in a variable
# aply the logic

# decide if you win or you lost

# recoger la elección de cada participante:
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
computer_choice = random.randint(0, 2)
print(f"Computer Choose: {computer_choice}")

#Lógica del juego:
# si yo saco piedra y computer saca tijeras, yo gano
# si yo saco paper y computer saca rock, yo gano
# si yo saco tijeras y computer saca paper, yo gano

# si son iguales, empatamos

# # si yo saco piedra y computer saca papel, yo pierdo
# # si yo saco paper y computer saca tijeras, yo pierdo
# # si yo saco tijeras y computer saca rock, yo pierdo

if my_choice == 0:
    print(rock)
    if computer_choice == 0:
        print(rock)
        print("This is a tie")
    elif computer_choice == 1:
        print(paper)
        print("You win")
    elif computer_choice == 2:
        print(scissors)
        print("You loose")
    else:
        print("You are type a invalid choice")
else:
    print("You are type an invalid number. You lose!")

if my_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(rock)
        print("You loose")
    elif computer_choice == 1:
        print(paper)
        print("This is a tie")
    elif computer_choice == 2:
        print(scissors)
        print("You win")
    else:
        print("You are type a invalid choice")
else:
    print("You are type an invalid number. You lose!")

if my_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print(rock)
        print("You loose")
    elif computer_choice == 1:
        print(paper)
        print("You win")
    elif computer_choice == 2:
        print(scissors)
        print("This is a tie")
    else:
        print("You are type a invalid choice")
else:
    print("You are type an invalid number. You lose!")

'''
rock_paper_scissors = [0, 1, 2]

my_choice[0] = "Rock"
my_choice[1] = "Paper"
my_choice[2] = "Scissors"

print(rock_paper_scissors)
'''



