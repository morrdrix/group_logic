# group_logic

A small utility package to apply grouped logical operations (`AND`, `OR`, `XOR`, `NOR`, `NAND`, `XNOR`, `NONE`, `NOT_ALL`, `ALL_EQUAL`) on lists of values.

## Installation
```bash
pip install group_logic
```

## Usage
```python
from group_logic import logic

# Wrapper
logic([1, 1, 0], "AND")   # False
```

## Tests
```bash
pytest
```
