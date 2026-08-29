# Triage Log — v0.2

## Issue Prioritization

| Rank | Issue | Severity | Priority | Decision |
|------|-------|----------|----------|----------|
| 1 | #17 — No return_book() method exists — borrowed books can never be returned | Critical | P0 | Fix this sprint |
| 2 | #15 — borrow() allows double-borrowing to bypass status check via direct attribute assignment | High | P1 | Fix this sprint |
| 3 | #16 — Book constructor allows duplicate item_id values | High | P2 | Fix this sprint |
| 4 | #19 — Borrower name comparisons are case-sensitive, allowing inconsistent borrower records | Medium | P2 | Won't fix this sprint |
| 5 | #18 — Book constructor accepts an empty string as a valid title | Low | P3 | Won't fix this sprint |

## Triage Rationale

### 1. Issue #17 — Critical / P0

This issue is ranked first because borrowed books cannot be returned at all. It has critical technical impact and P0 priority, so it must be fixed immediately.

### 2. Issue #15 — High / P1

This issue can allow double-borrowing and bypass the intended borrowing status check. It has high severity and P1 priority because it can cause incorrect library records and should be fixed quickly.

### 3. Issue #16 — High / P2

Duplicate item_id values can create confusion between books and may result in incorrect book records. It is high severity, but its P2 priority places it below the more urgent P0 and P1 issues.

### 4. Issue #19 — Medium / P2

Case-sensitive borrower name comparison can create inconsistent borrower records. Its severity is medium and the problem does not prevent the main borrowing workflow, so it is deferred for this sprint.

### 5. Issue #18 — Low / P3

Allowing an empty book title is undesirable but has low technical impact. Since it is P3, it is the lowest priority and will not be fixed in this sprint.

## Severity vs Priority Trade-offs

Issue #16 has High severity but P2 priority. Although duplicate item IDs can affect data correctness, it is less urgent than the Critical P0 return-book problem and the High P1 double-borrowing problem.

Issue #19 has Medium severity and P2 priority. It affects data consistency, but the main library operations can still work. Therefore, it is reasonable to defer it while higher-impact defects are fixed.

Issue #18 has Low severity and P3 priority. The empty title problem should eventually be addressed, but it has limited impact compared with the higher-severity issues.