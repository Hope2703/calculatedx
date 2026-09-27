from core.basic_ops import(
    Addition,
    Soustraction,
    Multiplication,
    Division )

class BasicCalculator:
    def __init__(self):
        self.operations = {
            "+": Addition(),
            "-": Soustraction(),
            "*": Multiplication(),
            "/": Division(),
        }

    def calculer(self,symbole,a,b):
        if symbole not in self.operations:
            raise ValueError("Opération inconnue.")
        operation = self.operations[symbole]
        return operation.calculer(a, b)
