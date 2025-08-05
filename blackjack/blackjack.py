import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#todo 0: Start game:
# print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if asks 'y':
# TODO 1: create 2 empty lists to hold user card and computer card

#by the moment mocked values:
user_cards = [2, 4]
computer_cards = [6, 7]

# TODO 2: pick up  2 cards to each player ramdomly and add to the list. Pick up from cards's list.

random.choice(cards)

# TODO 3: Calculate and add up players's scores

# calculate score adding the values of the cards:

def calculate_score(list_of_values):
    result = 0
    for value in list_of_values:
        result += value
    return result

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# print logo
print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")
#  print("Type 'y' to get another card, type 'n' to pass: ")

