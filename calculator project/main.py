import art

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

def calculator():
    print(art.logo)
    should_continue = True
    first_num = float(input("What's the first number?: "))

    while should_continue:
        # current_result = first_num
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        answer = operations[operation_symbol](first_num, next_num)
        print(f"{first_num} {operation_symbol} {next_num} = {answer}")

        restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        print(restart)
        if restart == 'y':
            should_continue = True
            first_num = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator() #recursive function (calls itself)

calculator()