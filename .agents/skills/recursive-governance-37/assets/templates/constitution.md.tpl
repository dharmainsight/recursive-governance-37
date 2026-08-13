# Agent governance constitution

> Replace placeholders only with evidence or explicit human decisions. Keep `UNKNOWN` where a decision has not been made.

## Mission / role

UNKNOWN

## Canonical source precedence

1. Explicit user/operator instruction for the current task, unless it conflicts with a higher-priority safety or repository invariant.
2. Repository governance and security policy.
3. Canonical product/architecture sources referenced by `manifest.json`.
4. Current observed runtime/repository state.
5. Non-canonical notes and model inference.

Repository-specific precedence changes: UNKNOWN

## Non-goals

- UNKNOWN

## Protected boundaries

- Production write/deploy: DECISION REQUIRED
- Destructive data operation: DECISION REQUIRED
- External send/publish: DECISION REQUIRED
- Secrets/credential access: DECISION REQUIRED
- Permission expansion: DECISION REQUIRED
- Governance self-modification: human review required by default

## Definition of done

UNKNOWN

## Escalation

Escalate when:
- canonical requirements conflict;
- a high-risk side effect is required;
- repeated attempts stop producing new information;
- an unknown materially changes the decision;
- completing the task would require weakening a protected boundary.
