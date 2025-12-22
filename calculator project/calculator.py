import art
from main import calculator
from operations import OperationManager

# should do something like: op_manager.operations["+"](n1, n2)

class Calculator:
    def __init__(self):
        self.operation_manager = OperationManager()

    #METODO:
    def run(self):
        print(art.logo)
        should_continue = True
        first_num = float(input("What's the first number?: "))
        while should_continue:
            symbols = self.operation_manager.provide_symbol()
            for symbol in symbols:
                print(symbol, end=" ")
            operation_symbol = input("Pick an operation: ")
            next_num = float(input("What's the next number?: "))
            answer = self.operation_manager.perform_operation(operation_symbol, first_num, next_num)
            print(answer)
