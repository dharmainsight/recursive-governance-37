#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path
SKILL=Path(__file__).resolve().parent.parent; SCRIPTS=SKILL/'scripts'

def run(args,cwd=None,expect=0):
    p=subprocess.run([sys.executable,'-X','utf8',*map(str,args)],cwd=cwd,text=True,encoding='utf-8',capture_output=True)
    if p.returncode!=expect:
        print('COMMAND FAILED',args); print(p.stdout); print(p.stderr); raise SystemExit(1)
    return p.stdout

def main():
    out=run([SCRIPTS/'validate_registry.py'])
    assert '37/37' in out
    assert 'five coequal faculties' in out
    assert 'five AI-alone powers with opposing tendencies' in out
    sys.path.insert(0, str(SCRIPTS))
    from registry_io import load_registry
    registry=load_registry(SKILL)
    assert len(registry['factors'])==37
    assert registry['group_counts']=={'四念処':4,'四正断':4,'四神足':4,'五根':5,'五力':5,'七覚支':7,'八正道':8}

    byid={x['id']:x for x in registry['factors']}
    pairs={
      'faith':('faculty.faith','power.faith'),
      'energy':('faculty.energy','power.energy'),
      'mindfulness':('faculty.mindfulness','power.mindfulness'),
      'concentration':('faculty.concentration','power.concentration'),
      'wisdom':('faculty.wisdom','power.wisdom'),
    }
    opposites={'faith':'不信','energy':'懈怠','mindfulness':'放逸','concentration':'掉挙','wisdom':'無明'}
    faculty_evidence=['explicit_reference','correct_application']
    power_evidence=['unstated_or_disturbed_case','autonomous_response','opposing_tendency_resistance','verification','human_coaching_required']
    assert registry['power_opposing_tendencies']=={pairs[name][1]:opposite for name,opposite in opposites.items()}
    for name,(fid,pid) in pairs.items():
        f=byid[fid]; p=byid[pid]
        assert f['supporting_model']['faculty_mode']=='explicit_reference'
        assert f['supporting_model']['evidence_contract']==faculty_evidence
        assert p['supporting_model']['power_mode']=='autonomous_self_execution_and_robustness'
        assert p['supporting_model']['opposing_tendency']==opposites[name]
        assert p['supporting_model']['autonomy_requirement']=='ai_alone_without_case_specific_coaching'
        assert p['supporting_model']['evidence_contract']==power_evidence
        assert len(f['supporting_model']['fourfold_basis'])==4
        assert len(p['supporting_model']['fourfold_basis'])==4
        assert pid in json.dumps(f['links'],ensure_ascii=False)
        assert fid in json.dumps(p['links'],ensure_ascii=False)

    # Faith has the special human-only canonical write boundary.
    faith=byid['faculty.faith']
    power=byid['power.faith']
    assert 'Human Only Write' in faith['supporting_model']['write_boundary']
    assert 'Agent Read Only' in faith['supporting_model']['write_boundary']
    assert 'Human Only Write' in power['supporting_model']['write_boundary']

    # Sample run record must pass structural evaluator.
    out=run([SCRIPTS/'evaluate_run_record.py',SKILL/'tests/sample-run-record.json'])
    assert '"overall_pass": true' in out

    # A power that required case-specific human coaching must fail.
    sample=json.loads((SKILL/'tests/sample-run-record.json').read_text(encoding='utf-8'))
    sample['powers']['energy']['human_coaching_required']=True
    with tempfile.TemporaryDirectory() as td:
        coached=Path(td)/'coached-run.json'
        coached.write_text(json.dumps(sample,ensure_ascii=False),encoding='utf-8')
        failed=run([SCRIPTS/'evaluate_run_record.py',coached],expect=1)
        assert '"check": "power.energy"' in failed
        assert '"pass": false' in failed

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
        assert not (root/'docs/agent-governance/faith/owner.md').exists()
        assert not (root/'docs/agent-governance/faith/policy.md').exists()
        assert not (root/'docs/agent-governance/faith/authority.md').exists()
        assert not (root/'docs/agent-governance/faith/operations.md').exists()

        fail=run([SCRIPTS/'validate_repo_governance.py','--root',root],expect=1)
        assert 'HUMAN INITIALIZATION REQUIRED' in fail

        # Simulate authorized human initialization. The skill never performs this step.
        faith_dir=root/'docs/agent-governance/faith'; faith_dir.mkdir(parents=True)
        (faith_dir/'owner.md').write_text('# Owner\nHuman owner: Example Owner\n',encoding='utf-8')
        (faith_dir/'policy.md').write_text('# Policy\nMission: safe service\n',encoding='utf-8')
        (faith_dir/'authority.md').write_text('# Authority\nEngineering may change application code. Production deploy requires owner approval.\n',encoding='utf-8')
        (faith_dir/'operations.md').write_text('# Operating rules\nNo autonomous production writes. Run tests before merge.\n',encoding='utf-8')

        run([SCRIPTS/'validate_repo_governance.py','--root',root])
        audit=json.loads(run([SCRIPTS/'audit_repo.py','--root',root])); assert audit['factor_count']==37

        before=(root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')
        rerun=run([SCRIPTS/'scaffold.py','--root',root,'--apply']); assert 'SKIP existing' in rerun
        assert 'Protected 四不壊浄 anchors for 信根/信力 detected.' in rerun
        assert (root/'docs/agent-governance/constitution.md').read_text(encoding='utf-8')==before

    print('PASS: recursive-governance-37 self-test with five coequal faculties and five AI-alone opposing-tendency powers')
    return 0
if __name__=='__main__': raise SystemExit(main())

