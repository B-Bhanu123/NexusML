"""
NexusML Machine Learning Algorithms & AutoML Engine Module
"""

from nexusml.models.base import BaseEstimator, BaseModel
from nexusml.models.linear import LinearRegression, LogisticRegression
from nexusml.models.tree import DecisionTreeClassifier
from nexusml.models.ensemble import RandomForestClassifier, GradientBoostingClassifier
from nexusml.models.neural import NeuralNetwork
from nexusml.models.automl import AutoMLPipeline
from nexusml.models.clustering import KMeans
from nexusml.models.evaluation import EvaluationReport

__all__ = [
    "BaseEstimator",
    "BaseModel",
    "LinearRegression",
    "LogisticRegression",
    "DecisionTreeClassifier",
    "RandomForestClassifier",
    "GradientBoostingClassifier",
    "NeuralNetwork",
    "AutoMLPipeline",
    "KMeans",
    "EvaluationReport"
]
