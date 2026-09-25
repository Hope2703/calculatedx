from abc import abstractmethod

from core.base_op import Operation

class Addition(Operation): 
    def calculer (self, a, b):
        return a + b

class Soustraction(Operation):
    def calculer (self, a, b):
        return a - b    

class Multiplication(Operation):
    def calculer(self, a, b):
        return a * b 

class Division(Operation):
    def calculer(self, a, b):
        if b == 0:
            raise ValueError("division par zero impossible")
        return a / b       