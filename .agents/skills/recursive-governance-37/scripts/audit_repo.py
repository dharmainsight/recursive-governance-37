#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from discover_repo import discover, root_of

PATTERNS={
 'satipatthana.body':['test','build','runtime','browser','schema','api','migration','deploy'],
 'satipatthana.feeling':['metric','slo','feedback','latency','error','quality','conversion','eval'],
 'satipatthana.mind':['agent','retry','trace','context','scope','run-record'],
 'satipatthana.dhamma':['policy','architecture','adr','rfc','taxonomy','governance','decision'],
 'effort.abandon':['bug','incident','fix','rollback','remediation','hotfix'],
 'effort.prevent':['regression','security','lint','validation','guard','permission','policy'],
 'effort.develop':['feature','roadmap','requirement','spec','experiment'],
 'effort.maintain':['refactor','maintenance','optimiz','documentation','slo'],
 'iddhipada.desire':['goal','objective','acceptance','non-goal','priority','roadmap'],
 'iddhipada.energy':['retry','budget','timeout','parallel','concurrency','resource'],
 'iddhipada.mind':['scope','worktree','branch','context','task'],
 'iddhipada.investigation':['hypothesis','experiment','root cause','rfc','adr','investigation'],
 'faculty.faith':['source of truth','canonical','provenance','review','policy','agents.md'],
 'faculty.energy':['workflow','repair','test','lint','incident'],
 'faculty.mindfulness':['state','trace','log','run-record','observability'],
 'faculty.concentration':['sandbox','ci','test','build','scope','approval'],
 'faculty.wisdom':['root cause','causal','incident','adr','desired state','acceptance'],
 'power.faith':['prompt injection','untrusted','provenance','precedence','canonical'],
 'power.energy':['retry','backoff','escalat','failure'],
 'power.mindfulness':['checkpoint','resume','state','history','trace'],
 'power.concentration':['scope','branch','parallel','worktree','limit'],
 'power.wisdom':['unknown','uncertainty','hypothesis','counterexample','falsif'],
 'awakening.mindfulness':['meta-control','stagnation','thrash','loop state'],
 'awakening.investigation':['alternative hypothesis','investigation','strategy','experiment'],
 'awakening.energy':['stagnation','retry budget','parallelism','effort'],
 'awakening.joy':['milestone','progress','validated progress','success metric'],
 'awakening.tranquility':['thrash','cooldown','churn','reduce parallel'],
 'awakening.concentration':['scope freeze','converge','single hypothesis','acceptance criteria'],
 'awakening.equanimity':['sunk cost','rollback','stop condition','neutral'],
 'path.view':['requirement','architecture','current state','desired state','root cause','source of truth'],
 'path.intention':['objective','non-goal','harmless','reversible','risk'],
 'path.speech':['communication','provenance','confidential','report','pr template'],
 'path.action':['permission','sandbox','approval','deploy','production','authorization'],
 'path.livelihood':['workflow','schedule','cron','queue','retry','escalat','resource'],
 'path.effort':['test','lint','security','regression','incident','eval'],
 'path.mindfulness':['log','trace','metric','observability','audit'],
 'path.concentration':['agents.md','sandbox','ci','test','build','approval','network policy']
}

def text_of(path:Path,limit=50000):
    try:
        if path.stat().st_size>limit*4:return ''
        return path.read_text(encoding='utf-8',errors='ignore')[:limit].lower()
    except Exception:return ''

def audit(root:Path):
    root=root_of(root); disc=discover(root)
    registry=json.loads((Path(__file__).resolve().parent.parent/'references/factor-registry.json').read_text(encoding='utf-8'))
    candidates=[]
    for vals in disc['categories'].values(): candidates+=vals
    # Also add root common manifests/docs to catch sparse repos.
    candidates=sorted(set(candidates))[:2000]
    result=[]
    for fac in registry['factors']:
        keys=PATTERNS.get(fac['id'],[]); hits=[]
        for rel in candidates:
            hay=rel.lower()
            matched=[k for k in keys if k in hay]
            if not matched:
                txt=text_of(root/rel)
                matched=[k for k in keys if k in txt]
            if matched:
                hits.append({'path':rel,'matched':matched[:4]})
                if len(hits)>=12:break
        result.append({'id':fac['id'],'group':fac['group'],'japanese':fac['japanese'],'status':'candidate_evidence' if hits else 'no_candidate_detected','evidence':hits,'semantic_review_required':True})
    groups={}
    for x in result:
        g=groups.setdefault(x['group'],{'total':0,'candidate':0})
        g['total']+=1; g['candidate']+=1 if x['status']=='candidate_evidence' else 0
    return {'root':str(root),'files_scanned':disc['files_scanned'],'factor_count':len(result),'group_summary':groups,'factors':result,'warning':'Heuristic evidence discovery only. Candidate presence is not compliance; absence may be false negative. The skill must perform semantic MAP review before changing the repository.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output'); args=ap.parse_args()
    data=audit(Path(args.root)); text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if args.output: Path(args.output).write_text(text,encoding='utf-8')
    else: print(text,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
