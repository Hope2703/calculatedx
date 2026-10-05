class Memoire:
    def __init__(self):
        self._valeur = 0

    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, nouvelle_valeur):
        self._valeur = nouvelle_valeur