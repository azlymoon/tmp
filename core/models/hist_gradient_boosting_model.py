from core.interfaces.base_model import BaseModel
from sklearn.ensemble import HistGradientBoostingClassifier
from art.estimators.classification import SklearnClassifier

class HistGradientBoostingModel(BaseModel):
    def __init__(self, **kwargs):
        self.art_model = None
        self.model = HistGradientBoostingClassifier(**kwargs)

    def build(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        self.art_model = SklearnClassifier(model=self.model)
        return self.art_model