# The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries

**Antonio Clim — reproducibility companion**

This repository contains exact-arithmetic checks, retained input data and analytic
figure sources for the study of competitive acquisition of Pareto and
unsupportedness certificates under prefix observations. Start with the
[result-to-check map](RESULTS_MAP.md) to locate the calculation supporting each
named result.

This is the locally prepared GitHub candidate, metadata revision P36, with the
licences adopted in P35. The scientific checks retain the P33 snapshot. Five
active citation/instruction files now use the adopted title and current rights
state; their exact prior versions and the original manifest are archived under
[`evidence/history/P33_metadata/`](evidence/history/P33_metadata/). The remaining
139 original manifest-bound files are byte-identical. The current manifest binds
152 files, including the preserved metadata and migration documentation.

The current SICOMP manuscript and Supplementary Materials are separate submission
documents. The historical P21 manuscript remains included as a checker dependency;
it is outside the new licence grant, as described below. No repository release or
new DOI has been created for this candidate.

## Run the checks

Use **Python 3.12 or later on Linux or WSL**, without `-O`. The scientific checks
use the Python standard library and run offline; no package installation,
LaTeX or laboratory hardware is required. Other platforms have not been tested.
Run commands from the directory containing `run_checks.py`.

```bash
python3 --version
python3 run_checks.py --verify-only --record results/Integrity_Local.json
python3 run_checks.py --record results/Current_Local.json
python3 run_checks.py --legacy --record results/Full_Local.json
```

| Command | What it does |
|---|---|
| `--verify-only` | Checks the identities of all 152 current manifest-bound files; executes no scientific checker. |
| Default run | Executes six current scientific checks and one malformed-certificate rejection control. |
| `--legacy` | Also executes 26 retained historical programs and compares their 27 outputs. |

The last command includes the current checks, so a full replay can be run directly.
The complete set is **32 scientific program entries and one control**; this count
is not a count of independent findings. The rejection control checks five
deliberately malformed algebraic certificates. One of the historical programs
produces both the wireless JSON and CSV outputs.

A successful command exits with code 0 and writes a fresh report with
`"status": "PASS"`. Check the report's run ID and completion time:

```bash
python3 -c "import json; r=json.load(open('results/Full_Local.json')); print(r['status'], r['run_id'], r['finished_at_utc'])"
```

`RUNNING` is incomplete. Exit code 1 indicates an execution or comparison failure;
code 2 indicates a preflight or command-line failure. A report left by an earlier
run is not evidence that a later command succeeded. The
[runtime README](README.txt) describes safe output destinations, atomic
reporting and exact comparison rules.

The retained full P33 execution took 37.0833 seconds with Python 3.12.14 on Linux;
see [its execution record](evidence/Execution_P33.json). This is a historical local
measurement, not a runtime guarantee or a GitHub Actions result.

## What the calculations establish

The companion checks finite ordinal games, band geometry, finite-prefix candidate
obstructions, exact rational upper-bound certificates and specified historical
examples. The upper-bound certificate covers 48 boxes and 4,644 rational Bernstein
coefficients; the two methods provide separate computational reconstructions of
the same certificate. The results map states the limits of every calculation.
Universal theorem proofs remain in the manuscript and Supplementary Materials.

The APEX trace analysis uses 1,536 overlapping tasks, with 41 positive tasks after
all nine observations and 1,495 negative tasks. It is a secondary analysis of
retained data, not a new physical experiment, independent replication, measured
acquisition saving or validation of a 6G/WPT system.

## Analytic figures

