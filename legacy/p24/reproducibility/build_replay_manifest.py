#!/usr/bin/env python3
"""Freeze the explicit P24 selected-evidence input inventory; no execution.

This packaging utility reads literal job lists from the unchanged earlier
replayers. It neither imports nor executes their scientific programs.
"""
from pathlib import Path
import ast
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def literals(path):
    out={}
    for node in ast.parse(path.read_text()).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            try:out[node.targets[0].id]=ast.literal_eval(node.value)
            except (ValueError,TypeError):pass
    return out

def main():
    files={};stages=[]
    def add(name,role):
        p=BASE/name
        if not p.is_file():raise FileNotFoundError(name)
        if name not in files:
            files[name]={'path':name,'size_bytes':p.stat().st_size,'sha256':sha(p),'roles':[]}
        if role not in files[name]['roles']:files[name]['roles'].append(role)
    for phase in ('p21','p22','p23'):
        replay=f'{phase}/reproduce_{phase}.py';cfg=literals(BASE/replay)
        add(replay,'unchanged_phase_replayer')
        jobs=[]
        for script,out in cfg['JOBS']:
            s=f'{phase}/{script}';o=f'{phase}/{out}'
            add(s,'selected_scientific_program');add(o,'retained_scientific_output')
            jobs.append({'script':s,'outputs':[o]})
        if phase=='p21':
            proofs=[f'{phase}/{x}' for x in cfg['SUPPORT']]
            record='p21/review/P21_Clean_Replay_Validation.json';args=[]
        elif phase=='p22':
            proofs=[f'p22/{x}' for x in (
                'structure/Band_Domain_Theorems_P22.md',
                'lower/Fixed_Alphabet_Constant_Overhead_P22.md',
                'lower/Nonvanishing_Triangular_Lower_Bounds_P22.md',
                'upper/N5_Upper_Proof.txt',
                'three_tail/Triangle_N5_Two_World_Lower_Proof.txt')]
            record='_p24_stage_reports/P22.json';args=['--record',record]
        else:
            proofs=[f'{phase}/{x}' for x in cfg['CURRENT_PROOFS']]+cfg['LEGACY_INPUTS']
            record='_p24_stage_reports/P23.json';args=['--record',record]
        for name in proofs:add(name,'proof_or_hash_binding_input')
        add(f'{phase}/review/{phase.upper()}_Clean_Replay_Validation.json','historical_phase_execution_record')
        stages.append({'id':phase.upper(),'kind':'unchanged_phase_replayer','entrypoint':replay,
                       'arguments':args,'report_path':record,'program_count':len(jobs),
                       'output_count':sum(len(j['outputs']) for j in jobs),'jobs':jobs,
                       'timeout_seconds':1800})

    wireless='p17/apex_replay/apex_subcatalogue_replay_v1.py'
    add(wireless,'selected_scientific_program')
    for name in ('fixtures_v1.json','PROTOCOL_v1.txt','FREEZE_v1.json'):
        add('p17/apex_replay/'+name,'wireless_frozen_input')
    for name in ('Crystal_results.json','RPL_results.json'):
        add('p9/licence/apex_dataset/'+name,'unchanged_reused_wireless_data')
    outputs=['p17/apex_replay/results_v1.json','p17/apex_replay/comparison_v1.csv']
    for name in outputs:add(name,'retained_scientific_output')
    for name in ('README.txt','ARTIFACT_MANIFEST_v1.json','execution_record_v1.json'):
        add('p17/apex_replay/'+name,'wireless_provenance_or_historical_record')
    for name in ('p9/licence/apex_dataset/README.md','p9/licence/THIRD_PARTY_APEX.txt','p9/licence/ccby4_legalcode.txt'):
        add(name,'upstream_data_attribution_or_licence')
    stages.append({'id':'P17_WIRELESS','kind':'preserved_data_program','entrypoint':wireless,
                   'arguments':[],'report_path':outputs[0],'program_count':1,'output_count':2,
                   'jobs':[{'script':wireless,'outputs':outputs}],'timeout_seconds':600})
    # Historical evidence is retained and hash-checked but not executed again.
    add('p20/output/Research_Companion_Paid_Prefix_v1.zip','retained_historical_scientific_companion_not_reexecuted')
    add('p20/review/RESEARCH_COMPANION_REPLAY_VALIDATION_v1.json','retained_historical_execution_record_not_reexecuted')
    add('p24/reproduce_p24.py','current_orchestrator')
    add('p24/reproducibility/build_replay_manifest.py','inventory_builder_not_scientific_execution')
    # P23's mathematical correction must accompany the frozen older input,
    # although it is not an executable dependency and must not replace it.
    for name in ('P21_Corrected_Continuation_Paragraph.txt','Foundational_Audit_P23.txt'):
        add('p23/foundation/'+name,'later_correction_to_retained_older_proof')

    manifest={'schema':'p24-selected-scientific-replay-inputs-v1','path_base':'Directory containing p21, p22, p23 and p24',
              'selection':'All six P21, eleven P22 and eight P23 canonical replay jobs, plus the single preserved-data P17 APEX subcatalogue replay.',
              'stage_count':len(stages),'selected_scientific_program_count':sum(s['program_count'] for s in stages),
              'selected_scientific_output_count':sum(s['output_count'] for s in stages),
              'file_count':len(files),'total_input_bytes':sum(f['size_bytes'] for f in files.values()),
              'stages':stages,'files':[files[k] for k in sorted(files)],
              'packaging_rule':'Retain every files[].path at exactly this relative path. Include this manifest and the final P24 replay record separately. No external data download or complete upstream archive is needed.',
              'retained_history_scope':'The P20 companion and its 31-job/35-output execution record are preserved, not reexecuted by P24. The selected P17 wireless job was included in that earlier history and is explicitly reexecuted here.',
              'scientific_limits':['Finite enumerations do not execute infinite Ramsey arguments or exhaust every continuous archive.',
                 'The two P23 universal-upper programs verify exact continuous Bernstein certificates conditional on the analytic reduction.',
                 'The wireless stage is an exact secondary replay of unchanged archived trial summaries, not a new radio measurement or original-framework execution.',
                 'New manuscript and supplement source bindings are separate from these frozen proof/checker inputs.']}
    target=ROOT/'reproducibility/Replay_Input_Manifest.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:manifest[k] for k in ('stage_count','selected_scientific_program_count','selected_scientific_output_count','file_count','total_input_bytes')}))

if __name__=='__main__':main()
