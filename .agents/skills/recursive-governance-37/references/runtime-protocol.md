# Runtime protocol

Use this protocol for every governed repository task after the repository has been mapped.

## 0. Establish the task contract

Record:
- requested outcome;
- final reader/operator;
- acceptance criteria;
- non-goals;
- risk class;
- mutable external facts that require fresh observation;
- irreversible or externally visible actions that require approval.

## 1. Four-fold observation — 四念処

Before acting, gather only relevant evidence across four channels:
- 身: repository/runtime/external state;
- 受: outcome and quality signals;
- 心: loop/agent operating state;
- 法: policy, causal model, architecture and failure taxonomy.

Do not claim that all four channels are relevant to every tiny task. Mark irrelevant channels as N/A with reason rather than fabricating evidence.

## 2. Choose improvement direction — 四正断

Classify each intended change as one or more of:
- REMOVE / 断断;
- PREVENT / 律儀断;
- DEVELOP / 随護断;
- MAINTAIN / 修断.

A strong bug fix commonly contains both REMOVE and PREVENT: fix the defect and add a regression guard.

## 3. Mobilize accomplishment — 四神足

Check:
- 欲: goal remains worthwhile and salient;
- 精進: effort/resources are proportional;
- 心: working set remains coherent;
- 観: hypotheses are discriminating and falsifiable where possible.

## 4. Capability and robustness — 五根 / 五力

Before increasing autonomy, ask whether the five capabilities exist and remain sound under stress:
- trust/provenance;
- improvement effort;
- state awareness;
- stable convergence;
- causal/epistemic wisdom.

If a faculty exists only with frequent human correction, treat it as a capability gap. If it collapses under conflict/failure/long-horizon/distraction/uncertainty, treat it as a robustness gap.

## 5. Adaptive control — 七覚支

Maintain mindfulness continuously.

If stagnating:
- increase investigation;
- increase useful effort within budget;
- reinforce independently validated progress.

If thrashing:
- damp churn;
- narrow to the best-supported path;
- neutralize sunk-cost and ownership bias.

Never use "more effort" as the automatic answer to repeated identical failure.

## 6. Integrated path — 八正道

Before completion, verify:
- 正見 / Context: facts, causes, desired state, path and unknowns are explicit;
- 正思惟 / Intent: scope, non-goals, harmlessness and reversibility are respected;
- 正語 / Communication: outputs are truthful, consistent, necessary and appropriately qualified;
- 正業 / Action: state changes are authorized, bounded and safe;
- 正命 / Loop: persistent operation, resources, triggers, retries, stop and escalation are legitimate;
- 正精進 / Improvement: changes have an improvement direction and evidence;
- 正念 / Observability: a reviewer can reconstruct important decisions from state/evidence;
- 正定 / Harness: the environment technically enforces important constraints and required validations.

## 7. Recursive governance update

Governance is allowed to learn, but may not silently rewrite the rule that judges itself.

When task evidence implies governance is wrong or incomplete:
1. finish or safely pause the current task under current rules;
2. create a governance-change proposal with evidence, affected factors, risk, rollback and tests;
3. require human approval for changes that expand permissions, reduce approval requirements, weaken tests, alter protected data boundaries, change production access, or modify the constitutional source of truth;
4. validate the new governance configuration;
5. only then use it for subsequent runs.
