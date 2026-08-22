#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil
from pathlib import Path
from discover_repo import root_of

FILES={
 'README.md':'README.md.tpl',
 'constitution.md':'constitution.md.tpl',
 'manifest.json':'manifest.json.tpl',
 'factor-overrides.json':'factor-overrides.json.tpl',
 'governance-change.md':'governance-change.md.tpl',
 'run-record.json':'run-record.json.tpl'
}

FAITH_PATHS={
 '仏 / Owner':'docs/agent-governance/faith/owner.md',
 '法 / Policy':'docs/agent-governance/faith/policy.md',
 '僧 / People and delegated authority':'docs/agent-governance/faith/authority.md',
 '戒 / Operating rules':'docs/agent-governance/faith/operations.md'
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--apply',action='store_true'); args=ap.parse_args()
    root=root_of(Path(args.root)); target=root/'docs/agent-governance'; templates=Path(__file__).resolve().parent.parent/'assets/templates'
    print('Mode:', 'APPLY' if args.apply else 'DRY RUN')
    for rel,tpl in FILES.items():
        dst=target/rel
        if dst.exists(): print('SKIP existing',dst.relative_to(root)); continue
        print('CREATE',dst.relative_to(root))
        if args.apply:
            dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(templates/tpl,dst)

    missing=[]
    for label,rel in FAITH_PATHS.items():
        if not (root/rel).exists(): missing.append((label,rel))

    if missing:
        print('\nHUMAN INITIALIZATION REQUIRED: the protected 四不壊浄 basis inside 信根/信力 is human-authored and agent-read-only.')
        print('This scaffold intentionally does NOT create or populate the following canonical files:')
        for label,rel in missing: print(f'- {label}: {rel}')
        print('An authorized human must create them directly, or update manifest.json to reference existing human-authored canonical documents.')
        print('After initialization, configure a hard agent write-deny/read-only boundary for those anchors and rerun validation.')
    else:
        print('\nProtected 四不壊浄 anchors for 信根/信力 detected. Do not modify them from an agent run.')
    return 0
if __name__=='__main__': raise SystemExit(main())

