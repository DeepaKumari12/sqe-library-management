# TDD Log — Lab 8: Test-Driven Development with GitHub

**Feature:** `rank_books_by_popularity(library)`
**Branch:** `feature/rank-books-tdd`
**Student:** Deepa Kumari
**Repo:** https://github.com/DeepaKumari12/sqe-library-management

---

## TDD Cycles Summary

| Cycle | Description | Red Commit | Green Commit | Refactor Commit |
|-------|-------------|------------|--------------|-----------------|
| 1 | Empty catalog returns empty list | `<red-hash-1>` | `<green-hash-1>` | `<refactor-hash-1>` |
| 2 | Single book returns that book | `<red-hash-2>` | `<green-hash-2>` | `<refactor-hash-2>` |
| 3 | Descending sort by borrow count | `<red-hash-3>` | `<green-hash-3>` | `<refactor-hash-3>` |
| 4 | Tie-breaking by title (alphabetical) | `<red-hash-4>` | `<green-hash-4>` | `<refactor-hash-4>` |
| 5 | Edge case: book with zero borrows | `<red-hash-5>` | `<green-hash-5>` | `<refactor-hash-5>` |

---

## Cycle Details

### Cycle 1 — Empty Catalog
- **RED:** `test_rank_books_empty_catalog_returns_empty_list` — failed because `rank_books_by_popularity` did not exist.
- **GREEN:** Added a stub returning `[]`.
- **REFACTOR:** Nothing to refactor at this trivial stage.

### Cycle 2 — Single Book
- **RED:** Test that a library with one book returns a list containing just that book.
- **GREEN:** Minimal implementation returning `[book]` when catalog has one entry.
- **REFACTOR:** Reviewed naming; no duplication yet.

### Cycle 3 — Descending Sort by Borrow Count
- **RED:** Test with 3 books of distinct borrow counts; asserted highest-to-lowest order.
- **GREEN:** Implemented `sorted(..., key=lambda b: b.borrow_count, reverse=True)`.
- **REFACTOR:** Extracted repeated "build a book with this borrow count" logic into a pytest fixture.

### Cycle 4 — Tie-Breaking by Title
- **RED:** Test with two books having identical borrow counts but different titles; asserted alphabetical order.
- **GREEN:** Extended sort key to `(-borrow_count, title)`.
- **REFACTOR:** Re-ran the **entire** test suite (all previous labs) — no regressions.

### Cycle 5 — Edge Case: Zero-Borrow Book
- **RED:** Test mixing a never-borrowed book with borrowed books; asserted it sorts last.
- **GREEN:** Confirmed existing `(-borrow_count, title)` key already handles zero correctly.
- **REFACTOR:** Cleaned up test helper; full suite re-run passed.

---

## TDD Retrospective

Working test-first fundamentally changed how I approached this feature compared to my usual implementation-first style. In previous labs I would write the whole `rank_books_by_popularity()` function in one go, then bolt on tests afterwards — which often meant my tests just confirmed whatever the code already did, rather than defining what it *should* do. With TDD, each cycle forced me to articulate the expected behaviour in a failing test before writing a single line of production code, so the tests genuinely drove the design instead of merely documenting it.

The Red-Green-Refactor rhythm also kept my commits small and meaningful. Instead of one giant commit at the end, I ended up with a clear audit trail of Red → Green → Refactor steps that makes the feature's evolution easy to review. The "minimum code to pass" rule was the hardest discipline to follow — I constantly wanted to generalise early — but resisting that urge meant every line of production code existed because a test demanded it. Refactoring under a passing suite felt safe and low-risk, and when I extended the sort key in Cycle 4, re-running the full regression suite immediately caught nothing broken, which gave me real confidence. Overall, TDD produced a simpler, more testable design and a test suite I actually trust, because I watched every test fail before it passed.