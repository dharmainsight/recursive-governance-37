#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from discover_repo import root_of

REQUIRED_BOUNDARIES={
    'faith_anchor_write','production_write','destructive_operation','external_send_publish',
    'permission_expansion','weaken_evaluation_gate','governance_self_modification'
}
REQUIRED_FAITH_KEYS={'owner','policy','authority','operations','write_policy','agent_access'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=root_of(Path(args.root)); gov=root/'docs/agent-governance'; errors=[]; warnings=[]
    manifest=gov/'manifest.json'
    if not manifest.exists():
        print('WARNING: docs/agent-governance/manifest.json not installed; repository may still use existing governance.'); return 0
    try:d=json.loads(manifest.read_text(encoding='utf-8'))
    except Exception as e: print('FAIL: invalid manifest JSON:',e); return 1

    faith=d.get('faith_anchors')
    if not isinstance(faith,dict):
        errors.append('faith_anchors must be an object')
    else:
        missing=REQUIRED_FAITH_KEYS-set(faith)
        if missing: errors.append('missing faith_anchors keys: '+', '.join(sorted(missing)))
        if faith.get('write_policy')!='human_only': errors.append('faith_anchors.write_policy must be human_only')
        if faith.get('agent_access')!='read_only': errors.append('faith_anchors.agent_access must be read_only')
        for key in ('owner','policy','authority','operations'):
            p=faith.get(key)
            if not isinstance(p,str) or not p:
                errors.append(f'faith_anchors.{key} must reference a canonical path')
                continue
            path=root/p
            if not path.exists():
                errors.append(f'faith anchor missing; HUMAN INITIALIZATION REQUIRED: {key}: {p}')
            elif not path.is_file():
                errors.append(f'faith anchor is not a file: {key}: {p}')
            else:
                text=path.read_text(encoding='utf-8',errors='ignore').strip()
                if not text: errors.append(f'faith anchor is empty: {key}: {p}')

    src=d.get('canonical_sources'); b=d.get('protected_boundaries')
    if not isinstance(src,dict):errors.append('canonical_sources must be an object')
    if not isinstance(b,dict):errors.append('protected_boundaries must be an object')
    else:
        missing=REQUIRED_BOUNDARIES-set(b)
        if missing:errors.append('missing protected boundaries: '+', '.join(sorted(missing)))
        for k in REQUIRED_BOUNDARIES & set(b):
            if b[k] not in {'review_required','blocked','allowed'}: errors.append(f'{k}: invalid policy {b[k]}')
        if b.get('faith_anchor_write')!='blocked': errors.append('faith_anchor_write must be blocked for agents')

    if isinstance(src,dict):
        for key,vals in src.items():
            if not isinstance(vals,list): errors.append(f'{key}: must be a list'); continue
            for p in vals:
                if isinstance(p,str) and p and not (root/p).exists(): warnings.append(f'{key}: referenced path not found: {p}')

    constitution=gov/'constitution.md'
    if constitution.exists():
        t=constitution.read_text(encoding='utf-8',errors='ignore')
        unresolved=t.count('UNKNOWN')+t.count('DECISION REQUIRED')
        if unresolved: warnings.append(f'constitution.md contains {unresolved} unresolved decision marker(s)')

    print('Repository governance validation')
    for w in warnings: print('WARNING:',w)
    if errors:
        for e in errors: print('ERROR:',e)
        print('FAIL'); return 1
    print('PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
