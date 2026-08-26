Testing rebase practice - step 1 
Testing rebase practice - step 2 
Testing rebase practice - step 3 
Testing rebase practice - step 4 


## Lab 1 — Task 5: Change Flow (Idea → Released)

This diagram shows how a change moves through the development lifecycle, and where a QA engineer typically intervenes.

```
[Idea]
   |
   v
[Issue Created] --------- QA Intervention: reviews issue for clarity,
   |                       reproducibility (bugs), and acceptance criteria
   v
[Branch Created: feature/xxx or fix/xxx]
   |
   v
[Commits Made] ----------- QA Intervention: encourages atomic commits,
   |                       Conventional Commits format for traceability
   v
[Pull Request Opened] ---- QA Intervention: this is the PRIMARY quality
   |                       gate — reviews code, checks tests, verifies
   |                       acceptance criteria are met
   v
[Code Review] ------------ QA Intervention: leaves review comments,
   |                       requests changes, verifies edge cases handled
   v
[Merge to main] ---------- QA Intervention: confirms branch protection
   |                       rules were respected (PR + approval required)
   v
[CI Pipeline Runs] ------- QA Intervention: monitors automated test
   |                       results, blocks release if checks fail
   v
[Release] ---------------- QA Intervention: final sign-off, smoke
                            testing on the released build
```

**Key QA touchpoints:** Issue triage (clarity & severity), PR review (the most critical gate), CI check monitoring, and pre-release verification. Catching defects earlier is far cheaper than catching them after release.
