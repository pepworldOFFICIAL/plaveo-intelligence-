# Contributing

Thank you for helping improve PEPWORLD Intelligence System V1. The repository
is an evolving, documentation-first foundation; contributions should be
accurate about current behavior and preserve the boundary between implemented
contracts and target architecture.

## Before changing the repository

Read [`AGENTS.md`](AGENTS.md), [`.github/copilot-instructions.md`](.github/copilot-instructions.md),
the relevant scoped files in [`.github/instructions/`](.github/instructions/),
and [`docs/architecture.md`](docs/architecture.md). Then follow:

**Search → Locate → Trace → Understand → Modify → Test**

Search existing contracts, symbols, callers, tests, documentation, and any
applicable registries before deciding something is absent. Trace inputs,
outputs, and dependencies, understand existing behavior and limitations, then
make the smallest complete change.

## Architectural boundaries

- Keep shared core contracts generic. Capabilities describe what the system can
  do; reusable engines implement mechanisms; operating systems coordinate
  capabilities and engines.
- Keep dependency direction from lower-level shared contracts toward higher
  layers. Higher layers may use lower-level contracts; lower layers must not
  depend on application-specific higher layers. Avoid circular dependencies.
- Intelligence connects only stages or relationships that actually occurred.
  Do not imply a fixed or universal serial pipeline.
- Intelligence informs decision support; it does not make or authorize a
  decision. Keep decision, action, and observed outcome distinct.
- Library is knowledge memory, Data Base is recorded world state, and Institute
  researches across both. Memory preserves records and history; governance
  applies across the system; interfaces expose functionality without owning
  core intelligence logic.

## Evidence, state, and traceability

- Preserve caller-provided source identifiers, raw evidence, supplied
  collection context, and explicit transformations. Never invent provenance,
  silently normalize source values, or assert that a source is true.
- Keep field states `PRESENT`, `MISSING`, `INVALID`, and `NOT_APPLICABLE`
  distinct. A `MISSING` field needs a specific missing reason.
- Keep knowledge states such as `UNKNOWN`, `INFERRED`, `ASSUMED`, `CONTESTED`,
  and `SCENARIO_DEPENDENT` distinct from one another and from field states.
  `UNKNOWN` is not a missing-data reason. Do not silently turn an inference or
  assumption into fact.
- Keep uncertainty, conflicts, limitations, and model/scenario status visible.
  A pattern is not a cause; a model or simulation is not reality.
- Preserve historical evidence, decisions, actions, outcomes, and prior
  versions. New intelligence or learning must not silently overwrite them.
- Tests should verify relevant provenance and trace continuity, state
  distinctions, uncertainty, and decision-support boundaries—not only rendered
  text.

## Adding components

Identify the architectural layer and contract before creating a component.
Search for an existing shared contract, capability, utility, engine, operating
system, or registry that can be extended. Check for duplicate evidence,
provenance, memory, engine, or operating-system mechanisms, including in domain
code. Add a new component only when the concrete need cannot be met by existing
shared components, and explain that reason.

Do not create speculative directory trees or registries. This repository
currently has no implemented engines, operating systems, or registries; refer
to these as future/planned until verified and implemented. A domain should use
shared mechanisms and add only its genuinely domain-specific contracts and
logic. For material architectural changes, describe affected dependencies,
contracts, data, tests, migration needs (if any), and documentation; add an
architecture decision record when appropriate.

## Tests and validation

Use the existing standard-library `unittest` tests. From the repository root,
run:

```sh
python -m unittest discover -s tests -v
```

Add or update focused tests when behavior changes. Do not add a test framework
or claim a linter, build, migration, or application-launch check exists unless
the repository has configured one.

## Pull request descriptions

Describe:

- the problem and intended behavior or documentation change;
- affected contracts, architecture layers, dependencies, or public interfaces;
- behavior and compatibility implications, if applicable;
- provenance/state/traceability effects and any limitations introduced;
- tests and other existing validation performed, with results;
- related documentation and any justified new component or exception.

Keep the change focused and distinguish implemented behavior from planned
architecture. Do not claim that unperformed stages, registries, engines,
operating systems, or workflows exist.
