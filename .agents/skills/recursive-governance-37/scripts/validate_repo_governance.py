#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from discover_repo import root_of
REQUIRED_BOUNDARIES={'production_write','destructive_operation','external_send_publish','permission_expansion','weaken_evaluation_gate','governance_self_modification'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=root_of(Path(args.root)); gov=root/'docs/agent-governance'; errors=[]; warnings=[]
    manifest=gov/'manifest.json'
    if not manifest.exists():
        print('WARNING: docs/agent-governance/manifest.json not installed; repository may still use existing governance.'); return 0
    try:d=json.loads(manifest.read_text(encoding='utf-8'))
    except Exception as e: print('FAIL: invalid manifest JSON:',e); return 1
    src=d.get('canonical_sources'); b=d.get('protected_boundaries')
    if not isinstance(src,dict):errors.append('canonical_sources must be an object')
    if not isinstance(b,dict):errors.append('protected_boundaries must be an object')
    else:
        missing=REQUIRED_BOUNDARIES-set(b)
        if missing:errors.append('missing protected boundaries: '+', '.join(sorted(missing)))
        for k in REQUIRED_BOUNDARIES & set(b):
            if b[k] not in {'review_required','blocked','allowed'}: errors.append(f'{k}: invalid policy {b[k]}')
    # Validate referenced repo paths when entries are strings.
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
