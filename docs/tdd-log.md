# TDD Log — Lab 8: Test-Driven Development with GitHub

**Feature:** `rank_books_by_popularity(library)`
**Branch:** `feature/rank-books-tdd`
**Student:** Deepa Kumari
**Repo:** https://github.com/DeepaKumari12/sqe-library-management

---

## TDD Cycles Summary

| Cycle | Description | Red Commit | Green Commit | Refactor Commit |
|-------|-------------|------------|--------------|-----------------|
| 1 | Empty catalog returns empty list | `2616c2e` | `dbe1aa8` | *(none — trivial stage)* |
| 2 | Single book returned in list | `6e2e4dc` | `eb09dbc` | `f06b85d` |
| 3 | Descending sort by borrow count | `0bce034` | `0f80cec` | `2ae504f` |
| 4 | Tie-break by title alphabetically | `0e161c6` | `4d03657` | `1827cff` |
| 5 | Case-insensitive title tie-break | `2390cf2` | `0c03058` | `939931a` |

**Full regression status:** 52 passed in 0.18s (all previous labs + Lab 8).

---

## Cycle Details

### Cycle 1 — Empty Catalog
- **RED (`2616c2e`):** `test_rank_books_empty_catalog_returns_empty_list` — failed because `rank_books_by_popularity` did not exist.
- **GREEN (`dbe1aa8`):** Added a stub returning `[]`.
- **REFACTOR:** Nothing to refactor at this trivial stage.

### Cycle 2 — Single Book
- **RED (`6e2e4dc`):** Test that a library with one book returns a list containing just that book.
- **GREEN (`eb09dbc`):** Minimal implementation returning books from the catalog.
- **REFACTOR (`f06b85d`):** Named the catalog books list for clarity.

### Cycle 3 — Descending Sort by Borrow Count
- **RED (`0bce034`):** Test with books of distinct borrow counts; asserted highest-to-lowest order.
- **GREEN (`0f80cec`):** Implemented `sorted(..., key=lambda b: b.borrow_count, reverse=True)`.
- **REFACTOR (`2ae504f`):** Extracted repeated "build a book with this borrow count" logic into a `make_book` pytest helper.

### Cycle 4 — Tie-Break by Title
- **RED (`0e161c6`):** Test with two books having identical borrow counts but different titles; asserted alphabetical order.
- **GREEN (`4d03657`):** Extended sort key to sort by title on ties.
- **REFACTOR (`1827cff`):** Extracted `_popularity_sort_key` for readability.

### Cycle 5 — Case-Insensitive Tie-Break (Own Edge Case)
- **RED (`2390cf2`):** Test where two books share borrow count but differ in title case (e.g. `"Zebra"` vs `"apple"`) — asserted alphabetical order ignoring case.
- **GREEN (`0c03058`):** Initial fix for case-insensitive tie-break.
- **REFACTOR (`939931a`):** Fixed `_popularity_sort_key` to return a proper `(-borrow_count, title.lower())` tuple — resolved `TypeError: '<' not supported between NoneType`.

---

## TDD Retrospective

Working test-first fundamentally changed how I approached this feature compared to my usual implementation-first style. In previous labs I would write the whole `rank_books_by_popularity()` function in one go, then bolt on tests afterwards — which often meant my tests just confirmed whatever the code already did, rather than defining what it *should* do. With TDD, each cycle forced me to articulate the expected behaviour in a failing test before writing a single line of production code, so the tests genuinely drove the design instead of merely documenting it.

The Red-Green-Refactor rhythm also kept my commits small and meaningful. Instead of one giant commit at the end, I ended up with a clear audit trail of Red → Green → Refactor steps that makes the feature's evolution easy to review. The "minimum code to pass" rule was the hardest discipline to follow — I constantly wanted to generalise early — but resisting that urge meant every line of production code existed because a test demanded it. Refactoring under a passing suite felt safe and low-risk, and when I extended the sort key in Cycle 4, re-running the full regression suite immediately caught nothing broken, which gave me real confidence. Overall, TDD produced a simpler, more testable design and a test suite I actually trust, because I watched every test fail before it passed.
