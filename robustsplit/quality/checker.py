import numpy as np
from scipy.stats import ks_2samp, chi2_contingency
# from .expectations.expectations import DistributionComparisonError

"""
Simple Distribution Checker
===========================

A minimal Python class for comparing statistical distributions.
Returns only True (same distribution) or False (different distribution).
"""

import numpy as np
from scipy.stats import ks_2samp, chi2_contingency
from typing import Any

class CheckDistribution:
    """
    Simple class to compare statistical distributions.
    """
    
    def __init__(self, data: Any, categorical: bool = None):
        """
        Initialize with reference data.
        
        Args:
            data: Reference dataset
            categorical: True for categorical, False for numerical, None for auto-detect
        """
        self.data = np.asarray(data)
        
        if categorical is None:
            # Auto-detect: numerical if numeric dtype, else categorical
            self.is_categorical = not np.issubdtype(self.data.dtype, np.number)
        else:
            self.is_categorical = categorical
    
    def compare(self, other_data: Any, alpha: float = 0.05) -> bool:
        """
        Compare distributions.
        
        Args:
            other_data: Data to compare against reference
            alpha: Significance level (default 0.05)
            
        Returns:
            bool: True if same distribution, False if different
        """
        other_data = np.asarray(other_data)
        
        if self.is_categorical:
            return self._compare_categorical(other_data, alpha)
        else:
            return self._compare_numerical(other_data, alpha)
    
    def _compare_numerical(self, other_data: np.ndarray, alpha: float) -> bool:
        """Kolmogorov-Smirnov test for numerical data."""
        _, p_value = ks_2samp(self.data, other_data)
        return p_value > alpha
    
    def _compare_categorical(self, other_data: np.ndarray, alpha: float) -> bool:
        """Chi-square test for categorical data."""
        # Get all categories
        categories = list(set(self.data) | set(other_data))
        
        # Create frequency table
        freq1 = [np.sum(self.data == cat) for cat in categories]
        freq2 = [np.sum(other_data == cat) for cat in categories]
        
        # Chi-square test
        _, p_value, _, _ = chi2_contingency([freq1, freq2])
        return p_value > alpha


# Even simpler function-based approach
def same_distribution(data1: Any, data2: Any, alpha: float = 0.05, categorical: bool = None) -> bool:
    """
    Simple function to check if two datasets have the same distribution.
    
    Args:
        data1: First dataset
        data2: Second dataset
        alpha: Significance level
        categorical: Force categorical comparison (None for auto-detect)
        
    Returns:
        bool: True if same distribution, False if different
    """
    checker = CheckDistribution(data1, categorical)
    return checker.compare(data2, alpha)


if __name__ == "__main__":
    import numpy as np
    
    # Test numerical data
    np.random.seed(42)
    x = np.random.normal(0, 1, 1000)
    y_same = np.random.normal(0, 1, 500)
    y_diff = np.random.normal(2, 1, 500)
    
    checker = CheckDistribution(x)
    print(f"Same numerical: {checker.compare(y_same)}")      # Should be True
    print(f"Different numerical: {checker.compare(y_diff)}")  # Should be False
    
    # Test categorical data
    a = np.random.choice(['A', 'B', 'C'], 1000, p=[0.5, 0.3, 0.2])
    b_same = np.random.choice(['A', 'B', 'C'], 500, p=[0.5, 0.3, 0.2])
    b_diff = np.random.choice(['A', 'B', 'C'], 500, p=[0.2, 0.3, 0.5])
    
    checker_cat = CheckDistribution(a, categorical=True)
    print(f"Same categorical: {checker_cat.compare(b_same)}")    # Should be True
    print(f"Different categorical: {checker_cat.compare(b_diff)}") # Should be False
    
    # Test function approach
    print(f"Function same: {same_distribution(x, y_same)}")     # Should be True
    print(f"Function different: {same_distribution(x, y_diff)}") # Should be False