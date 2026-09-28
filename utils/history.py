class Historique:
    def __init__(self):
        self._calculs = []

    def ajouter(self, calcul):
        self._calculs.append(calcul)

    @property
    def calculs(self):
        return self._calculs