#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from registry_io import load_registry

EXPECTED={'四念処':4,'四正断':4,'四神足':4,'五根':5,'五力':5,'七覚支':7,'八正道':8}
REQUIRED={'id','group','japanese','pali','layer','engineering_role','responsibility','observables','failure_modes','interventions','eval_questions','canonical_sources','links','supporting_model'}
PAIRS={
  'faith':('faculty.faith','power.faith'),
  'energy':('faculty.energy','power.energy'),
  'mindfulness':('faculty.mindfulness','power.mindfulness'),
  'concentration':('faculty.concentration','power.concentration'),
  'wisdom':('faculty.wisdom','power.wisdom'),
}

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
      'power.energy':{'effort.abandon','effort.prevent','effort.develop','effort.maintain'},
      'power.mindfulness':{'satipatthana.body','satipatthana.feeling','satipatthana.mind','satipatthana.dhamma'},
    }
    for owner,targets in required_edges.items():
        serialized=json.dumps(byid[owner].get('links',{}),ensure_ascii=False)
        miss=[t for t in targets if t not in serialized]
        if miss: errors.append(f'{owner}: missing recursive links {miss}')

    # Universal faculty-power duality.
    for name,(fid,pid) in PAIRS.items():
        f=byid.get(fid)
        p=byid.get(pid)
        if not f or not p:
            errors.append(f'{name}: missing faculty/power pair')
            continue
        fs=f.get('supporting_model') or {}
        ps=p.get('supporting_model') or {}
        if fs.get('faculty_mode')!='explicit_reference':
            errors.append(f'{fid}: faculty_mode must be explicit_reference')
        if not str(ps.get('power_mode','')).startswith('autonomous_'):
            errors.append(f'{pid}: power_mode must be an autonomous_* mode')
        if len(fs.get('fourfold_basis') or [])!=4:
            errors.append(f'{fid}: fourfold_basis must contain exactly four elements')
        if len(ps.get('fourfold_basis') or [])!=4:
            errors.append(f'{pid}: fourfold_basis must contain exactly four elements')
        if pid not in json.dumps(f.get('links',{}),ensure_ascii=False):
            errors.append(f'{fid}: must link to paired power {pid}')
        if fid not in json.dumps(p.get('links',{}),ensure_ascii=False):
            errors.append(f'{pid}: must link to paired faculty {fid}')

    # Faith has a special write boundary; duality itself is not special to faith.
    ff=byid.get('faculty.faith',{}).get('supporting_model') or {}
    fp=byid.get('power.faith',{}).get('supporting_model') or {}
    if 'Human Only Write' not in str(ff.get('write_boundary','')):
        errors.append('faculty.faith: canonical faith must be Human Only Write')
    if 'Agent Read Only' not in str(ff.get('write_boundary','')):
        errors.append('faculty.faith: canonical faith must be Agent Read Only')
    if 'Human Only Write' not in str(fp.get('write_boundary','')):
        errors.append('power.faith: canonical faith must remain Human Only Write')

    print(f'Registry: {path}')
    print(f'Factors: {len(factors)}')
    print('Groups:', counts)
    print('Faculty-power pairs:', ', '.join(PAIRS))
    if errors:
        print('\nFAIL')
        for e in errors: print('-',e)
        return 1
    print('\nPASS: exact 37/37 registry, five faculty-power dual pairs, faith-root boundary, and recursive links validated')
    return 0
if __name__=='__main__': raise SystemExit(main())
