#!/usr/bin/env python3
"""Check that malformed certificates are actually rejected in isolation.

Each mutation attacks a mathematical verification obligation. No original
certificate or result is overwritten. These are schema/integrity controls,
not evidence that the analytic policy reduction is correct.
"""
from copy import deepcopy
from pathlib import Path
from fractions import Fraction
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'upper/Improved_Upper_Exact_Certificate.json'

def main():
    data=json.loads(SOURCE.read_text())
    def target(d):
        return [r for r in d['polynomial_certificates'] if r['excess']=='73/800']
    def duplicate_endpoint(d):
        r=target(d); r[1].clear();r[1].update(deepcopy(r[0]))
    def understate_degree(d):
        target(d)[0]['degrees']=[1,1,1]
    def omit_box(d):
        target(d)[0]['leaves'].pop()
    def falsify_minimum(d):
        leaf=target(d)[0]['leaves'][0]
        leaf['minimum_coefficient']=str(Fraction(leaf['minimum_coefficient'])+1)
    records=[]
    for change in (duplicate_endpoint,understate_degree,omit_box,falsify_minimum):
        changed=deepcopy(data);change(changed)
        with tempfile.TemporaryDirectory(prefix='p30_bad_certificate_') as temp:
            work=Path(temp)
            shutil.copy2(ROOT/'upper/check_improved_upper_independent.py',work)
            (work/SOURCE.name).write_text(json.dumps(changed))
            result=subprocess.run([sys.executable,str(work/'check_improved_upper_independent.py')],
                                  text=True,capture_output=True)
            assert result.returncode!=0, change.__name__+' was accepted'
            assert 'AssertionError' in result.stderr, result.stderr
            reason=result.stderr.strip().splitlines()[-1]
            records.append({'mutation':change.__name__,'rejected':True,'reason':reason})
    report={'status':'PASS','mutations':records,
            'scope':'Four malformed algebraic certificates rejected. No universal proof or analytic reduction is checked here.'}
    (ROOT/'Verifier_Rejection_Check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
