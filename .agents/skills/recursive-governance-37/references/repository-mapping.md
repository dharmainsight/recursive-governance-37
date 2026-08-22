# Repository mapping rules

The skill augments an existing repository; it does not rename the repository into Buddhist terminology and does not create duplicate sources of truth.

## Mapping precedence

Map the human-authored 四不壊浄 basis when evaluating 信根, alongside the other four faculties:

1. **Owner / 仏** — identify the ultimate human authority for the domain.
2. **Policy / 法** — identify owner-issued mission, principles, policy, and direction.
3. **People and delegated authority / 僧** — identify human roles and the authority delegated to each.
4. **Operating rules / 戒** — identify human-authored invariants, prohibitions, approvals, and procedures.

These anchors must be human-authored and agent-read-only. Existing canonical human documents should be referenced directly. Do not copy them into a new faith directory merely to fit this model, and do not present them as an extra maturity layer before 五根.

For every ordinary governance concern:
1. discover existing canonical artifacts;
2. determine whether they are current and authoritative under protected human sources;
3. point the governance manifest to them;
4. create a new ordinary-governance artifact only when no adequate canonical source exists;
5. never copy a canonical document merely to fit this model.

## Typical evidence

### Protected 四不壊浄 basis / 信根・信力

- Owner / 仏: ownership records, founder/owner decision document, authorized service owner declaration.
- Policy / 法: mission, product principles, strategic policy, explicit owner decisions.
- People and delegated authority / 僧: role matrix, team ownership, approval matrix, CODEOWNERS-like human responsibility map, operator authority.
- Operating rules / 戒: security/privacy policy, production rules, approval requirements, prohibited actions, incident procedures, operational invariants.

The agent may discover and map these documents, but may not author their canonical content.

### Integrated governance

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

Create `docs/agent-governance/manifest.json` only when useful. It should be an index of pointers and policy metadata, not a second copy of product, architecture, or faith truth.

The manifest may point to the four anchors, but the manifest itself does not make an agent-authored document canonical. Canonical authority comes from authorized human authorship plus the configured read-only boundary; this protection serves 信根・信力 and is not an additional faith factor.

