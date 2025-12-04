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

# TODO 1: Prompt user what drink they want.
# TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3 Resources resume: Print report when the user enters “report” to the prompt.
#  this report shows the current resource values.
# TODO 4 : check if there are enough resources to make that drink.
# TODO: if there are not enough or zero resources, it do not continue to make the drink and print: “Sorry there is not enough {ingredient}.”

def is_sufficient_resource(order_ingredient): # You have selected a latte
    for element in order_ingredient: # {'water': 200, 'milk': 150, 'coffee': 24}
        if order_ingredient[element] >= resources[element]:
            print(f"Sorry, there is not enough{element}.")
            return False
    return True

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
        print(drink["ingredients"])
        print(is_sufficient_resource(drink["ingredients"]))
    else:
       print(f"Please, type your choice again")

