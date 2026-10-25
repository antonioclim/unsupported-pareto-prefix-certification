# Current scientific scope — P46

This note identifies the claims supported by the current companion. It does not
replace the article's proofs. The [result map](../RESULTS_MAP.md) gives executable
paths and comparison rules. The earlier statement-number migration remains in
`Statement_Crosswalk_P41.json`; the current additions below do not rewrite that
historical record.

## Triangle acquisition and the candidate-census class

Main Theorem 19 proves a uniform randomised upper bound of **12/11** for three
configurations, every archive length, unit row prices and an optional common
compulsory information-free setup charge. The comparator ranges over all
realised robust TRUE prefixes, including those that leave the candidate partly
unread. The policy itself fully observes the candidate on positive archives.

The upper transfers pointwise to independent subdomains of the triangle
containing `(0,0)` and `(1,1)`. This upper transfer alone does not establish an
exact asymptotic optimum for every such subdomain: a matching lower-bound family
must also be present.

Combining Main Theorems 17 and 19 gives the exact limiting ratio **12/11** for the
candidate-census class on both the triangle and the fixed three-symbol alphabet
`S = {(0,0),(1,0),(1,1)}`, with three configurations, unit prices and zero setup.
This class contains every globally valid policy that fully observes the
candidate before TRUE on every positive archive. It permits arbitrary
interleaving and early FALSE decisions; it is not restricted to candidate-first
policies or the particular continuation policy used for the upper bound.

For unrestricted policies, Main Theorem 16 supplies the asymptotic lower bound
**23/22** and Theorem 19 the uniform upper bound **12/11**. The interval has exact
width **1/22**. Neither convergence nor the exact unrestricted triangle optimum
has been established. Approaching the exhibited lower bound requires partial
candidate observation on the hard family; this necessity does not construct a
policy attaining it. The numerical upper is not established for arbitrary
positive row tariffs or general catalogue size.

## Exact polynomial evidence

The current piecewise rule uses separate certificate files under
`checks/triangle_12_11/`. Its seven polynomial families contain **58 boxes and
4,824 multivariate Bernstein coefficients**. A separate rational collocation
implementation checks values, degrees and partitions without importing the
producer. **Seven additional univariate coefficients** check the discriminant;
**nine independent algebraic identities** check the analytic reductions. These
checks supplement the continuous-domain proof.

The earlier **873/800** rule and its **4,644-coefficient** certificate remain
unchanged controls for their original rule. The older bound is not the current
best upper bound. Historical filenames, outputs, manifests and failed
discovery-stage records retain their original meaning and values.

## Public blocks and comparator distortion

**Supplementary Proposition S11** assumes a public partition of each archive
into consecutive equal-row blocks. Distinct blocks and groups admit
Cartesian-product completions; the row domain contains `(0,0)` and `(1,1)`.
For a prefix `b`, let `R(b)` round each nonempty group prefix to the end of its
last touched block. On a realised block-model archive,

`TRUE_block(b) if and only if TRUE_independent(R(b))`.

The independent-row comparator lies between the block-model comparator and
`rho_B(w)` times that comparator, where

`rho_B(w) = max_{g, 1 <= b <= N} W_g(R_g(b)) / W_g(b)`

and `W_g` is the cumulative strictly positive public row price. At unit prices,
`rho_B(w)` is at most the largest block length `m`. The inequalities remain valid
with an identical compulsory information-free setup charge added to both costs.
The factor `m` is attained at zero setup even on the three-configuration
triangle; the weighted factor is attained when each group has one block and
shares a common positive price profile.

For `N = m = 2` with common row prices `(1,M)`, distortion is `1+M`. Thus bounded
block length alone gives no uniform bound under arbitrary tariffs. The result
is a conservative-relaxation bound for a specified public equality contract,
not a claim about general statistical correlation, measured communication
savings or expected economic utility.

The independent finite checker in `checks/public_blocks/` covers 11 partition
families and 1,329,000 prefix states, with 7,140 cost comparisons across five
price profiles and three setup charges. It also checks sharp-family completion
witnesses for `N=1,...,30`. These overlapping finite cases are mathematical
controls, not physical replications.

## Evidence limits and version identity

The APEX replay remains a secondary analysis of retained upstream data. All
41 positive tasks require nine disclosures; its 1,536 tasks overlap. No new
radio measurement or measured disclosure saving is reported. The synthetic
prefix demonstrator also retains adverse tariff cases.

A PASS report supports only the computations named in it. Universal validity
comes from the stated proofs; novelty and prior-art completeness require
separate scholarly assessment. P46 identifies the mathematical and checker
baseline. P52 prepares software version `1.0.0` and tag `v1.0.0` for the existing
repository https://github.com/antonioclim/unsupported-pareto-prefix-certification.
Version DOI `10.5281/zenodo.23632859` is reserved; the release and Zenodo
record are unpublished at preparation on 25 October 2026. The public release URL,
concept DOI and publication dates remain unset until confirmed. P49 and P46
execution records remain historical; the current packaged replay record is
`results/Full_Local_P52.json`.

The current Main Table 3 summarises the 12/11 certificate families. The complete
58-leaf inventory is retained in Supplementary Section S9, Table S13; the
analytic reductions remain in Main Section 6.
