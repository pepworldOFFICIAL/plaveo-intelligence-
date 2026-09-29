# PEPWORLD Intelligence System V1 — repository agent guidance

This repository is part of the PEPWORLD Central Operating System and builds
PEPWORLD Intelligence System V1 as one reusable, traceable, evidence-aware
architecture—not as disconnected features. Preserve the distinction between
implemented contracts and the broader target architecture. The current
implementation is a small Python package in `pepworld_intelligence/`, with
standard-library tests in `tests/` and architecture documentation in
`docs/architecture.md`.

## Before changing the repository

Read `.github/copilot-instructions.md` and the relevant scoped instructions in
`.github/instructions/`. Then follow this search protocol:

**Search → Locate → Trace → Understand → Modify → Test**

Search existing files, symbols, contracts, tests, documentation, and any
applicable registries before deciding a component is absent. Trace callers,
inputs, outputs, and dependencies; understand existing behavior and limitations
before making the smallest complete change.

## Architectural boundaries

- Keep shared **core** contracts generic. **Capabilities** describe what the
  system can do; reusable **engines** implement mechanisms; **operating
  systems** coordinate capabilities and engines.
- **Intelligence** connects evidence, data, knowledge, research, analysis,
  modeling, and assessment as traceable stages or relationships that actually
  occurred; do not imply unperformed processing or force a universal serial
  pipeline.
- **Decision support** informs an authorized human or decision authority.
  Intelligence must never silently make or authorize a decision. Keep decision,
  action, and observed outcome distinct.
- **Data Base** is recorded world state; **Library** is knowledge memory; and
  **Institute** researches across both. **Memory** preserves records and
  history. **Governance** applies across the system. **Interfaces** expose
  functionality but do not own core intelligence logic.
- Keep dependency direction from lower-level shared contracts toward higher
  layers: core → capabilities → engines → operating systems → intelligence →
  decision support/decision → interfaces. Higher layers may use lower-layer
  contracts; lower layers must not depend on application-specific higher layers.
  Avoid circular dependencies. Shared data, memory, and governance concerns
  must not become hidden, duplicated domain-specific systems.

## Evidence, state, and history

- Preserve source identifiers, raw evidence, supplied collection context, and
  explicit transformations. Never invent provenance, silently normalize raw
  values, or present an inference or assumption as fact.
- Keep field states `PRESENT`, `MISSING`, `INVALID`, and `NOT_APPLICABLE`
  distinct. A missing field needs a specific missing reason; `UNKNOWN` is a
  knowledge state, not a missing-data reason.
- Keep uncertainty, assumptions, conflicts, evidence limitations, and
  model/scenario status visible. A source is not automatically truth, a pattern
  is not a cause, and a model or simulation is not reality.
- Preserve historical records. New intelligence or learning must not silently
  overwrite evidence, decisions, actions, outcomes, or prior versions.

## Adding or changing components

Before creating a component, identify its architectural layer and contract, then
search for an existing capability, shared utility, engine, OS, or registry to
extend. Check for duplicate engines, OS coordination, provenance, evidence, or
memory systems, including in domain code. Create a new component only when
existing shared components cannot meet the concrete need; document the reason
for justified exceptions.

Do not create speculative source/documentation directory trees or registries
because they appear in the target architecture. Update a registry only when one
exists or a concrete implemented capability justifies introducing one. For
material architectural changes, record what changed and why, affected
dependencies/contracts/data, tests, migrations, and documentation; add an
architecture decision record when appropriate. Update directly relevant
documentation and distinguish implemented behavior from planned architecture.

## Validation

Tests should verify behavior and, where relevant, trace continuity, provenance,
explicit field and knowledge states, relationships, uncertainty, assumptions,
model inputs/outputs, and decision-support boundaries—not only rendered text.
Use the existing standard-library tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

No separate configured linter, build, migration, or application-launch command
currently exists. Do not invent commands or claim those checks ran.
