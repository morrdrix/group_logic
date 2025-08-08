# group-logic

[![PyPI](https://img.shields.io/pypi/v/logic-grp.svg)](https://pypi.org/project/logic-grp/)  
[![Python Versions](https://img.shields.io/pypi/pyversions/logic-grp.svg)](https://pypi.org/project/logic-grp/)  
[![License](https://img.shields.io/pypi/l/logic-grp.svg)](LICENSE)

> **Grouped logical operations on iterables** — with full type hints, scalar support, and a simple, consistent API.

---

## Features

- **Simple API**: `logic(seq, mode="AND")` for all grouped boolean ops.
- **Multiple modes**: AND, OR, XOR, NOR, NAND, XNOR/ALL_EQUAL, NONE, NOT_ALL.
- **Flexible input**: Works with lists, tuples, sets, generators, and scalars.
- **Edge-case aware**: Strings and bytes treated as scalars (not iterated by character).
- **Type-hinted**: Full Python type annotations.
- **No dependencies**: Pure Python, lightweight.

---

## Installation

```bash
pip install logic-grp
```

Requires **Python ≥ 3.8**.

---

## Quick Start
```python
from group_logic import logic, and_, or_, xor_, all_equal_

# Single operations
and_([True, True, False])        # False
or_([0, 0, 3])                   # True
xor_([True, False, False])       # True
all_equal_([1, 1, 1])            # True

# Wrapper
logic([1, 1, 0], mode='AND')       # False
logic([1, 0, 0], mode='OR')        # True
logic([1, 0, 0], mode='NONE')      # False
logic([1, 1, 1], mode='ALL_EQUAL') # True
```

---

## Supported Modes

| Mode         | Alias(es)       | Description                                     |
|--------------|-----------------|-------------------------------------------------|
| `AND`        | —               | True if **all** values are truthy               |
| `OR`         | —               | True if **any** value is truthy                  |
| `XOR`        | —               | True if **exactly one** value is truthy          |
| `NOR`        | `NONE`          | True if **no** value is truthy                   |
| `NAND`       | `NOT_ALL`       | True if **not all** values are truthy            |
| `XNOR`       | `ALL_EQUAL`     | True if all values have the **same** truthiness  |

Empty sequence semantics:  
- `AND([])` → `True` (vacuous truth)  
- `OR([])` → `False`  
- `ALL_EQUAL([])` → `True`  
(These rules are consistent with Python’s built-in `all()` / `any()`).

---

## Why use `logic-grp`?

While Python has `all()` and `any()`, this package adds:

- Named operations for **NAND**, **NOR**, **XOR**, and **XNOR** out of the box.
- Consistent scalar handling (strings as scalars, not iterables).
- A single `logic()` dispatcher for runtime-selectable modes.
- Clear, predictable semantics for empty inputs.

Perfect for:
- **Data pipelines**: compact boolean aggregations
- **Feature flags**: group conditions into a single check
- **Voting logic**: quickly evaluate counts & equality
- **Validation**: uniform checks across collections

---

## API Reference

### `and_(values)`
True if all elements are truthy. Scalars wrapped in a list internally.

### `or_(values)`
True if any element is truthy.

### `xor_(values)`
True if exactly one element is truthy.

### `nor_(values)`
True if no element is truthy.

### `nand_(values)`
True if at least one element is falsy.

### `xnor_(values)` / `all_equal_(values)`
True if all elements have the same truthiness.

### `logic(values, mode="AND")`
Dispatches to the corresponding operation by `mode`. Case-insensitive.  
Raises `ValueError` if `mode` is unsupported.

---

## Contributing

Pull requests are welcome!  
To set up a dev environment:

```bash
git clone https://github.com/morrdrix/group_logic.git
cd group_logic
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

---

## License

[MIT](LICENSE) © Julian Klein
