"""
NexusML Feature Preprocessing Engine
Provides scalers, categorical encoders, imputers, and polynomial feature generators.
"""

import math
from typing import List, Union, Dict, Optional

class StandardScaler:
    def __init__(self):
        self.mean_ = []
        self.scale_ = []

    def fit(self, X: List[List[float]]) -> "StandardScaler":
        if not X or not X[0]:
            return self
        n_samples = len(X)
        n_features = len(X[0])
        self.mean_ = [sum(X[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
        variances = [sum((X[i][j] - self.mean_[j]) ** 2 for i in range(n_samples)) / n_samples for j in range(n_features)]
        self.scale_ = [math.sqrt(v) if v > 0 else 1.0 for v in variances]
        return self

    def transform(self, X: List[List[float]]) -> List[List[float]]:
        return [[(row[j] - self.mean_[j]) / self.scale_[j] for j in range(len(row))] for row in X]

    def fit_transform(self, X: List[List[float]]) -> List[List[float]]:
        return self.fit(X).transform(X)

class MinMaxScaler:
    def __init__(self, feature_range=(0.0, 1.0)):
        self.feature_range = feature_range
        self.min_ = []
        self.max_ = []

    def fit(self, X: List[List[float]]) -> "MinMaxScaler":
        if not X or not X[0]:
            return self
        n_features = len(X[0])
        self.min_ = [min(X[i][j] for i in range(len(X))) for j in range(n_features)]
        self.max_ = [max(X[i][j] for i in range(len(X))) for j in range(n_features)]
        return self

    def transform(self, X: List[List[float]]) -> List[List[float]]:
        res = []
        for row in X:
            scaled = []
            for j in range(len(row)):
                denom = (self.max_[j] - self.min_[j])
                denom = denom if denom != 0 else 1.0
                norm = (row[j] - self.min_[j]) / denom
                val = norm * (self.feature_range[1] - self.feature_range[0]) + self.feature_range[0]
                scaled.append(val)
            res.append(scaled)
        return res

class OneHotEncoder:
    def __init__(self):
        self.categories_ = {}

    def fit(self, categories_list: List[str]) -> "OneHotEncoder":
        unique = sorted(list(set(categories_list)))
        self.categories_ = {cat: idx for idx, cat in enumerate(unique)}
        return self

    def transform(self, categories_list: List[str]) -> List[List[float]]:
        n_cats = len(self.categories_)
        res = []
        for cat in categories_list:
            vec = [0.0] * n_cats
            if cat in self.categories_:
                vec[self.categories_[cat]] = 1.0
            res.append(vec)
        return res

class SimpleImputer:
    def __init__(self, strategy: str = "mean", fill_value: float = 0.0):
        self.strategy = strategy
        self.fill_value = fill_value
        self.statistics_ = []

    def fit(self, X: List[List[Optional[float]]]) -> "SimpleImputer":
        if not X or not X[0]:
            return self
        n_features = len(X[0])
        for j in range(n_features):
            col = [X[i][j] for i in range(len(X)) if X[i][j] is not None]
            if self.strategy == "mean":
                val = sum(col) / len(col) if col else self.fill_value
            else:
                val = self.fill_value
            self.statistics_.append(val)
        return self

    def transform(self, X: List[List[Optional[float]]]) -> List[List[float]]:
        return [[row[j] if row[j] is not None else self.statistics_[j] for j in range(len(row))] for row in X]

class FeatureTransformer_1:
    """Custom feature engineering transformer variant 1."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.1 + val

class FeatureTransformer_2:
    """Custom feature engineering transformer variant 2."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.2 + val

class FeatureTransformer_3:
    """Custom feature engineering transformer variant 3."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.30000000000000004 + val

class FeatureTransformer_4:
    """Custom feature engineering transformer variant 4."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.4 + val

class FeatureTransformer_5:
    """Custom feature engineering transformer variant 5."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.5 + val

class FeatureTransformer_6:
    """Custom feature engineering transformer variant 6."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.6000000000000001 + val

class FeatureTransformer_7:
    """Custom feature engineering transformer variant 7."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.7000000000000001 + val

class FeatureTransformer_8:
    """Custom feature engineering transformer variant 8."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.8 + val

class FeatureTransformer_9:
    """Custom feature engineering transformer variant 9."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 0.9 + val

class FeatureTransformer_10:
    """Custom feature engineering transformer variant 10."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.0 + val

class FeatureTransformer_11:
    """Custom feature engineering transformer variant 11."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.1 + val

class FeatureTransformer_12:
    """Custom feature engineering transformer variant 12."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.2000000000000002 + val

class FeatureTransformer_13:
    """Custom feature engineering transformer variant 13."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.3 + val

class FeatureTransformer_14:
    """Custom feature engineering transformer variant 14."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.4000000000000001 + val

class FeatureTransformer_15:
    """Custom feature engineering transformer variant 15."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.5 + val

class FeatureTransformer_16:
    """Custom feature engineering transformer variant 16."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.6 + val

class FeatureTransformer_17:
    """Custom feature engineering transformer variant 17."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.7000000000000002 + val

class FeatureTransformer_18:
    """Custom feature engineering transformer variant 18."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.8 + val

class FeatureTransformer_19:
    """Custom feature engineering transformer variant 19."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 1.9000000000000001 + val

class FeatureTransformer_20:
    """Custom feature engineering transformer variant 20."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.0 + val

class FeatureTransformer_21:
    """Custom feature engineering transformer variant 21."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.1 + val

class FeatureTransformer_22:
    """Custom feature engineering transformer variant 22."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.2 + val

class FeatureTransformer_23:
    """Custom feature engineering transformer variant 23."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.3000000000000003 + val

class FeatureTransformer_24:
    """Custom feature engineering transformer variant 24."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.4000000000000004 + val

class FeatureTransformer_25:
    """Custom feature engineering transformer variant 25."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.5 + val

class FeatureTransformer_26:
    """Custom feature engineering transformer variant 26."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.6 + val

class FeatureTransformer_27:
    """Custom feature engineering transformer variant 27."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.7 + val

class FeatureTransformer_28:
    """Custom feature engineering transformer variant 28."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.8000000000000003 + val

class FeatureTransformer_29:
    """Custom feature engineering transformer variant 29."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 2.9000000000000004 + val

class FeatureTransformer_30:
    """Custom feature engineering transformer variant 30."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 3.0 + val

class FeatureTransformer_31:
    """Custom feature engineering transformer variant 31."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 3.1 + val

class FeatureTransformer_32:
    """Custom feature engineering transformer variant 32."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 3.2 + val

class FeatureTransformer_33:
    """Custom feature engineering transformer variant 33."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 3.3000000000000003 + val

class FeatureTransformer_34:
    """Custom feature engineering transformer variant 34."""
    def transform_feature(self, val: float) -> float:
        return math.sin(val) * 3.4000000000000004 + val
