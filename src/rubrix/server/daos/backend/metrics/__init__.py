from .commons import METRICS as COMMON_METRICS
from .text_classification import METRICS as TEXT_CLASSIFICATION
from .token_classification import METRICS as TOKEN_CLASSIFICATION

ALL_METRICS = {**COMMON_METRICS, **TEXT_CLASSIFICATION, **TOKEN_CLASSIFICATION}
