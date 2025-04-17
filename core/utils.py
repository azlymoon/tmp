import json
import logging


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")


def load_config(file_path):
    """
    Loads the configuration from the specified JSON file.

    :param file_path: Path to the configuration file (by default ‘config.json’).
    :return: Dictionary with configuration parameters.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config