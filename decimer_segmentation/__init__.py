# -*- coding: utf-8 -*-

"""
DECIMER Segmentation Python Package.

Segmentation of chemical structure depictions from scientific literature.


For comments, bug reports or feature requests,
please raise an issue on our GitHub repository.
"""

import os

# Use Keras 2 instead of 3, see
# https://blog.tensorflow.org/2024/03/whats-new-in-tensorflow-216.html
os.environ['TF_USE_LEGACY_KERAS'] = "1"
del os

__version__ = "1.3.0"

__all__ = [
    "decimer_segmentation",
]

from .decimer_segmentation import *
from .complete_structure import *
