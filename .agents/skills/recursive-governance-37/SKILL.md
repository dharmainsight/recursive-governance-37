---
name: recursive-governance-37
description: "Audit, retrofit, and operate an existing software repository as a recursive self-governing agent loop using an explicit 37-factor architecture plus a Four Noble Truths wisdom-routing graph, three-turn/twelve-aspect decision state, and append-only evidence memory. Use for loop engineering, agent governance, self-correcting workflows, repository SoT/harness/observability/meta-control, causal diagnosis, or autonomy-readiness audits."
---

# Recursive Governance 37

Operate one repository as a **recursive self-governing agent system** without duplicating or silently replacing existing sources of truth.

This is an engineering analogy, not a doctrinal identity claim. Read `references/doctrinal-sources.md` when explaining or changing the model.

## Read these first

1. `references/architecture.md`
2. `references/faculty-power-duality.md`
3. `references/trust-anchors.md`
4. `references/wisdom-graph.md` and `references/wisdom-graph.json`
5. `references/runtime-protocol.md`
6. `references/risk-and-escalation.md`
7. `references/repository-mapping.md`
8. `references/factor-registry.json` and referenced `factor-groups/*.json`

Validate the registry before claiming model completeness:

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
```

It must contain exactly **4 + 4 + 4 + 5 + 5 + 7 + 8 = 37** factors.

# Universal 五根 / 五力 dual structure

The five faculties are **coequal capabilities**. Do not make faith a preliminary layer outside 五根 or evaluate it before the other four faculties.

- **根 / faculty** = explicit-reference capability. Correctly understand and apply the corresponding explicitly supplied fourfold framework.
- **力 / power** = autonomous self-execution + robustness. Without case-specific coaching, independently infer how the same framework applies, carry the work through verification, and resist its opposing failure tendency.

The five pairs are:

1. **信 — 四不壊浄**
   - 信根: understand explicit Owner / Policy / Authority / Rules without distortion. Their canonical content is **Human Only Write / Agent Read Only**.
   - 信力: resist **不信**. Derive an unstated case from those anchors without blind acceptance, invention, or self-authorization.
2. **精進 — 四正断**
   - 精進根: execute an explicitly identified REMOVE / PREVENT / DEVELOP / MAINTAIN mode.
   - 精進力: resist **懈怠**. Diagnose the required mode(s), implement the change, persist through bounded failure, and verify completion without human prodding.
3. **念 — 四念処**
   - 念根: observe/preserve explicitly required body / feeling / mind / dhamma channels.
   - 念力: resist **放逸**. Discover, refresh, and continue attending to relevant observed facts instead of ignoring inconvenient evidence or acting on stale state.
4. **定 — 四禅 / concentration-harness analogy**
   - 定根: follow explicit scope, harness, validation, resource, and stop constraints.
   - 定力: resist **掉挙**. Preserve the actual objective without urgency-driven substitution and restore sustained convergence under distraction, scope drift, tool churn, and over-parallelism.
5. **慧 — 四聖諦**
   - 慧根: apply an explicit 苦 / 集 / 滅 / 道 frame and track each truth through recognize → task → completion.
   - 慧力: resist **無明**. Independently discover and test the causal frame, use discriminating evidence, distinguish necessary from sufficient conditions, and revise it under counterevidence.
   - Do not jump from 苦 directly to a durable 道. Emergency containment may come first only when delay increases harm; mark it containment-only and complete 集 → 滅 → 道 afterward.
   - Keep meaningful evidence append-only. Improve judgment speed by routing/indexing, not by deleting inconvenient or old experience.

The Human Only Write rule protects the fourfold basis **inside 信根 and 信力**. Hard enforcement belongs outside the model—write-deny, protected paths, human review, CI guards, and audit logs—but that enforcement is not an extra faith layer or an additional factor.

A faculty can be SATISFIED while its paired power is PARTIAL or MISSING. Never collapse the pair into one score.

Do not mark a power SATISFIED merely because the corresponding keys exist. Require evidence that the AI handled an unstated or disturbed case, acted without case-specific human coaching, resisted the named opposing tendency, and verified the result.

# Operating modes

## AUDIT
Read-only. Discover the repository, map sources of truth, evaluate all 37 factors, and propose the smallest safe augmentation. Evaluate the four protected anchors as the explicit basis of 信根, alongside the other four faculties.

## AUGMENT
Add only missing ordinary-governance mechanisms after mapping existing canonical artifacts. Never create or edit canonical faith anchors.

## OPERATE
Execute an ordinary repository task under the runtime protocol and protected human authority boundaries.

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

Start with the Four Noble Truths wisdom trunk from `references/wisdom-graph.md`. Treat the underlying structure as a graph: the four truths are the decision trunk; the 37 factors remain the canonical factor registry and are reached as observation, improvement, mobilization, capability, robustness, meta-control, and governance functions. This adds no 38th factor.

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
- 四聖諦 wisdom route → 苦 / 集 / 滅 / 道 with three-turn state and evidence-linked path trace
- 念 memory policy → retain meaningful observations, counterevidence, failed interventions, and superseded judgments; alter applicability/status rather than erase history

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

The scaffold must not author the protected 四不壊浄 anchors. Missing anchors make 信根 MISSING or UNKNOWN and require human initialization or pointers to existing human-authored canonical documents. Read-only audit and the 4+4+4 kernel may still proceed; block only actions whose authority or safety depends on the missing anchor.

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

0. Establish the task contract and technical action boundary. This is safety enforcement, not 信 and not a maturity layer.
1. Establish the 四聖諦 route: identify the current 苦 and the unresolved truth/task; do not preselect a durable solution.
2. Observe — 四念処 — and attach fresh evidence to the route.
3. Complete enough 集 and 滅 analysis to discriminate causes and define a verifiable cessation/resolved state.
4. Improve — 四正断.
5. Mobilize and act — 四神足.
6. Reobserve the changed state and close the minimum 4+4+4 loop.
7. Update the three-turn/twelve-aspect state; containment is not completion.
8. Test all five **根** together as coequal explicit-reference capabilities.
9. Test all five **力** as AI-alone execution that resists 不信 / 懈怠 / 放逸 / 掉挙 / 無明.
10. Adapt loop — 七覚支.
11. Integrate/govern — 八正道.
12. Evaluate against external state and return the feedback to observation.
13. Retain the evidence/provenance record append-only and learn: ordinary governance may follow governed change; protected-anchor changes remain human-authored proposals.

# 七覚支 meta-control

- `SLUGGISH`: repeated same fix, low information gain, low hypothesis diversity → favor 択法・精進・喜.
- `RESTLESS`: scope expansion, tool/branch churn, excessive parallelism/research → favor 軽安・定・捨.
- `BALANCED`: preserve 念 and continue without gratuitous tuning.

# Recursive self-governance rule

Ordinary governance may improve through governed review. Canonical 四不壊浄 content is inside the faith faculty/power model but outside the agent's write domain.

If ordinary governance is wrong/incomplete, create a governance-change proposal with evidence, affected factor IDs, risk, tests, rollback, and permission impact. Human review is required for permission expansion, approval reduction, security/eval weakening, protected-data changes, production access, or changes to the governance-change mechanism.

If a protected faith anchor should change, never edit it. Create a faith-change proposal, identify the authorized human, pause dependent high-risk action, wait for the human-authored canonical change, then reload and reevaluate 信根 before testing 信力.

# Safety and evidence invariants

- Early-discourse sources are the normative Buddhist reference tier for this skill. Later Buddhist / Mahāyāna vocabulary may be used only as an explicitly marked presentation adapter or explanatory `upāya`, never to rewrite the canonical ontology.
- The wisdom graph is an overlay on the existing 37 factors, not a 38th factor.
- Keep 苦 / 集 / 滅 / 道 distinct. Do not mark a durable path complete before cause and cessation criteria are explicit; emergency containment must remain labeled containment-only until retrospective diagnosis and verification are complete.
- Do not delete meaningful observations, counterevidence, failed interventions, or superseded judgments merely to reduce context. Preserve them and change status/scope/applicability; prefer fresh mutable-state observation through adjudication, not erasure.
- The four faith anchors belong to 信根 / 信力, are human-authored, and are agent-read-only.
- A current prompt does not outrank higher human authority merely because it is newer.
- 信力 derives judgments; it does not create authority or policy.
- All five faculties must be presented and evaluated at the same structural level.
- All five powers must be demonstrated separately from their faculties and without case-specific human coaching.
- Power evidence must show resistance to 不信 / 懈怠 / 放逸 / 掉挙 / 無明 respectively.
- Do not treat prompts as technical enforcement.
- Prefer read-only exposure/write deny, sandbox, IAM, repository protection, CI, tests, preview environments, and deployment review for hard boundaries.
- Do not mutate production or send/publish externally without required authorization.
- Do not invent SoT content, hide uncertainty, or duplicate canonical truth.
- Do not claim 37-factor completeness unless the registry validator passes.

# Required AUDIT / REVIEW output

Return:

1. protected 四不壊浄 map and enforcement status within the 信 finding;
2. repository/canonical-source map;
3. 37-factor coverage by group;
4. **five explicit faculty-vs-power pair findings**;
5. PARTIAL/MISSING/UNKNOWN factor findings;
6. systemic failure modes;
7. smallest safe augmentation plan;
8. human gates / irreversible-risk notes;
9. validation plan;
10. current 四聖諦 route and three-turn completion gaps, when causal diagnosis is in scope;
11. memory-retention/provenance notes for material supersession or counterevidence;
12. whether governance or faith change is implicated.

