# Packaging and validation boundaries

The P42 delivery separates the flat public repository from browser upload aids.
`01_Repository_Files/` in the outer GitHub kit contains this repository;
`02_Browser_Upload_Batches/` contains path-preserving batches of at most 90 files;
`03_Release_Asset/` contains the same complete ZIP supplied for manual Zenodo
deposit. The batches and release-asset copy do not belong inside the repository.
The [browser guide](Ghid_GitHub_Release_Browser_RO.html) explains the author route.

No GitHub Actions workflow is installed. Repository upload and draft-release
creation are manual browser operations. The retained execution records describe
local computation. Uploading files, viewing a PASS record or checking a ZIP's
identity does not execute the scientific programs again.

The complete scientific entry point is `run_all_checks.py`. It combines the
current checks, the selected historical replay and seven audited checks: 39
scientific program entries and one rejection control with four mutations. The
retired historical source is omitted from the public payload. Its digest is
retained without claiming fresh verification of its bytes. The ordinal adapter
recomputes the scientific quantities against the remaining public proof inputs;
[the provenance note](Provenance_Migration_P41.md) defines that comparison.

The input freeze binds reviewed files, including nested scientific `results/`
directories and historical manifests. Top-level runtime `results/`, the two root
administrative inventories and the named final integrated execution record are
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

The local candidate label is `P42`; `v1.0.0` is the proposed first
public tag. Public URLs, release dates and DOIs remain unset until real identifiers
exist. Publishing a release and depositing a Zenodo record are separate decisions;
this kit does not enable an automatic connection between the services.
