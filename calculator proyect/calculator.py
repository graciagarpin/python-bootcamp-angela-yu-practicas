# TODO1: Print calc logo

# Ask user for a first number, operation and next number
first_num = float(input("What's the first number?: "))
print("+\n-\n*\n/\n")
operation = input("Pick an operation: ")
next_num = float(input("What's the next number?: "))

#TODO 2: calculate operation and print the result (float) ej: 2.0 + 4.0 = 6.0

def calculation(num1, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    return print(result)
# TODO 3: Ask user if wants to continue calculating with result or restart the calculation.
# print(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

calculation(first_num, next_num)