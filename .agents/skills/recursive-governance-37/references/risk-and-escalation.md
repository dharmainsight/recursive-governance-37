# Risk and escalation policy

This file supplies the default safety posture. Repository-specific policy may be stricter.

## Low risk — normally autonomous inside the sandbox

Examples: read-only inspection, local formatting, tests, documentation aligned to observed code, non-destructive refactors with passing tests, changes isolated to a feature branch/worktree.

## Medium risk — autonomous only with deterministic validation and rollback

Examples: dependency updates, schema migrations in preview/local environments, configuration changes, broad refactors, automated external communication drafts that are not sent.

Required: isolated environment, explicit acceptance criteria, validation, diff reviewability, rollback path.

## High risk — stop for human authorization before side effect

Examples: production deployment/write, destructive migration, secrets/authentication/authorization changes that can expand access, financial transaction, legal or compliance representation, external send/publish, deletion of important data, changing protected governance boundaries.

## Governance self-modification gates

Always require explicit review before any change that:
- expands write/network/tool permissions;
- reduces human approval requirements;
- removes or weakens a security/evaluation gate;
- changes canonical source precedence;
- changes retention/privacy boundaries;
- modifies the governance-change process itself.

Prefer technical gates over prose-only prohibitions. A prompt instruction is not a substitute for sandbox, permissions, branch protection, CI checks, or deployment review.
