# PEPWORLD Intelligence System V1

**A documentation-first foundation for building reusable, traceable,
evidence-aware intelligence systems.**

> **Status:** early foundation. This repository currently provides small,
> in-memory Python contracts and tests—not a complete intelligence platform,
> database, service, or decision system. The architecture described here is a
> direction, not a claim that every component or stage has been implemented.

## Overview

PEPWORLD Intelligence System V1 is intended to connect observation, evidence,
data, knowledge, research, analysis, modeling, assessment, intelligence,
decision support, authorized decisions, actions, outcomes, memory, and learning.
The goal is to make the relationships between work and its inputs visible while
preserving uncertainty and history.

These are connected stages, not a mandatory linear workflow. A trace should
represent only processing that actually occurred; it must not imply missing
stages or automatically establish that a source or conclusion is true.

## Why PEPWORLD

Intelligence work can become fragmented across data stores, research, analytic
tools, and decision processes. PEPWORLD's architectural direction is to provide
shared contracts and reusable mechanisms that connect those responsibilities
without collapsing their distinct roles. Evidence should remain traceable,
uncertainty should remain visible, and decision authority should stay with the
authorized person or body.

The current repository is a small starting point for those principles, not a
claim that this broader system already exists.

## Architecture

The target architecture distinguishes shared platform contracts, capabilities,
engines, operating systems, intelligence, decision support, decisions, actions,
outcomes, memory, and learning:

```text
core → capabilities → engines → operating systems → intelligence
     → decision support → authorized decision → action → outcome
     → memory and learning
```

This describes architectural boundaries and dependency direction, not a set of
directories or components already present. Higher layers may use lower-level
contracts; shared foundations should not depend on application-specific layers.
The V1 semantic stages and current limits are described in
[`docs/architecture.md`](docs/architecture.md).

### Library, Data Base, and Institute

These names describe distinct responsibilities in the wider architecture:

- **Library** is knowledge memory: preserve, organize, retrieve, and reference
  sources, evidence, methods, models, and lessons.
- **Data Base** is recorded world state: observations, entities, attributes,
  events, relationships, and changes.
- **Institute** researches across Library knowledge and Data Base records; it
  is not another database.

They are architectural roles, not implemented services in this repository.

### Universal and domain intelligence

**Universal intelligence** is the shared, cross-domain foundation: generic
contracts and reusable approaches for evidence, data, knowledge, relationships,
time and space, research, analysis, modeling, assessment, and synthesis.
**Domain intelligence** applies domain-specific context, terminology, sources,
and methods above that foundation. It should extend shared components when
possible rather than duplicate evidence, provenance, memory, engine, or
operating-system mechanisms.

These are architectural distinctions. The package does not currently implement
domain intelligence or a complete universal intelligence workflow.

### Five Lenses

The Five Lenses are a conceptual way to examine an intelligence problem from
complementary perspectives—not five implemented modules or a required sequence:

1. **Evidence and provenance:** What was observed, by which source, and what
   transformations were explicitly applied?
2. **State and uncertainty:** What is present, missing, invalid, inapplicable,
   unknown, inferred, assumed, contested, or scenario-dependent?
3. **Relationships and context:** Which entities, relationships, time, and space
   matter, and what is recorded versus interpreted?
4. **Analysis and alternatives:** What patterns, explanations, models, or
   scenarios are considered, and what limitations or competing explanations
   remain?
5. **Decisions and outcomes:** What options and consequences inform the
   authorized decision-maker, what happened after action, and what should be
   retained as history or learning?

These lenses are explanatory perspectives for the target architecture; the
repository does not currently provide a Five Lenses engine or assessment.

## Evidence, provenance, and traceability

The implemented `EvidenceRecord` keeps a caller-provided source identifier,
evidence identifier, and raw value; a collection-event identifier is optional
when supplied. `TraceEvent` records a stage, input identifiers, output
identifiers, and an optional transformation description. These references can
support **reverse traceability** from a finding or output through recorded
inputs, when callers preserve and connect those identifiers.

The current contracts do not resolve references, verify source truth, prove
causality, persist records, or guarantee a complete lineage graph. Preserve raw
values and collection context when supplied; record transformations explicitly.
Never invent provenance or silently normalize evidence.

## Explicit data and knowledge states

Field states and knowledge states describe different things:

| Field state | Meaning |
| --- | --- |
| `PRESENT` | A field has a supplied value. |
| `MISSING` | A value is absent and requires a specific missing reason. |
| `INVALID` | A supplied value is retained with a validation reason. |
| `NOT_APPLICABLE` | The field does not apply; it carries no field value. |

The available missing reasons are `NOT_COLLECTED`, `NOT_PROVIDED`,
`NOT_ACCESSIBLE`, `EVIDENCE_INSUFFICIENT`, and `PENDING_COLLECTION`.
`UNKNOWN` is a knowledge state, **not** a missing-data reason. Knowledge states
also distinguish `KNOWN`, `MISSING`, `INVALID`, `INFERRED`, `ASSUMED`,
`CONTESTED`, and `SCENARIO_DEPENDENT`. An inference or assumption must not be
silently promoted to fact.

