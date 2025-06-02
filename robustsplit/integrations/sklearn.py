from core import BaseSplitter
from sklearn.base import BaseEstimator

class SKLearnSplitter(BaseEstimator, BaseSplitter):
    """Scikit-learn compatible wrapper"""
    pass