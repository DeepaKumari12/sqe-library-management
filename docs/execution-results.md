# Manual/Automated Execution Results — SQE Library Management System

Executed against `src/library/book.py` on the `fix-double-borrow` branch using `pytest`. A minimal `Book.__init__` was added to make the file importable/testable (the committed `book.py` only contained the `borrow()` method with no class wrapper); this constructor sets `title`, `item_id`, `author`, `status="available"`, `borrower=None` and adds no other logic, so it does not change any test outcome below.

| ID | Requirement | Result | Note | Linked Issue |
|---|---|---|---|---|
| TC-001 | REQ-1 | ✅ Pass | Valid borrow sets status/borrower correctly | — |
| TC-002 | REQ-2 | ✅ Pass | Empty string borrower correctly rejected | — |
| TC-003 | REQ-2 | ✅ Pass | `None` borrower correctly rejected | — |
| TC-004 | REQ-2 | ✅ Pass | Whitespace-only borrower correctly rejected | — |
| TC-005 | REQ-3 | ✅ Pass | Second borrow on an already-borrowed book correctly rejected | — |
| TC-006 | REQ-3 | ✅ Pass | Attribute-manipulation bypass still caught by the `borrower is not None` check | — |
| TC-007 | REQ-4 | ❌ Fail | Creating a second `Book` with a duplicate `item_id` raises no error — no enforcement exists anywhere in the codebase | Issue #16 |
| TC-008 | REQ-4 | ✅ Pass | Two books with distinct `item_id` values create successfully | — |
| TC-009 | REQ-5 | ❌ Fail | `AttributeError: 'Book' object has no attribute 'return_book'` — method does not exist | Issue #17 |
| TC-010 | REQ-5 | ❌ Fail | Same as TC-009 — `return_book()` not implemented | Issue #17 |
| TC-011 | REQ-6 | ❌ Fail | Borrower comparison is case-sensitive; `"aisha khan"` != `"Aisha Khan"` | Issue #19 |
| TC-012 | REQ-7 | ❌ Fail | Constructing a `Book` with `title=""` raises no error | Issue #18 |

## Summary
- **Total:** 12 | **Pass:** 7 | **Fail:** 5 | **Blocked:** 0
- **Pass rate:** 58.3% — below the 95% Pass/Fail Criteria defined in the Test Plan.
- All 5 failures map to **pre-existing, already-triaged issues** (#16, #17, #18, #19) documented in `docs/triage-log.md` prior to this lab — no new defects were discovered during this execution pass.
- Per the triage log, Issue #17 (`return_book()` missing) is Critical/P0 and should be prioritized to close before the pass rate can meet the 95% criterion; #16 is High/P1; #18 and #19 are explicitly "Won't fix this sprint" and are expected to remain Fail/red until re-prioritized.

## GitHub Issues
No new issues were filed, as every failure traces to an issue already open in the repository's issue tracker (#16, #17, #18, #19) — the corresponding rows above link to those existing issue numbers rather than duplicating them.