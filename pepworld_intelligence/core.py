"""Small shared contracts for evidence, explicit field states, and traceability."""

from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar


class FieldState(str, Enum):
    PRESENT = "present"
    MISSING = "missing"
    INVALID = "invalid"
    NOT_APPLICABLE = "not_applicable"


class MissingReason(str, Enum):
    NOT_COLLECTED = "not_collected"
    NOT_PROVIDED = "not_provided"
    NOT_ACCESSIBLE = "not_accessible"
    EVIDENCE_INSUFFICIENT = "evidence_insufficient"
    PENDING_COLLECTION = "pending_collection"


class KnowledgeState(str, Enum):
    KNOWN = "known"
    UNKNOWN = "unknown"
    MISSING = "missing"
    INVALID = "invalid"
    INFERRED = "inferred"
    ASSUMED = "assumed"
    CONTESTED = "contested"
    SCENARIO_DEPENDENT = "scenario_dependent"


T = TypeVar("T")


@dataclass(frozen=True)
class FieldValue(Generic[T]):
    """A value with explicit applicability, validity, and missingness semantics."""

    state: FieldState
    value: T | None = None
    missing_reason: MissingReason | None = None
    invalid_reason: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.state, FieldState):
            raise ValueError("state must be a FieldState")
        if self.missing_reason is not None and not isinstance(
            self.missing_reason, MissingReason
        ):
            raise ValueError("missing_reason must be a MissingReason")
        if self.state is FieldState.PRESENT and self.value is None:
            raise ValueError("present fields require a value")
        if self.state is FieldState.MISSING:
            if self.value is not None or self.missing_reason is None:
                raise ValueError("missing fields require a reason and cannot have a value")
        elif self.missing_reason is not None:
            raise ValueError("missing_reason is only valid for missing fields")
        if self.state is FieldState.INVALID:
            if self.value is None or not self.invalid_reason:
                raise ValueError("invalid fields require a value and invalid_reason")
        elif self.invalid_reason is not None:
            raise ValueError("invalid_reason is only valid for invalid fields")
        if self.state is FieldState.NOT_APPLICABLE and self.value is not None:
            raise ValueError("not-applicable fields cannot have a value")


@dataclass(frozen=True)
class EvidenceRecord:
    """Raw evidence linked to its source; collection metadata is recorded when known."""

    evidence_id: str
    source_id: str
    raw_value: object
    collection_event_id: str | None = None

    def __post_init__(self) -> None:
        if not self.evidence_id or not self.source_id:
            raise ValueError("evidence_id and source_id are required")


class IntelligenceStage(str, Enum):
    WORLD = "world"
    OBSERVATION = "observation"
    COLLECTION = "collection"
    EVIDENCE = "evidence"
    DATA = "data"
    KNOWLEDGE = "knowledge"
    ENTITY = "entity"
    RELATIONSHIP = "relationship"
    TIME = "time"
    SPACE = "space"
    RESEARCH = "research"
    ANALYZE = "analyze"
    MODEL = "model"
    ASSESS = "assess"
    SYNTHESIZE = "synthesize"
    INTELLIGENCE = "intelligence"
    DECISION_SUPPORT = "decision_support"
    DECISION = "decision"
    ACTION = "action"
    OUTCOME = "outcome"
    MEMORY = "memory"
    LEARNING = "learning"
    ADAPTATION = "adaptation"


@dataclass(frozen=True)
class TraceEvent:
    """A pipeline step connecting input and output identifiers and its transformation."""

    stage: IntelligenceStage
    input_ids: tuple[str, ...]
    output_ids: tuple[str, ...]
    event_id: str
    transformation: str | None = None

    def __post_init__(self) -> None:
        if not self.event_id:
            raise ValueError("event_id is required")
        if not isinstance(self.stage, IntelligenceStage):
            raise ValueError("stage must be an IntelligenceStage")
        if self.transformation is not None and not self.transformation.strip():
            raise ValueError("transformation cannot be empty")
        if any(not identifier for identifier in self.input_ids + self.output_ids):
            raise ValueError("trace identifiers cannot be empty")


@dataclass(frozen=True)
class PipelineTrace:
    """Append-only-by-convention trace; each addition returns a new trace."""

    events: tuple[TraceEvent, ...] = ()

    def record(self, event: TraceEvent) -> "PipelineTrace":
        return PipelineTrace(events=self.events + (event,))
