{
  "schema_version": "1.0.0",
  "canonical_sources": {
    "context_current_state": [],
    "context_causal_model": [],
    "context_desired_state": [],
    "context_operating_model": [],
    "intent_objectives": [],
    "intent_non_goals": [],
    "communication_policy": [],
    "action_policy": [],
    "loop_definitions": [],
    "improvement_policy": [],
    "observability_state_model": [],
    "harness_execution_policy": [],
    "meta_control_policy": []
  },
  "protected_boundaries": {
    "production_write": "review_required",
    "destructive_operation": "review_required",
    "external_send_publish": "review_required",
    "permission_expansion": "review_required",
    "weaken_evaluation_gate": "review_required",
    "governance_self_modification": "review_required"
  },
  "notes": [
    "Prefer references to existing canonical artifacts over duplication.",
    "Replace defaults only after repository-specific evidence or explicit human decision."
  ]
}
