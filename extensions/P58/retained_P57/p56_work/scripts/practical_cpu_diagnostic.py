#!/usr/bin/env python3
"""Exploratory CPU-cost diagnostic; excludes transport/fees and uses fixed old tasks."""
from pathlib import Path
import importlib.util,json,time,statistics,platform,sys,hashlib,gc
HERE=Path(__file__).resolve();spec=importlib.util.spec_from_file_location('p56negative',HERE.with_name('practical_negative_stopping.py'));p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
rows=[x['rows'] for x in p.tasks()]
variants={'full_census':('census',False),'early_false_census':('census',True),'early_false_screened_det':('det',True)}
order=tuple(variants)
def run(key):
    name,enhanced=variants[key];q=0;pos=0
    for item in rows:
        out=p.execute(item,name,enhanced);q+=out['queries'];pos+=int(out['answer'])
    return q,pos
# Warm each implementation using all input data; timings below include policy
# arithmetic, local next-row calls, access bookkeeping, not task loading.
for key in order:run(key)
records=[]
for repetition in range(9):
    sequence=order[repetition%3:]+order[:repetition%3]
    if repetition%2:sequence=sequence[::-1]
    for key in sequence:
        gc.collect();t=time.process_time_ns();q,pos=run(key);elapsed=time.process_time_ns()-t
        records.append({'repetition':repetition,'variant':key,'process_cpu_ns':elapsed,'rows':q,'positive_answers':pos})
medians={key:int(statistics.median([r['process_cpu_ns'] for r in records if r['variant']==key])) for key in order}
summary={key:{'median_process_cpu_ns':medians[key],'min_process_cpu_ns':min(r['process_cpu_ns'] for r in records if r['variant']==key),'max_process_cpu_ns':max(r['process_cpu_ns'] for r in records if r['variant']==key)} for key in order}
saved=12365-11515;overhead=medians['early_false_screened_det']-medians['early_false_census']
result={'status':'PASS','tasks':len(rows),'warmups_per_variant':1,'repetitions_per_variant':9,'rotating_reversing_run_order':True,'summary':summary,'early_false_screened_vs_early_false_census':{'saved_disclosures':saved,'difference_of_median_process_cpu_ns':overhead,'conditional_equal_sequential_access_latency_break_even_ns_per_disclosure':f'{overhead}/{saved}'},'measurements':records,'python':sys.version,'platform':platform.platform(),'script_sha256':hashlib.sha256(HERE.read_bytes()).hexdigest(),'limitations':['Process CPU time in this container only; timing is not a physical service trial or stable hardware benchmark.','Formula assumes identical sequential fixed latency per disclosed row with no batching, caching, parallel transport or overlap, plus these CPU costs.','No actual row-access latency, price, electricity, joules, byte transport or financial gain was measured.','Same overlapping tasks are reused; timing repetition is not scientific data replication.']}
p.m.freeze_check();(p.OUT/'practical_cpu_diagnostic_P56.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='measurements'},indent=2))
