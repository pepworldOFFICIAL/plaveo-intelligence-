---
applyTo: "pepworld_intelligence/**/*.py"
---

# Evidence and provenance

- Preserve raw source values and distinguish them from normalized values,
  inferences, assumptions, and intelligence outputs.
- Link evidence to source identifiers and record collection context only when
  supplied. Never fabricate provenance or assert source truth.
- Make transformations and their inputs/outputs traceable; do not silently
  mutate source evidence.
- Keep missing reasons, invalid values, uncertainty, and evidence limitations
  explicit.
