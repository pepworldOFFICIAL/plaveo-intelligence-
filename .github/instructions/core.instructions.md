---
applyTo: "pepworld_intelligence/**/*.py"
---

# Shared Python contracts

- Keep this package generic; do not put domain-specific intelligence logic in
  the shared core.
- Preserve explicit field and knowledge states and validate invalid
  combinations at construction time.
- Keep data contracts immutable unless a concrete use case requires otherwise.
- Preserve caller-provided identifiers and raw values. Do not invent IDs,
  sources, timestamps, or evidence.
- Add or extend shared contracts before introducing one-off abstractions.
