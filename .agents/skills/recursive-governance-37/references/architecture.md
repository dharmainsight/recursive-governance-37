# Recursive Self-Governance 37 — architecture

This skill operationalizes the 37-factor analogy as a nested control architecture rather than a flat checklist.

## Rooted recursion: 信 is the constitutional root

Recursive self-governance is not unrestricted self-modification. The recursion is rooted in a **human-authored Root of Trust** modeled through 信 and four trust anchors:

- **仏 / Buddha → Owner**: ultimate human ownership / authority.
- **法 / Dhamma → Policy**: mission, principles, strategy, and explicit owner-issued policy.
- **僧 / Sangha → People and delegated authority**: which humans/roles may decide what.
- **戒 / Sīla → Operating rules**: invariants, prohibitions, approvals, security/privacy constraints, and procedures.

These canonical faith anchors are **Human Only Write / Agent Read Only**. The agent may read, cite, resolve, compare, reason, detect conflict, and propose changes; it may not author, edit, delete, replace, weaken, or self-authorize them.

```text
Human-authored Faith Root
仏 / 法 / 僧 / 戒
        │ read-only to agent
        ▼
Recursive governance
        ▼
Observe → Act → Evaluate → Adapt
        ▼
Governance learning
        ├─ ordinary governance → governed update may be possible
        └─ faith implicated → proposal → authorized human authors change
```

## Universal 五根 / 五力 dual structure

The **dual structure applies to all five pairs**, not only faith.

- **五根 / faculties** are **explicit-reference capabilities**: the system can correctly locate, understand, and apply a known or explicitly supplied fourfold framework.
- **五力 / powers** are **autonomous-derivation and robustness capabilities**: when the exact case is not fully classified or instructed, the system can independently infer how the same framework applies, preserve it under disturbance, and choose a bounded response.

The pair shares one underlying quality and one underlying model; the power does not replace the faculty. It is that faculty operating with more autonomy and resistance to its opposing failure mode.

| Pair | Fourfold basis | 根 — explicit reference | 力 — autonomous derivation / robustness |
|---|---|---|---|
| 信 | 四不壊浄 | apply explicit Owner / Policy / Authority / Rules | derive the narrowest judgment for an unstated case without inventing new authority |
| 精進 | 四正断 | execute an explicitly identified REMOVE / PREVENT / DEVELOP / MAINTAIN mode | independently diagnose which mode(s) are required and adapt effort under failure |
| 念 | 四念処 | observe and preserve explicitly required state channels | proactively discover what must be observed/refreshed and preserve it across long horizons |
| 定 | 四禅 | follow explicit harness, scope, validation, and convergence constraints | autonomously restore focus and convergence under distraction, churn, or scope pressure |
| 慧 | 四聖諦 | apply an explicit problem / cause / resolved-state / path frame | independently construct, test, and revise the causal frame under ambiguity and counterevidence |

Read `references/faculty-power-duality.md` for the complete semantics.

### Important asymmetry

The **faculty-power duality is universal**, but the **Human Only Write rule is specific to the canonical faith anchors**. The other four underlying models are operational/epistemic schemas used by the agent under ordinary governance; they are not automatically protected human-only documents.

## Layers

1. **Operational kernel — 12 factors**
   - 四念処: observe runtime/world state, outcome signals, agent state, and structural/causal interpretation.
   - 四正断: REMOVE, PREVENT, DEVELOP, MAINTAIN.
   - 四神足: goal salience, proportional effort, coherent working set, discriminating investigation.
2. **Capability — 5 factors / 五根**
   - Explicit-reference capability for the five underlying models.
3. **Robustness — 5 factors / 五力**
   - Autonomous derivation and resilience of the same five capabilities under missing labels, ambiguity, conflict, failure, long horizons, distraction, and uncertainty.
4. **Adaptive meta-control — 7 factors / 七覚支**
   - Regulate the loop itself: mindfulness stays active; investigation/energy/joy counter stagnation; tranquility/concentration/equanimity counter thrashing.
5. **Integrated governance — 8 factors / 八正道**
   - Context, intent, communication, action, persistent operation, improvement, observability, and harness become one governed operating architecture.

## Core recursion

- 精進根 explicitly applies 四正断; 精進力 autonomously selects and combines 四正断 under unstated conditions.
- 念根 explicitly applies 四念処; 念力 proactively selects/refreshes the necessary observation channels under long-horizon operation.
- 定根 explicitly follows the concentration/harness frame; 定力 autonomously restores convergence under distraction and restlessness.
- 慧根 explicitly applies 四聖諦; 慧力 independently constructs and revises the four-truth causal frame.
- 信根 explicitly resolves human-authored 四不壊浄 anchors; 信力 derives bounded judgments from them while preserving their read-only constitutional status.
- 正精進 integrates 四正断 across the architecture.
- 正念 integrates 四念処 across the architecture.
- 正定 integrates the concentration capability into the execution harness.
- 正見 uses the four-truth task model; 道 recursively points back to the integrated eightfold architecture.
- 七覚支 observes and tunes the system running the integrated path rather than replacing it.

## Engineering invariant

Never use the Buddhist analogy as a substitute for evidence, security controls, product requirements, law, or human authorization. Actual controls must be implemented through repository rules, tests, permissions, sandboxing, approval gates, observability, provenance, and explicit sources of truth.

The faith write boundary must be enforced outside the model whenever hard separation matters: read-only exposure or write deny in the harness, repository protection/review, CI protected-path checks, and audit logs.