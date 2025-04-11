from abc import ABC, abstractmethod
from art.attacks.attack import Attack

class BaseAttack(ABC):
    """
    Abstract base class for attacks.
    """

    @abstractmethod
    def execute(self, **kwargs):
        pass
