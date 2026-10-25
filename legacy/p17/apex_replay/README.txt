P17 exact APEX subcatalogue replay
23 October 2026

Result and scientific consequence

The first frozen native execution passed all 1,536 tasks, 98,304 prefix
states and 9,216 policy paths. There are 41 GOOD tasks: 33 Crystal and eight
RPL. Every one has exact closed-square retrospective certificate cost nine.
The randomised mixture, deterministic screening policy, observed-value greedy
policy and full census each cost nine on every positive task. The positive
cost total is 369 for every policy. There are no positive acquisition savings.
All 1,495 negative tasks terminate correctly at full census.

The 41 positive labels are subcatalogue/candidate/block tasks, not 41 distinct
configurations and not the classification against the full protocol catalogue.
Removing configurations changes the decision problem. The sample therefore
does not estimate how often a full-catalogue configuration is GOOD.

This is adverse evidence for an empirical acquisition-benefit claim on these
data. A ratio of one here reflects certificate saturation: no positive
certificate uses fewer than all nine records. It does not experimentally
demonstrate an advantage of the minimax policy, and it does not refute its
25/23 worst-case theorem. Cost-seven and cost-eight positive classes do not
occur in this data-derived benchmark; the separately declared synthetic
controls must remain distinct.

Selection and observation semantics

The original JSONs contain six trial rows for each of 16 Crystal and 36 RPL
configurations. Configuration labels are zero-based lexicographic indices of
the parameter tuples. For each protocol, every unordered configuration triple
is ranked by SHA256 of the UTF-8 text

  P17_APEX_SUBCATALOGUE_V1|protocol|i,j,k

with ascending decimal indices, no spaces and no newline. The first 128
triples are used, without selecting by outcomes. All three configurations are
in turn designated as the initially unknown paid candidate. Both fixed
nonoverlapping three-row blocks, rows 1–3 and 4–6 in ascending original trial
ID order, are retained. The actual selected triples, parameter labels and
trial IDs are in results_v1.json. These selections cover all 52 source
configurations and all 312 original trial IDs, reused across overlapping
subcatalogues. They are not independent physical replications or a heldout
experiment. Subcatalogue labels and ordering are given to the client; unseen
numeric values, true labels and certificate minima are not given to policies.

Each latency x in milliseconds is replaced by x/(x+100), separately per row;
failure is exactly 1-reliability. Arithmetic uses Python Fraction throughout.
This is the predeclared bounded row objective, not a physical latency cap or
an unchanged scientific objective. The exact comparator for this replay is
the declared independent closed-square completion domain [0,1]^2. Because
the transformed coordinate is strictly below one, this square is an audit
relaxation. No equality with the unknown physical completion domain is claimed.

The retrospective comparator enumerates all 64 legal count triples and uses
closed supporting-weight intervals, including axes and ties. Client policies
hold only already received rows, and their TRUE test uses strict convex-mixture
feasibility. A server accepts a configuration label and returns only its next
record. Python-object separation is not a security boundary. Prefix order,
record count, terminal soundness, full-domain FALSE fallback and per-positive
25/23 mixture and 9/8 deterministic upper bounds are asserted in the program.

Policies

A_LR and A_RL census the candidate, screen competitors for P2, test TRUE
before prefetch, raise unfinished competitor prefixes to two and use the two
opposite final-row orders. B reads candidate prefix two and both competitors
fully, tests TRUE and otherwise reads the remaining candidate row. Their
mixture weights are 8/23, 8/23 and 7/23, respectively, giving the exact
expectation without Monte Carlo.

The deterministic policy censuses the candidate, performs the same screening
and uses a fixed full-census fallback, testing TRUE on the way. The new greedy
policy performs the same candidate/screening stage and then chooses the
unfinished competitor with the smaller sum of its current upper-corner
coordinates, breaking ties by public label. It uses only current observations;
it is not the earlier project policy S and no universal greedy ratio is claimed.
The census baseline reads all nine records.

Reproduction and provenance

From the complete dossier root, run:

  python3 p17/apex_replay/apex_subcatalogue_replay_v1.py

This uses only Python's standard library. It verifies the freeze and original
data hashes, performs the complete fixed replay and writes deterministic
results_v1.json and comparison_v1.csv. For a preserving replay, copy the
public subtree and the two original p9/licence/apex_dataset JSONs into a
temporary tree first. There is no network, installation, external-project
execution or hardware operation. Variable completion time appears only in
execution_record_v1.json, which is separate from scientific replay outputs.

Source/fixture/protocol and original data hashes were frozen before first
confirmatory execution. Data extraction and protocol design preceded freezing;
preregistered discovery is not claimed. No failure or after-results tuning
occurred in this unit. The execution record names exact native outputs and
hashes. A separate overall dossier replay can verify byte-identical output.

The reused APEX dataset is cited by DOI10.3217/3dhx0-2k125 under CC BY4.0.
The source article DOI10.1145/3770918 is distinct. The original data remain
unchanged, and this row transformation/subcatalogue derivation is explicit.
Licensing of external software is separate; no external project code ran.
No new radio measurements, service deployment, security, physical savings,
whole-catalogue empirical superiority or historical priority is established.
