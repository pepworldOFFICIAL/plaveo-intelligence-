# PEPWORLD Intelligence System V1 — Foundation

## Purpose and current scope

This repository started without application code, existing engines or operating
systems, data models, or a test/build system. V1 therefore establishes a small
set of reusable Python contracts in `pepworld_intelligence.core`; it does not
claim to implement the full master architecture or fabricate domain data.

## Repository layout and guidance

The implementation remains in the existing Python package
`pepworld_intelligence/`; tests remain in `tests/`; and this guide remains in
`docs/`. Repository-wide Copilot architecture guidance is in
`.github/copilot-instructions.md`, scoped rules for existing package/tests/docs
are in `.github/instructions/`, and `AGENTS.md` records repository commands and
operating rules. This deliberately does not create empty `src/`, engine, OS,
registry, schema, or domain directories: the architecture permits the actual
language/framework layout to vary, and no implementation currently needs those
directories.

The contracts are:

- `EvidenceRecord`: preserves a raw value and requires identifiers for its
  source and evidence. A collection event identifier can be recorded when one
  exists; identifiers and metadata are supplied by the caller, never generated.
- `FieldValue`: distinguishes `PRESENT`, `MISSING`, `INVALID`, and
  `NOT_APPLICABLE`. Missing values require a specific `MissingReason`;
  invalid values retain the supplied value and a validation reason.
- `KnowledgeState`: keeps `UNKNOWN`, `MISSING`, `INVALID`, `INFERRED`,
  `ASSUMED`, `CONTESTED`, and `SCENARIO_DEPENDENT` separate from `KNOWN`.
- `TraceEvent` and `PipelineTrace`: record a semantic stage and the identifiers
  consumed and produced, with an optional transformation description.
  Recording returns a new trace; no processing, persistence, or
  referential-integrity lookup is implied.

These are in-memory contracts, not a database schema or a service API. The
caller is responsible for preserving identifiers and linking records across
storage boundaries. An absent collection timestamp, method, or other metadata
remains absent rather than being inferred.

## Placement in the system

The intended system hierarchy is PEPWORLD → Central Operating System →
Intelligence System V1 → shared capabilities/engines and operating systems →
domain and universal intelligence. No new engine or OS wrappers are created
here: the repository had no prior inventory to extend, and the shared contracts
are not themselves a complete engine or operating system.

There is no engine or OS registry yet because the repository contains no
implemented engines or operating systems to register. Add a registry only when
it can describe real components and provide architectural discoverability.

The V1 loop is modeled as traceable, connected stages rather than an enforced
linear workflow:

`WORLD → OBSERVATION → COLLECTION → EVIDENCE → DATA → KNOWLEDGE → ENTITY →
RELATIONSHIP → TIME/SPACE → RESEARCH → ANALYZE → MODEL → ASSESS → SYNTHESIZE →
INTELLIGENCE → DECISION_SUPPORT → DECISION → ACTION → OUTCOME → MEMORY →
LEARNING → ADAPTATION`

`IntelligenceStage` gives events stable semantic stage names. Consumers can
record only the stages they actually perform; the trace does not assert that
unobserved stages occurred or require a fixed ordering. Inputs and outputs are
references, so source-to-evidence-to-analysis lineage can be followed when
the caller records those links.

## Role separation

These are distinct responsibilities, not separate applications implemented by
this foundation:

| Role | Responsibility |
| --- | --- |
| Library | Knowledge memory: preserve, organize, retrieve, and reference sources, evidence, methods, models, and lessons. |
| Data Base | World memory: capture and query recorded observations, entities, attributes, events, relationships, and changes. |
| Institute | Research and intelligence across Library knowledge and Data Base records; it is not another database. |
| Analytic | Examine relationships, patterns, causes, and dynamics while retaining uncertainty and limitations. |
| Intelligence | Synthesize connected knowledge, data, analysis, and assessment into a traceable output. |
| Decision Support | Present options, trade-offs, consequences, uncertainty, robustness, and stress-test findings for an authorized decision-maker. |
| Decision | An authorized choice; this foundation does not make or authorize decisions. |
| Action | Execution of an authorized decision. |
| Outcome | What was observed to happen after action; it can be compared with expectations and retained. |
| Memory | Preserve evidence, decisions, actions, outcomes, versions, and history without overwriting prior records. |
| Learning | Use observed outcomes and deviations to inform lessons and adaptation without rewriting historical truth. |

## Provenance and state contracts

`EvidenceRecord.raw_value` is the unmodified value supplied by the collector;
normalization belongs in an explicit later transformation, not silent mutation.
Evidence links to a source, and trace events link stage inputs to outputs. This
first version does not define a source registry, transformation schema,
validation framework, storage adapter, or provenance graph resolver.

For field semantics, `MISSING` requires one of `NOT_COLLECTED`, `NOT_PROVIDED`,
`NOT_ACCESSIBLE`, `EVIDENCE_INSUFFICIENT`, or `PENDING_COLLECTION`. `UNKNOWN` is
a knowledge state, not a missing-data reason. `INVALID` retains the rejected
value and its reason. `NOT_APPLICABLE` carries no field value.

Uncertainty, assumptions, evidence quality, model governance, and conflict
assessment remain explicit system requirements but are not yet implemented as
dedicated data structures. AI-generated interpretation and simulation output
must not be represented as evidence or fact without independently supplied
source/evidence records.

## Decision boundary and limitations

There was no existing decision logic in this repository. Accordingly, no
decision engine, stress-test runner, decision gate, domain-specific model,
database, external collector, or automatic learning behavior is introduced.
The documented target decision flow is integrated view → question/objective/
constraints → options/trade-offs/consequences/uncertainty → robustness and
stress-test → gate → decision support → authorized human decision. Any future
implementation must preserve that authority boundary and record conditions
that could reopen a decision.

This foundation does not validate whether a source is truthful, whether
evidence is sufficient, or whether a conclusion follows from its inputs. Trace
references are caller-provided identifiers and are not checked for existence.
These limitations are intentional until concrete consumers and persistence
requirements exist.

## Validation

Run the standard-library contract tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

The tests cover state invariants, missing reasons, invalid-value preservation,
source/raw-evidence linkage, and pipeline reference continuity. There is no
separate configured linter, build, or integration test suite at this stage.
