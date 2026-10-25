# Packaging and validation boundaries

The P52 delivery separates the flat public repository from browser upload aids.
`01_Repository_Files/` in the outer GitHub kit contains this repository;
`02_Browser_Upload_Batches/` contains path-preserving batches of at most 90 files;
`03_Release_Asset/` contains the same complete ZIP supplied for manual Zenodo
deposit. The batches and release-asset copy do not belong inside the repository.
The [browser guide](Browser_Release_Guide_RO.md) explains the author route.

No GitHub Actions workflow is installed. Repository upload and draft-release
creation are manual browser operations. The retained execution records describe
local computation. Uploading files, viewing a PASS record or checking a ZIP's
identity does not execute the scientific programs again.

The complete scientific entry point is `run_all_checks.py`. It combines the
six base scientific checks, 26 selected historical programs and ten additional
checks: 42 scientific program entries and one rejection control with four
mutations. The current triangle and public-block checks have separate data and
entry points; the earlier upper-bound controls remain unchanged. The
retired historical source is omitted from the public payload. Its digest is
retained without claiming fresh verification of its bytes. The ordinal adapter
recomputes the scientific quantities against the remaining public proof inputs;
[the provenance note](Provenance_Migration_P41.md) defines that comparison.

The input freeze binds reviewed files, including nested scientific `results/`
directories and historical manifests. Top-level runtime `results/`, the two root
administrative inventories and named final integrated execution records are
excluded to avoid circular dependencies. The final package manifest binds the
delivered administrative files and execution evidence. Exact exclusions are
recorded in `frozen_manifest.json`; only its maintainer regenerates this snapshot.
An integrity failure is resolved by restoring or reviewing the changed files,
not by refreshing hashes until a check passes.

The root `.gitattributes` disables automatic text conversion for Git operations.
GitHub's web uploader ignores that file's attributes, so it is not a guarantee
about browser-uploaded bytes. The supplied release asset preserves the locally
verified archive. A GitHub-generated source ZIP and this attached ZIP are
different containers; their archive hashes are not expected to match. A downloaded
source ZIP can be checked against the packaged file manifest before publication.

Three native ODG figures accompany the source and exported representations.
Their object checks concern editability and content, not a new scientific run.
The current grant is in `LICENSING.md`; `LICENSE_SCOPE.json` inventories covered
files and nested archive members. Historical pending-licence statements and
historical file counts describe their original snapshots. They do not override
the adopted BSD-3-Clause/CC BY 4.0 grant or current package inventories.

The local preparation label is `P52`; the software version and tag are `1.0.0`
and `v1.0.0`. The existing repository is https://github.com/antonioclim/unsupported-pareto-prefix-certification.
The version DOI `10.5281/zenodo.23632859` is reserved. At preparation on
25 October 2026, the release and Zenodo record are unpublished; release URL,
concept DOI and publication dates remain unset until confirmed. The current
packaged replay record is `results/Full_Local_P52.json`; P49 and P46 replay
records retain their historical identities. Release publication and Zenodo
record publication are separate operations; this kit does not enable an
automatic connection between the services.

The current scientific conditions and the distinction between the 12/11 bound
and the retained 873/800 control are recorded in
[Current_Scientific_Scope_P46.md](Current_Scientific_Scope_P46.md). The current
article abstract is copied exactly into both active release-metadata JSON files.
Pre-integration public metadata is preserved under
`evidence/history/P42_metadata/`; those files describe the earlier local snapshot
and are not current release instructions.
