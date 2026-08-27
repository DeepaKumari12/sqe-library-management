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

## Lab 2 — Task 3: Merge Conflict Documentation

**What caused the conflict:**
Two branches (`feature/rename-field-a` and `feature/rename-field-b`) were both created from the same commit and both modified the same line in `src/library/book.py` — the constructor parameter originally named `book_id`. Branch A renamed it to `item_id` and was merged into `main` first. Branch B, created from the same starting point, independently renamed the identical field to `catalog_id`. When Branch B was compared against the now-updated `main`, Git could not automatically determine which rename should win because both branches had diverged from the same original line with two different, non-identical changes.

**How it was resolved:**
1. Attempted to open a PR for `feature/rename-field-b` on GitHub — GitHub reported "Can't automatically merge."
2. Ran `git checkout feature/rename-field-b` followed by `git merge main` locally, which produced a real merge conflict in `src/library/book.py`.
3. Opened the file, located the conflict markers, and manually chose to keep `main`'s version (`item_id`), since that branch had already been merged and represented the agreed-upon name.
4. Removed all conflict markers, saved the file, then ran `git add`, `git commit`, and `git push` to push the resolved merge commit.
5. The PR then showed "Able to merge" and was merged normally with Squash and merge.

**Key takeaway:** Merge conflicts happen when two branches edit the same line differently after diverging from a shared ancestor. Resolving them requires a human decision about which change should survive — Git cannot guess intent.