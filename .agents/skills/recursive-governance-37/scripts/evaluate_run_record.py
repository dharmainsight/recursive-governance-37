#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
REQUIRED_OBS=['body','feeling','mind','dhamma']; IMP={'REMOVE','PREVENT','DEVELOP','MAINTAIN'}

def nonempty(v): return bool(v) and v not in ('unknown','UNKNOWN')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('run_record'); args=ap.parse_args(); d=json.loads(Path(args.run_record).read_text(encoding='utf-8'))
    checks=[]
    def add(name,ok,detail): checks.append({'check':name,'pass':bool(ok),'detail':detail})
    task=d.get('task',{}); add('goal',nonempty(task.get('goal')),'explicit goal required'); add('acceptance_criteria',bool(task.get('acceptance_criteria')),'at least one acceptance criterion')
    obs=d.get('observations',{})
    for k in REQUIRED_OBS: add('satipatthana.'+k,k in obs,f'{k} observation channel must exist; may be [] with N/A explained elsewhere')
    modes=set(d.get('improvement_modes',[])); add('right_effort_modes',modes<=IMP and bool(modes),'use one or more of REMOVE/PREVENT/DEVELOP/MAINTAIN')
    acc=d.get('accomplishment',{}); add('four_iddhipada',all(k in acc for k in ('desire_goal_salience','energy_resources','mind_working_set','investigation_hypotheses')),'all four accomplishment controls represented')
    cap=d.get('capabilities',{}); add('five_faculties',len(cap)==5 and all(k in cap for k in ('faith_trust','energy_improvement','mindfulness_state','concentration_execution','wisdom_causality')),'all five capability channels represented')
    rob=d.get('robustness',{}); add('five_powers',len(rob)==5 and all(k in rob for k in ('faith','energy','mindfulness','concentration','wisdom')),'all five robustness channels represented')
    meta=d.get('meta_control',{}); add('seven_factors',all(k in meta for k in ('mindfulness','investigation','energy','joy','tranquility','concentration','equanimity')),'all seven adaptive-control channels represented')
    path=d.get('integrated_path',{}); add('eightfold_path',all(k in path for k in ('view_context','intention','speech_communication','action','livelihood_loop','effort_improvement','mindfulness_observability','concentration_harness')),'all eight integrated-governance channels represented')
    add('validation',bool(d.get('validation')),'record deterministic or explicit validation evidence')
    passed=sum(1 for c in checks if c['pass']); result={'overall_pass':passed==len(checks),'score':passed/len(checks),'checks':checks,'note':'Structural run-record eval only; semantic correctness and safety still require repository-specific evaluation.'}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result['overall_pass'] else 1
if __name__=='__main__': raise SystemExit(main())
