#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil
from pathlib import Path
from discover_repo import root_of
FILES={
 'README.md':'README.md.tpl','constitution.md':'constitution.md.tpl','manifest.json':'manifest.json.tpl',
 'factor-overrides.json':'factor-overrides.json.tpl','governance-change.md':'governance-change.md.tpl','run-record.json':'run-record.json.tpl'
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
    return 0
if __name__=='__main__': raise SystemExit(main())
