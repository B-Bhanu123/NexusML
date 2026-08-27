"""
NexusML Serving API & Microservices Module
"""

from nexusml.serving.api import create_app
from nexusml.serving.inference import RealtimeInferenceEngine
from nexusml.serving.schemas import PredictionRequest, PredictionResponse

__all__ = ["create_app", "RealtimeInferenceEngine", "PredictionRequest", "PredictionResponse"]
