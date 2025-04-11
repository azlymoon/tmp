import importlib


class AttackFactory:
    @staticmethod
    def create_attack(model, attack_config):
        attack_type = attack_config.get("type")
        params = attack_config.get("params", {})
        module_name = f"core.attacks.{attack_type}_attack" #abs_art_tabular.
        class_name = "".join(word.capitalize() for word in attack_type.split('_')) + "Attack"
        try:
            module = importlib.import_module(module_name)
            attack_class = getattr(module, class_name)
            return attack_class(model, **params)
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Unknown type of attack: {attack_type}") from e