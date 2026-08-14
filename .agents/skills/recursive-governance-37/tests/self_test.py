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

    faith=next(x for x in registry['factors'] if x['id']=='faculty.faith')
    assert faith['supporting_model']['human_only_write'] is True
    assert faith['supporting_model']['agent_access']=='read_only'
    assert faith['supporting_model']['reasoning_scope']=='explicit_reference_only'
    power=next(x for x in registry['factors'] if x['id']=='power.faith')
    assert power['supporting_model']['human_only_write'] is True
    assert power['supporting_model']['reasoning_scope']=='bounded_principled_derivation'

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
        assert 'HUMAN INITIALIZATION REQUIRED' in dry

        applied=run([SCRIPTS/'scaffold.py','--root',root,'--apply'])
        assert (root/'docs/agent-governance/manifest.json').exists()
        assert 'HUMAN INITIALIZATION REQUIRED' in applied
        # The agent scaffold must not author faith content.
        assert not (root/'docs/agent-governance/faith/owner.md').exists()
        assert not (root/'docs/agent-governance/faith/policy.md').exists()
        assert not (root/'docs/agent-governance/faith/authority.md').exists()
        assert not (root/'docs/agent-governance/faith/operations.md').exists()

        # Validation must fail until an authorized human initializes the trust root.
        fail=run([SCRIPTS/'validate_repo_governance.py','--root',root],expect=1)
        assert 'HUMAN INITIALIZATION REQUIRED' in fail

        # Simulate authorized human initialization. The skill itself never performs this step.
        faith_dir=root/'docs/agent-governance/faith'; faith_dir.mkdir(parents=True)
        (faith_dir/'owner.md').write_text('# Owner\nHuman owner: Example Owner\n',encoding='utf-8')
        (faith_dir/'policy.md').write_text('# Policy\nMission: safe service\n',encoding='utf-8')
        (faith_dir/'authority.md').write_text('# Authority\nEngineering may change application code. Production deploy requires owner approval.\n',encoding='utf-8')
        (faith_dir/'operations.md').write_text('# Operating rules\nNo autonomous production writes. Run tests before merge.\n',encoding='utf-8')

        run([SCRIPTS/'validate_repo_governance.py','--root',root])
        audit=json.loads(run([SCRIPTS/'audit_repo.py','--root',root])); assert audit['factor_count']==37

        # Non-destructive: re-run scaffold and ensure existing ordinary governance file is skipped.
        before=(root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')
        rerun=run([SCRIPTS/'scaffold.py','--root',root,'--apply']); assert 'SKIP existing' in rerun
        assert 'Faith anchors detected. Do not modify them from an agent run.' in rerun
        assert (root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')==before

    print('PASS: recursive-governance-37 self-test')
    return 0
if __name__=='__main__': raise SystemExit(main())
