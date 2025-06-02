from ..core import BaseSplitter
from typing import Iterable, Any, Optional 

class TrainTestSplit(BaseSplitter):
    def __init__(self, test_size=0.2, shuffle=True, **kwargs):
        super().__init__(**kwargs)
        self.test_size = test_size
        self.shuffle = shuffle

class TrainValidTestSplit(BaseSplitter):
    def __init__(self, test_size=0.2, valid_size=0.2, **kwargs):
        super().__init__(**kwargs)
        self.test_size = test_size
        self.valid_size = valid_size