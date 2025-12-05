MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coins_types = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# TODO 1: Prompt user what drink they want.
# TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3 Resources resume: Print report when the user enters “report” to the prompt.
#  this report shows the current resource values.
# TODO 4 : check if there are enough resources to make that drink.
# TODO 5 : if there are not enough or zero resources, it do not continue to make the drink and print: “Sorry there is not enough {ingredient}.”
# TODO 6: If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.

def is_sufficient_resource(order_ingredient): #(drink["ingredients"]) latte
    for element in order_ingredient:  # {'water': 200, 'milk': 150, 'coffee': 24}
        if order_ingredient[element] >= resources[element]:
            print(f"Sorry, there is not enough {element}.")
            return False
    return True

# TODO 7: Calculate the monetary value of the coins inserted.

def process_coins():
    print("Please, insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    list_amounts_coin_types = [quarters, dimes, nickles, pennies] # [1, 2, 3, 4]
    total = 0
    #print(coins_types) # {'quarters': 0.25, 'dimes': 0.1, 'nickles': 0.05, 'pennies': 0.01}
    for coins_type, amount in zip (coins_types, list_amounts_coin_types):
        total = total + amount * coins_types[coins_type]
    print(total)
    return total

# TODO 8: To process the payment :  If the user has inserted too much money, the machine should offer change.

def is_transaction_successful(money_received, drink_cost,):
    # el pago es suficiente?
    if money_received >= drink_cost:
        # add the cost to the machine -> update the profit invoking the global scope:
        global profit
        profit += drink_cost
        return True
    # process the change:  Check the price of the drink and calculate the rest
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(
            f"Water: {resources["water"]}ml\n"
            f"Milk: {resources["milk"]}\n"
            f"Coffee: {resources["coffee"]}\n"
            f"Money: ${profit}")
    elif choice == "latte" or choice == "espresso" or choice == "capuccino":
        print(f"You have selected a {choice}")
        drink = MENU[choice]
        if is_sufficient_resource(drink["ingredients"]):
            payment = process_coins() # total del pago
            is_transaction_successful(payment, drink["cost"])
    else:
       print(f"Please, type your choice again")