#!/usr/bin/env python3
"""Run exact, synthetic paid-prefix demonstrations and independent certificates.
BSD-3-Clause. Prepared for Antonio Clim with AI assistance.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
from fractions import Fraction as Q
from prefix_service import GROUPS, N, BRANCHES, PrefixService, ObservedState, run_branch, require
from independent_comparator import CompletionEnumerator, good_complete

HERE = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def corner_truth(archive, prices, setup, prefix):
    client = ObservedState(lambda _: (_ for _ in ()).throw(AssertionError('not acquisition')), prices, setup)
    client.rows = {g: [tuple(map(Q, r)) for r in archive[g][:b]] for g, b in zip(GROUPS, prefix)}
    return client.robust_true()

def run_case(name, fixture, alphabet):
    archive = fixture['archive']
    prices = fixture.get('prices', {g: ['1'] * N for g in GROUPS})
    setup = Q(fixture.get('setup', '0'))
    comparator = CompletionEnumerator(archive, alphabet).all_prefixes(prices, setup)
    truth = comparator['C_star'] is not None
    require(truth == fixture['expected_answer'], 'synthetic fixture truth mismatch: ' + name)
    for record in comparator['all_prefixes']:
        require(corner_truth(archive, prices, setup, record['prefix']) == record['truth'],
                'corner/direct-completion mismatch: ' + name + str(record['prefix']))
    runs = {}
    mean_cost = Q(0)
    mean_queries = Q(0)
    certificate_prefixes = {tuple(p) for p in comparator['true_prefixes']}
    for label, probability, order in BRANCHES:
        run = run_branch(archive, alphabet, prices, setup, label, order)
        require(run['answer'] == truth, 'wrong answer: ' + name)
        if truth:
            require(tuple(run['prefix']) in certificate_prefixes, 'stop not independently certified')
        else:
            require(run['prefix'] == [3, 3, 3], 'negative did not reach census')
        # Recheck each billed record against the fixed archive and public prices.
        counters = dict.fromkeys(GROUPS, 0)
        for r in run['transcript']:
            g = r['group']; counters[g] += 1
            require(r['index'] == counters[g], 'skipped/repeated paid row')
            require(list(map(Q, r['row'])) == list(map(Q, archive[g][counters[g]-1])), 'wrong disclosed row')
            require(Q(r['charge']) == Q(prices[g][counters[g]-1]), 'wrong charge')
        run['probability'] = str(probability)
        runs[label] = run
        mean_cost += probability * Q(run['paid_cost'])
        mean_queries += probability * run['queries']
    c = Q(comparator['C_star']) if truth else None
    unit = all(Q(w) == 1 for ws in prices.values() for w in ws) and setup == 0
    ratio = mean_cost / c if truth else None
    if unit and truth:
        require(ratio <= Q(25, 23), 'unit-price ratio exceeded on tested fixture')
    return {'description': fixture['description'], 'synthetic': True,
            'answer': truth, 'prices': prices, 'setup': str(setup),
            'comparator': comparator, 'runs': runs,
            'expected_queries': str(mean_queries), 'expected_paid_cost': str(mean_cost),
            'ratio': None if ratio is None else str(ratio),
            'unit_price_zero_setup_25_over_23_scope': unit,
            'global_guarantee_source': 'Manuscript Supplement S1.6 theorem; not established by this finite run'}

def protocol_controls(alphabet):
    prices = {g: ['1'] * N for g in GROUPS}
    zero = {g: [['0','0']] * N for g in GROUPS}
    rejected = []
    server = PrefixService(zero, alphabet, prices)
    for _ in range(N): server.next_row('candidate')
    for request in ('candidate', 'unknown'):
        try: server.next_row(request)
        except ValueError: rejected.append(request)
        else: raise AssertionError('illegal request accepted')
    for label, reply in [('wrong_index', ('candidate', 2, (Q(0),Q(0)),Q(1))),
                         ('wrong_price', ('candidate', 1, (Q(0),Q(0)),Q(2)))]:
        client = ObservedState(lambda _, response=reply: response, prices)
        try: client.query('candidate', 'negative_control')
        except AssertionError: rejected.append(label)
        else: raise AssertionError('bad server response accepted')
    boundary = {
        'scalarisation_tie': (((1,1),(0,2),(2,0)),False),
        'axis_support': (((0,1),(0,2),(2,0)),False),
        'duplicate_candidate': (((1,1),(1,1),(2,0)),False),
        'dominated': (((2,2),(1,1),(3,0)),False),
        'strict_unsupported': (((3,3),(0,4),(4,0)),True),
    }
    for label, (points, truth) in boundary.items():
        require(good_complete(points) == truth, 'complete boundary case: ' + label)
    return {'rejected_requests_or_responses': rejected,
            'independent_complete_predicate_boundary_cases': len(boundary)}

def indistinguishability_check(cases):
    count = 0
    for label, _, _ in BRANCHES:
        a, d = cases['A']['runs'][label]['transcript'], cases['D']['runs'][label]['transcript']
        for ra, rd in zip(a, d):
            require((ra['group'],ra['index']) == (rd['group'],rd['index']),
                    'world-dependent choice before distinguishing observation')
            count += 1
            if ra['row'] != rd['row']:
                require((ra['group'],ra['index']) in [('candidate',3),('right',3)],
                        'unexpected distinguishing row')
                break
        else:
            raise AssertionError('hard worlds never distinguished')
    return {'branches_checked': 3, 'common_history_action_pairs_checked': count,
            'scope': 'finite hard-world history check; interface separation is not a Python security sandbox'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=HERE/'results'/'Demo_Execution_P40.json')
    args = p.parse_args()
    if args.output.exists():
        raise SystemExit('Output exists; preserve it and choose a fresh --output path.')
    if not __debug__:
        raise SystemExit('Run without -O; this demonstration requires ordinary Python mode.')
    start = time.perf_counter()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    fixture_path = HERE/'fixtures.json'
    fixtures = json.loads(fixture_path.read_text())
    report = {'schema': 'sicomp-paid-prefix-independent-comparator-demo-v1',
              'started_at_utc': started, 'python': platform.python_version(), 'platform': platform.platform(),
              'randomness': 'All three private-randomness branches enumerated with exact rational probabilities; no Monte Carlo.',
              'domain': 'Public finite alphabet containing (0,0),(1,1); independent missing whole rows; three labelled length-three archives.',
              'scope': ['Synthetic model-designed examples, not physical measurements or a deployed paid service.',
                        'Direct finite completion enumeration computes the retrospective comparator independently.',
                        'Endpoint-containing domain equivalence to the square is an analytic manuscript theorem.',
                        'The unit-price zero-setup 25/23 global guarantee is not inferred from these fixtures.',
                        'Tariff examples use the same unit-price policy deliberately; no arbitrary-tariff 25/23 claim.',
                        'Python object privacy is organisational, not a security boundary.'],
              'code_sha256': {f: digest(HERE/f) for f in ['prefix_service.py','independent_comparator.py','run_demo.py']},
              'fixtures_sha256': digest(fixture_path)}
    exit_code = 0
    try:
        cases = {name: run_case(name, f, fixtures['alphabet']) for name,f in fixtures['cases'].items()}
        report.update(status='PASS', cases=cases, protocol_controls=protocol_controls(fixtures['alphabet']),
                      indistinguishability=indistinguishability_check(cases))
        require(cases['A']['comparator']['C_star']=='8', 'A independent comparator')
        require(cases['D']['comparator']['C_star']=='7', 'D independent comparator')
        require(cases['A']['ratio']==cases['D']['ratio']=='25/23', 'hard-pair ratio')
        report['totals'] = {'cases':len(cases), 'positive_cases':sum(c['answer'] for c in cases.values()),
            'executed_branches':3*len(cases),'prefix_states':sum(c['comparator']['prefixes_examined'] for c in cases.values()),
            'complete_sum_triples_examined':sum(c['comparator']['complete_sum_triples_examined'] for c in cases.values())}
    except Exception as exc:
        exit_code=1; report.update(status='FAIL',error_type=type(exc).__name__,error=str(exc))
    report.update(finished_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  elapsed_seconds=time.perf_counter()-start)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    write_json(args.output,report)
    print(json.dumps({'status':report['status'],'output':str(args.output), 'elapsed_seconds':report['elapsed_seconds'],
                      'totals':report.get('totals'),'error':report.get('error')}))
    return exit_code

if __name__=='__main__':raise SystemExit(main())
