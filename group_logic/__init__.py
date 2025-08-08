"""logic_grp package"""
import sys
if sys.version_info < (3, 8):
    raise RuntimeError(
        "logic-grp requires Python >= 3.8. "
        f"Detected: {sys.version.split()[0]}"
    )

from .ops import logic, and_, or_, xor_, nor_, nand_, xnor_, all_equal_  # re-export
__all__ = ["logic", "and_", "or_", "xor_", "nor_", "nand_", "xnor_", "all_equal_"]