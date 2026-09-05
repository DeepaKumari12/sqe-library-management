# Test Plan — SQE Library Management System

## 1. Introduction
This document is the Test Plan for the `sqe-library-management` project (repo: `DeepaKumari12/sqe-library-management`, `main` branch). The system currently implements a single core capability — `Book.borrow()` — with validation logic guarding against empty borrower names and double-borrowing. Several additional requirements exist as open, triaged backlog issues (`docs/triage-log.md`, issues #15–#19) that describe both defects in the current implementation and functionality not yet built (notably `return_book()`). This plan defines how the existing and near-term planned behavior of the `Book` class will be verified.

## 2. Test Items
- `src/library/book.py` → `Book.borrow(self, borrower)`
- `Book` constructor (validation of `item_id` and `title` at creation time)
- Planned: `Book.return_book()` (not yet implemented — Issue #17, Critical/P0)

## 3. Features to be Tested
- Borrowing a book with a valid borrower name (REQ-1)
- Rejection of empty/None borrower names (REQ-2)
- Prevention of double-borrowing, including bypass attempts via direct attribute assignment (REQ-3)
- Rejection of duplicate `item_id` values at construction (REQ-4)
- Returning a borrowed book once `return_book()` exists (REQ-5)
- Case-insensitive borrower name handling (REQ-6)
- Rejection of an empty string as a book title (REQ-7)

## 4. Features Not to be Tested
- **UI is out of scope for this document** — this is a library module, not an end-user application; there is no UI layer in the repository to exercise.
- **Persistence/database behavior is out of scope** — the current codebase holds state in memory only (plain Python objects); no database or file-persistence layer exists to test.
- **Fine calculation and borrow-limit enforcement are out of scope for this cycle** — neither exists in the codebase yet and there is no tracked issue defining their behavior, so there is nothing verifiable to test against.

## 5. Approach
Testing will be primarily functional, unit-level, black-box testing of the `Book` class using `pytest`, executed both automatically (where implemented) and manually against the current build (for behavior not yet coded). Each test case traces to a requirement derived either from existing code behavior or an open triage-log issue. Negative/error-path cases are prioritized given the class's role in enforcing borrowing invariants. A minimum of 3 of the 12 test cases in Task 2 are negative tests.

## 6. Pass/Fail Criteria
- A test case **passes** if the actual result matches the expected result exactly (including the exact exception type raised, where applicable).
- The release/cycle is considered **test-complete** when: 95% of the 12 planned test cases pass, and zero Critical or High severity defects remain open.
- Test cases targeting not-yet-implemented functionality (e.g., `return_book()`) are expected to **fail** or be marked **Blocked** until Issue #17 is resolved; this is tracked, not treated as a release blocker for the current sprint scope.

## 7. Test Deliverables
- `docs/test-plan.md` (this document)
- `docs/test-cases.md` — 12 fully specified test cases
- `docs/rtm.md` — requirements traceability matrix
- Execution results (Pass/Fail/Blocked per test case) with linked GitHub Issues for failures

## 8. Environmental Needs
- Python 3.10+
- `pytest` for automated execution
- Local clone of `DeepaKumari12/sqe-library-management` (`main` branch)
- GitHub access to the repository's Issues for defect filing

## 9. Schedule
Aligned to the 3-hour lab session: Test Plan (60 min) → Test Cases (75 min) → RTM (30 min) → Manual Execution Pass (35 min).

## 10. Risks
- **Scope drift risk**: several requirements (REQ-5, REQ-6, REQ-7) describe behavior that is either unimplemented or explicitly deprioritized ("won't fix this sprint"), so test cases for them will legitimately fail or block — this must not be mistaken for test-writing error.
- **Traceability risk**: because functionality is thin, there is a risk of writing redundant test cases against the same method to reach the 12-case quota rather than genuinely new coverage; mitigated by mapping each case to a distinct requirement/edge case in the RTM.
- **Environment risk**: no CI pipeline exists yet in this repo, so all execution in this cycle is manual, increasing the chance of inconsistent results between runs.