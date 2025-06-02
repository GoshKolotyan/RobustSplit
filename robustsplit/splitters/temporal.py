from ..core import BaseSplitter
from typing import Iterable, Any, Optional

class TimeSeriesSplit(BaseSplitter):
    def __init__(self, n_splits=5, gap=0, **kwargs):
        super().__init__(**kwargs)
        self.n_splits = n_splits
        self.gap = gap

class BlockingTimeSeriesSplit(BaseSplitter):
    def __init__(self, block_size='1M', **kwargs):
        super().__init__(**kwargs)
        self.block_size = block_size