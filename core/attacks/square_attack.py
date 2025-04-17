# под нейронку
from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import SquareAttack as ArtSquareAttack

class SquareAttack(BaseAttack):
    def __init__(self, classifier, **params):
        self.attack = ArtSquareAttack(
            estimator=classifier,
            **params
        )

    def generate(self, x, y=None):
        return self.attack.generate(x=x)