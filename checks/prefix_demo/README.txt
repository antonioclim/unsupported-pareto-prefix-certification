PAID-PREFIX DEMONSTRATOR WITH AN INDEPENDENT RETROSPECTIVE COMPARATOR
SICOMP companion / retained finite demonstrator
Antonio Clim; new implementation prepared with AI assistance.

PURPOSE
This small exact demonstration implements the two blind policies in Supplement
S1.6 for three labelled configurations with three ordered records each. Every
record has two objectives to be minimised. A request buys the next whole record
of one configuration. The decision is whether the designated candidate is both
Pareto nondominated and unsupported by every nonzero nonnegative weighted sum.
Scalarisation ties and coordinate-axis weights count as support.

The retrospective minimum C* is COMPUTED here, not supplied in the fixtures.
An independent checker enumerates every prefix vector and all compatible
finite-alphabet completion means. It uses a different complete-data geometric
test and imports no online certificate routine. Because the alphabet includes
(0,0) and (1,1), Theorem 1 of the manuscript identifies its TRUE prefixes with
those of the independent square completion model. That continuous-domain
identification is analytic; this finite run does not prove it.

REPRODUCING THE RETAINED CHECK
The retained report records the original run. The instructions below create
a fresh execution record; a retained PASS is not evidence of a later run.

FILES
prefix_service.py: public next-record interface, observed client state and
                  policies A/B. The client never receives a complete archive.
independent_comparator.py: retrospective exhaustive verification, used by the
                          audit harness only after/beside policy execution.
run_demo.py: executes all three random branches exactly and checks transcripts.
fixtures.json: public alphabet and ten synthetic cases; no C* inputs.
results/Demo_Execution_P44.json: current full report with execution time and hashes.
results/Demo_Summary_P40.json: concise extraction of that report, not a new run.
results/Runner_Controls_P40.json: refusal of old output overwrite and Python -O.
development_history/initial: initial code/result retained before stronger input
                            validation was added; not the final implementation.

REPEAT STEP BY STEP (OPTIONAL)
1. Extract the delivered archive into a new folder and keep the original ZIP.
2. Open a terminal in its demo folder, where run_demo.py is located.
3. Confirm Python 3.12 or later:

   python3 --version

4. Run with a NEW output filename:

   python3 run_demo.py --output results/Repeat_01.json

   On Windows, if Python is named python, replace python3 with python. Windows
   was not executed in this audit. No additional package or network is needed.
5. Expected: a short JSON message containing status PASS, followed by return
   to the prompt. Its totals are 10 cases, 6 positive cases, 30 branches,
   640 prefix states and 1058 complete-sum triples examined.
6. Inspect results/Repeat_01.json. On a subsequent run choose Repeat_02.json,
   etc. Existing output is deliberately refused rather than overwritten.
7. If FAIL or an error occurs, retain the output and error message for diagnosis. Do not relabel a retained PASS as evidence of a fresh run.

Do not use -O. The runner rejects optimised Python mode. It records actual UTC
execution timestamps, runtime, Python/platform and SHA-256 of all three modules
and the fixture file. Dates and runtime are expected to differ on repetition.
The computations use exact fractions/integers and no Monte Carlo. The three
private-randomness branches have probabilities 8/23,8/23,7/23: their costs are
weighted exactly. There is no claim to have sampled random outcomes here.

WHAT THE OUTPUT SHOWS
A: independently computed C*=8 at prefix(2,3,3), expected cost200/23, ratio25/23.
D: independently computed C*=7 at prefix(3,3,1), expected cost175/23, ratio25/23.
New candidate-census example: C*=8, expected cost191/23, ratio191/184.
New full-census example: C*=9, cost9, ratio1.
Four negative controls (tie, domination, axis support, equal points): all three
branches finish census and return FALSE. No positive-input promise is used.
Same A rows with candidate-tail price25: C*=8, expected paid cost584/23,
ratio73/23. The unchanged unit-price policy is NOT 25/23-competitive under
arbitrary prices. This adverse example is deliberately retained.
Same D rows with common setup10: C*=17 and expected total cost405/23. Setup is
charged once, equally to policy and comparator, and reveals no information.

The tariff/setup variants reuse A/D rows; the ten cases are not ten independent
scientific discoveries. The reported count 1058 is the number of complete sum
triples actually evaluated. Rejected prefixes stop at one explicit legal
negative completion; accepted prefixes exhaust all distinct legal completion
mean triples. All 64 prefix vectors are considered for every case. Groupwise sum
aggregation removes permutations/duplicates that give the identical means;
it does not omit a possible complete-data predicate value.

IMPLEMENTATION AND CLAIM LIMITS
This is a local Python interface model. Private attributes are organisational,
not a security sandbox, cryptographic enforcement or an OGC implementation.
All examples are synthetic and designed from the mathematical model. There are
no new radio, network, energy, bandwidth, payment or deployment measurements.
The theorem's global 25/23 guarantee belongs to the analytic proof for unit
prices and zero setup. Tests on these fixtures do not establish global minimax
optimality. The comparator is exponential in general and intended only for
small finite instances. Policy accounting supports public positive tariffs,
but the policy probabilities are not retuned to solve the general tariff case.
The interface enforces prefix ordering; no bypass, correlations or approximate
measurements are modelled. Observations are exact and unread rows range
independently over the public alphabet.

REUSE
The modules are readable and importable. The ready-to-run harness is a fixed
regression suite for K=N=3. Editing fixtures changes the experiment and invalidates
its retained hashes. Do not reuse the hard-pair assertions as evidence for a new
fixture or change the public domain based on unseen archive values. Before
extending to real data, specify the completion domain, access rule, tariff and
comparator independently of the observed favourable outcome.

LICENCE
New code: BSD-3-Clause, as adopted by the author. New documentation and fixture
presentation: CC BY4.0 within the author's rights. Third-party source claims
retain their attributions. This implementation is new; it does not relicense
any external code. The historical simulator was read to identify the model and
its limitation, but no legacy file or frozen result was modified.
