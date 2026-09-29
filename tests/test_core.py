import unittest

from pepworld_intelligence import (
    EvidenceRecord,
    FieldState,
    FieldValue,
    IntelligenceStage,
    KnowledgeState,
    MissingReason,
    PipelineTrace,
    TraceEvent,
)


class FieldValueTests(unittest.TestCase):
    def test_missing_requires_a_specific_reason(self):
        value = FieldValue(
            state=FieldState.MISSING,
            missing_reason=MissingReason.NOT_COLLECTED,
        )

        self.assertEqual(value.state, FieldState.MISSING)
        self.assertEqual(value.missing_reason, MissingReason.NOT_COLLECTED)
        with self.assertRaises(ValueError):
            FieldValue(state=FieldState.MISSING)
        with self.assertRaises(ValueError):
            FieldValue(state=FieldState.MISSING, missing_reason="unknown")

    def test_invalid_value_is_preserved_with_reason(self):
        value = FieldValue(
            state=FieldState.INVALID,
            value="not-a-number",
            invalid_reason="expected a numeric value",
        )

        self.assertEqual(value.value, "not-a-number")
        with self.assertRaises(ValueError):
            FieldValue(state=FieldState.INVALID, value="not-a-number")

    def test_present_and_not_applicable_states_are_explicit(self):
        self.assertEqual(
            FieldValue(state=FieldState.PRESENT, value=0).value,
            0,
        )
        with self.assertRaises(ValueError):
            FieldValue(state=FieldState.PRESENT)
        with self.assertRaises(ValueError):
            FieldValue(state=FieldState.NOT_APPLICABLE, value="value")

    def test_knowledge_states_do_not_collapse_missing_and_unknown(self):
        self.assertNotEqual(KnowledgeState.MISSING, KnowledgeState.UNKNOWN)
        self.assertNotEqual(KnowledgeState.INFERRED, KnowledgeState.KNOWN)


class TraceabilityTests(unittest.TestCase):
    def test_evidence_preserves_raw_value_and_source(self):
        evidence = EvidenceRecord(
            evidence_id="evidence-1",
            source_id="source-1",
            raw_value="Up to 400+ Mbps",
            collection_event_id="collection-1",
        )

        self.assertEqual(evidence.raw_value, "Up to 400+ Mbps")
        self.assertEqual(evidence.source_id, "source-1")
        self.assertEqual(evidence.collection_event_id, "collection-1")

    def test_pipeline_trace_preserves_stage_and_reference_chain(self):
        observed = TraceEvent(
            event_id="event-1",
            stage=IntelligenceStage.EVIDENCE,
            input_ids=("source-1",),
            output_ids=("evidence-1",),
        )
        analyzed = TraceEvent(
            event_id="event-2",
            stage=IntelligenceStage.ANALYZE,
            input_ids=("evidence-1",),
            output_ids=("finding-1",),
            transformation="compare evidence against the recorded question",
        )
        trace = PipelineTrace().record(observed).record(analyzed)

        self.assertEqual(trace.events, (observed, analyzed))
        self.assertEqual(analyzed.transformation, "compare evidence against the recorded question")
        self.assertEqual(PipelineTrace().events, ())
        with self.assertRaises(ValueError):
            TraceEvent(
                event_id="event-3",
                stage="analyze",
                input_ids=(),
                output_ids=(),
            )


if __name__ == "__main__":
    unittest.main()
