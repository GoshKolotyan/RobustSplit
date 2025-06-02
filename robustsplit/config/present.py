class PresetConfig:
    @staticmethod
    def timeseries_forecasting():
        return {
            'splitter': 'TimeSeriesSplit',
            'n_splits': 5,
            'gap': 1,
            'quality_checks': ['temporal_leakage', 'stationarity']
        }
    
    @staticmethod
    def computer_vision():
        return {
            'splitter': 'StratifiedKFold',
            'n_splits': 5,
            'quality_checks': ['class_balance', 'data_leakage']
        }