PUBLIC CONSTANT-BLOCK DEPENDENCE

Run the principal command from the repository root:

  python3 run_all_checks.py --record results/Full_Local_P45.json

The runner executes check_public_blocks.py in a temporary copy. It compares
all scientific fields of Public_Block_Dependence_Check.json, excluding only
elapsed_seconds and finished_at_utc, and validates the producing source hash.
The checker uses Python's standard library; do not run with -O or -OO.

The finite check intersects independent block-model truth tables and enumerates
attainable independent-row completion means, without the project's endpoint
oracle. It checks 1,329,000 prefix states over 11 partition families and 7,140
cost/setup comparisons. Sharp-family predecessor completions are verified for
N=1,...,30. These counts are overlapping mathematical cases, not measurements.

Supplementary Proposition S11 provides the all-size proof: TRUE_D(b) is
TRUE_Q(R(b)); independent-row certificates incur at most the maximum block
length m at unit prices, or the explicit rho_B(w) under arbitrary positive
prices. These bounds are sharp under the theorem's stated conditions. Block
partitions and equalities must be public, and legal block values form a
Cartesian product. Statistical dependence alone is not the stated model.

The standalone checker rejects existing output files and symbolic-link paths.
For a direct rerun from the repository root, select a new JSON output:

  python3 checks/public_blocks/check_public_blocks.py --output results/Blocks_Repeat_01.json

A second run requires a new filename. The principal runner handles temporary
output creation and retained-output comparison automatically.
