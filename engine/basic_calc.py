from core.basic_ops import(addition, subtraction, multiplication, division )

class BasicCalculator:
    def __init__(self):
        self.operations = {
            "+": addition(),
            "-": subtraction(),
            "*": multiplication(),
            "/": division(),
        }
