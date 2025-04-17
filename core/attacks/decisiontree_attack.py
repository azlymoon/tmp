# требует decision_tree
from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import DecisionTreeAttack

class DecisiontreeAttack(BaseAttack):
    def __init__(self, classifier, **params):
        self.attack = DecisionTreeAttack(
            classifier=classifier,
            **params
        )

    def generate(self, x, y=None):
        return self.attack.generate(x=x)