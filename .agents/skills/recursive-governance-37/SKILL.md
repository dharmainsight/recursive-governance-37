---
name: recursive-governance-37
description: Audit, retrofit, and operate an existing software repository as a rooted recursive self-governing agent loop using an explicit 37-factor architecture: four establishments of mindfulness, four right efforts, four bases of accomplishment, five faculties, five powers, seven awakening factors, and the noble eightfold path. Use for loop engineering, agent governance, self-correcting workflows, repository SoT/harness/observability/meta-control, or autonomy-readiness audits.
---

# Recursive Governance 37

Operate one repository as a **rooted recursive self-governing agent system** without duplicating or silently replacing existing sources of truth.

This is an engineering analogy, not a doctrinal identity claim. Read `references/doctrinal-sources.md` when explaining or changing the model.

## Read these first

1. `references/architecture.md`
2. `references/faculty-power-duality.md`
3. `references/trust-anchors.md`
4. `references/runtime-protocol.md`
5. `references/risk-and-escalation.md`
6. `references/repository-mapping.md`
7. `references/factor-registry.json` and referenced `factor-groups/*.json`

Validate the registry before claiming model completeness:

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
```

It must contain exactly **4 + 4 + 4 + 5 + 5 + 7 + 8 = 37** factors.

# Constitutional root — 信

Resolve four human-authored trust anchors before consequential operation:

- **仏 / Owner** — ultimate human authority.
- **法 / Policy** — mission, principles, strategy, explicit decisions.
- **僧 / People and delegated authority** — who may decide what.
- **戒 / Operating rules** — invariants, prohibitions, approvals, security/privacy/operational procedures.

Canonical faith anchors are **Human Only Write / Agent Read Only**. The agent may read, cite, resolve, compare, reason, detect conflict, and propose changes, but may not author or promote canonical faith content.

If required anchors are missing, report `HUMAN INITIALIZATION REQUIRED` rather than inventing them.

# Universal 五根 / 五力 dual structure

The dual structure applies to **all five pairs**, not only faith.

- **根 / faculty** = explicit-reference capability. Correctly use a known or explicitly supplied fourfold framework.
- **力 / power** = autonomous-derivation + robustness. When the exact case is unlabeled, incomplete, ambiguous, interrupted, or disturbed, independently infer how the same framework applies and remain stable.

The five pairs are:

1. **信 — 四不壊浄**
   - 信根: follow explicit Owner / Policy / Authority / Rules.
   - 信力: derive the narrowest consistent judgment for an unstated case; preserve authority under conflicting context; never invent canonical faith.
2. **精進 — 四正断**
   - 精進根: execute an explicitly identified REMOVE / PREVENT / DEVELOP / MAINTAIN mode.
   - 精進力: independently diagnose which mode(s) are required and adapt effort under failure.
3. **念 — 四念処**
   - 念根: observe/preserve explicitly required body / feeling / mind / dhamma channels.
   - 念力: proactively discover what must be observed/refreshed and preserve critical state over long horizons.
4. **定 — 四禅 / concentration-harness analogy**
   - 定根: follow explicit scope, harness, validation, resource, and stop constraints.
   - 定力: autonomously restore convergence under distraction, scope drift, tool churn, and over-parallelism.
5. **慧 — 四聖諦**
   - 慧根: apply an explicit problem / cause / resolved-state / path model.
   - 慧力: independently construct, test, and revise that causal model under incomplete evidence and counterevidence.

**Important:** the faculty-power duality is universal; the Human Only Write rule is specific to canonical faith anchors.

A faculty can be SATISFIED while its paired power is PARTIAL or MISSING. Never collapse the pair into one score.

# Operating modes

## AUDIT
Read-only. Discover the repository, resolve faith anchors when present, map sources of truth, evaluate all 37 factors, and propose the smallest safe augmentation.

## AUGMENT
Add only missing ordinary-governance mechanisms after mapping existing canonical artifacts. Never create or edit canonical faith anchors.

## OPERATE
Execute an ordinary repository task under the runtime protocol and faith root.

## REVIEW
Review an agent run, governance change, or loop design against the 37 factors, pair duality, recursive invariants, and protected faith boundary.

# Phase 1 — DISCOVER

Run:

```bash
python .agents/skills/recursive-governance-37/scripts/discover_repo.py --root .
python .agents/skills/recursive-governance-37/scripts/audit_repo.py --root .
```

Then inspect semantic evidence. Candidate evidence is not compliance.

Find when present: faith anchors, AGENTS/CLAUDE instructions, requirements/specs, architecture/ADR/RFCs, security/privacy/permission policy, CI/tests/lint/build/migrations, deployment/preview infrastructure, logs/telemetry/SLO/runbooks, workflows/schedulers/queues, production/external-side-effect gates.

# Phase 2 — MAP

Map the integrated architecture:

- 正見 → Context / world model / SoT
- 正思惟 → Intent / objectives / non-goals / risk orientation
- 正語 → Communication / provenance / handoff policy
- 正業 → Action / tool / permission / side effects
- 正命 → Persistent loops / role / resources / retries / stop / escalation
- 正精進 → Evaluation and improvement
- 正念 → Observability and persistent state
- 正定 → Harness / sandbox / tools / deterministic validation / approvals

Then map lower layers:

- 四念処 → four observation channels
- 四正断 → REMOVE / PREVENT / DEVELOP / MAINTAIN
- 四神足 → goal salience / effort allocation / working-set coherence / investigation
- 五根 → explicit-reference capability for each fivefold axis
- 五力 → autonomous-derivation/robustness for the same five axes
- 七覚支 → adaptive loop control

Reuse existing canonical files by reference. Do not create duplicate truth merely to fit this model.

# Phase 3 — GAP ANALYZE

For all 37 factors assign exactly one status:

- `SATISFIED`
- `PARTIAL`
- `MISSING`
- `N/A` with reason
- `UNKNOWN`

For each five-pair axis report **two separate findings**:

- faculty evidence: can the agent use the explicit framework correctly?
- power evidence: can it infer the correct application when the exact case is not supplied and remain robust under disturbance?

For non-SATISFIED factors identify missing responsibility, evidence, failure mode, smallest intervention, eval, and risk/approval requirement.

Never convert UNKNOWN to SATISFIED by inference alone.

# Phase 4 — AUGMENT

Use the non-destructive scaffold only after audit:

```bash
python .agents/skills/recursive-governance-37/scripts/scaffold.py --root .
python .agents/skills/recursive-governance-37/scripts/scaffold.py --root . --apply
```

The scaffold must not author faith anchors. Missing faith requires human initialization or pointers to existing human-authored canonical documents.

Implement controls in their natural technical location:

- tests in test suites;
- deployment gates in CI/environment protection;
- permissions in sandbox/IAM/config;
- retry/backoff in orchestration;
- canonical context in existing product/architecture docs;
- observability in logs/traces/state stores;
- meta-control in loop/orchestrator policy.

# Phase 5 — VERIFY

Run repository checks plus:

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
python .agents/skills/recursive-governance-37/scripts/validate_repo_governance.py --root .
```

