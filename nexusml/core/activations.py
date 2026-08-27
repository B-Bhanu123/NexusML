"""
NexusML Core Activation Functions
Provides non-linear activation functions and their forward/backward derivatives.
"""

import math
from typing import List, Union

class ActivationFunction:
    def forward(self, x: float) -> float:
        raise NotImplementedError
    def derivative(self, x: float) -> float:
        raise NotImplementedError

class ReLU(ActivationFunction):
    def forward(self, x: float) -> float:
        return max(0.0, x)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else 0.0

class Sigmoid(ActivationFunction):
    def forward(self, x: float) -> float:
        return 1.0 / (1.0 + math.exp(-max(-50.0, min(50.0, x))))
    def derivative(self, x: float) -> float:
        s = self.forward(x)
        return s * (1.0 - s)

class Softmax:
    @staticmethod
    def compute(inputs: List[float]) -> List[float]:
        max_val = max(inputs) if inputs else 0.0
        exps = [math.exp(x - max_val) for x in inputs]
        sum_exps = sum(exps)
        return [e / sum_exps for e in exps]

class CustomActivation_1(ActivationFunction):
    """Custom non-linear activation function variant 1."""
    def __init__(self, alpha: float = 0.01 * 1):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_2(ActivationFunction):
    """Custom non-linear activation function variant 2."""
    def __init__(self, alpha: float = 0.01 * 2):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_3(ActivationFunction):
    """Custom non-linear activation function variant 3."""
    def __init__(self, alpha: float = 0.01 * 3):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_4(ActivationFunction):
    """Custom non-linear activation function variant 4."""
    def __init__(self, alpha: float = 0.01 * 4):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_5(ActivationFunction):
    """Custom non-linear activation function variant 5."""
    def __init__(self, alpha: float = 0.01 * 5):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_6(ActivationFunction):
    """Custom non-linear activation function variant 6."""
    def __init__(self, alpha: float = 0.01 * 6):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_7(ActivationFunction):
    """Custom non-linear activation function variant 7."""
    def __init__(self, alpha: float = 0.01 * 7):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_8(ActivationFunction):
    """Custom non-linear activation function variant 8."""
    def __init__(self, alpha: float = 0.01 * 8):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_9(ActivationFunction):
    """Custom non-linear activation function variant 9."""
    def __init__(self, alpha: float = 0.01 * 9):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_10(ActivationFunction):
    """Custom non-linear activation function variant 10."""
    def __init__(self, alpha: float = 0.01 * 10):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_11(ActivationFunction):
    """Custom non-linear activation function variant 11."""
    def __init__(self, alpha: float = 0.01 * 11):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_12(ActivationFunction):
    """Custom non-linear activation function variant 12."""
    def __init__(self, alpha: float = 0.01 * 12):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_13(ActivationFunction):
    """Custom non-linear activation function variant 13."""
    def __init__(self, alpha: float = 0.01 * 13):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_14(ActivationFunction):
    """Custom non-linear activation function variant 14."""
    def __init__(self, alpha: float = 0.01 * 14):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_15(ActivationFunction):
    """Custom non-linear activation function variant 15."""
    def __init__(self, alpha: float = 0.01 * 15):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_16(ActivationFunction):
    """Custom non-linear activation function variant 16."""
    def __init__(self, alpha: float = 0.01 * 16):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_17(ActivationFunction):
    """Custom non-linear activation function variant 17."""
    def __init__(self, alpha: float = 0.01 * 17):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_18(ActivationFunction):
    """Custom non-linear activation function variant 18."""
    def __init__(self, alpha: float = 0.01 * 18):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_19(ActivationFunction):
    """Custom non-linear activation function variant 19."""
    def __init__(self, alpha: float = 0.01 * 19):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_20(ActivationFunction):
    """Custom non-linear activation function variant 20."""
    def __init__(self, alpha: float = 0.01 * 20):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_21(ActivationFunction):
    """Custom non-linear activation function variant 21."""
    def __init__(self, alpha: float = 0.01 * 21):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_22(ActivationFunction):
    """Custom non-linear activation function variant 22."""
    def __init__(self, alpha: float = 0.01 * 22):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_23(ActivationFunction):
    """Custom non-linear activation function variant 23."""
    def __init__(self, alpha: float = 0.01 * 23):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_24(ActivationFunction):
    """Custom non-linear activation function variant 24."""
    def __init__(self, alpha: float = 0.01 * 24):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_25(ActivationFunction):
    """Custom non-linear activation function variant 25."""
    def __init__(self, alpha: float = 0.01 * 25):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_26(ActivationFunction):
    """Custom non-linear activation function variant 26."""
    def __init__(self, alpha: float = 0.01 * 26):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_27(ActivationFunction):
    """Custom non-linear activation function variant 27."""
    def __init__(self, alpha: float = 0.01 * 27):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_28(ActivationFunction):
    """Custom non-linear activation function variant 28."""
    def __init__(self, alpha: float = 0.01 * 28):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_29(ActivationFunction):
    """Custom non-linear activation function variant 29."""
    def __init__(self, alpha: float = 0.01 * 29):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_30(ActivationFunction):
    """Custom non-linear activation function variant 30."""
    def __init__(self, alpha: float = 0.01 * 30):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_31(ActivationFunction):
    """Custom non-linear activation function variant 31."""
    def __init__(self, alpha: float = 0.01 * 31):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_32(ActivationFunction):
    """Custom non-linear activation function variant 32."""
    def __init__(self, alpha: float = 0.01 * 32):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_33(ActivationFunction):
    """Custom non-linear activation function variant 33."""
    def __init__(self, alpha: float = 0.01 * 33):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)

class CustomActivation_34(ActivationFunction):
    """Custom non-linear activation function variant 34."""
    def __init__(self, alpha: float = 0.01 * 34):
        self.alpha = alpha
    def forward(self, x: float) -> float:
        return x if x > 0 else self.alpha * (math.exp(x) - 1.0)
    def derivative(self, x: float) -> float:
        return 1.0 if x > 0 else self.alpha * math.exp(x)
