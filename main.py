from core.utils import load_config
from core.factories.model_factory import ModelFactory
from core.factories.attack_factory import AttackFactory
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    config = load_config()

    model_config = config.get("model")
    model = ModelFactory.create_model(model_config)

    data = load_iris()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.build(x_train=X_train, y_train=y_train)

    attacks = config.get("attacks", [])
    for attack_conf in attacks:
        attack = AttackFactory.create_attack(model.art_model, attack_conf)

        print(f"Выполнение атаки: {attack_conf['type']} с параметрами: {attack_conf.get('params')}")
        attack_result = attack.execute(X_test, y_test)

        print("Результат атаки:")
        preds_clean = np.argmax(model.art_model.predict(X_test), axis=1)
        preds_adv = np.argmax(model.art_model.predict(attack_result), axis=1)
        acc_clean = np.mean(preds_clean == y_test)
        acc_adv = np.mean(preds_adv == y_test)
        print("Точность на оригинальных данных: {:.2f}%".format(acc_clean * 100))
        print("Точность на атакованных данных: {:.2f}%".format(acc_adv * 100))


if __name__ == "__main__":
    main()