from core.interfaces.BaseAttack import BaseAttack #abs_art_tabular.
import art


class HopskipjumpAttack(BaseAttack):
    def __init__(self, classifier, **params):
        print(params)
        print(type(classifier))
        self.attack = art.attacks.evasion.hop_skip_jump.HopSkipJump(classifier=classifier, **params)


    def execute(self, x_train, y_train):
        return self.attack.generate(x=x_train, y=y_train)
