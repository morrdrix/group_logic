import pytest
from logic_grp.core import *

@pytest.mark.parametrize("func, true_input, false_input, description", [
    (and_grp, [True, True], [True, False], "AND True/False"),
    (or_grp, [True, False], [False, False], "OR True/False"),
    (xor_grp, [True, False, False], [True, True, False], "XOR True/False"),
    (nor_grp, [False, False], [False, True], "NOR True/False"),
    (nand_grp, [True, False], [True, True], "NAND True/False"),
    (xnor_grp, [True, True], [True, False], "XNOR True/False"),
    (none_grp, [False, False], [True, False], "NONE alias"),
    (not_all_grp, [True, False], [True, True], "NOT_ALL alias"),
    (all_equal_grp, [True, True], [True, False], "ALL_EQUAL alias"),
])
def test_bool_logic(func, true_input, false_input, description):
    assert func(true_input), f"{description} should be True"
    assert not func(false_input), f"{description} should be False"

@pytest.mark.parametrize("func, true_input, false_input, description", [
    (and_grp, [1, 1], [1, 0], "AND int"),
    (or_grp, [1, 0], [0, 0], "OR int"),
    (xor_grp, [1, 0, 0], [1, 1, 0], "XOR int"),
    (nor_grp, [0, 0], [0, 1], "NOR int"),
    (nand_grp, [1, 0], [1, 1], "NAND int"),
    (xnor_grp, [1, 1], [1, 0], "XNOR int"),
    (none_grp, [0, 0], [1, 0], "NONE alias int"),
    (not_all_grp, [1, 0], [1, 1], "NOT_ALL alias int"),
    (all_equal_grp, [1, 1], [1, 0], "ALL_EQUAL alias int"),
])
def test_int_logic(func, true_input, false_input, description):
    assert func(true_input), f"{description} should be True"
    assert not func(false_input), f"{description} should be False"

@pytest.mark.parametrize("func, empty_input", [
    (and_grp, []),
    (or_grp, []),
    (xor_grp, []),
    (nor_grp, []),
    (nand_grp, []),
    (xnor_grp, []),
])
def test_empty_list(func, empty_input):
    assert not func(empty_input), f"{func.__name__}([]) should be False"

@pytest.mark.parametrize("mode, expected", [
    ('AND', True),
    ('OR', True),
    ('XOR', False),
    ('NOR', False),
    ('NONE', False),
    ('NAND', False),
    ('NOT_ALL', False),
    ('XNOR', True),
    ('ALL_EQUAL', True),
])
def test_wrapper_various_modes(mode, expected):
    sample = [True, True, True]
    result = logic_grp(sample, mode)
    assert result == expected, f"Wrapper mode {mode} returned {result}, expected {expected}"

def test_wrapper_invalid_mode():
    with pytest.raises(ValueError):
        logic_grp([True], 'UNKNOWN')
