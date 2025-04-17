from core.interfaces.base_attack import BaseAttack
from art.attacks.evasion import HopSkipJump as ArtHopSkipJump


class HopskipjumpAttack(BaseAttack):
    def __init__(self, classifier, **params):
        self.classifier = classifier
        self.params = params
        self.attack = ArtHopSkipJump(classifier=self.classifier, **self.params)

    def generate(self, X, y=None):
        return self.attack.generate(x=X, y=y)