# TODO1: Print calc logo
import art

print(art.logo)

#TODO 2: calculate operation and print the result (float) ej: 2.0 + 4.0 = 6.0

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculation(num1, num2):
    current_result = 0
    current_result = operations[operation_symbol](num1, num2)
    return current_result

# Ask user for a first number, operation_symbol and next number

should_continue = True
while should_continue:
    first_num = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    answer = calculation(first_num, next_num)
    print(f"{first_num} {operation_symbol} {next_num} = {answer}")

# TODO 3: Ask user if wants to continue calculating with result or restart the calculation.
    restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    print(restart)
    if restart == 'y':
        should_continue = True
    if restart == 'n':
        should_continue = False

