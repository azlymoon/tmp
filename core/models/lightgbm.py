from art.estimators.classification import LightGBMClassifier
from core.interfaces.BaseModel import BaseModel
import lightgbm as lgb
import numpy as np

class LightgbmModel(BaseModel):
    def __init__(self, **kwargs):
        self.art_model = None
        self.params = self._process_params(kwargs)
        self.booster = None
    
    def _process_params(self, params):
        param_mapping = {
            "iterations": "num_boost_round",
            "n_estimators": "num_boost_round"
        }
        
        processed = {}
        for k, v in params.items():
            new_key = param_mapping.get(k, k)
            processed[new_key] = v
        
        processed.setdefault("objective", "multiclass")
        #processed.setdefault("verbosity", -1)
        
        return processed
    
    def build(self, x_train, y_train):
        num_classes = len(np.unique(y_train))
        if num_classes <= 1:
            raise ValueError("Number of classes must be greater than 1")
        
        self.params['num_class'] = num_classes
        
        num_boost_round = self.params.pop('num_boost_round', 100)
        
        train_data = lgb.Dataset(
            data=x_train,
            label=y_train
        )

        self.booster = lgb.train(
            params=self.params,
            train_set=train_data,
            num_boost_round=num_boost_round
        )
        
        self.art_model = LightGBMClassifier(
            model=self.booster
        )
        return self.art_model