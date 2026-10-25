P39 - Independent finite audit of endpoint and band claims

Run from any directory with Python 3.12 or later:

    python3 /absolute/path/to/independent_band_audit.py

The program uses only Python's standard library and no network access.
It imports none of the manuscript's retained checkers. It writes a fresh
Independent_Band_Audit.json next to itself and prints the same result.
The assertions are part of the checks: do not use python -O.

Expected successful result: process exit code 0 and status PASS in the new
JSON. The record includes measured runtime, Python version, case counts
and the SHA-256 of the exact script. A previously retained PASS does not
prove that a new run completed.

Scope:
- direct support-weight interval intersection and finite completions;
- B2 legal rational feasibility witnesses and equality rejection;
- B4 exact prefix sets of both hard worlds;
- B5 exact tariff balancing including both-suffice cases;
- B3 bounded K=5 unique-inversion geometry and comparator;
- supplementary square N=3 and triangle N=5/N=6 prefix sets and shapes;
- exact affine setup residuals for the five-row mixture.

The code does not prove universal continuous-domain results, Ramsey
restriction, causal compression or minimax. Those require the separate
analytic arguments. Canonical P37 files are not read or changed.

The development_history directory records an initial test-coverage weakness
and its repair. Its older PASS is not the final coverage report.
