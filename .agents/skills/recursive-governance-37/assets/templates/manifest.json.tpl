{
  "schema_version": "1.1.0",
  "faith_anchors": {
    "owner": "docs/agent-governance/faith/owner.md",
    "policy": "docs/agent-governance/faith/policy.md",
    "authority": "docs/agent-governance/faith/authority.md",
    "operations": "docs/agent-governance/faith/operations.md",
    "write_policy": "human_only",
    "agent_access": "read_only"
  },
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
    "faith_anchor_write": "blocked",
    "production_write": "review_required",
    "destructive_operation": "review_required",
    "external_send_publish": "review_required",
    "permission_expansion": "review_required",
    "weaken_evaluation_gate": "review_required",
    "governance_self_modification": "review_required"
  },
  "notes": [
    "Faith anchors are human-authored and agent-read-only. The scaffold intentionally does not create their canonical contents.",
    "Prefer references to existing canonical human-authored anchors over duplication.",
    "Replace ordinary governance defaults only after repository-specific evidence or explicit human decision."
  ]
}
