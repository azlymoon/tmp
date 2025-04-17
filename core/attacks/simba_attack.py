# не работает с деревьями
from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import SimBA

class SimbaAttack(BaseAttack):
    def __init__(self, classifier, **params):
        self.attack = SimBA(
            classifier=classifier,
            **params
        )

    def generate(self, x, y=None):
        return self.attack.generate(x=x)