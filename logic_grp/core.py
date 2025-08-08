"""
Core logic functions for grouped boolean operations with type annotations.
Supports iterables (lists, tuples, etc.) und scalars als Edge‑Cases.
"""
from typing import Any, Iterable, Union, Callable, Dict
from collections.abc import Iterable as _Iterable

def _ensure_iterable(values: Union[Any, _Iterable]) -> Iterable:
    """
    Wrap scalars (inkl. str/bytes) in a list; leave andere Iterables.
    Strings/bytes werden als Skalar behandelt, um nicht über einzelne Zeichen zu iterieren.
    """
    if isinstance(values, (str, bytes)) or not isinstance(values, _Iterable):
        return [values]
    return values  # already iterable

def and_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if all elements evaluate to True."""
    seq = list(_ensure_iterable(values))
    return bool(seq) and all(bool(el) for el in seq)

def or_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if any element evaluates to True."""
    seq = list(_ensure_iterable(values))
    return bool(seq) and any(bool(el) for el in seq)

def xor_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if exactly one element evaluates to True."""
    seq = list(_ensure_iterable(values))
    return sum(bool(el) for el in seq) == 1

def nor_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if no element evaluates to True."""
    return not or_grp(values)

def nand_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if at least one element evaluates to False."""
    return not and_grp(values)

def xnor_grp(values: Union[Any, _Iterable]) -> bool:
    """Returns True if all elements have the same boolean value."""
    seq = list(_ensure_iterable(values))
    return bool(seq) and all(bool(el) == bool(seq[0]) for el in seq)

# Aliases
none_grp = nor_grp
not_all_grp = nand_grp
all_equal_grp = xnor_grp

def logic_grp(values: Union[Any, _Iterable], mode: str = 'AND') -> bool:
    """
    Wrapper to call any grouped logic function by name.

    :param values: scalar or iterable of values
    :param mode: one of 'AND', 'OR', 'XOR', 'NOR', 'NONE', 'NAND', 'NOT_ALL', 'XNOR', 'ALL_EQUAL'
    :raises ValueError: if mode is unknown
    """
    logic_map: Dict[str, Callable] = {
        'AND': and_grp,
        'OR': or_grp,
        'XOR': xor_grp,
        'NOR': nor_grp,
        'NONE': none_grp,
        'NAND': nand_grp,
        'NOT_ALL': not_all_grp,
        'XNOR': xnor_grp,
        'ALL_EQUAL': all_equal_grp,
    }
    key = mode.upper()
    if key not in logic_map:
        raise ValueError(f"Unknown logic mode: {mode}. Supported modes: {', '.join(logic_map)}")
    return logic_map[key](values)
