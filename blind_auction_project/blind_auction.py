from art import logo

print(logo)

# TODO 4: Compare bids in dictionary
def find_highest_bidder(total_bids):
    highest_bid_amount = 0
    winner = ""

    for bidder, bid in total_bids.items():
        if bid > highest_bid_amount:
            highest_bid_amount = bid
            winner = bidder
    return print(f"The winner is {winner} with a bid of ${highest_bid_amount}")

# TODO 3: Whether if new bids need to be added

bids = {} # It is necessary to start the bid with an empty dictionary.

turn_off_game = False
while not turn_off_game:
    # TODO 1: ask user for a name and ask user for a bid price
    user_name = input("What is your name?:")
    user_price = int(input("What is your bid?: $ "))

    # TODO 2: Save data into dictionary: key - value
    bids[user_name] = user_price # we have only one bidder stored in the dictionary.

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n".lower())
    if should_continue == 'no':
        find_highest_bidder(bids)
        turn_off_game = True
    elif should_continue == 'yes':
        print("\n" * 20)
        '''
    elif should_continue != 'no' or should_continue != 'yes':
        print("Please, type 'yes' or 'no'")
        '''