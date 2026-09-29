from core.basic_ops import Addition, Division, Multiplication, Soustraction
from utils.history import Historique


class BasicCalculator:
    def __init__(self):
        self.operations = {
            "+": Addition(),
            "-": Soustraction(),
            "*": Multiplication(),
            "/": Division(),
        }
        self.historique = Historique()

    def calculer(self, symbole, a, b):
        if symbole not in self.operations:
            raise ValueError("Opération inconnue.")
        
        operation = self.operations[symbole]

        resultat = operation.calculer(a, b)

        self.historique.ajouter(
            {
                "operation": symbole,
                "operandes": [a, b],
                "resultat": resultat,
            }
        )

        return resultat
