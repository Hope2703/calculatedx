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

class Sinus(Operation):
    def calculer(self, a, b="radians"):
        angle = math.radians(a) if b == "degres" else a
        return math.sin(angle)

class Cosinus(Operation):
    def calculer(self, a, b="radians"):
        angle = math.radians(a) if b == "degres" else a
        return math.cos(angle)

class Tangente(Operation):
    def calculer(self, a, b="radians"):
        angle = math.radians(a) if b == "degres" else a
        return math.tan(angle)