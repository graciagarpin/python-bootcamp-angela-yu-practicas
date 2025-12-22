#TODO:
# definir la clase OperationManager:
# debe contener el diccionario de símbolos → métodos
# debe contener métodos matemáticos

class OperationManager:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    # MÉTODOS
    def add(self, n1, n2):
            return n1 + n2

    def subtract(self, n1, n2):
            return n1 - n2

    def multiply(self, n1, n2):
            return n1 * n2

    def divide(self, n1, n2):
            return n1 / n2

    def perform_operation(self,symbol, n1, n2):
        operation_selected = self.operations[symbol]
        result = operation_selected(n1, n2)
        return result

    def provide_symbol(self):
        return self.operations.keys()