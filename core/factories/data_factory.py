import pandas as pd
import logging
from sklearn.utils import Bunch

logger = logging.getLogger(__name__)


class DataFactory:
    @staticmethod
    def load_dataset(dataset_config):
        """
        Loads a dataset from a CSV file according to the provided configuration
        and returns a Bunch object with 'data' and 'target' attributes, similar to sklearn's load_iris.

        The expected configuration is a dictionary with the following keys:
            - type: must be "csv"
            - path: path to the CSV file
            - target: name of the target column in the CSV file
        """
        ds_type = dataset_config.get("type")
        if ds_type != "csv":
            raise ValueError("DataFactory currently supports only 'csv' type datasets.")

        path = dataset_config.get("path")
        if not path:
            raise ValueError("For CSV datasets, the configuration must include a 'path'.")

        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise ValueError(f"Error reading CSV file at '{path}': {e}")

        target = dataset_config.get("target")
        if not target:
            raise ValueError("The configuration must specify the 'target' column name.")

        if target not in df.columns:
            raise ValueError(f"The target column '{target}' was not found in the CSV file.")

        X = df.drop(columns=[target]).values
        y = df[target].values

        feature_names = list(df.drop(columns=[target]).columns)

        logger.info(f"Dataset loaded successfully from {path} with {len(df)} samples.")
        return Bunch(data=X, target=y, feature_names=feature_names)