# Risk and escalation policy

This file supplies the default safety posture. Repository-specific policy may be stricter.

## Protected 四不壊浄 boundary — absolute agent read-only

The four faith anchors are the protected basis inside 信根 and 信力:

- 仏 / Owner
- 法 / Policy
- 僧 / People and delegated authority
- 戒 / Operating rules

For the agent, these are **read-only constitutional inputs**, not ordinary governance files. They are not a separate factor or maturity stage before 五根.

The agent must not create, edit, delete, rename, replace, weaken, or re-authorize any canonical faith anchor. It must not alter the mechanism that makes those anchors read-only.

If an anchor is missing, report `HUMAN INITIALIZATION REQUIRED` rather than filling it.

If an anchor should change, the agent may create a proposal outside the protected anchor paths. An authorized human must directly author the canonical change.

### Required enforcement posture

Do not rely on prompt obedience alone. Use at least one hard control outside the model and preferably several:

- deny agent write access to faith-anchor paths in the harness or expose them through a read-only interface;
- protect those paths with human review/merge controls in the repository;
- fail CI when an agent change set modifies protected faith-anchor paths;
- retain auditable human identity for anchor changes.

A repository that merely says “do not edit these files” but gives the agent unrestricted write capability has not implemented the faith boundary strongly enough for high-autonomy operation.

## Low risk — normally autonomous inside the sandbox

Examples: read-only inspection, local formatting, tests, documentation aligned to observed code, non-destructive refactors with passing tests, changes isolated to a feature branch/worktree.

## Medium risk — autonomous only with deterministic validation and rollback

Examples: dependency updates, schema migrations in preview/local environments, configuration changes, broad refactors, automated external communication drafts that are not sent.

Required: isolated environment, explicit acceptance criteria, validation, diff reviewability, rollback path.

## High risk — stop for human authorization before side effect

Examples: production deployment/write, destructive migration, secrets/authentication/authorization changes that can expand access, financial transaction, legal or compliance representation, external send/publish, deletion of important data, changing protected governance boundaries.

## Governance self-modification gates

Always require explicit review before any ordinary-governance change that:
- expands write/network/tool permissions;
- reduces human approval requirements;
- removes or weakens a security/evaluation gate;
- changes canonical source precedence below protected human-authored anchors;
- changes retention/privacy boundaries;
- modifies the governance-change process itself.

Changes to the **protected fourfold anchor content itself are stricter**: they are not agent self-modification at all. Only an authorized human may author them.

## 信力 escalation rule against 不信

信力 permits principled derivation for an unstated case, but it does not permit policy invention or blind acceptance. It must compare the anchors with observed fact and surface counterevidence.

Escalate instead of deriving autonomously when multiple reasonable interpretations would materially alter:
- who has authority;
- user or employee rights;
- privacy or data boundaries;
- money or financial commitment;
- production access;
- permission scope;
- irreversible external effects;
- the faith anchors themselves.

Prefer technical gates over prose-only prohibitions. A prompt instruction is not a substitute for sandbox, permissions, branch protection, CI checks, deployment review, or read-only trust-anchor exposure.

