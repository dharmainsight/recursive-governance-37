---
name: recursive-governance-37
description: Audit, retrofit, and operate an existing software repository as a recursive self-governing agent loop using an explicit 37-factor architecture: four establishments of mindfulness, four right efforts, four bases of accomplishment, five faculties, five powers, seven awakening factors, and the noble eightfold path. Use when asked to add loop engineering, agent governance, self-correcting agent workflows, repository SoT/harness/observability/meta-control, or to evaluate whether a repo can safely run autonomous coding/operations loops. Do not use merely for ordinary coding tasks that do not ask for governance/loop architecture.
---

# Recursive Governance 37

Your job is to **audit, retrofit, and operate one repository as a recursive self-governing agent system without duplicating or silently replacing its existing sources of truth**.

The model is an engineering analogy. Do not present the Buddhist mapping as doctrine. Read `references/doctrinal-sources.md` when explaining the analogy or changing the factor model.

## Mandatory model integrity

Before making governance changes, read:

1. `references/architecture.md`
2. `references/runtime-protocol.md`
3. `references/risk-and-escalation.md`
4. `references/repository-mapping.md`
5. `references/factor-registry.json` and its referenced `factor-groups/*.json` files when factor-level detail is needed

The factor registry index plus its seven group files contains **exactly 37 factors**. Never collapse or silently omit factors in an audit that claims 37-factor coverage.