## Decision architecture and authority

Intelligence informs **decision support**; it does not silently make or
authorize a decision. Decision support is intended to present options,
trade-offs, consequences, uncertainty, robustness, and stress-test findings to
an authorized human or decision authority. Keep the decision, its authorized
execution, and the observed outcome distinct, and preserve their histories.

### Stress-testing and Decision Gate

The target architecture describes stress-testing options against relevant
conditions and assumptions before a Decision Gate. The gate is a planned
decision-support checkpoint for reviewing readiness, constraints, unresolved
uncertainty, and conditions that could reopen a decision. It does not replace
authorized human judgment.

Neither stress-test execution nor a Decision Gate is implemented here; there is
no decision engine, gate, or stress-test runner in the current package.

## Reusable engines and no premature collapse

In the target architecture, **capabilities** describe what the system can do,
**engines** implement reusable mechanisms, and **operating systems** coordinate
capabilities and engines. A domain should compose shared mechanisms rather than
create parallel copies of them. The current repository has no implemented
engines, operating systems, or component registries.

Keep evidence distinct from data, knowledge distinct from analysis, analysis
distinct from intelligence, intelligence distinct from decision support, and
decision support distinct from decisions and actions. Keep models and scenarios
distinct from observed reality. This separation makes provenance, uncertainty,
authority, and history inspectable instead of obscuring them in one
all-purpose component.

## Current project status

| Status | What it means here |
| --- | --- |
| **Implemented** | In-memory Python contracts for `FieldValue`, field and missing-reason states, `KnowledgeState`, `EvidenceRecord`, semantic stage names, `TraceEvent`, and append-by-copy `PipelineTrace`; standard-library tests cover their core invariants. |
| **Partial** | Trace references connect supplied input and output identifiers, but identifiers are not resolved, and no persistence or complete provenance graph is provided. |
| **Architecture** | Library / Data Base / Institute responsibilities, the connected intelligence loop, Five Lenses, shared-engine direction, domain boundaries, Decision Gate, and stress-testing concepts are documented as target architecture. |
| **Prototype** | No separate application, service, or runnable intelligence workflow is present. |
| **Experimental** | No separately identified experimental subsystem is present. |
| **Planned** | Additional concrete capabilities may be developed when needed; the architecture does not promise a particular implementation or roadmap date. No engine/OS registries, persistence, collectors, decision system, or automatic learning are currently provided. |

The contracts do not validate source truth, evidence sufficiency, or whether a
conclusion follows from its inputs. See
[`docs/architecture.md`](docs/architecture.md) for the detailed scope and
limitations.

## Getting started

The project currently has a plain Python package at the repository root and no
packaging or external runtime-dependency configuration. Work from the repository
root to import the package directly:

```python
from pepworld_intelligence import EvidenceRecord, FieldState, FieldValue

field = FieldValue(state=FieldState.PRESENT, value="recorded value")
evidence = EvidenceRecord(
    evidence_id="evidence-1",
    source_id="source-1",
    raw_value=field.value,
)
```

The identifiers and value above are illustrative caller-provided values, not
repository evidence. This example demonstrates contracts only; it does not
collect, validate, store, or analyze information.

Run the existing tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

## Repository structure

```text
.
├── AGENTS.md                         # Repository-wide contributor/agent guidance
├── CONTRIBUTING.md                   # Contribution workflow
├── CODE_OF_CONDUCT.md                # Community expectations
├── LICENSE                           # MIT license
├── README.md                         # Project overview and status
├── SECURITY.md                       # Security limitations and disclosure
├── docs/
│   └── architecture.md               # Implemented contracts and target architecture
├── pepworld_intelligence/
│   ├── __init__.py
│   └── core.py                       # In-memory shared contracts
├── tests/
│   └── test_core.py                  # Standard-library unittest coverage
└── .github/
    ├── copilot-instructions.md
    └── instructions/                 # Scoped guidance for code, evidence, tests, and docs
```

There is no `src/` tree or engine, operating-system, domain, or registry
directory. Such components and directories are future possibilities only; add
them when an implemented capability requires them, not speculatively.

## Contributing

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md), [`AGENTS.md`](AGENTS.md), and
the [architecture guide](docs/architecture.md). Contributions should preserve
the distinction between implemented contracts and target architecture.

## Security

Read [`SECURITY.md`](SECURITY.md) before handling any security-sensitive issue.
Do not commit credentials, private information, or sensitive operational data.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

This project is available under the [MIT License](LICENSE).

## Disclaimer

This architecture is evolving. Names, stage definitions, roles, lenses, and
architectural descriptions do not imply that corresponding software is
implemented. The current package is a small foundation and is not a source of
verified truth or a substitute for domain review, governance, security controls,
or authorized human judgment. Do not use it as the sole basis for consequential
decisions.
