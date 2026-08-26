# Contributing to SQE Library Management

This project follows a simple feature-branch workflow. All work happens on a short-lived branch created from `main`, named using one of the prefixes: `feature/<slug>` for new functionality, `fix/<slug>` for bug fixes, or `docs/<slug>` for documentation-only changes.

Commits should be small, atomic, and follow the Conventional Commits style (e.g. `feat(library): add Book class`). Once work on a branch is complete, open a Pull Request against `main`, ensure at least one review (self-review for solo work) is completed and all conversations are resolved, then merge using **Squash and merge** and delete the branch.

Direct commits to `main` are not allowed; `main` is protected and always expected to be in a releasable state.