
#TODO:

# definir la clase OperationManager:
# debe contener métodos matemáticos
# debe contener el diccionario de símbolos → métodos

class OperationManager:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }



#MÉTODOS