# The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries

Antonio Clim — reproducibility companion, local revision P52

This companion provides exact-arithmetic checks, retained inputs, editable
figures and execution records for paid-prefix Pareto certification. It supports
the article's mathematical arguments and finite checks; the article and its
Supplementary Materials are separate submission documents.

P52 records the existing GitHub repository and reserved Zenodo version DOI. The P46 mathematical and checker baseline and P49 black figure text are retained. The current packaged replay record is results/Full_Local_P52.json; results/Full_Local_P49.json and results/Full_Local_P46.json remain historical execution records. The replay format identifies the unchanged P46 runner implementation, not the delivery edition.

## Scientific scope

For three configurations on the triangle, the current policy has acquisition
ratio at most **12/11** for every archive length, at unit row prices. A common
compulsory information-free setup charge is allowed. The ratio compares policy
cost with the cheapest realised robust TRUE prefix, which may leave the
candidate partly unread.

For policies that fully observe the candidate before TRUE on every positive
archive, **12/11 is the exact asymptotic optimum** on the triangle and the fixed
three-symbol alphabet. The unrestricted asymptotic lower bound is **23/22**;
the remaining interval has width **1/22**. Convergence and the exact unrestricted
triangle optimum remain open. These constants concern three configurations and
do not assert a bound for arbitrary row tariffs.

Supplementary Proposition S11 treats public consecutive blocks of equal rows,
with Cartesian-product completions across blocks. It identifies block-model
certificates with rounded independent-row prefixes and gives sharp
comparator-distortion bounds: the largest block length at unit prices, and an
explicit price-dependent factor under positive public tariffs. It is not a
claim about arbitrary statistical dependence.

[Current scientific scope](docs/Current_Scientific_Scope_P46.md) records these
conditions, the new exact certificates and the distinction between current and
historical checks. The [result map](RESULTS_MAP.md) links claims to proofs,
sources, inputs, outputs and comparison rules.

## Reproduce the checks

Run from the extracted repository directory with Python 3.12 or later, without
`-O`:

```bash
python3 run_all_checks.py --record results/Full_Local_P52.json
```

The suite uses only the Python standard library, needs no network or
installation and writes a fresh report. Success requires exit code 0 and
`"status": "PASS"` for the new run ID and finish time. Linux execution is
recorded; Windows native execution is not claimed. [README.txt](README.txt)
explains status inspection, safe output paths and failure handling.

The integrated route comprises six base scientific checks, 26 selected
historical programs and ten additional checks: **42 scientific program entries
and one rejection control**. These are program entries, not 42 independent
findings. The separate control tests four malformed algebraic certificates; the current
12/11 checker rejects four further mutations, for eight rejection cases in total.

| Component | Scope |
|---|---|
| Base checks | Finite ordinal games, reductions, candidate-observation obstruction, transfer and the earlier rational Bernstein certificate |
| Historical replay | 27 scientifically matching outputs: 26 byte-identical and one with explicitly migrated source provenance |
| Additional checks | Exact continuations, band cases, analytic projection, transcript profiles, complete-catalogue verification, a prefix demonstrator and an economic control |
| Current triangle upper | Independent rational verification of 58 boxes and 4,824 Bernstein coefficients, seven further univariate coefficients, and nine algebraic identities |
| Public constant blocks | Independent finite certificate enumeration, weighted/setup comparisons and sharp-family completion checks |

Fresh outputs are generated in temporary copies; retained results remain
unchanged. Only explicitly named runtime metadata are excluded when exact
scientific JSON is compared. A successful run does not establish a universal
proof or a historical-priority judgment.

For file-identity verification without scientific execution:

```bash
python3 run_all_checks.py --verify-only --record results/Integrity_Local_P52.json
```

## Evidence and provenance

The earlier **873/800** upper bound and its 4,644-coefficient certificate remain
unchanged historical controls for their original policy. The current **12/11**
rule has separate source files, certificate data and independent checks.

A retired historical source is omitted from this public snapshot. Its digest
is retained as historical provenance, not as freshly verified source bytes.
A current ordinal adapter recomputes the same scientific quantities and verifies
the three remaining public proof inputs. The old code, results and manifests
remain unchanged historical records. Use the root replay command; historical
entry points can require material omitted from this snapshot. The
[migration note](docs/Provenance_Migration_P41.md) specifies the comparison.

The APEX secondary analysis retains the unfavourable result: all 41 positive
tasks require nine disclosures. The 1,536 tasks overlap and are not independent
replications. It provides no new physical measurement or measured disclosure
saving. The [data note](docs/APEX_Erratum_Note.md) records the APEX authors'
parameter-table correction and explains why it does not alter the computation.

## Files and publication preparation

| Path | Contents |
|---|---|
| `run_all_checks.py` | Complete reviewer entry point |
| `run_checks.py`, `run_legacy_checks.py` | Base and historical replay layers |
| `checks/` | Executable checks, certificate data and expected outputs |
| `legacy/`, `evidence/` | Historical science and execution records |
| `provenance/` | Record of the retired historical source |
| `figures/`, `editable_figures/` | Figure sources, exports and editable native objects |
| `RESULTS_MAP.md/json` | Proof and computation mapping |
| `frozen_manifest.json` | Scientific-input identities |
| `CITATION.cff` | Citation metadata for the proposed software version 1.0.0 |

Figure regeneration has optional dependencies described with the figure
sources; it is separate from the standard-library science command. New reports
belong in `results/`. Exact manifest boundaries are described in
[PACKAGING.md](docs/PACKAGING.md). Do not regenerate a manifest to make an
integrity failure pass. `freeze_inputs.py` is a maintainer snapshot tool.

The [Romanian browser guide](docs/Browser_Release_Guide_RO.md) explains repository
upload and manual release preparation. The outer delivery wrapper contains
upload batches and the release asset; they do not belong inside the repository.
No GitHub Actions workflow is included. P52 prepares software version `1.0.0`
and tag `v1.0.0` for the existing [GitHub repository](https://github.com/antonioclim/unsupported-pareto-prefix-certification).
At preparation on 25 October 2026, the version DOI **10.5281/zenodo.23632859** is
reserved; the release and Zenodo record are unpublished. A reserved DOI does
not establish public availability. The public release URL, concept DOI and
publication dates remain unset until confirmed.

## Citation and rights

Use [CITATION.cff](CITATION.cff) and cite the version actually used. The author's
covered code is BSD-3-Clause; covered documentation, tables and figures are
CC BY 4.0. Third-party APEX data, DejaVu fonts and retained notices keep their
own terms. See [LICENSING.md](LICENSING.md), [RIGHTS.md](RIGHTS.md) and
[LICENSE_SCOPE.json](LICENSE_SCOPE.json) for component scope. Historical
undecided-licence language records its original snapshot and does not revoke
the subsequently adopted grant for covered author-owned material.
