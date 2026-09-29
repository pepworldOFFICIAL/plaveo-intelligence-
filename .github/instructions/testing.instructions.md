---
applyTo: "tests/**/*.py"
---

# Tests

- Use the existing standard-library `unittest` test style; do not add a test
  framework without a demonstrated need.
- Test semantic contracts such as provenance, explicit state, invalid and
  missing cases, and trace continuity rather than only final text.
- Run tests from the repository root with
  `python -m unittest discover -s tests -v`.
- Do not add fabricated source data or modify unrelated tests.
