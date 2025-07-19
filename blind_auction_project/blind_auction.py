from art import logo

print(logo)

# TODO 4: Compare bids in dictionary
def compare_bids():
    print("comparing bids")

# TODO 3: Whether if new bids need to be added

bids = {} #empty dictionary

turn_off_game = False
while not turn_off_game:
    # TODO 1: ask user for a name and ask user for a bid price
    user_name = input("What is your name?:")
    user_price = int(input("What is your bid?: $ "))

    # TODO 2: Save data into dictionary: key - value
    bids[user_name] = user_price
    print(bids) # we have only one bidder stored in the dictionary.

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    if another_bidder == 'no':
        print(bids)
        compare_bids()
        turn_off_game = True