# UPPC research notes and reproducibility documentation

Antonio Clim. Companion version **1.2.0** for *The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries*.

The public companion collects the scientific software, retained inputs and outputs, evidence maps and selected research notes. The article, Essential Supplement and their canonical sources form a separate submission package.

## Additional research and evidence
- [Complete square/comparator research note](research_notes/SQUARE_EXTENSIONS_COMPLETE.md)
- [Complete finite-triangle classifications](research_notes/TRIANGLE_FINITE_EXTENSIONS_COMPLETE.md)
- [Complete earlier many-criterion extensions and controls](research/MATHEMATICAL_EXTENSIONS_P61.md)
- [Secondary access-model and implementation boundaries](research/ACCESS_MODELS_AND_IMPLEMENTATION_BOUNDARIES.md)
- [Extended methods, replay evidence and interpretation](research_notes/EXTENDED_METHODS_AND_REPLAYS.md)
- [Historical triangle bounds and adverse arguments](history/TRIANGLE_UPPER_BOUND_CONTROLS.md)
- [APEX replay](replays/APEX.md) and [SAT 2024 replay](replays/SAT2024.md)
- [Proposed application contracts](applications/SCENARIOS_AND_ASSUMPTIONS.md) and [extended service interpretation](applications/AUDIT_SERVICE_AND_STOPPING.md)
- [Overhead protocol and conditional accounting](economics/OVERHEAD_AND_BREAK_EVEN.md)

The retained replays do not measure production profit, energy savings or new solver performance. Negative-only SAT tasks, the lack of positive APEX disclosure savings and computation overhead remain visible in the essential scientific synopsis and in the complete notes.

<a name="heading-readme-reproduce-and-inspect-provenance"></a>

## Reproduce and inspect provenance
- [Baseline commands and coverage](reproducibility/BASELINE_REPLAY.md)
- [P58 extension modes and dependencies](reproducibility/P58_EXTENSIONS.md)
- [Operational policy walkthrough](implementation/CONSTRUCTIVE_POLICIES.md)
- [Disclosure demonstrators and controls](implementation/DISCLOSURE_SERVICE.md)
- [Source data and rights](provenance/SOURCE_DATA_AND_RIGHTS.md)
- [Research/control history](provenance/RESEARCH_HISTORY.md)
- [Shared bibliography](REFERENCES.md)
- [All modules and their roles](INTEGRATION_INDEX.md)

## Software paths and offline reading

In the downloaded release ZIP, run scientific commands from `companion/reproduction/`. In a GitHub checkout, run the same commands from the repository root. The technical modules give the paths and prerequisites for the frozen programs. Begin with [Baseline replay](reproducibility/BASELINE_REPLAY.md) and [P58 extensions](reproducibility/P58_EXTENSIONS.md).

Each Markdown module has a neighbouring offline HTML view. The HTML uses native MathML and local styles. Open [the offline index](README.html) after extracting the ZIP.

## Citation and component rights

- Companion version 1.2.0. <https://doi.org/10.5281/zenodo.23936602>
- Frozen software baseline version 1.1.0. <https://doi.org/10.5281/zenodo.23646970>

The archived baseline commit is `1d8c97b0dbb675843894e0644563b99481eb65a3`. The baseline DOI cites that earlier snapshot. The v1.2.0 DOI identifies the software and documentation package described here.

Existing software, documentation and third-party licences apply to their respective components. Manuscript-derived research notes retain their existing rights. See the [component rights notice](../RIGHTS_NOTICE.md).
