# Requirements Traceability Matrix — SQE Library Management System

| Requirement ID | Requirement Description | Linked Test Case(s) | Test Case Count | Status |
|---|---|---|---|---|
| REQ-1 | System shall allow `Book.borrow()` to mark a book as borrowed by a valid borrower | TC-001 | 1 | ✅ Traced |
| REQ-2 | System shall reject `borrow()` when borrower name is empty/None | TC-002, TC-003, TC-004 | 3 | ✅ Traced |
| REQ-3 | System shall prevent double-borrowing, including bypass via direct attribute manipulation (Issue #15) | TC-005, TC-006 | 2 | ✅ Traced |
| REQ-4 | System shall prevent duplicate `item_id` values on Book creation (Issue #16) | TC-007, TC-008 | 2 | ✅ Traced |
| REQ-5 | System shall provide a `return_book()` capability for borrowed books (Issue #17, Critical) | TC-009, TC-010 | 2 | ⚠️ Traced but currently unimplemented — tests Blocked |
| REQ-6 | Borrower name comparisons shall be case-insensitive (Issue #19) | TC-011 | 1 | ⚠️ Traced but "won't fix this sprint" — test expected to Fail |
| REQ-7 | Book constructor shall reject an empty string as a valid title (Issue #18) | TC-012 | 1 | ⚠️ Traced but "won't fix this sprint" — test expected to Fail |

## Coverage Gap Check

**Requirements with zero linked test cases:** None. All 7 requirements (REQ-1 through REQ-7) have at least one linked test case — no orphan requirements were found.

**Orphan test cases (tests with no requirement):** None. All 12 test cases (TC-001–TC-012) map back to exactly one requirement.

Because no coverage gap exists in this cycle, no additional test case was required to close a gap. Instead, the matrix surfaces a **different kind of risk**: REQ-5, REQ-6, and REQ-7 are traced but map to functionality that is either unimplemented (`return_book()`, Issue #17) or explicitly deprioritized this sprint (Issues #18, #19). These are not testing gaps — they are **implementation gaps** that the RTM makes visible: the requirement is defined and a test exists, but the system cannot yet satisfy it. This distinction is tracked in the Status column so that a Fail/Blocked result on TC-009 through TC-012 during execution is correctly read as "known, expected" rather than a new defect.