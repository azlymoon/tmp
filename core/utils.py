import json


def load_config(file_path="test_config_catboost.json"):
    """
    Loads the configuration from the specified JSON file.

    :param file_path: Path to the configuration file (by default ‘config.json’).
    :return: Dictionary with configuration parameters.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config