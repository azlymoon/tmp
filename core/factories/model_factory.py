import importlib

class ModelFactory:
    @staticmethod
    def create_model(model_config):
        model_type = model_config.get("type")
        params = model_config.get("params", {})
        module_name = f"core.models.{model_type}_model" #abs_art_tabular.
        class_name = "".join(word.capitalize() for word in model_type.split('_')) + "Model"
        try:
            module = importlib.import_module(module_name)
            model_class = getattr(module, class_name)
            return model_class(**params)
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Unknown type of model: {model_type}") from e