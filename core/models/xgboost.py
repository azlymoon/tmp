from art.estimators.classification import XGBoostClassifier
from core.interfaces.BaseModel import BaseModel #abs_art_tabular.
import xgboost as xgb
import numpy as np


class XgboostModel(BaseModel):
    def __init__(self, **kwargs):
        self.art_model = None
        self.model = self._init_model(kwargs)
    
    def _init_model(self, params):
        param_mapping = {
            "iterations": "n_estimators",
            "learning_rate": "learning_rate"
        }
        xgb_params = {param_mapping.get(k, k): v for k, v in params.items()}
        return xgb.XGBClassifier(**xgb_params)


    def build(self, x_train, y_train):
        self.model.fit(
            x_train, 
            y_train,
            eval_set=[(x_train, y_train)],
            verbose=False
        )
        self.art_model = XGBoostClassifier(
            model=self.model,
            nb_features=x_train.shape[1],
            nb_classes=len(np.unique(y_train))
        )
        return self.art_model