# Repository mapping rules

The skill augments an existing repository; it does not rename the repository into Buddhist terminology and does not create duplicate sources of truth.

## Mapping precedence

For every governance concern:
1. discover existing canonical artifacts;
2. determine whether they are current and authoritative;
3. point the governance manifest to them;
4. create a new artifact only when no adequate canonical source exists;
5. never copy a canonical document merely to fit this model.

## Typical evidence

- Context / 正見: product requirements, architecture docs, ADRs, RFCs, SLOs, issue acceptance criteria.
- Intent / 正思惟: goals, principles, non-goals, scope, risk appetite.
- Communication / 正語: reporting conventions, confidentiality rules, provenance and review policies.
- Action / 正業: permissions, sandbox, branch protection, deployment permissions, data-access rules.
- Loop / 正命: workflows, schedules, retries, task queues, escalation, service role, resource limits.
- Improvement / 正精進: tests, lint, security scanners, incident processes, regression suites, feature/eval processes.
- Observability / 正念: logs, traces, metrics, state tables, audit records, run summaries.
- Harness / 正定: AGENTS.md, tool constraints, CI, preview environments, test commands, approval gates.
- Meta-control / 七覚支: stagnation/thrashing detection, retry strategy changes, scope freeze, alternate-hypothesis rules.

## Canonical manifest

Create `docs/agent-governance/manifest.json` only when useful. It should be an index of pointers and policy metadata, not a second copy of product or architecture truth.
