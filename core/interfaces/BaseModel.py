from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    Abstract base class for models.
    """

    @abstractmethod
    def build(self, x_train, y_train):
        pass
