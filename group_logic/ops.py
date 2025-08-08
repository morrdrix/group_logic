"""
Core logic functions for grouped boolean operations with type annotations.
Supports iterables (lists, tuples, etc.) und scalars als Edge‑Cases.
"""
from typing import Any, Iterable, Union, Callable, Mapping
from types import MappingProxyType
from collections.abc import Iterable as _Iterable

def _ensure_iterable(values: Union[Any, _Iterable]) -> Iterable:
    """
    Wrap scalars (inkl. str/bytes) in a list; leave andere Iterables.
    Strings/bytes werden als Skalar behandelt, um nicht über einzelne Zeichen zu iterieren.
    """
    if isinstance(values, (str, bytes)) or not isinstance(values, _Iterable):
        return [values]
    return values  # already iterable

def and_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if all elements evaluate to True."""
    return all(bool(x) for x in _ensure_iterable(values))

def or_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if any element evaluates to True."""
    return any(bool(x) for x in _ensure_iterable(values))

def xor_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if exactly one element evaluates to True."""
    return sum(bool(el) for el in _ensure_iterable(values)) == 1

def nor_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if no element evaluates to True."""
    return not or_(values)

def nand_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if at least one element evaluates to False."""
    return not and_(values)

def xnor_(values: Union[Any, _Iterable]) -> bool:
    """Returns True if all elements have the same boolean value."""
    mask = 0
    for v in _ensure_iterable(values):
        mask |= 1 if bool(v) else 2  # True -> 1, False -> 2
        if mask == 3:                # both seen
            return False
    return True

# Aliases
none_ = nor_
not_all_ = nand_
all_equal_ = xnor_

# Imutable Dispatch-Map (Case-insensitive)
_LOGIC_FUNCS: Mapping[str, Callable[[Any], bool]] = MappingProxyType({
    'AND': and_,
    'OR': or_,
    'XOR': xor_,
    'NOR': nor_,
    'NONE': none_,
    'NAND': nand_,
    'NOT_ALL': not_all_,
    'XNOR': xnor_,
    'ALL_EQUAL': all_equal_,
})


SUPPORTED_MODES = tuple(_LOGIC_FUNCS.keys())

def logic(values: Union[Any, _Iterable], mode: str = 'AND') -> bool:
    """
    Wrapper to call any grouped logic function by name.

    :param values: scalar or iterable of values
    :param mode: one of 'AND', 'OR', 'XOR', 'NOR', 'NONE', 'NAND', 'NOT_ALL', 'XNOR', 'ALL_EQUAL'
    :raises ValueError: if mode is unknown
    """

    key = mode.upper()
    if key not in _LOGIC_FUNCS:
        raise ValueError(f"Unknown logic mode: {mode}. Supported modes: {SUPPORTED_MODES}")
    return _LOGIC_FUNCS[key](values)
