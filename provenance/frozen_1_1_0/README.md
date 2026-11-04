# The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries

Antonio Clim — reproducibility companion **1.1.0**.

This release brings the P57/P58 software and evidence together with the existing companion. The main manuscript and Supplementary Materials are separate documents and are not included in this software archive.

## Version and citation

- Version DOI: https://doi.org/10.5281/zenodo.23646970
- Version-independent concept DOI: https://doi.org/10.5281/zenodo.23632858
- GitHub release: https://github.com/antonioclim/unsupported-pareto-prefix-certification/releases/tag/v1.1.0
- Release date selected during preparation: 2026-10-25
- Previous published version 1.0.0: https://doi.org/10.5281/zenodo.23632859

These links and metadata were prepared for the manual release. The preparation program checks DOI syntax and local bytes; it does not reserve a DOI or certify that either service has published the release. The attached archive `unsupported-pareto-prefix-certification-v1.1.0.zip` is the payload intended for both GitHub and Zenodo. GitHub's automatically generated source archives have different container bytes.

## Scientific scope

The additions include the **87/80** upper-bound certificate for three configurations on the triangle, operational controls, a faster retrospective comparator, controlled APEX/SAT archive replays and higher-dimensional certification checks. The stated triangle result uses unit row prices and all other hypotheses of the accompanying manuscript; it is not a guarantee for arbitrary tariffs. The **12/11** asymptotic optimum remains valid for the candidate-complete policy class. The unrestricted asymptotic lower bound is **23/22**; the unrestricted optimum and convergence remain open.

For three alternatives, unsupportedness in arbitrary dimension can be checked by scalar interval feasibility. This does not reduce the number of purchased records. Exact paid-prefix transfer requires the stated public two-anchor representation and full raw-row/completion, observation and price correspondence. A universal nonnegative affine compression to two dimensions does not exist for general catalogues. Approximate reconstruction gives a sufficient certificate only with valid error bounds and strict margins; failure is inconclusive.

Finite exact controls and separately labelled floating-point cross-checks support reproducibility; they do not alone prove universal theorems. No measured monetary, energy or deployed-service benefit is claimed. Author-side AI-assisted checks are distinct from external peer review and proof-assistant verification.

## Files and provenance

- `extensions/P58/` contains all 84 files of the P58 addendum unchanged.
- `extensions/P58/retained_P57/` preserves its earlier code, research notes, evidence and manifest unchanged.
- `extensions/P58/retained_P57/dependencies/unsupported-pareto-prefix-certification-v1.0.0.zip` is the unchanged published archive, SHA-256 `19b24d6f9e3cb4f4417fb554988e9d5dbefd8180792bc02ea47790287a9a37ff`. It is required by the APEX replay.
- Existing scientific files and historical reports in the root repository retain their original scope and results. Current root release metadata has been updated from base commit `004b06e63ac2a2a2ed0eccecf924534f2ae65ad1`.

The inner P58/P57 README statements about being unpublished describe their original preparation snapshots. They are preserved for provenance; the root metadata identifies this release. Historical browser guides under `docs/`, dated scope notes and historical execution records describe their own versions. They are not instructions to republish version 1.0.0.

## Run the checks

Preparation of this release uses Python 3.10+ standard library only. Scientific replays have their own requirements. Run Python without `-O`. Use the supplied runners so delivered evidence remains unchanged.

New dimensional controls (the validated environment used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0):

```bash
python3 -m pip install -r extensions/P58/dimension_reduction/requirements.txt
python3 extensions/P58/run_research_P58.py --mode dimensions
```

The P57 core and APEX controls use the Python standard library:

```bash
python3 extensions/P58/run_research_P58.py --mode core
python3 extensions/P58/run_research_P58.py --mode apex
```

The SAT replay requires the official source ZIP, downloaded separately as described in `extensions/P58/retained_P57/README.md`:

```bash
python3 extensions/P58/run_research_P58.py --mode sat --sat-source /path/to/detailed_results.zip
python3 extensions/P58/run_research_P58.py --mode all --sat-source /path/to/detailed_results.zip
```

`--mode all` runs the new dimensional and retained P57 modes. The original 1.0.0/P46 suite is a separate baseline:

```bash
python3 run_all_checks.py --record results/Full_Local_1_1_0_baseline.json
```

The root legacy runner alone does not run the P58 additions. Its optional `--verify-only` checks frozen identities and executes no scientific programs. The retained P58 validation reran four dimensional programs and compared 39 scientific fields; it did not rerun all P57 experiments. No scientific rerun is implied merely by preparing or publishing this archive.

## Data, licences and local outputs

APEX source: https://doi.org/10.3217/3dhx0-2k125; associated article: https://doi.org/10.1145/3770918. Original notices and covered source bytes are retained. SAT source: https://satcompetition.github.io/2024/. Raw SAT ZIP/CSV files are not redistributed. The SAT runner verifies its required checksum before use.

BSD-3-Clause applies to covered author code; CC BY 4.0 applies to covered author documentation, results and figures. Original APEX, DejaVu and standard-text rights remain unchanged. See `LICENSING.md`, `LICENSE_SCOPE.json` and the inner P58/P57 notices. This is component licensing, not a choice of two alternative licences for every file.

Generated `reruns/` directories and local environments are excluded from publication. SAT reruns contain a local copy of the external source ZIP. Do not commit or redistribute those run directories. No GitHub Actions workflow, credentials, author contact form or manuscript source is included.
