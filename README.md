RobustSplit - ML Data Splitting Framework
Directory Structure
robustsplit/
├── robustsplit/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── base.py              # Base splitter classes and interfaces
│   │   ├── validators.py        # Data validation and leakage detection
│   │   └── utils.py            # Common utilities and helpers
│   │
│   ├── splitters/
│   │   ├── __init__.py
│   │   ├── basic.py            # Train/test/validation splits
│   │   ├── stratified.py       # Stratified splitting strategies
│   │   ├── temporal.py         # Time-based splitting
│   │   ├── group.py            # Group-aware splitting
│   │   ├── cross_validation.py # CV strategies (nested, blocked, etc.)
│   │   ├── spatial.py          # Geographic/spatial splitting
│   │   └── custom.py           # Custom splitting strategies
│   │
│   ├── data_types/
│   │   ├── __init__.py
│   │   ├── tabular.py          # Pandas DataFrame handling
│   │   ├── timeseries.py       # Time series specific logic
│   │   ├── text.py             # NLP data handling
│   │   ├── image.py            # Computer vision data
│   │   └── multimodal.py       # Mixed data types
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── sklearn.py          # Scikit-learn integration
│   │   ├── pytorch.py          # PyTorch DataLoader integration
│   │   ├── tensorflow.py       # TensorFlow integration
│   │   ├── pandas.py           # Enhanced pandas support
│   │   └── dask.py             # Big data with Dask
│   │
│   ├── quality/
│   │   ├── __init__.py
│   │   ├── leakage_detector.py # Data leakage detection
│   │   ├── balance_checker.py  # Class/group balance analysis
│   │   ├── metrics.py          # Split quality metrics
│   │   └── visualizers.py      # Split visualization tools
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── presets.py          # Common splitting configurations
│   │   └── schema.py           # Configuration validation schemas
│   │
│   └── io/
│       ├── __init__.py
│       ├── serializers.py      # Save/load split configurations
│       └── exporters.py        # Export splits to various formats
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── benchmarks/
│
├── examples/
│   ├── basic_usage.py
│   ├── advanced_strategies.py
│   ├── timeseries_example.py
│   └── integration_examples/
│
├── docs/
│   ├── source/
│   ├── tutorials/
│   └── api_reference/
│
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