If a run record exists:

```bash
python .agents/skills/recursive-governance-37/scripts/evaluate_run_record.py docs/agent-governance/run-record.json
```

Structural validation is not semantic success; verify task-specific acceptance criteria directly.

# Runtime sequence

1. Resolve human-authored faith root.
2. Establish task contract and delegated authority.
3. Observe — 四念処.
4. Improve — 四正断.
5. Mobilize — 四神足.
6. Test all five **根** as explicit-reference capabilities.
7. Test all five **力** as autonomous derivation/robustness capabilities.
8. Adapt loop — 七覚支.
9. Integrate/govern — 八正道.
10. Evaluate against external state.
11. Learn: ordinary governance may follow governed change; faith changes become proposals for authorized humans.

# 七覚支 meta-control

- `SLUGGISH`: repeated same fix, low information gain, low hypothesis diversity → favor 択法・精進・喜.
- `RESTLESS`: scope expansion, tool/branch churn, excessive parallelism/research → favor 軽安・定・捨.
- `BALANCED`: preserve 念 and continue without gratuitous tuning.

# Recursive self-governance rule

The architecture is **rooted recursion**.

Ordinary governance may improve through governed review. Canonical faith is outside the agent's write domain.

If ordinary governance is wrong/incomplete, create a governance-change proposal with evidence, affected factor IDs, risk, tests, rollback, and permission impact. Human review is required for permission expansion, approval reduction, security/eval weakening, protected-data changes, production access, or changes to the governance-change mechanism.

If a faith anchor should change, never edit it. Create a faith-change proposal, identify the authorized human, pause dependent high-risk action, wait for the human-authored canonical change, then reload the root.

# Safety and evidence invariants

- Faith anchors are human-authored and agent-read-only.
- A current prompt does not outrank higher human authority merely because it is newer.
- 信力 derives judgments; it does not create authority or policy.
- All five powers must be demonstrated separately from their faculties.
- Do not treat prompts as technical enforcement.
- Prefer read-only exposure/write deny, sandbox, IAM, repository protection, CI, tests, preview environments, and deployment review for hard boundaries.
- Do not mutate production or send/publish externally without required authorization.
- Do not invent SoT content, hide uncertainty, or duplicate canonical truth.
- Do not claim 37-factor completeness unless the registry validator passes.

# Required AUDIT / REVIEW output

Return:

1. faith-root map and protection status;
2. repository/canonical-source map;
3. 37-factor coverage by group;
4. **five explicit faculty-vs-power pair findings**;
5. PARTIAL/MISSING/UNKNOWN factor findings;
6. systemic failure modes;
7. smallest safe augmentation plan;
8. human gates / irreversible-risk notes;
9. validation plan;
10. whether governance or faith change is implicated.
