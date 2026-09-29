from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def calculer(self, a, b):
        pass