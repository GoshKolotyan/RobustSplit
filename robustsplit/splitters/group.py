from ..core import BaseSplitter

class GroupKFold(BaseSplitter):
    def __init__(self, n_splits=5, **kwargs):
        super().__init__(**kwargs)
        self.n_splits = n_splits