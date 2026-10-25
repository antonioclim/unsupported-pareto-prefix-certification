# Reproducibility addendum to the P57 submission

Antonio Clim — *The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries*.

This submission-supplied addendum contains exact code, certificates, derived results and mathematical working notes for the additions integrated after the published companion version 1.0.0. It is not a new public release and has no separate DOI. The immutable published companion remains:

- https://github.com/antonioclim/unsupported-pareto-prefix-certification/releases/tag/v1.0.0
- https://doi.org/10.5281/zenodo.23632859

The published archive is included unchanged in `dependencies/` solely to make the APEX replay reproducible. Its SHA256 is `19b24d6f9e3cb4f4417fb554988e9d5dbefd8180792bc02ea47790287a9a37ff`. Its existing proof certificates concern the preceding results. The new 87/80 certificate and new replay evidence are in this addendum; they are not represented as contents of the published DOI archive.

## Run the checks

Use Python 3.10 or later, without `-O`. The required programs use only the Python standard library. From this extracted directory:

```bash
python3 run_research_P57.py --mode core
python3 run_research_P57.py --mode apex
```

The core run executes eight exact programs: the 87/80 certificate producer, independently implemented Bernstein verifier, operational tests, separate mixed-policy arithmetic audit, faster comparator, dimensional/margin checks, independent comparator cross-check and finite-corpus search oracle. The APEX run executes the stopping-wrapper replay and its independent raw-data verifier. On the author's validation environment the combined twelve-program run took approximately one minute; this is an indicative local observation, not a performance claim.

The SAT run needs the original archive, which is not redistributed. Retrieve `detailed_results.zip` from the official source:

https://satcompetition.github.io/2024/downloads/detailed_results.zip

The required ZIP SHA256 is `dfdf1d515fc95e95d3b76f907a2ce67932af1f8905f90c3dd7f743ea6c2b751a`. The runner verifies it before using it. Supply its location:

```bash
python3 run_research_P57.py --mode sat --sat-source /path/to/detailed_results.zip
python3 run_research_P57.py --mode all --sat-source /path/to/detailed_results.zip
```

An optional local CPU diagnostic, distinct from disclosure counts, is available:

```bash
python3 run_research_P57.py --mode apex --cpu
```

The runner verifies every delivered file against `MANIFEST_P57.json`, creates a new `reruns/<timestamp>_<id>/` directory, and leaves the delivered evidence unchanged. It removes the expected generated outputs from that isolated copy before executing the programs, so an old output cannot masquerade as a successful rerun. `Replay_P57.json` reports program exit codes, regenerated outputs and equality of scientific fields against the delivered results. Machine-dependent timing fields and hashes of reports containing those timings are excluded from equality comparisons. The optional CPU measurements are not expected to match. Rerun directories are local work products and are not part of the addendum manifest.

## Evidence and scope

See `RESULTS_MAP.md` for the claim-to-code map. The certificate proof and conceptual reductions are presented in the accompanying manuscript and supplement. The retained research notes provide further derivations and provenance; they do not replace those canonical documents.

Files under `p56_work/` retain their original P56 names and bytes to preserve audit hashes. Statements in those dated notes that the P55 manuscript had not yet been changed describe the research snapshot. P57 is the subsequent integration. References to historical manuscript section numbers should be resolved using the current manuscript and `RESULTS_MAP.md`.

The 87/80 result is a uniform mathematical upper bound for the stated triangle model. The unrestricted optimum remains open, between a lower asymptotic bound of 23/22 and an upper bound of 87/80; convergence is not asserted. The 12/11 candidate-census result remains valid for its restricted class. Finite tests corroborate implementations; they do not alone prove the continuous-domain theorem. The independent implementations and conceptual reviews here are AI-assisted author-side checks, not external peer review or proof-assistant verification.

APEX and SAT results count disclosed records in controlled blind replays of public archives. All 41 positive APEX tasks still use full census. The 1,092 SAT tasks are all negative. The SAT transformation uses published PAR-2 scores divided by 10,000 and the 10,000 failure sentinel; the declared triangle is a conservative completion contract, not the exact physical image. No monetary, radio-energy or deployed-service benefit is claimed. Optional CPU timing can increase despite reduced disclosure counts.

This addendum contains no article or supplement source, cover letter, private author report, postal/contact form, continuity prompt, or downloaded SAT ZIP/CSV. No GitHub Actions or remote publication operation is involved in running it. Third-party source rights and notices are described in `LICENSING.md`.
