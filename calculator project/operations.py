
#TODO:

# definir la clase OperationManager:
# debe contener el diccionario de símbolos → métodos
# debe contener métodos matemáticos
# no calcula, si no que provee de operaciones a calculator

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
