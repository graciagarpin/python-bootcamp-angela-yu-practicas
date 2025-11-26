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

chosen_drink = input("What would you like? (espresso/latte/cappuccino): ")

print(f"You have selected a {chosen_drink}")

#TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.

if chosen_drink == "off":
    pass # here the code to turn off the program

# TODO 3 Resources resume: Print report when the user enters “report” to the prompt.
#  this report shows the current resource values.
if chosen_drink == "report":
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {"money"}")

# TODO: check if there are enough resources to make that drink.


# TODO: if there are not enough or zero resources, it do not continue to make the drink and print: “Sorry there is not enough water.”

