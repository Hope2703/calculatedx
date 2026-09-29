import math
from core.base_op import Operation

class LogarithmeNaturel(Operation):
    def calculer(self, a, b=None):
        if a <= 0:
            raise ValueError("Le logarithme naturel n'est défini que pour les nombres positifs.")
        return math.log(a)

class LogarithmeDecimal(Operation):
    def calculer(self, a, b=None):
        if a <= 0:
            raise ValueError("Le logarithme décimal n'est défini que pour les nombres positifs.")
        return math.log10(a)