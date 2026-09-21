# Boundary Value Analysis - LibraryHub (Lab 6)

Tools: Python, pytest. Extends the Equivalence Partitioning in `docs/ep-analysis.md`.
For every boundary the values value-1, value and value+1 are tested.

## 1. fine_tier(days_overdue)

Tiers: 0 = 'None', 1-7 = 'Low', 8-14 = 'Medium', 15-30 = 'High', 31+ = 'Severe'.
Negative values raise ValueError. Cut-off values in the code: 0, 1, 8, 15, 31.

| Boundary | value-1 -> expected | value -> expected | value+1 -> expected |
|---|---|---|---|
| Domain edge (0) | -1 -> ValueError | 0 -> 'None' | 1 -> 'Low' |
| 0 / 1 | 0 -> 'None' | 1 -> 'Low' | 2 -> 'Low' |
| 7 / 8 | 7 -> 'Low' | 8 -> 'Medium' | 9 -> 'Medium' |
| 14 / 15 | 14 -> 'Medium' | 15 -> 'High' | 16 -> 'High' |
| 30 / 31 | 30 -> 'High' | 31 -> 'Severe' | 32 -> 'Severe' |

## 2. Library.borrow_book() - books-on-loan limit (0 to 5 valid)

The limit is MAX_BOOKS_PER_MEMBER = 5. A member who already holds 5 books must be rejected with ValueError.

| Boundary | Books currently on loan | Attempt: borrow one more -> expected |
|---|---|---|
| limit - 1 | 4 | succeeds, count becomes 5 |
| limit | 5 | raises ValueError, count stays 5 |
| limit + 1 | 6 | raises ValueError, count stays 6 |

Note: a member cannot reach 6 books through borrow_book(), so the test sets library.member_loans["M1"] = 6 directly.


## 3. validate_isbn(isbn) - exactly 13 digits

validate_isbn returns True / False (it does not raise an exception).

| Boundary | value-1 -> expected | value -> expected | value+1 -> expected |
|---|---|---|---|
| Length 13 | 12 digits -> False | 13 digits -> True | 14 digits -> False |
| Extra points | 11 digits -> False | - | 15 digits -> False |

## 4. fine_tier() - values immediately next to the boundaries (non-integer days)

BVA also checks the values just below/above a cut-off. For a numeric input this includes fractional values.

| Boundary | Input | Expected | Actual before fix |
|---|---|---|---|
| 0 / 1 | 0.5 | rejected (TypeError) | 'Severe' (wrong) |
| 0 / 1 | 0.99 | rejected (TypeError) | 'Severe' (wrong) |
| 7 / 8 | 7.5 | rejected (TypeError) | 'Severe' (wrong) |
| 14 / 15 | 14.5 | rejected (TypeError) | 'Severe' (wrong) |
| 30 / 31 | 30.5 | rejected (TypeError) | 'Severe' (wrong) |

Test: `test_fine_tier_fractional_days_rejected` in `tests/test_fine_tier_bva.py`.

## Defect log (found through boundary testing)

| # | Function | Boundary | Expected | Actual (before fix) | Root cause | Fix | Issue / PR |
|---|---|---|---|---|---|---|---|
| 1 | fine_tier | 0.5, 0.99, 7.5, 14.5, 30.5 | reject non-integer days | returned 'Severe' | tier ranges cover whole numbers only, so fractions fall in the gaps and reach the final `return "Severe"` | fine_tier raises TypeError if days_overdue is not an int | Issue #28, fixed in PR #29 |
| - | Library.borrow_book | 4, 5, 6 books | as per table 2 | as per table 2 | - | no defect found | - |
| - | validate_isbn | lengths 11-15 | as per table 3 | as per table 3 | - | no defect found | - |

## Result

pytest -v: all 41 tests pass (Lab 5 EP tests + Lab 6 BVA tests) after the fix.