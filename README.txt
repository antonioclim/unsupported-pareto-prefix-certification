REPRODUCIBILITY COMPANION — P52
The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries
Antonio Clim

Version 1.0.0 was published on GitHub and Zenodo on 25 October 2026. P53 updates publication metadata on main; the published tag, archive, scientific code, data and retained P52 replay are unchanged. The P46 mathematical and checker baseline and P49 black figure text are retained. The current packaged replay record is results/Full_Local_P52.json; results/Full_Local_P49.json and results/Full_Local_P46.json remain historical execution records. The replay format identifies the unchanged P46 runner implementation, not the delivery edition.

BROWSER-ONLY REPOSITORY PREPARATION

Open docs/Browser_Release_Guide_RO.md or the companion HTML/TXT guide.
The author can prepare the repository and a draft release without a terminal,
Git, GitHub Desktop or GitHub Actions. The delivery wrapper contains prepared
upload batches and the full release asset outside this repository.

OPTIONAL COMPUTATIONAL REPRODUCTION FOR REVIEWERS

1. Extract the archive into a new directory. Open a terminal in the directory
   containing run_all_checks.py. Keep the original archive unchanged.
2. Check Python 3.12 or later:

   python3 --version

3. Execute the complete suite:

   python3 run_all_checks.py --record results/Full_Local_P52.json

4. After the process returns, inspect the current completion record:

   python3 -c "import json; r=json.load(open('results/Full_Local_P52.json')); print(r['status'], r['run_id'], r['finished_at_utc'])"

Expected: exit code 0 and PASS, with a fresh run ID and finish time. RUNNING is an
incomplete attempt. FAIL or a nonzero process exit is not success. A saved PASS
from a previous invocation is not evidence for the current one.

Use Python without -O. The implementation uses only the standard library and
runs offline. No network service, package installation, LaTeX or hardware access
is required. The executed platform is Linux; Windows native execution has not
been performed. WSL can provide a Linux environment, but this is not evidence
that the current snapshot was executed under every WSL version.

Optional identity-only command (no scientific execution):

   python3 run_all_checks.py --verify-only --record results/Integrity_Local_P52.json

The complete route runs six original current scientific checks, one control,
26 historical jobs and ten additional scientific checks: 42 scientific program
entries plus one control. These counts include related checks of the same
result. The separate algebraic rejection control tests four mutations; the
current 12/11 checker rejects four further mutations, eight cases in total.

Comparison rules

All computation takes place in temporary copies. Outputs are removed before
production. Original current checks retain their exact comparison rules: six
outputs compare bytes; the candidate checker compares JSON after excluding only
elapsed_seconds and python_version. The historical layer compares 26 of its 27
outputs byte-for-byte. The remaining ordinal output must match every scientific
field; only its adapted script identity and explicit historical-source provenance
differ. The retired historical-source digest is not a freshly verified source hash.
The other three public proof inputs are still verified from actual bytes.

Ten additional checks compare their exact JSON after excluding only the explicitly
listed runtime fields in run_all_checks.py. The new triangle certificate check
excludes only elapsed_seconds; its analytic check excludes no fields. The public
block check excludes only elapsed_seconds and finished_at_utc. The prefix demo enumerates random
branches exactly; it does not use Monte Carlo. Its comparator is independently
computed on a small finite alphabet rather than read from a fixture. The adverse
price example and all negative inputs remain in the suite.

Reports and failure handling

Reports are written atomically after recording RUNNING. Inside the package,
--record must be under results/. Protected source paths, symbolic links and
unrelated existing external files cannot be overwritten. Relative report paths
are relative to the terminal's current directory. Standard replay reports may be
replaced by a new invocation; use a different filename to preserve every run.

If a command fails, retain its report and error message. A preflight failure
writes FAIL where the destination is valid and writable. Invalid arguments or
an unsafe destination may prevent report creation; the terminal error remains
a failure. Restore a fresh extraction if frozen input bytes differ. Never edit
expected outputs or regenerate a manifest simply to suppress a failure.

Historical records and direct commands

The old scientific sources, results and manifests are retained. Their original
entry points are historical code and can require the retired source. Use
run_all_checks.py for the public snapshot. run_checks.py --legacy reproduces the
base suite only; it does not execute the ten additional scientific checks. The retirement
and comparison contract is in docs/Provenance_Migration_P41.md.

RESULTS_MAP.md/json links named mathematical claims to proof locations and
finite checks. The universal proofs, numeric-to-ordinal reduction and novelty
arguments are not established by a PASS result. Figures have separate optional
rendering dependencies. The recorded APEX analysis uses retained upstream data,
not new physical trials; its no-saving result is preserved. See the erratum note
for the upstream parameter-table correction.

Rights are component-specific: read LICENSING.md, RIGHTS.md and LICENSE_SCOPE.json.
New execution reports are written under results/ and are not frozen inputs.

Manifest boundaries

The scientific-input manifest excludes top-level results/, root LICENSE_SCOPE.json
and PACKAGE_MANIFEST_SHA256.json, and named final integrated replay records
listed in frozen_manifest.json.
These are post-freeze administrative or execution records. The final package
manifest binds their delivered bytes; they are not science inputs. Historical
manifest and execution files elsewhere remain retained and hash-bound. This
explicit separation avoids a manifest/result/licensing circular dependency.

CURRENT SCIENTIFIC SCOPE

The current triangle upper bound is 12/11 for three configurations, every archive
length and unit row prices; a common compulsory information-free setup charge is
allowed. The exact asymptotic candidate-census optimum is 12/11 on the triangle
and fixed three-symbol alphabet at zero setup. Candidate-census means observing
the entire candidate before TRUE on every positive archive, while permitting
interleaving and early FALSE. The unrestricted lower bound is asymptotically
23/22, leaving an interval of width 1/22. Its convergence and exact optimum remain
open. No arbitrary-tariff guarantee follows from these numerical constants.

Supplementary Proposition S11 gives sharp comparator-distortion bounds for public
consecutive equal-row blocks with Cartesian-product completions across blocks.
The factor is at most the largest block length at unit prices and an explicit
price-dependent factor otherwise. Short blocks alone do not bound distortion
under arbitrary tariffs.

The earlier 873/800 bound and its 4,644-coefficient certificate remain historical
controls. The new rule has a distinct exact certificate: 58 boxes and 4,824
multivariate Bernstein coefficients, seven additional univariate coefficients
and nine algebraic identities checked independently. See
docs/Current_Scientific_Scope_P46.md and RESULTS_MAP.md for exact scope.

PUBLISHED SOFTWARE VERSION 1.0.0 — 25 OCTOBER 2026
Repository: https://github.com/antonioclim/unsupported-pareto-prefix-certification
Release: https://github.com/antonioclim/unsupported-pareto-prefix-certification/releases/tag/v1.0.0
Version DOI: 10.5281/zenodo.23632859
Concept DOI: 10.5281/zenodo.23632858
Published source commit: 6517a174a03eaceb0bc9adc31a51959ecb7e7fd6
Archive bytes: 7849303
SHA-256: 19b24d6f9e3cb4f4417fb554988e9d5dbefd8180792bc02ea47790287a9a37ff
Public downloads from both services match the prepared archive byte for byte.
P53 changes current-main publication metadata only. The published tag/archive and scientific sources are unchanged.
The retained P52 replay concerns the original release snapshot; its manifests are preserved under evidence/history/P52_publication/.
Cite the version DOI for this release. See docs/Publication_Verification_P53.json.
