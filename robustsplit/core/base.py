from abc import ABC, abstractmethod
from typing import Iterable, Tuple, Any, Optional, Dict

class BaseSplitter(ABC):
    def __init__(self, random_state: Optional[int] = None, **kwargs):
        self.random_state = random_state
        self.config = kwargs
    
    @abstractmethod
    def split(self, X: Iterable[Any], y: Iterable[Any]=None, groups=None) -> int:
        """"Generate train test indeces"""
        pass 

    @abstractmethod
    def get_n_splits(self, X:Iterable[Any], y: Iterable[Any]=None, groups=None) -> int:
        """Get number of splits"""
        pass
    
    @abstractmethod
    def validate_input(self, X: Iterable[Any], y: Iterable[Any]=None, groups=None) -> Tuple[Iterable[Any], Iterable[Any]]:
        """Validate input data"""
        pass

class DataTypeMixin:
    """Mixin for data type specific handling"""
    
    def handle_pandas(self, X): 
        pass
    def handle_numpy(self, X): 
        pass
    def handle_torch(self, X): 
        pass