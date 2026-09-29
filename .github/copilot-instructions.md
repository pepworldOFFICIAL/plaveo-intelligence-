# PEPWORLD Intelligence System V1

This repository builds a reusable, traceable, evidence-aware intelligence
system on the PEPWORLD Central Operating System. Treat it as one coherent
architecture, not a collection of unrelated features.

## Architecture

Preserve the distinctions between shared platform contracts, capabilities,
engines, operating systems, intelligence, decisions, actions, outcomes, memory,
and learning. Capabilities define what the system can do; engines implement
reusable mechanisms; operating systems coordinate capabilities and engines.
Library is knowledge memory, Data Base is recorded world state, and Institute
is research across both. Intelligence informs decision support; only an
authorized human or decision authority makes the decision.

The semantic pipeline runs from world observation and collection through
evidence, data, knowledge, relationships, research, analysis, modeling,
assessment, synthesis, intelligence, decision support, decision, action,
outcome, memory, learning, and adaptation. Represent actual processing as
traceable connected stages; do not imply unperformed stages or force universal
intelligence into a serial pipeline.

## Engineering and data principles

- Inspect and search the current repository before adding a component. Extend
  existing shared contracts before creating parallel engines, OS layers,
  registries, or domain stacks.
- Preserve source, raw evidence, collection context when supplied, and explicit
  transformations. Never manufacture provenance or silently normalize a value.
- Keep `PRESENT`, `MISSING`, `INVALID`, and `NOT_APPLICABLE` distinct. A missing
  field requires a specific missing reason; `UNKNOWN` is a knowledge state, not
  a missing-data reason. Never silently turn an inference or assumption into a
  fact.
- Keep uncertainty, assumptions, conflicts, limitations, and model/scenario
  status visible. A source is not automatically truth; a pattern is not a cause;
  a model or simulation is not reality.
- Preserve historical records and decision authority. Intelligence must not
  silently make decisions or overwrite outcome history.
- Treat external input as untrusted; protect secrets and private data.
- Make the smallest complete change, validate it with the repository's existing
  tests, and update directly relevant documentation.

## Current implementation

The current implementation is a small Python package at
`pepworld_intelligence/`, with standard-library tests in `tests/` and
architecture documentation in `docs/architecture.md`. It provides in-memory
contracts, not a database, service, complete engine inventory, or decision
system. Do not create the architecture's proposed directories or registries
until a concrete implemented capability needs them.

See scoped instructions in `.github/instructions/` for source contracts, tests,
evidence, and documentation.
