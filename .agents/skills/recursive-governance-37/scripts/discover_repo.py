#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os
from pathlib import Path
IGNORE={'.git','node_modules','.next','.nuxt','dist','build','coverage','.venv','venv','__pycache__','.pytest_cache','.mypy_cache','.turbo','.cache','vendor','target'}

def root_of(p:Path)->Path:
    p=p.resolve(); p=p.parent if p.is_file() else p
    for q in [p,*p.parents]:
        if (q/'.git').exists(): return q
    return p

def walk(root:Path,max_files=15000):
    out=[]
    for base,dirs,files in os.walk(root):
        dirs[:]=[d for d in dirs if d not in IGNORE]
        for n in files:
            out.append(Path(base)/n)
            if len(out)>=max_files:return out
    return out

def discover(root:Path):
    root=root_of(root); fs=walk(root); rel=lambda p:p.relative_to(root).as_posix(); ps=[rel(p) for p in fs]
    cats={
      'agent_rules':[], 'docs':[], 'ci':[], 'tests':[], 'deployment':[], 'database':[], 'security':[], 'observability':[], 'task_workflows':[]
    }
    for p in ps:
        lo=p.lower(); name=Path(p).name.lower()
        if name in {'agents.md','claude.md'} or '/.agents/' in '/'+lo: cats['agent_rules'].append(p)
        if lo.startswith(('docs/','specs/','architecture/','adr/','rfcs/')) or any(k in lo for k in ('requirement','architecture','design','policy','roadmap','runbook','decision')): cats['docs'].append(p)
        if lo.startswith('.github/workflows/') or name in {'.gitlab-ci.yml','azure-pipelines.yml'}: cats['ci'].append(p)
        if any(seg in {'test','tests','spec','specs','__tests__'} for seg in Path(lo).parts) or any(x in name for x in ('.test.','.spec.')) or name.startswith('test_'): cats['tests'].append(p)
        if name in {'vercel.json','netlify.toml','fly.toml','dockerfile'} or lo.startswith(('infra/','infrastructure/','terraform/')): cats['deployment'].append(p)
        if lo.startswith(('supabase/','migrations/','prisma/','db/','database/')) or 'migration' in lo or name in {'schema.prisma','schema.sql'}: cats['database'].append(p)
        if any(k in lo for k in ('security','permission','auth','threat','secret','privacy')): cats['security'].append(p)
        if any(k in lo for k in ('observability','telemetry','logging','monitor','metric','trace','slo')): cats['observability'].append(p)
        if any(k in lo for k in ('workflow','cron','schedule','queue','worker','automation','agent')): cats['task_workflows'].append(p)
    for k in cats: cats[k]=sorted(set(cats[k]))[:500]
    return {'root':str(root),'files_scanned':len(fs),'categories':cats}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output'); args=ap.parse_args()
    data=discover(Path(args.root)); text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if args.output: Path(args.output).write_text(text,encoding='utf-8')
    else: print(text,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
