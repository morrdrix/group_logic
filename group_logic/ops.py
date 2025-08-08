"""
Core logic functions for grouped boolean operations with type annotations.
Supports iterables (lists, tuples, etc.) and scalars as edge cases.
Python >= 3.8. No external dependencies.
"""
from typing import Any, Callable, Mapping
from types import MappingProxyType
from collections.abc import Iterable as _Iterable

def _ensure_iterable(values: Any) -> _Iterable:
    """
    Wrap scalars (inkl. str/bytes) in a list; leave andere Iterables.
    Strings/bytes werden als Skalar behandelt, um nicht über einzelne Zeichen zu iterieren.
    """
    if isinstance(values, (str, bytes)) or not isinstance(values, _Iterable):
        return [values]
    return values  # already iterable

def and_(values: Any) -> bool:
    """Returns True if all elements evaluate to True."""
    return all(bool(x) for x in _ensure_iterable(values))

def or_(values: Any) -> bool:
    """Returns True if any element evaluates to True."""
    return any(bool(x) for x in _ensure_iterable(values))

def xor_(values: Any) -> bool:
    """Returns True if exactly one element evaluates to True."""
    return sum(bool(el) for el in _ensure_iterable(values)) == 1

def nor_(values: Any) -> bool:
    """Returns True if no element evaluates to True."""
    return not or_(values)

def nand_(values: Any) -> bool:
    """Returns True if at least one element evaluates to False."""
    return not and_(values)

def xnor_(values: Any) -> bool:
    """Returns True if all elements have the same boolean value."""
    mask = 0
    for v in _ensure_iterable(values):
        mask |= 1 if bool(v) else 2  # True -> 1, False -> 2
        if mask == 3:                # both seen
            return False
    return True

# Aliases
none_ = nor_
all_= and_
not_all_ = nand_
all_equal_ = xnor_
one_ = xor_
nxor_ = xnor_



# Immutable Dispatch-Map (Case-insensitive)
_LOGIC_FUNCS: Mapping[str, Callable[[Any], bool]] = MappingProxyType({
    'AND': and_,
    'NAND': nand_,
    'OR': or_,
    'NOR': nor_,
    'XOR': xor_,
    'XNOR': xnor_,
    'NXOR': nxor_,
    'NONE': none_,
    'ONE':one_,
    'ALL': all_,
    'NOT_ALL': not_all_,    
    'ALL_EQUAL': all_equal_,
})


SUPPORTED_MODES = tuple(_LOGIC_FUNCS.keys())

def logic(values: Any, mode: str = 'AND') -> bool:
    """
    Wrapper to call any grouped logic function by name.

    :param values: scalar or iterable of values
    :param mode: one of 'AND', 'OR', 'XOR', 'NOR', 'NONE', 'NAND', 'NOT_ALL', 'XNOR', 'ALL_EQUAL'
    :raises ValueError: if mode is unknown
    """

    key = mode.strip().upper()
    if key not in _LOGIC_FUNCS:
        raise ValueError(f"Unknown logic mode: {key!r}. Supported modes: {', '.join(SUPPORTED_MODES)}")
    return _LOGIC_FUNCS[key](values)


# ----- Threshold helpers (cover common business logic) -----

def count_true(values: Any) -> int:
    """Return the number of truthy items."""
    return sum(1 for x in _ensure_iterable(values) if bool(x))
    
def count_false(values: Any) -> int:
    """Return the number of falsy items."""
    return sum(1 for x in _ensure_iterable(values) if not bool(x))

def exactly(n: int, values: Any) -> bool:
    """True if exactly n items are truthy."""
    if n < 0:
        return False
    return count_true(values) == n

def at_least(n: int, values: Any) -> bool:
    """True if at least n items are truthy."""
    if n <= 0:
        return True
    seen = 0
    for x in _ensure_iterable(values):
        if bool(x):
            seen += 1
            if seen >= n:
                return True
    return False

def at_most(n: int, values: Any) -> bool:
    """True if at most n items are truthy."""
    if n < 0:
        return False
    seen = 0
    for x in _ensure_iterable(values):
        if bool(x):
            seen += 1
            if seen > n:
                return False
    return True

def majority(values: Any) -> bool:
    """True if strictly more than half of the items are truthy.

    Empty input -> False (no majority can be established).
    """
    it = list(_ensure_iterable(values))
    total = len(it)
    if total == 0:
        return False
    # Early-exit scan
    needed = total // 2 + 1
    seen = 0
    remaining = total
    for x in it:
        if bool(x):
            seen += 1
            if seen >= needed:
                return True
        remaining -= 1
        # Even if all remaining were True, can we still reach 'needed'?
        if seen + remaining < needed:
            return False

    return False
