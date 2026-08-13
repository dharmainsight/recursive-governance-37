# Recursive Governance 37 — repo-scoped Agent Skill

Install by extracting this package at the repository root so that the skill lives at:

```text
.agents/skills/recursive-governance-37/
```

The skill implements the full **4 + 4 + 4 + 5 + 5 + 7 + 8 = 37** engineering model discussed in the accompanying design conversation.

## First run

Invoke explicitly:

```text
$recursive-governance-37
Audit this repository only. Do not change files. Map the existing SoT, evaluate all 37 factors, identify governance gaps, and propose the smallest safe augmentation plan.
```

The skill defaults to explicit invocation (`allow_implicit_invocation: false`) because retrofitting governance is consequential and should not happen merely because an ordinary coding prompt happens to resemble one of its concepts.

## Deterministic self-check

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
python .agents/skills/recursive-governance-37/tests/self_test.py
```

Expected registry result: `PASS: exact 37/37 registry and recursive invariants validated`.

## What it installs into a target repository

Nothing automatically. The skill first audits. If augmentation is authorized, `scripts/scaffold.py --apply` can create a non-destructive `docs/agent-governance/` index/constitution. Existing canonical docs should be referenced, not copied.
