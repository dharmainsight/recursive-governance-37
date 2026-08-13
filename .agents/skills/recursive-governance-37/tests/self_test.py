#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path
SKILL=Path(__file__).resolve().parent.parent; SCRIPTS=SKILL/'scripts'

def run(args,cwd=None,expect=0):
    p=subprocess.run([sys.executable,*map(str,args)],cwd=cwd,text=True,capture_output=True)
    if p.returncode!=expect:
        print('COMMAND FAILED',args); print(p.stdout); print(p.stderr); raise SystemExit(1)
    return p.stdout

def main():
    out=run([SCRIPTS/'validate_registry.py'])
    assert '37/37' in out
    sys.path.insert(0, str(SCRIPTS))
    from registry_io import load_registry
    registry=load_registry(SKILL)
    assert len(registry['factors'])==37
    assert registry['group_counts']=={'四念処':4,'四正断':4,'四神足':4,'五根':5,'五力':5,'七覚支':7,'八正道':8}
    # Sample run record must pass structural evaluator.
    out=run([SCRIPTS/'evaluate_run_record.py',SKILL/'tests/sample-run-record.json'])
    assert '"overall_pass": true' in out
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); (root/'.git').mkdir(); (root/'src').mkdir(); (root/'tests').mkdir(); (root/'.github/workflows').mkdir(parents=True)
        (root/'README.md').write_text('# Demo\nGoal: safe service\n',encoding='utf-8')
        (root/'AGENTS.md').write_text('Run tests before completion. Do not deploy production.\n',encoding='utf-8')
        (root/'tests/test_demo.py').write_text('def test_ok(): assert True\n',encoding='utf-8')
        (root/'.github/workflows/ci.yml').write_text('name: ci\n',encoding='utf-8')
        dry=run([SCRIPTS/'scaffold.py','--root',root]); assert 'DRY RUN' in dry; assert not (root/'docs/agent-governance').exists()
        run([SCRIPTS/'scaffold.py','--root',root,'--apply']); assert (root/'docs/agent-governance/manifest.json').exists()
        run([SCRIPTS/'validate_repo_governance.py','--root',root])
        audit=json.loads(run([SCRIPTS/'audit_repo.py','--root',root])); assert audit['factor_count']==37
        # Non-destructive: re-run scaffold and ensure existing file is skipped.
        before=(root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')
        rerun=run([SCRIPTS/'scaffold.py','--root',root,'--apply']); assert 'SKIP existing' in rerun
        assert (root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')==before
    print('PASS: recursive-governance-37 self-test')
    return 0
if __name__=='__main__': raise SystemExit(main())
