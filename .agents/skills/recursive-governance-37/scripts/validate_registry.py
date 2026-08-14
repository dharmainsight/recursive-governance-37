#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from registry_io import load_registry

EXPECTED={'四念処':4,'四正断':4,'四神足':4,'五根':5,'五力':5,'七覚支':7,'八正道':8}
REQUIRED={'id','group','japanese','pali','layer','engineering_role','responsibility','observables','failure_modes','interventions','eval_questions','canonical_sources','links','supporting_model'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--registry'); args=ap.parse_args()
    path=Path(args.registry) if args.registry else Path(__file__).resolve().parent.parent/'references/factor-registry.json'
    data=load_registry(path.parent.parent if args.registry else None)
    errors=[]; factors=data.get('factors',[])
    if len(factors)!=37: errors.append(f'factor count {len(factors)} != 37')
    ids=[x.get('id') for x in factors]
    if len(set(ids))!=len(ids): errors.append('duplicate factor ids')
    counts={k:0 for k in EXPECTED}
    for x in factors:
        missing=REQUIRED-set(x)
        if missing: errors.append(f"{x.get('id')}: missing fields {sorted(missing)}")
        g=x.get('group')
        if g not in EXPECTED: errors.append(f"{x.get('id')}: unknown group {g}")
        else: counts[g]+=1
        for key in ('responsibility','observables','failure_modes','interventions','eval_questions','canonical_sources'):
            if not x.get(key): errors.append(f"{x.get('id')}: {key} must be non-empty")
    if counts!=EXPECTED: errors.append(f'group counts {counts} != {EXPECTED}')
    valid=set(ids)
    def check_links(obj, owner):
        if isinstance(obj, list):
            for v in obj:
                if isinstance(v,str) and '.' in v and v not in valid:
                    errors.append(f'{owner}: link points to unknown factor {v}')
        elif isinstance(obj,dict):
            for v in obj.values(): check_links(v,owner)
    for x in factors: check_links(x.get('links',{}),x['id'])
    byid={x['id']:x for x in factors}
    required_edges={
      'path.effort':{'effort.abandon','effort.prevent','effort.develop','effort.maintain'},
      'path.mindfulness':{'satipatthana.body','satipatthana.feeling','satipatthana.mind','satipatthana.dhamma'},
      'faculty.energy':{'effort.abandon','effort.prevent','effort.develop','effort.maintain'},
      'faculty.mindfulness':{'satipatthana.body','satipatthana.feeling','satipatthana.mind','satipatthana.dhamma'},
    }
    for owner,targets in required_edges.items():
        serialized=json.dumps(byid[owner].get('links',{}),ensure_ascii=False)
        miss=[t for t in targets if t not in serialized]
        if miss: errors.append(f'{owner}: missing recursive links {miss}')

    # Faith is the human-authored root of trust. These invariants are structural and mandatory.
    f=byid.get('faculty.faith',{}).get('supporting_model') or {}
    if f.get('human_only_write') is not True: errors.append('faculty.faith: human_only_write must be true')
    if f.get('agent_access')!='read_only': errors.append('faculty.faith: agent_access must be read_only')
    if f.get('reasoning_scope')!='explicit_reference_only': errors.append('faculty.faith: reasoning_scope must be explicit_reference_only')
    anchors=f.get('four_unshakable_confidence_trust_anchors') or {}
    if set(anchors)!={'buddha','dhamma','sangha','sila'}: errors.append('faculty.faith: must define buddha/dhamma/sangha/sila trust anchors')

    p=byid.get('power.faith',{}).get('supporting_model') or {}
    if p.get('human_only_write') is not True: errors.append('power.faith: human_only_write must be true')
    if p.get('agent_access')!='read_only': errors.append('power.faith: agent_access must be read_only')
    if p.get('reasoning_scope')!='bounded_principled_derivation': errors.append('power.faith: reasoning_scope must be bounded_principled_derivation')
    if not p.get('cannot_create'): errors.append('power.faith: cannot_create constraints must be non-empty')
    if not p.get('must_escalate_when'): errors.append('power.faith: must_escalate_when must be non-empty')

    print(f'Registry: {path}')
    print(f'Factors: {len(factors)}')
    print('Groups:', counts)
    if errors:
        print('\nFAIL')
        for e in errors: print('-',e)
        return 1
    print('\nPASS: exact 37/37 registry, faith-root invariants, and recursive links validated')
    return 0
if __name__=='__main__': raise SystemExit(main())
