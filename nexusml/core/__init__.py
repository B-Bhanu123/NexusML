"""
NexusML Core Module: Mathematical Foundations, Tensor Calculus & Optimization
"""

from nexusml.core.tensor import Tensor
from nexusml.core.linalg import MatrixOps
from nexusml.core.activations import ActivationFunction, ReLU, Sigmoid, Softmax
from nexusml.core.losses import LossFunction, MeanSquaredError, CrossEntropyLoss
from nexusml.core.optimizers import Optimizer, Adam, SGD

__all__ = [
    "Tensor",
    "MatrixOps",
    "ActivationFunction",
    "ReLU",
    "Sigmoid",
    "Softmax",
    "LossFunction",
    "MeanSquaredError",
    "CrossEntropyLoss",
    "Optimizer",
    "Adam",
    "SGD"
]
