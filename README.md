# logic-grp

A small utility package to apply grouped logical operations (`AND`, `OR`, `XOR`, `NOR`, `NAND`, `XNOR`, `NONE`, `NOT_ALL`, `ALL_EQUAL`) on lists of values.

## Installation
```bash
pip install logic-grp
```

## Usage
```python
from logic_grp import core

# Einzel-Operationen
core.and_grp([True, True, False])      # False
core.or_grp([0, 0, 3])                  # True
core.xor_grp([True, False, False])      # True

# Wrapper
core.logic_grp([1, 1, 0], mode='AND')   # True
```

## Tests
```bash
pytest
```
