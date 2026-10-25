# Packaging and validation boundaries — version 1.1.0

The root repository retains the baseline from commit `004b06e63ac2a2a2ed0eccecf924534f2ae65ad1` and adds the complete P58 component at `extensions/P58/`. The root README describes current scope and separate scientific runners. Inner P58/P57 preparation-status notes and dated browser guides remain historical records. `release_preparation/Release_Metadata_Draft.json` is the current manual metadata recipe; it does not activate GitHub/Zenodo integration.

The attached release asset is `unsupported-pareto-prefix-certification-v1.1.0.zip`. Upload the exact same asset to GitHub and the new Zenodo version. GitHub-generated source archives use different ZIP containers; verify their extracted member bytes against `PACKAGE_MANIFEST_SHA256.json` rather than comparing container hashes.

The legacy `frozen_manifest.json` preserves its existing member set and has been refreshed only for intentionally changed administrative files. It does not incorporate the new P58 component into the legacy scientific suite. P58 and P57 each retain their own exact manifest. The final root package manifest binds every delivered file except itself. Licence inventories preserve original component rights and nested original-ZIP assignments.

The historical maintainer script `freeze_inputs.py` is not needed to prepare this release and must not be used to hide a failed check. Its historical scanner does not understand the new nested rerun directories. Do not run it on a tree containing generated reruns. The supplied preparation program constructs the reviewed manifests directly and excludes all runtime outputs from the payload.

Root `.gitattributes` preserves bytes for Git operations; GitHub's browser uploader is not guaranteed to apply those attributes. Verify the final downloaded source archive before publishing the release. Browser batches contain changed/new files only and no deletions. Keep both nested directory paths and hidden root `.gitignore` when uploading.

Publication metadata was prepared using reserved DOI `10.5281/zenodo.23646970` and selected date `2026-10-25`. Local preparation checks syntax and bytes, not DOI registration or remote publication. No Actions workflow or automatic integration is added. The original 1.0.0 archive and DOI remain unchanged.
