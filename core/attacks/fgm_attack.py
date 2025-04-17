# не работает с деревьями, пока не протестировано
from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import FastGradientMethod

class FgmAttack(BaseAttack):
    def __init__(self, estimator, **params):
        self.attack = FastGradientMethod(
            estimator=estimator, 
            **params
        )

    def generate(self, x, y=None):
        return self.attack.generate(x=x, y=y)