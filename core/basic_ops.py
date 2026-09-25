from core.base_op import Operation

class Addition(Operation): 
    def calculer (self, a, b):
        return a + b

class Soustraction(Operation):
    def calculer (self, a, b):
        return a - b    