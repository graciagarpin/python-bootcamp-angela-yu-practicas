import random


#TODO 0: Start game:
# input(print("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
# if asks 'y':
# TODO 1: create 2 empty lists to hold user card and computer card: ✓

user_cards = []
computer_cards = []

#TODO 2.1: Deal a random card from the deck: ✓

def deal_card(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# TODO 3: Calculate players's scores: ✓

def calculate_score(list_of_values):
    result = 0
    for value in list_of_values:
        result += value
    return result

# TODO 2: pick up  2 cards to each player ramdomly and add to the list: ✓
for _ in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

#add up scores:
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# print logo
print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")

# TODO 4: Has computer or user a blackjack? (Ace + 10) ---> Check the hands:
'''
if user_score == 21:
    print("You win 😄")
elif computer_score == 21:
    print()
'''

# TODO 5: Ask for another card
should_continue = input(print("Type 'y' to get another card, type 'n' to pass: "))

