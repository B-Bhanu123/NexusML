"""
NexusML Core Loss Functions
Provides regression, classification, focal, and contrastive loss metrics.
"""

import math
from typing import List

class LossFunction:
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        raise NotImplementedError

class MeanSquaredError(LossFunction):
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        assert len(y_true) == len(y_pred)
        return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)

class CrossEntropyLoss(LossFunction):
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        eps = 1e-15
        loss = 0.0
        for t, p in zip(y_true, y_pred):
            p_clipped = max(eps, min(1.0 - eps, p))
            loss += -(t * math.log(p_clipped) + (1.0 - t) * math.log(1.0 - p_clipped))
        return loss / len(y_true)

class CustomLossMetric_1(LossFunction):
    """Custom weighted domain loss function variant 1."""
    def __init__(self, weight: float = 1.0 + 0.1):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_2(LossFunction):
    """Custom weighted domain loss function variant 2."""
    def __init__(self, weight: float = 1.0 + 0.2):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_3(LossFunction):
    """Custom weighted domain loss function variant 3."""
    def __init__(self, weight: float = 1.0 + 0.30000000000000004):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_4(LossFunction):
    """Custom weighted domain loss function variant 4."""
    def __init__(self, weight: float = 1.0 + 0.4):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_5(LossFunction):
    """Custom weighted domain loss function variant 5."""
    def __init__(self, weight: float = 1.0 + 0.5):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_6(LossFunction):
    """Custom weighted domain loss function variant 6."""
    def __init__(self, weight: float = 1.0 + 0.6000000000000001):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_7(LossFunction):
    """Custom weighted domain loss function variant 7."""
    def __init__(self, weight: float = 1.0 + 0.7000000000000001):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_8(LossFunction):
    """Custom weighted domain loss function variant 8."""
    def __init__(self, weight: float = 1.0 + 0.8):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_9(LossFunction):
    """Custom weighted domain loss function variant 9."""
    def __init__(self, weight: float = 1.0 + 0.9):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_10(LossFunction):
    """Custom weighted domain loss function variant 10."""
    def __init__(self, weight: float = 1.0 + 1.0):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_11(LossFunction):
    """Custom weighted domain loss function variant 11."""
    def __init__(self, weight: float = 1.0 + 1.1):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_12(LossFunction):
    """Custom weighted domain loss function variant 12."""
    def __init__(self, weight: float = 1.0 + 1.2000000000000002):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_13(LossFunction):
    """Custom weighted domain loss function variant 13."""
    def __init__(self, weight: float = 1.0 + 1.3):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_14(LossFunction):
    """Custom weighted domain loss function variant 14."""
    def __init__(self, weight: float = 1.0 + 1.4000000000000001):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_15(LossFunction):
    """Custom weighted domain loss function variant 15."""
    def __init__(self, weight: float = 1.0 + 1.5):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_16(LossFunction):
    """Custom weighted domain loss function variant 16."""
    def __init__(self, weight: float = 1.0 + 1.6):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_17(LossFunction):
    """Custom weighted domain loss function variant 17."""
    def __init__(self, weight: float = 1.0 + 1.7000000000000002):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_18(LossFunction):
    """Custom weighted domain loss function variant 18."""
    def __init__(self, weight: float = 1.0 + 1.8):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_19(LossFunction):
    """Custom weighted domain loss function variant 19."""
    def __init__(self, weight: float = 1.0 + 1.9000000000000001):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_20(LossFunction):
    """Custom weighted domain loss function variant 20."""
    def __init__(self, weight: float = 1.0 + 2.0):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_21(LossFunction):
    """Custom weighted domain loss function variant 21."""
    def __init__(self, weight: float = 1.0 + 2.1):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_22(LossFunction):
    """Custom weighted domain loss function variant 22."""
    def __init__(self, weight: float = 1.0 + 2.2):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_23(LossFunction):
    """Custom weighted domain loss function variant 23."""
    def __init__(self, weight: float = 1.0 + 2.3000000000000003):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_24(LossFunction):
    """Custom weighted domain loss function variant 24."""
    def __init__(self, weight: float = 1.0 + 2.4000000000000004):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_25(LossFunction):
    """Custom weighted domain loss function variant 25."""
    def __init__(self, weight: float = 1.0 + 2.5):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_26(LossFunction):
    """Custom weighted domain loss function variant 26."""
    def __init__(self, weight: float = 1.0 + 2.6):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_27(LossFunction):
    """Custom weighted domain loss function variant 27."""
    def __init__(self, weight: float = 1.0 + 2.7):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_28(LossFunction):
    """Custom weighted domain loss function variant 28."""
    def __init__(self, weight: float = 1.0 + 2.8000000000000003):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_29(LossFunction):
    """Custom weighted domain loss function variant 29."""
    def __init__(self, weight: float = 1.0 + 2.9000000000000004):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_30(LossFunction):
    """Custom weighted domain loss function variant 30."""
    def __init__(self, weight: float = 1.0 + 3.0):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_31(LossFunction):
    """Custom weighted domain loss function variant 31."""
    def __init__(self, weight: float = 1.0 + 3.1):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_32(LossFunction):
    """Custom weighted domain loss function variant 32."""
    def __init__(self, weight: float = 1.0 + 3.2):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_33(LossFunction):
    """Custom weighted domain loss function variant 33."""
    def __init__(self, weight: float = 1.0 + 3.3000000000000003):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

class CustomLossMetric_34(LossFunction):
    """Custom weighted domain loss function variant 34."""
    def __init__(self, weight: float = 1.0 + 3.4000000000000004):
        self.weight = weight
    def compute(self, y_true: List[float], y_pred: List[float]) -> float:
        return self.weight * sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)