Validate the installed registry with:

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
```

If that fails, stop and repair the skill before claiming model completeness.

## Operating modes

Determine the requested mode from the user's task. If unclear and changing files would be consequential, default to **AUDIT** first.

### AUDIT

Read-only. Discover the repository, map existing sources of truth, evaluate all 37 factors, identify gaps and risks, and propose the smallest augmentation set. Do not modify files.

### AUGMENT

Modify repository governance only after mapping existing canonical artifacts. Reuse existing files by reference. Create only missing governance structure. Never overwrite an existing file without explicit reason and diff review.

### OPERATE

Execute an ordinary repository task under the installed governance protocol. Use the 37-factor model proportionately: do not create ceremony for trivial tasks, but preserve the required safety and evidence invariants.

### REVIEW

Review a prior agent run, governance change, or loop design against all relevant factors and recursive invariants.

## Phase 1 — DISCOVER

Run:

```bash
python .agents/skills/recursive-governance-37/scripts/discover_repo.py --root .
python .agents/skills/recursive-governance-37/scripts/audit_repo.py --root .
```

Then inspect relevant artifacts semantically. The scripts provide candidate evidence only; **candidate evidence is not compliance**.

Find at minimum when present:

- `AGENTS.md`, `CLAUDE.md`, repository instructions;
- requirements/specifications/product docs;
- architecture/ADR/RFC material;
- security/privacy/permission policy;
- CI, tests, lint, build, migrations;
- deployment/preview infrastructure;
- logs, telemetry, SLOs, incident/runbook material;
- workflow/scheduler/queue/agent definitions;
- production and external-side-effect gates.

## Phase 2 — MAP

Map existing artifacts to the integrated eightfold architecture:

- 正見 → Context / world model / SoT
- 正思惟 → Intent / objectives / non-goals / risk orientation
- 正語 → Communication / provenance / handoff policy
- 正業 → Action / tool / permission / side-effect policy
- 正命 → Persistent loops / role / resources / retries / stop / escalation
- 正精進 → Evaluation and improvement policy
- 正念 → Observability and persistent state
- 正定 → Harness / sandbox / tools / deterministic validation / approval gates

Then map the lower layers explicitly:

- 四念処 → four observation channels
- 四正断 → REMOVE / PREVENT / DEVELOP / MAINTAIN
- 四神足 → goal salience / effort allocation / working-set coherence / discriminating inquiry
- 五根 → reusable capabilities
- 五力 → stress-tested robustness of those capabilities
- 七覚支 → adaptive loop control

Do not create a new canonical file if an adequate one already exists. Point to the existing source instead.

## Phase 3 — GAP ANALYZE

For every one of the 37 factors, assign one status:

- `SATISFIED` — strong semantic and operational evidence exists;
- `PARTIAL` — some evidence exists but an important responsibility/eval is missing;
- `MISSING` — no adequate mechanism exists;
- `N/A` — genuinely irrelevant to this repository/task, with a reason;
- `UNKNOWN` — evidence is insufficient or inaccessible.

For each non-SATISFIED factor, identify:

- missing responsibility;
- observed evidence;
- failure mode;
- smallest intervention;
- deterministic or rubric eval;
- risk and approval requirements.

Never convert `UNKNOWN` into `SATISFIED` by inference alone.

## Phase 4 — AUGMENT

When the user authorizes implementation, initialize a non-destructive governance index if useful:

```bash
python .agents/skills/recursive-governance-37/scripts/scaffold.py --root .
# inspect dry-run output
python .agents/skills/recursive-governance-37/scripts/scaffold.py --root . --apply
```

Then edit generated placeholders using observed repository evidence. Prefer pointers in `docs/agent-governance/manifest.json` over copied content.

Implement missing controls in their natural location. Examples:

- tests belong in the test suite, not governance prose;
- deployment gates belong in CI/environment protection;
- permissions belong in sandbox/IAM/configuration;
- retry/backoff belongs in orchestration code;
- canonical context belongs in existing product/architecture docs;
- observability belongs in logs/traces/state stores;
- meta-control belongs in loop policy/orchestrator logic.

The governance directory is an **index and constitution**, not a dumping ground.

## Phase 5 — VERIFY

Run the repository's normal checks plus:

```bash
python .agents/skills/recursive-governance-37/scripts/validate_registry.py
python .agents/skills/recursive-governance-37/scripts/validate_repo_governance.py --root .
```

If a run record exists, evaluate its structural coverage:

```bash
python .agents/skills/recursive-governance-37/scripts/evaluate_run_record.py docs/agent-governance/run-record.json
```

Do not claim semantic success solely from this structural evaluator. Verify task-specific acceptance criteria and safety invariants directly.

## Runtime behavior — the complete 37-factor loop

When operating a governed task, follow this sequence proportionately.

### A. Observe — 四念処

1. 身念処: inspect actual repository/runtime/external state.
2. 受念処: capture outcome/quality signals.
3. 心念処: inspect loop state such as uncertainty, stagnation, thrashing, scope drift.
4. 法念処: classify with policy, causal model, architecture, and failure taxonomy.

### B. Improve — 四正断

5. 断断: remove harmful state already present.
6. 律儀断: prevent foreseeable harmful state from arising/reappearing.
7. 随護断: develop beneficial capability not yet present.
8. 修断: preserve and strengthen beneficial state already present.

### C. Mobilize — 四神足

9. 欲神足: keep worthwhile goal and acceptance criteria salient.
10. 精進神足: allocate effort/resources proportionately.
11. 心神足: maintain a coherent working set without fixation.
12. 観神足: investigate with alternative hypotheses and discriminating tests.

### D. Capability — 五根

13. 信根: use evidence-governed trust and provenance.
14. 精進根: autonomously select/execute the right improvement mode.
15. 念根: preserve state across the task.
16. 定根: sustain coherent bounded execution.
17. 慧根: separate problem, cause, resolved state, and path.

### E. Robustness — 五力

18. 信力: preserve trust hierarchy under contradiction/injection/stale context.
19. 精進力: keep useful effort adaptive under failure without retry storms.
20. 念力: retain critical state across long horizons/resume/compaction.
21. 定力: converge despite distraction and scope pressure.
22. 慧力: expose unknowns and revise causal beliefs under counterevidence.

### F. Adapt the loop — 七覚支

23. 念覚支: continuously estimate meta-state.
24. 択法覚支: increase strategy/hypothesis discrimination when stuck.
25. 精進覚支: increase useful activation when under-powered.
26. 喜覚支: reinforce independently validated progress.
27. 軽安覚支: damp churn when restless/thrashing.
28. 定覚支: narrow to the best-supported path when evidence is sufficient.
29. 捨覚支: neutralize sunk-cost, authorship, praise/blame, and attachment bias.

Mindfulness stays active. When **sluggish**, favor 24–26. When **restless/thrashing**, favor 27–29. Do not activate both sides indiscriminately.

### G. Integrate and govern — 八正道

30. 正見: maintain current, causal, provenance-aware context.
31. 正思惟: govern objective formation through restraint, goodwill/cooperation, harmlessness, and reversibility.
32. 正語: govern truthful, consistent, necessary communication edges.
33. 正業: govern authorized, bounded, safe state-changing actions.
34. 正命: govern the persistent role, trigger, resource use, retry, stop, and escalation pattern.
35. 正精進: apply the four improvement modes across the whole architecture.
36. 正念: make important decisions reconstructable from four-channel evidence.
37. 正定: unify the other factors in a technically bounded harness with deterministic validation and approval gates.

## Meta-control decision rule

Classify loop state from evidence:

- `SLUGGISH`: repeated same fix, no information gain, low hypothesis diversity, stalled progress with available avenues.
- `RESTLESS`: scope expansion, excessive tool/branch churn, too many parallel paths, research beyond decision value.
- `BALANCED`: progress and information gain are adequate without churn.

Responses:

- SLUGGISH → strengthen investigation, useful effort, validated-progress reinforcement.
- RESTLESS → strengthen tranquility, convergence, neutral stop/rollback judgment.
- BALANCED → preserve state awareness and continue without gratuitous tuning.

## Recursive self-governance rule

The system may propose changes to its governance, but must not silently weaken the rule that governs itself.

If evidence shows governance is wrong or incomplete:

1. pause or finish the current task safely under current rules;
2. create a governance-change proposal;
3. identify affected factor IDs;
4. include evidence, risk, tests, rollback, and permission impact;
5. require human review for any permission expansion, approval reduction, security/eval weakening, protected-data change, production-access change, or change to the governance-change mechanism itself;
6. validate after the change;
7. use new governance only on subsequent runs unless explicitly approved otherwise.

## Safety and evidence invariants

- Do not treat prompts as technical enforcement.
- Prefer sandbox, IAM, branch protection, CI, tests, preview environments, and deployment review for hard boundaries.
- Do not mutate production or send/publish externally without the required authorization.
- Do not invent SoT content to make the model look complete.
- Do not duplicate existing canonical truth just to fit directory structure.
- Do not hide uncertainty.
- Do not claim 37-factor completeness unless the registry validator passes and the audit reports all 37 factors.
- Keep normal engineering names in the repository. Buddhist terms belong primarily in the model registry and explanatory mapping, not in application source code unless the repository explicitly chooses otherwise.

## Required output for AUDIT / REVIEW

Return:

1. repository map and canonical sources;
2. 37-factor coverage summary by group;
3. factor-level findings for all PARTIAL/MISSING/UNKNOWN items;
4. top systemic failure modes;
5. smallest safe augmentation plan ordered by dependency;
6. human gates and irreversible-risk notes;
7. validation plan;
8. whether governance self-modification is implicated.

Do not reduce the report to a single maturity score. A score may summarize, but factor-specific evidence and failure modes are authoritative.
