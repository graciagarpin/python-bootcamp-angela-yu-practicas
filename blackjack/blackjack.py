import random

# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#TODO 0: Start game:
# print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if asks 'y':
# TODO 1: create 2 empty lists to hold user card and computer card: ✓

user_cards = []
computer_cards = []

#TODO 2.1: Deal une card from the deck: ✓

def deal_card(deck):
    values = random.choice(cards)
    return values

# TODO 3: Calculate players's scores: ✓

def calculate_score(list_of_values):
    result = 0
    for value in list_of_values:
        result += value
    return result

# TODO 2: pick up  2 cards to each player ramdomly and add to the list: ✓
for card in range(2):
    user_cards.append(deal_card(cards))

for card in range(2):
    computer_cards.append(deal_card(cards))

#add up scores:
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# print logo
print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")

#  print("Type 'y' to get another card, type 'n' to pass: ")

