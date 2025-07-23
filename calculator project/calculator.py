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

def calculation(num1, num2, operation):
    current_result = 0
    current_result = operations[operation](num1, num2)
    return current_result

# Ask user for a first number, operation and next number
first_num = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation = input("Pick an operation: ")
next_num = float(input("What's the next number?: "))

print(f"{first_num} {operation} {next_num} = {calculation(first_num, next_num, operation)}")

# TODO 3: Ask user if wants to continue calculating with result or restart the calculation.
# print(f"Type 'y' to continue calculating with {current_result}, or type 'n' to start a new calculation: ")

