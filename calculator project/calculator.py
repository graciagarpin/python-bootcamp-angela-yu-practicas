import art
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
            pass