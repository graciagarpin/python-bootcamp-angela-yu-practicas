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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# TODO 1: Prompt user what drink they want.
#TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3 Resources resume: Print report when the user enters “report” to the prompt.
#  this report shows the current resource values.

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(
            f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${"money"}")
    if choice == "latte" or choice == "espresso" or choice == "capuccino":
        print(f"You have selected a {choice}")

# TODO: check if there are enough resources to make that drink.
# aqui tendría que mapear para comparar si los recursos de la bebida requerida son = ó > que los current resources


# TODO: if there are not enough or zero resources, it do not continue to make the drink and print: “Sorry there is not enough water.”

