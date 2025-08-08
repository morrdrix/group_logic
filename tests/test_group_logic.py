import pytest
from group_logic import *

@pytest.mark.parametrize("func, true_input, false_input, description", [
    (and_, [True, True], [True, False], "AND True/False"),
    (or_, [True, False], [False, False], "OR True/False"),
    (xor_, [True, False, False], [True, True, False], "XOR True/False"),
    (nor_, [False, False], [False, True], "NOR True/False"),
    (nand_, [True, False], [True, True], "NAND True/False"),
    (xnor_, [True, True], [True, False], "XNOR True/False"),
    (none_, [False, False], [True, False], "NONE alias"),
    (not_all_, [True, False], [True, True], "NOT_ALL alias"),
    (all_equal_, [True, True], [True, False], "ALL_EQUAL alias"),
])
def test_bool_logic(func, true_input, false_input, description):
    assert func(true_input), f"{description} should be True"
    assert not func(false_input), f"{description} should be False"

@pytest.mark.parametrize("func, true_input, false_input, description", [
    (and_, [1, 1], [1, 0], "AND int"),
    (or_, [1, 0], [0, 0], "OR int"),
    (xor_, [1, 0, 0], [1, 1, 0], "XOR int"),
    (nor_, [0, 0], [0, 1], "NOR int"),
    (nand_, [1, 0], [1, 1], "NAND int"),
    (xnor_, [1, 1], [1, 0], "XNOR int"),
    (none_, [0, 0], [1, 0], "NONE alias int"),
    (not_all_, [1, 0], [1, 1], "NOT_ALL alias int"),
    (all_equal_, [1, 1], [1, 0], "ALL_EQUAL alias int"),
])
def test_int_logic(func, true_input, false_input, description):
    assert func(true_input), f"{description} should be True"
    assert not func(false_input), f"{description} should be False"

@pytest.mark.parametrize("func, empty_input", [
    (and_, []),
    (or_, []),
    (xor_, []),
    (nor_, []),
    (nand_, []),
    (xnor_, []),
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
    result = logic_(sample, mode)
    assert result == expected, f"Wrapper mode {mode} returned {result}, expected {expected}"

def test_wrapper_invalid_mode():
    with pytest.raises(ValueError):
        logic_([True], 'UNKNOWN')
