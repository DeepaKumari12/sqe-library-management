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
