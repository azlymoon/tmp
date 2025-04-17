import argparse
import numpy as np
import logging
import sys

from core.utils import setup_logging, load_config
from core.factories import model_factory, attack_factory, data_factory

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="ART Project Pipeline")
    parser.add_argument('-c', '--config', dest='config_path', required=True,
                        help='Path to the JSON configuration file')
    args = parser.parse_args()

    config = load_config(args.config_path)

    try:
        data = data_factory.DataFactory.load_dataset(config.get("dataset"))
        X = data.data
        y = data.target
    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        sys.exit(1)

    try:
        model_cls = model_factory.ModelFactory.create_model(config.get("model"))
        art_model = model_cls.build(X, y)
    except Exception as e:
        logger.error(f"Error creating model: {e}")
        sys.exit(1)

    attacks = config.get("attacks", [])
    for attack_config in attacks:
        try:
            attack = attack_factory.AttackFactory.create_attack(art_model, attack_config)
        except Exception as e:
            logger.error(f"Error creating attack: {e}")
            sys.exit(1)

        try:
            original_predict = np.argmax(art_model.predict(X), axis=1)
            attacked_X = attack.generate(X, y)
            attacked_predict = np.argmax(art_model.predict(attacked_X), axis=1)
            logger.info("Original accuracy: {:.2f}%".format(np.mean(original_predict == y) * 100))
            logger.info("Attacked accuracy: {:.2f}%".format(np.mean(attacked_predict == y) * 100))
        except Exception as e:
            logger.error(f"Error during attack execution: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()