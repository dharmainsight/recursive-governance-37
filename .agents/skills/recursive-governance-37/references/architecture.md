# Recursive Self-Governance 37 — architecture

This skill operationalizes the 37-factor analogy as a nested control architecture rather than a flat checklist.

## Rooted recursion: 信 is outside the agent's write domain

Recursive self-governance is not unrestricted self-modification. The recursion is rooted in a **human-authored Root of Trust** modeled through 信 and the four unshakable-confidence anchors:

- **仏 / Buddha → Owner**: who ultimately owns the company, service, repository, or delegated domain.
- **法 / Dhamma → Policy**: mission, principles, strategic direction, and explicit owner-issued policy.
- **僧 / Sangha → People and delegated authority**: employees, teams, operators, reviewers, and which decisions each may make.
- **戒 / Sīla → Operating rules**: invariants, prohibitions, approval requirements, security/privacy constraints, and procedures.

These anchors are **human-authored and agent-read-only**. The agent may reference and reason from them, but it may not create, edit, delete, replace, weaken, or re-authorize them.

This creates a rooted recursive structure:

```text
Human-authored Faith Root
仏 / 法 / 僧 / 戒
        │ read-only to agent
        ▼
Recursive governance
        ▼
Observe → Act → Evaluate → Adapt
        ▼
Governance-change proposal
        ├─ ordinary governance: governed update is possible
        └─ faith root: authorized human must author the change
```

The faith layer breaks the dangerous infinite regress in which an agent could redefine the authority that judges the agent.

Read `references/trust-anchors.md` for the complete trust model and enforcement rules.

## Layers

1. **Operational kernel — 12 factors**
   - 四念処: observe physical/runtime state, outcomes, agent state, and diagnostic structure.
   - 四正断: remove, prevent, develop, and maintain.
   - 四神足: preserve worthwhile goal salience, mobilize effort, maintain a coherent working set, and investigate discriminatingly.
2. **Capability — 5 factors**
   - 五根: faith/reference, improvement, state awareness, stable execution, and causal wisdom become reusable capabilities.
   - In particular, **信根** means accurately resolving and applying what authorized humans explicitly established in the faith anchors.
3. **Robustness — 5 factors**
   - 五力: the same capabilities remain reliable under contradiction, failure, long horizons, distraction, and uncertainty.
   - In particular, **信力** means deriving the narrowest defensible judgment for unstated cases from the human-authored faith anchors without inventing new authority or policy.
4. **Adaptive meta-control — 7 factors**
   - 七覚支: regulate the loop itself. Mindfulness stays active; investigation/energy/joy counter stagnation; tranquility/concentration/equanimity counter thrashing.
5. **Integrated governance — 8 factors**
   - 八正道: context, intent, communication, action, persistent operation, improvement, observability, and harness become one governed operating architecture.

## Core recursion

- 正精進 integrates 四正断.
- 正念 integrates 四念処.
- 正定 integrates the concentration capability into the execution harness.
- 正見 uses the four-truth task model: problem/loss, cause, resolved state, path. The path recursively points back to the integrated governance architecture.
- 五根 reuse operational-kernel capabilities; 五力 stress-test those capabilities.
- 信根 resolves explicit human authority; 信力 generalizes from it under unspecified conditions without rewriting the authority root.
- 七覚支 observes and tunes the system running 八正道 rather than replacing it.
- Governance may recursively improve below the faith layer; changes to the faith layer must be authored by an authorized human.

## Engineering invariant

Never use the Buddhist analogy as a substitute for evidence, security controls, product requirements, law, or human authorization. The analogy organizes engineering responsibilities. Actual controls must be implemented with repository rules, tests, permissions, sandboxing, approval gates, observability, and explicit source-of-truth documents.

The human-only faith boundary must be enforced outside the model whenever hard separation matters. At minimum, deny the agent write access to the faith-anchor paths or expose them through a read-only interface. Repository review, CI guards, and audit logs should provide additional defense in depth.