The two figures illustrate exact constructions and analytic bounds. Their source,
captions and vector/PDF/PNG exports are in [`figures/`](figures/README.txt). Plotting
dependencies are optional; they are unnecessary for the scientific checks.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r figures/requirements-figures.txt
python3 figures/make_figures.py --output-dir results/figures_regenerated
python3 figures/check_figure_values.py results/figures_regenerated/Figure_Exact_Values.json
```

Both figure commands must report `PASS`. Exact-value checking uses only the
standard library. Rendering was recorded with Matplotlib 3.10.8 and NumPy 2.3.5;
other rendering environments may change export hashes without changing the
rational values.

Native LibreOffice Draw files are supplied in
[`editable_figures/odg/`](editable_figures/odg/). Their text boxes, marker geometry,
lines, regions and individual hatch lines remain editable. The accompanying
editing guide, native builder, fonts and verification records are in
[`editable_figures/`](editable_figures/). Reference exports reproduce the
manuscript figures; native ODG exports may have minor font-metric differences.
These additions sit outside the scientific snapshot manifest.

## Repository guide

| Path | Contents |
|---|---|
| `run_checks.py`, `run_legacy_checks.py` | Current entry points and clean-workspace historical replay |
| `checks/` | Current checkers and expected results |
| `legacy/` | Retained historical sources, inputs, results and component notices |
| `evidence/` | Recorded P33 execution and retained execution provenance |
| `figures/` | Active figure generators, exact values and exports |
| `editable_figures/` | Native ODG drawings, sources, fonts, editing guide and representation checks |
| `RESULTS_MAP.md`, `RESULTS_MAP.json` | Named results, proof locations, commands and finite-check scope |
| `frozen_manifest.json` | Current 152-file identity map, including the preserved pre-P36 metadata |
| `CITATION.cff` | Current P36 local citation with the adopted article title |
| `release_preparation/` | Current citation/release draft/component map and historical rights inventory |
| `docs/` | Packaging and validation notes |
| `.github/workflows/reproduce.yml` | Prepared workflow for a future GitHub run |

New execution reports belong under `results/` and are ignored by Git. The
`.gitattributes` file preserves file bytes, including on Windows, because automatic
newline conversion would invalidate the frozen hashes. Do not regenerate the
manifest to make a failed integrity check pass. `freeze_inputs.py` is a maintainer
snapshot utility, not a repair command for reviewers.

## Citation and rights

Use [`CITATION.cff`](CITATION.cff) for this local P36 candidate. Its title matches
the current article; the scientific snapshot remains P33. P34 added the
GitHub-facing documentation and prepared workflow; P35 adopted component
licences; P36 synchronises the title and current metadata. These packaging changes
add no scientific result. The current state is also recorded in
[`CURRENT_RELEASE_METADATA.json`](CURRENT_RELEASE_METADATA.json). Repository URL,
public release date and DOI must be added only when they exist; see
[release notes](RELEASE_NOTES.md).

On 24 October 2026, Antonio Clim adopted **BSD-3-Clause** for his new code and
**CC BY 4.0** for his explanatory documentation, tables and figures, within his
rights. Read the current [`LICENSING.md`](LICENSING.md), scoped [`LICENSE`](LICENSE)
and exact [`LICENSE_SCOPE.json`](LICENSE_SCOPE.json). Full texts are in
[`LICENSES/`](LICENSES/). These terms are effective for their listed components;
they are not a blanket dual licence for this mixed collection.

The retained APEX dataset and DejaVu fonts preserve their own terms and notices.
The historical manuscript
[`legacy/p21/article/Manuscript_Paid_Prefix_Certification_P21_v10.md`](legacy/p21/article/Manuscript_Paid_Prefix_Certification_P21_v10.md)
is included as an unchanged input to a retained checker, but remains outside the
new CC BY grant. Current submission documents are supplied separately.

Earlier undecided-licence wording in frozen files and the embedded P20 archive
is historical evidence. The current P35 grant supersedes those statements only
for the covered author-owned components. It leaves scientific results, source
attributions and excluded rights unchanged. The separate P36 metadata migration
is documented above and preserves the full original snapshot by reconstruction. Follow
[`RIGHTS.md`](RIGHTS.md) when extracting or redistributing components.

The author's instruction to update local kits does not authorise the assistant
to submit the article or publish a repository or Zenodo record. This operational
boundary is separate from the reuse rights already granted by the licences.
