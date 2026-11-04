<a name="heading-provenance-source_data_and_rights-source-data-provenance-and-component-rights"></a>


# Source data, provenance and component rights
<a name="s9-3-data-rights"></a>

[Documentation index](../README.md)

**Role:** Detailed source-data provenance, transformations and component-specific rights. **Source:** UPPC P61, S9.3, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-provenance-source_data_and_rights-s9-3-source-data-and-component-specific-rights"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


### S9.3. Source data and component-specific rights
The APEX dataset attribution and licence notice are retained in `legacy/p9/licence/THIRD_PARTY_APEX.txt`; the licence text is `legacy/p9/licence/ccby4_legalcode.txt`. The source is M. H. Mohamed Hydher, *APEX Dataset: Testbed Traces and Evaluation Results*, version 1.0, DOI `10.3217/3dhx0-2k125`, licensed under Creative Commons Attribution 4.0 International. Original files are retained under `legacy/p9/licence/apex_dataset/`: `Crystal_results.json`, `RPL_results.json` and `README.md`.

The secondary analysis sorts configurations and rows, derives failure from reliability, forms exact finite means and partial-sum bounds, transforms the declared latency objective and constructs simulated disclosure transcripts. These changes are identified; no new radio experiment is represented. Attribution, the dataset DOI, the licence link and the description of changes accompany the retained data.

The [APEX authors' erratum](https://www.carloalbertoboano.com/documents/hydher25tosn_errata.pdf) corrects the article's RPL rank-threshold values from $\{4,8,12,16\}$ to $\{1.5,3,6\}$. The frozen data already store `_RANK_THRESHOLD` as $\{192,384,768\}$, which gives the corrected set after division by 128. The separate `_RPL_DIO_INTERVAL_MIN` parameter has values $\{4,8,12,16\}$. Inspection of the retained replay loader confirms that it groups actual parameter dictionaries and does not hard-code the erroneous article table. This provenance correction requires no change to the frozen input bytes or to the replay calculation. The static inspection is distinct from a new execution of that calculation.

The associated APEX software record, DOI `10.3217/ckwaw-z8h92`, has a separate MIT licence. Its firmware and framework software were not executed by this work and are not the source of a blanket licence for this companion. The APEX article, DOI `10.1145/3770918`, is a separate cited work. Dataset reuse permission is not inferred from article access.

The author's new code is licensed under BSD-3-Clause and the author's new documentation, tables and figures under CC BY 4.0, to the extent of the author's rights. Third-party components retain their own licences and attributions; the dataset's CC BY 4.0 licence does not supply rights to other components. The companion repository is <https://github.com/antonioclim/unsupported-pareto-prefix-certification>. Version 1.1.0 is archived at <https://doi.org/10.5281/zenodo.23646970>; the earlier version 1.0.0 remains at <https://doi.org/10.5281/zenodo.23632859>. The source versions and reading limits remain explicit; bibliography verification and internal computational checks do not establish historical priority or substitute for external peer review.
