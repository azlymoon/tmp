from core.interfaces.BaseAttack import BaseAttack #abs_art_tabular.
import art


class ZooAttack(BaseAttack):
    def __init__(self, classifier, **params):
        print(params)
        print(type(classifier))
        self.attack = art.attacks.evasion.zoo.ZooAttack(classifier=classifier, **params)


    def execute(self, x_train, _):
        return self.attack.generate(x=x_train)
