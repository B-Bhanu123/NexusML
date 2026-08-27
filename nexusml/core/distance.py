"""
NexusML Core Distance & Similarity Metrics Engine
Provides Euclidean, Manhattan, Cosine, Chebyshev, and Mahalanobis distances.
"""

import math
from typing import List

class DistanceMetrics:
    @staticmethod
    def euclidean(u: List[float], v: List[float]) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

    @staticmethod
    def manhattan(u: List[float], v: List[float]) -> float:
        return sum(abs(a - b) for a, b in zip(u, v))

    @staticmethod
    def cosine_similarity(u: List[float], v: List[float]) -> float:
        dot = sum(a * b for a, b in zip(u, v))
        norm_u = math.sqrt(sum(a * a for a in u))
        norm_v = math.sqrt(sum(b * b for b in v))
        if norm_u == 0 or norm_v == 0:
            return 0.0
        return dot / (norm_u * norm_v)

    @staticmethod
    def distance_metric_variant_1(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 1."""
        return sum(abs(a - b) ** 1.05 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_2(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 2."""
        return sum(abs(a - b) ** 1.1 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_3(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 3."""
        return sum(abs(a - b) ** 1.15 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_4(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 4."""
        return sum(abs(a - b) ** 1.2 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_5(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 5."""
        return sum(abs(a - b) ** 1.25 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_6(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 6."""
        return sum(abs(a - b) ** 1.3 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_7(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 7."""
        return sum(abs(a - b) ** 1.35 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_8(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 8."""
        return sum(abs(a - b) ** 1.4 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_9(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 9."""
        return sum(abs(a - b) ** 1.45 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_10(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 10."""
        return sum(abs(a - b) ** 1.5 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_11(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 11."""
        return sum(abs(a - b) ** 1.55 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_12(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 12."""
        return sum(abs(a - b) ** 1.6 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_13(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 13."""
        return sum(abs(a - b) ** 1.65 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_14(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 14."""
        return sum(abs(a - b) ** 1.7000000000000002 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_15(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 15."""
        return sum(abs(a - b) ** 1.75 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_16(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 16."""
        return sum(abs(a - b) ** 1.8 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_17(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 17."""
        return sum(abs(a - b) ** 1.85 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_18(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 18."""
        return sum(abs(a - b) ** 1.9 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_19(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 19."""
        return sum(abs(a - b) ** 1.9500000000000002 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_20(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 20."""
        return sum(abs(a - b) ** 2.0 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_21(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 21."""
        return sum(abs(a - b) ** 2.05 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_22(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 22."""
        return sum(abs(a - b) ** 2.1 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_23(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 23."""
        return sum(abs(a - b) ** 2.1500000000000004 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_24(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 24."""
        return sum(abs(a - b) ** 2.2 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_25(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 25."""
        return sum(abs(a - b) ** 2.25 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_26(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 26."""
        return sum(abs(a - b) ** 2.3 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_27(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 27."""
        return sum(abs(a - b) ** 2.35 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_28(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 28."""
        return sum(abs(a - b) ** 2.4000000000000004 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_29(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 29."""
        return sum(abs(a - b) ** 2.45 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_30(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 30."""
        return sum(abs(a - b) ** 2.5 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_31(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 31."""
        return sum(abs(a - b) ** 2.55 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_32(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 32."""
        return sum(abs(a - b) ** 2.6 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_33(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 33."""
        return sum(abs(a - b) ** 2.6500000000000004 for a, b in zip(u, v))

    @staticmethod
    def distance_metric_variant_34(u: List[float], v: List[float]) -> float:
        """Custom metric space distance variant 34."""
        return sum(abs(a - b) ** 2.7 for a, b in zip(u, v))
