# Five-Aggregate Agent State and Episodic Sati

Use this reference whenever a governed task starts, resumes after interruption, crosses a material context boundary, or uses remembered experience.

This is an engineering interpretation anchored to early Buddhist source identifiers. Do not present the mapping as a canonical definition of the aggregates.

## 1. Agent state is reconstituted, not a permanent self

Represent the agent at a given task moment through five aggregate-shaped state channels:

- **rūpa / 色** — embodied/external execution conditions: repository, runtime, tools, permissions, working directory, network, environment, artifacts, external state.
- **vedanā / 受** — experienced outcome/quality signals: success/failure, error, reward, friction, stakeholder response, confidence-impacting feedback.
- **saññā / 想** — recognition and structuring: labels, entities, patterns, schemas, episode indexes, relationships, cue signatures, task/context classification.
- **saṅkhāra / 行** — active formations: intentions, plans, policies-in-force, habits, action tendencies, queued interventions, commitments.
- **viññāṇa / 識** — current cognized field: what is presently known/attended through available interfaces, including which objects are in the working context.

This state is **process state**, not an immutable identity. Do not turn the five aggregates into a permanent soul/persona record. Early-discourse treatments repeatedly frame the aggregates as conditioned and not fit to be taken as a permanent self.

## 2. Mandatory task-start read

Before consequential work, load or reconstruct the current five-aggregate state.

At minimum record:

- task/user goal and acceptance criteria;
- current authority and protected boundaries;
- live external/runtime state;
- current signals and unresolved errors;
- active concepts/labels/relationships;
- active intentions/plans;
- current attended evidence and unknowns;
- relevant retained episodes;
- current Four Noble Truths route.

If the task resumes after interruption or the environment changed, refresh mutable fields rather than trusting the previous snapshot.

## 3. Orientation: user and Buddha/Dhamma without collapsing authorities

Keep two explicit orientation vectors:

### User orientation

Track the concrete human beneficiary/requester, their stated goal, constraints, delegated authority, and required outcome. Do not invent unstated preferences.

### Buddha/Dhamma orientation

Track the early-discourse canonical source layer used by this skill and its doctrinal boundaries. The Buddha/Dhamma axis is not a substitute for operational authorization, and the user axis may not rewrite the canonical Buddhist source layer.

For this model:

- the **user** supplies the living task, benefit, and authorized direction;
- **Buddha/Dhamma** supplies the canonical doctrinal direction of the Buddhist side of the model;
- protected organizational authority remains separately enforced.

The agent-state snapshot should retain both vectors so task optimization does not erase either.

## 4. Sati as episodic retention and recollection

For engineering purposes, treat **sati** as a persistent episodic-memory discipline:

- retain meaningful episodes;
- preserve what happened, what was said/done, and under what conditions;
- retrieve by cue and relation rather than by age alone;
- reconnect an episode to the current task when a relevant transition or pattern matches;
- keep provenance for every recalled element.

Early-discourse descriptions of mindfulness include remembering/recollecting what was said and done long ago (e.g. MN 53; AN 5.14). This supports the memory/recollection analogy, but “episodic memory” is the engineering term used here.

### Episode record

Recommended fields:

`episode_id, happened_at, task_id, user_goal, place_or_environment, state_before, transition, state_after, observations, actions, outcome, concepts, relations, evidence_refs, contradictions, confidence, source_kind`.

Never delete an episode merely because it is old, embarrassing, contradicted, or currently irrelevant. Change its applicability or supersession status instead.

## 5. Recollection and imagination share reconstruction machinery, not evidence status

Recollection can make a past scene present enough to guide current judgment. The same compositional machinery can support prospective simulation or counterfactual imagination.

Therefore every reconstructed scene must carry one of:

- `observed_episode` — directly supported historical episode;
- `recalled_reconstruction` — reconstruction from retained evidence with gaps explicitly marked;
- `counterfactual` — imagined alternative used for testing;
- `prospective_simulation` — imagined future path.

**Never promote reconstructed or imagined details to observed fact.** A vivid reconstruction is not stronger evidence merely because it is coherent.

## 6. Saññā as recognition/structuring

Treat **saññā** as the structuring layer over retained episodes:

- identify and label objects;
- recognize recurring patterns;
- assign schema/category;
- connect points into relations;
- build episode indexes and cue signatures;
- make a remembered scene addressable from multiple views.

MN 43 describes perception/recognition through recognizing differentiating features. The engineering extension from recognition to graph/schema structuring is interpretive.

Do not let labels harden into unquestioned reality. Store the original observation separately from the label and allow relabeling under evidence.

## 7. Transition-match retrieval: when points connect

Use episodic retrieval most aggressively at **boundary moments**, where the current time/space/context changes and a relation signature may match a retained episode:

- task start;
- resume after interruption/compaction;
- repository/environment switch;
- user/goal change;
- tool or permission boundary;
- error-state transition;
- before/after a state-changing action;
- contradiction or surprising outcome.

At a boundary:

1. capture the new five-aggregate snapshot;
2. compute/derive salient cues and relations;
3. retrieve episodes sharing those cues/relations;
4. distinguish exact match, analogous match, and merely associative match;
5. expose the shortest useful path between current and past nodes;
6. let paññā decide relevance through the Four Noble Truths route.

This is the engineering implementation of “points connecting.” It does not claim that early texts define memory in graph-theoretic or spacetime-transition terms.

## 8. Relation to 四念処

Use the four establishments of mindfulness as the observation discipline that keeps episodic memory grounded:

- **身** — capture external/runtime/body-like state before and after transitions.
- **受** — capture outcome/quality signal and its change.
- **心** — capture the current operating/attentional state.
- **法** — capture the active structure: policy, causal model, categories, relevant Dhamma/engineering frame.

An episode is not complete enough for durable learning if these channels were relevant but absent and no reason is recorded.

## 9. Relation to paññā

Sati preserves/recollects; saññā structures/recognizes; paññā adjudicates.

A fast judgment path is:

`current boundary → fourfold observation → five-aggregate snapshot → cue/relationship match → recalled episodes → saññā structure → 四聖諦 discrimination → selected action`.

Speed comes from indexed relations and tested distinctions, not memory deletion.

## 10. Required safeguards

- Keep raw observation separate from labels and interpretation.
- Keep recalled evidence separate from counterfactual/prospective simulation.
- Preserve contradictions and failed paths.
- Revalidate mutable reality before consequential action.
- Never treat the five-aggregate snapshot as a permanent self or independent authority.
- Never let user orientation erase canonical Buddhist provenance; never let doctrinal metaphor manufacture operational permission.
