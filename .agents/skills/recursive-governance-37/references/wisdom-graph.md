# 四聖諦 Wisdom Graph

Use this reference whenever the task involves diagnosis, causal judgment, retained experience, or visual/navigation logic. This is an engineering control model anchored to early Buddhist discourse identifiers; it is not a claim that software architecture and Buddhist doctrine are identical.

## Canonical priority

Use four source tiers and never silently promote a lower tier upward.

1. **L0 — Early-discourse source**: the normative Buddhist reference for this skill. Prefer early Nikāya/Āgama material and stable discourse identifiers.
2. **L1 — Canonical ontology**: machine-readable relationships extracted from L0, with provenance.
3. **L2 — Engineering interpretation**: repository/agent mappings such as Problem, Cause, Resolved State, Path, observability, authority, or harness.
4. **L3 — Presentation adapter**: UI language and metaphors. Later Buddhist / Mahāyāna vocabulary may be borrowed here as `upāya`-style explanatory dialect only. It may not rewrite L0–L2 semantics or authority.

If a doctrinal claim is uncertain, preserve the uncertainty. Do not use a later-tradition metaphor as evidence for an early-discourse claim.

## Wisdom trunk: 四聖諦

The decision graph is rooted in four distinct questions:

- **苦 / dukkha** — What is actually unsatisfactory, failing, risky, or lost? What must be understood?
- **集 / samudaya** — Under which causes and conditions does it arise? What must be abandoned, removed, or interrupted?
- **滅 / nirodha** — What observable state would show that the relevant arising has ceased? What must be realized/verified?
- **道 / magga** — What reproducible practice or intervention leads there? What must be developed?

Do not collapse symptom, cause, target state, and intervention into one field.

### No solution jump

A durable remedy may not be recorded as `magga-complete` while `samudaya` and `nirodha` remain undefined.

Emergency containment is allowed when delay would increase harm, but mark it `containment_only`. After stabilization, complete samudaya → nirodha → magga before treating the issue as resolved.

## Three turns / twelve aspects

For each truth track three states derived from SN 56.11's three-turn/twelve-aspect structure:

| Truth | Recognize | Task | Completion evidence |
|---|---|---|---|
| 苦 | this is the problem/loss | understand it completely | scope, impact, observation boundaries are known |
| 集 | this is the origin/condition | abandon or interrupt it | causal condition is removed/bounded and counterevidence considered |
| 滅 | this is cessation/resolved state | realize/verify it | observable cessation invariant holds |
| 道 | this is the path/intervention | develop it | intervention is implemented, exercised, and reverified |

The engineering labels are interpretive. Keep SN 56.11 as the canonical source reference.

## Sati memory: retention without indiscriminate activation

The skill does **not** implement knowledge deletion as an optimization mechanism.

Preserve meaningful observations, hypotheses, counterevidence, failed interventions, governance decisions, and superseded interpretations as append-only records when the repository has a suitable state store. A record may change status, scope, confidence, or applicability; it should not disappear merely because it is old or inconvenient.

This is a design rule, not the doctrinal equation “forgetting = defilement.” Early-discourse descriptions of `sati` include remembering and recollecting what was done and said long ago (for example AN 8.30), which supports treating retention/recollection as a useful engineering analogy.

Separate:

- **retention** — keep the evidence;
- **indexing** — make it discoverable;
- **activation** — load only what is relevant now;
- **adjudication** — prefer fresh observed state when old records conflict with mutable reality;
- **provenance** — record why a judgment changed instead of erasing the prior judgment.

Recommended record fields:

`id, observed_at, source, claim, scope, status, confidence, supports, contradicts, supersedes, superseded_by, last_revalidated_at, revalidation_condition`.

## Paññā routing

Wisdom reduces decision latency by compiling tested distinctions, not by deleting experience.

A route should answer:

1. Which truth is unresolved?
2. Which distinction will reduce uncertainty most?
3. Which evidence would discriminate competing causes?
4. Which 37-factor capability is needed next?
5. Which prior record is relevant, and under what scope?
6. What would falsify the current route?

Prefer a short, evidence-backed route over exhaustive recall.

## Multi-projection UI contract

The underlying structure is a graph. Tree views are projections, not the storage model.

Provide these projections when a UI exists:

- **Sacca Tree / 幹ビュー** — four truths as the main trunk, with the current branch expanded.
- **Path Trace / 筋ビュー** — illuminate only the currently traversed decision route.
- **Sibling Compare / 横ビュー** — compare peer factors such as 五根, 五力, or 七覚支.
- **Causal Graph / 縁起ビュー** — traverse conditions forward and reverse; engineering causal edges must keep evidence and confidence.
- **Three-turn Matrix / 三転ビュー** — four truths × recognize/task/completion.
- **Memory Timeline / 時間ビュー** — show retained observations, revisions, counterevidence, and supersession without deletion.

Keyboard access, visible focus, 320px reflow, reduced motion, and non-color-only status indicators are required for production UI.

## Relation to the 37 factors

This graph does not add a 38th factor. It is a navigation and judgment layer over the existing 37-factor registry.

- 四念処 supplies observation channels to the graph.
- 四正断 supplies improvement direction once the causal frame is sufficiently formed.
- 四神足 mobilizes the selected path.
- 慧根/慧力 operate the explicit/autonomous four-truth frame.
- 正見 integrates the four-truth model into system governance.
- 正念 preserves reconstructable evidence and state.
- 七覚支 adjusts exploration versus convergence when the current route is sluggish or restless.

The canonical registry count remains **37**.
