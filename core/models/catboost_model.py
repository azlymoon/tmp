from art.estimators.classification import CatBoostARTClassifier
from core.interfaces.base_model import BaseModel #abs_art_tabular.
from catboost import CatBoostClassifier


class CatboostModel(BaseModel):
    def __init__(self, **kwargs):
        self.art_model = None
        self.model = CatBoostClassifier(**kwargs)


    def build(self, x_train, y_train):
        self.model.fit(x_train, y_train, cat_features=None, eval_set=(x_train, y_train))
        self.art_model = CatBoostARTClassifier(model=self.model, nb_features=x_train.shape[1])
        return self.art_model