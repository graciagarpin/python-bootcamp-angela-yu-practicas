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
    "milk": 100,
    "coffee": 100
}

COINS = {
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

def is_sufficient_resource(order_ingredient): #(drink["ingredients"]) latte
    for element in order_ingredient:  # {'water': 200, 'milk': 150, 'coffee': 24}
        if order_ingredient[element] >= resources[element]:
            print(f"Sorry, there is not enough {element}.")
            return False
    return True

def calculate_amount(list_coins, coins_values):
    total = 0
    print(coins_values)
    for coin in list_coins:
        amount_of_coin = coin * coins_values[coin]
        total += amount_of_coin
    print(total)

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
        is_enough = is_sufficient_resource(drink["ingredients"])
        if is_enough:
            print("Please, insert coins.")
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickles = input("How many nickles?: ")
            pennies = input("How many pennies?: ")
            calculate_amount([quarters, dimes, nickles, pennies], COINS)
    else:
       print(f"Please, type your choice again")

# TODO 6: If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.

# TODO 7: Calculate the monetary value of the coins inserted.
# E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52