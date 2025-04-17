from abc import ABC, abstractmethod

class BaseAttack(ABC):
    """
    Abstract base class for attacks.
    """

    @abstractmethod
    def generate(self, X, y=None):
        pass