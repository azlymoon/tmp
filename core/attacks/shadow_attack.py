# не работает с деревьями и бустингами, требует нейронку
from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import ShadowAttack as ArtShadowAttack

class ShadowAttack(BaseAttack):
    def __init__(self, estimator, **params):
        
        self.attack = ArtShadowAttack(
            estimator=estimator,
            **params
        )

    def generate(self, x, y=None):
        return self.attack.generate(x=x)