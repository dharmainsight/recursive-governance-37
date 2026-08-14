# Recursive Governance 37 — repo-scoped Agent Skill

Install by extracting this package at the repository root so that the skill lives at:

```text
.agents/skills/recursive-governance-37/
```

The skill implements the full **4 + 4 + 4 + 5 + 5 + 7 + 8 = 37** engineering model as a **rooted recursive self-governance architecture**.

## Human-authored Root of Trust — 信

The recursion is rooted in four trust anchors that only authorized humans may author:

- **仏 / Owner** — ultimate human ownership and authority
- **法 / Policy** — owner-issued mission, principles, policy, and direction
- **僧 / People and delegated authority** — employees/roles and what each may decide
- **戒 / Operating rules** — invariants, prohibited actions, approvals, security/privacy rules, procedures

Agents may **read, cite, and reason from** these anchors, but must not create or modify their canonical content.

- **信根** = accurately refer to what humans explicitly established.
- **信力** = reason from those anchors when the exact case was not explicitly stated, without inventing new authority or policy.

See `.agents/skills/recursive-governance-37/references/trust-anchors.md`.

## First run

Invoke explicitly:

```text
$recursive-governance-37
Audit this repository only. Do not change files. Resolve the human-authored Owner / Policy / Authority / Operations trust anchors first, then map the existing SoT, evaluate all 37 factors, identify governance gaps, and propose the smallest safe augmentation plan.
```

The skill defaults to explicit invocation because retrofitting governance is consequential and should not happen merely because an ordinary coding prompt happens to resemble one of its concepts.

## Deterministic self-check

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
python .agents/skills/recursive-governance-37/tests/self_test.py
```

Expected registry result: `PASS: exact 37/37 registry and recursive invariants validated`.

## What augmentation creates

`scripts/scaffold.py --apply` may create a non-destructive `docs/agent-governance/` index/constitution after audit.

It intentionally **does not create or populate canonical faith anchors**. If they are absent, the scaffold prints `HUMAN INITIALIZATION REQUIRED` for:

```text
docs/agent-governance/faith/owner.md
docs/agent-governance/faith/policy.md
docs/agent-governance/faith/authority.md
docs/agent-governance/faith/operations.md
```

An authorized human must create those documents directly, or point the manifest to existing human-authored canonical documents. The agent harness should then expose those anchors as read-only or deny agent writes to their paths. Existing canonical docs should be referenced, not copied.
