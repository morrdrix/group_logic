"""
group_logic – grouped boolean operations with a tiny, consistent API.
"""

from __future__ import annotations

import sys

# ---- Runtime guard (matches pyproject's requires-python) --------------------
if sys.version_info < (3, 8):
    raise RuntimeError(
        "logic-grp requires Python >= 3.8. "
        f"Detected: {sys.version.split()[0]}"
    )

# ---- Package version (best effort) -----------------------------------------
try:
    # Python 3.8+: importlib.metadata is in stdlib (backport not needed)
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
    try:
        # NOTE: use your distribution name on PyPI here:
        __version__ = version("logic-grp")
    except PackageNotFoundError:
        __version__ = "0.0.0"
except Exception:  # extremely defensive
    __version__ = "0.0.0"

# ---- Public API re-exports --------------------------------------------------
from .ops import (
    # core ops
    and_,
    or_,
    xor_,
    nor_,
    nand_,
    xnor_,
    nxor_,
    all_equal_,
    none_,
    one_,
    all_,
    not_all_,
    # dispatcher
    logic,
    SUPPORTED_MODES,
    # threshold helpers
    count_true,
    count_false,
    exactly,
    at_least,
    at_most,
    majority,
)

# Explicit export surface for `from group_logic import *`
__all__ = [
    # core ops
    "and_",
    "or_",
    "xor_",
    "nor_",
    "nand_",
    "xnor_",
    "nxor_",
    "all_equal_",
    "none_",
    "one_",
    "all_",
    "not_all_",
    # dispatcher
    "logic",
    "SUPPORTED_MODES",
    # helpers
    "count_true",
    "count_false",
    "exactly",
    "at_least",
    "at_most",
    "majority",
    # metadata
    "__version__",
]
