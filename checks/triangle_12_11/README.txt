CURRENT 12/11 TRIANGLE CERTIFICATE

Run from the repository root:

  python3 run_all_checks.py --record results/Full_Local_P45.json

The principal replay uses only Python's standard library. It copies the inputs
and sources to a temporary workspace, removes each expected output there,
executes its producer/checker and compares the complete scientific payload.
The retained files are not overwritten. Do not use Python -O or -OO.

upper_check/verify_upper_certificate.py derives the sparse polynomial degree
and independently recovers rational Bernstein coefficients by collocation.
It checks 58 boxes and 4,824 coefficients in seven modes. It verifies complete
prefix-free dyadic coverage and includes four malformed-certificate controls.
Only elapsed_seconds is excluded from its retained-output comparison.

upper_check/verify_high_analytic.py uses that checker's sparse arithmetic and
collocation routines, without importing any SymPy construction program. It
checks nine named algebraic/coefficient identities and seven univariate
coefficients. Its output comparison excludes no fields.

Both outputs include the exact producing source hash. The seven certificate
JSON files and optional producers are byte-preserved from the P44 derivation.
The verifier copies add fresh-output safeguards and point to the self-contained
proof in Main Section 6, Theorem 19, supplied in the separate manuscript.
A standalone verifier refuses any existing output and symbolic-link path; use
--output followed by a new .json filename. The default beside the verifier is
intended for the principal runner, which first removes its temporary copy. The independent checker is an independent method,
not a claim of external authorship, peer review or formal proof-assistant use.

SCOPE
The all-size theorem is for three configurations, unit row prices and permits
a common nonnegative information-free setup charge. The exact asymptotic
candidate-census ratio is 12/11 on the triangle and fixed alphabet S at zero
setup. The unrestricted asymptotic interval remains [23/22,12/11]. The analytic
reduction and real-domain coverage require the written proof. Polynomial
certificates establish continuum positivity once that reduction is supplied;
finite catalogue enumerations are a different kind of corroborating evidence.
The unchanged historical 873/800 certificate is in checks/upper/.

OPTIONAL CERTIFICATE CONSTRUCTION
Construction is not required by the principal replay. The original producers
are retained to make the coefficient data auditable:

  upper_check/low_bernstein.py
  upper_primary/high_bernstein.py
  upper_primary/check_high_identities.py

Their optional dependency is SymPy 1.14.0, pinned in
upper_check/requirements_upper_producer.txt. No dependency source or environment
is bundled. The producer's legacy local 'deps' search path is harmless when
absent; Python imports SymPy from the explicitly prepared environment.

If constructing certificates, first duplicate this whole triangle_12_11 folder
and work in the duplicate: producers write their outputs beside themselves.
In a separately prepared SymPy 1.14.0 environment, from the duplicate folder:

  python3 upper_check/low_bernstein.py g
  python3 upper_check/low_bernstein.py gtlow
  python3 upper_check/low_bernstein.py gtcut
  python3 upper_check/low_bernstein.py h
  python3 upper_primary/high_bernstein.py h
  python3 upper_primary/high_bernstein.py middlecut
  python3 upper_primary/high_bernstein.py middlefull
  python3 upper_primary/check_high_identities.py
  python3 upper_check/verify_upper_certificate.py --output Upper_Reconstruction.json
  python3 upper_check/verify_high_analytic.py --output Analytic_Reconstruction.json

Verify a retained package before any deliberate scientific change. Do not
rebuild frozen_manifest.json to silence a failed identity or coefficient
check. SymPy construction output is auxiliary and does not substitute for the
standard-library verifier. high_endpoint_discriminant.json and
High_Analytic_Identity_Check.json retain the symbolic derivation output; the
standard-library replay derives the displayed identities and constants itself.
