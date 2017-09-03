"""
Main package
"""

from ._version import __version__, __version_info__
from ._util import Decorated
from .decorators import (
    after,
    before,
    construct_decorator,
    decorate,
    instead,
    intercept,
    log_call,
    memoize,
)
