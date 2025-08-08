
# logic-grp — Cookbook Additions

## Before/After: Feature Flags
**Ohne `group_logic`:**
```python
user_is_beta = True
env_is_staging = False
country_allowed = True
quota_ok = True

if (user_is_beta and (env_is_staging or country_allowed)) and quota_ok:
    enable_feature = True
else:
    enable_feature = False
```
**Mit `group_logic`:**
```python
from group_logic import logic

gates_all = [quota_ok]
gates_any = [env_is_staging, country_allowed]

enable_feature = logic([user_is_beta, logic(gates_any, "OR"), logic(gates_all, "AND")], "AND")
```

## Before/After: Voting (exactly one)
```python
from group_logic import logic
votes = [True, False, False, False]
approve_exactly_one = logic(votes, "XOR")
```

## Threshold Helpers
```python
from group_logic import count_true, exactly, at_least, at_most, majority

flags = [True, False, True, True]

count_true(flags)        # 3
exactly(2, flags)        # False
at_least(2, flags)       # True
at_most(1, flags)        # False
majority(flags)          # True (3/4)
```
