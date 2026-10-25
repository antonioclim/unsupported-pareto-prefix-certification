# The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries

Antonio Clim — reproducibility companion, P42

For browser-only GitHub preparation, use the [Romanian guide](docs/Ghid_GitHub_Release_Browser_RO.html) or its [plain-text version](docs/Ghid_GitHub_Release_Browser_RO.txt). The delivery wrapper provides upload batches and the release asset; these are kept outside the repository. GitHub Actions are not included.

For computational reproduction, run the complete exact-arithmetic suite with Python 3.12 or later, without `-O`:

```bash
python3 run_all_checks.py --record results/Full_Local_P42.json
```

Run this command from the extracted repository directory. It uses the Python
standard library, needs no network or installation and writes a fresh report.
Success requires exit code 0 and `"status": "PASS"` for the new run ID and finish
time. Linux execution is recorded; Windows native execution is not claimed.
[README.txt](README.txt) explains status inspection, safe output paths and failures.

The suite executes six original current scientific checks, one rejection control,
26 selected historical jobs and seven added checks. The total is **39 scientific
program entries and one control**, not 39 independent findings. The control
rejects **four** malformed algebraic certificates.

## What is reproduced

| Component | Scope |
|---|---|
| Original current checks | Finite ordinal games, reductions, candidate-observation obstruction, transfer and the rational Bernstein certificate |
| Selected historical replay | 27 scientifically matching outputs: 26 byte-identical and one with explicitly migrated source provenance |
| Additional P39 checks | Exact continuations, band cases, analytic parameter projection, transcript profiles and complete-catalogue verification |
| Prefix demonstrator | Independently enumerated certificate minima and exact policy branches on ten synthetic cases, including adverse tariff behaviour |
| Economic control | A finite counterexample to adaptive submodularity of the naive certificate indicator |

The [result map](RESULTS_MAP.md) links claims to sources, inputs, outputs and
comparison rules. Fresh outputs are generated in temporary copies; retained
results remain unchanged. Only named runtime metadata are excluded where exact
scientific JSON is compared. Universal proofs and historical-priority judgments
are not computed by these tests.

To verify file identities without executing scientific programs:

```bash
python3 run_all_checks.py --verify-only --record results/Integrity_Local_P42.json
```

## Evidence and provenance

A retired historical source is omitted from this public snapshot. Its digest is
retained as historical provenance, **not freshly verified source bytes**. A
current ordinal adapter recomputes the same scientific quantities and verifies
the three remaining public proof inputs. The old code, results and manifests
remain unchanged historical records. Use the root replay command; historical
entry points can require material deliberately omitted from this snapshot.
[The migration note](docs/Provenance_Migration_P41.md) specifies the comparison.

The APEX secondary analysis retains the unfavourable result: all 41 positive
tasks require nine disclosures. The 1,536 tasks overlap and are not independent
replications. It provides no new physical measurement or measured disclosure
saving. [The data note](docs/APEX_Erratum_Note.md) records the authors' parameter-table
correction and explains why it does not alter the retained computation.

## Files

| Path | Contents |
|---|---|
| `run_all_checks.py` | Complete reviewer entry point |
| `run_checks.py`, `run_legacy_checks.py` | Current and selected historical replay layers |
| `checks/` | Executable checks, prefix demonstrator and retained expected outputs |
| `legacy/`, `evidence/` | Historical science and execution records |
| `provenance/` | Explicit record of the retired historical source |
| `figures/`, `editable_figures/` | Figure sources, exports and editable native objects |
| `RESULTS_MAP.md/json` | Result, proof and computation mapping |
| `frozen_manifest.json` | Current input identities; not a mathematical proof |
| `CITATION.cff` | Citation metadata for software version 1.0.0 |

Figure regeneration has optional dependencies described with the figure sources;
it is separate from the standard-library science command. New reports belong in
`results/`. The scientific-input manifest excludes runtime reports, the two root
administrative inventories and `evidence/Final_Integrated_Replay_P42.json` to avoid
a circular dependency. The final package manifest binds those delivered records. Do not regenerate the manifest to make an integrity failure pass.
`freeze_inputs.py` is a maintainer snapshot tool, not a reviewer repair command.
Publishing uses browser uploads and a manually prepared draft release. No workflow
is installed, and local results do not assert a GitHub-hosted execution.

## Citation and rights

Use [CITATION.cff](CITATION.cff). No repository URL, release DOI or public deposit
is implied by this local package. The author's covered code is BSD-3-Clause;
covered documentation, tables and figures are CC BY 4.0. Third-party APEX data,
DejaVu fonts and retained notices keep their own terms. See
[LICENSING.md](LICENSING.md), [RIGHTS.md](RIGHTS.md) and
[LICENSE_SCOPE.json](LICENSE_SCOPE.json) for component scope. Historical
undecided-licence language is preserved as evidence and does not revoke the
subsequently adopted grant for covered author-owned material.
