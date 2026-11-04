<a name="heading-reproducibility-p58_extensions-frozen-p58-research-extension-reproduction"></a>


# Frozen P58 research-extension reproduction
<a name="s9-4-extensions"></a>

[Documentation index](../README.md)

**Role:** Technical execution modes, dependencies and result-to-script navigation for the retained research extensions. **Source:** UPPC P61, S9.4, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-reproducibility-p58_extensions-s9-4-published-research-extensions-in-version-1-1-0"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


### S9.4. Published research extensions in version 1.1.0
The published companion version 1.1.0 includes the complete P58 addendum under `extensions/P58/`, preserving its files and internal manifest byte-for-byte. Version 1.2.0 retains the same scientific files under `reproduction/` in the downloaded companion. Historical `P56`, `P57` and `P58` components in paths identify research stages, rather than public software version numbers. Exact replay preserves the delivered evidence and writes a fresh attempt in a separate directory.

From the companion's `reproduction/` directory, run the research extensions with:

```sh
cd extensions/P58
python3 run_research_P58.py --mode dimensions
python3 run_research_P58.py --mode core
python3 run_research_P58.py --mode apex
python3 run_research_P58.py --mode all --sat-source /path/to/detailed_results.zip
```

Python optimisation must remain disabled. The SAT source argument must name the official, checksum-matching archive described in Section S11.4; the addendum does not redistribute that source. The runner documentation defines the exact modes and output location. The dimensional controls additionally require the NumPy and SciPy versions specified in `dimension_reduction/requirements.txt`; the numerical LP comparisons are labelled separately from exact rational checks. The retained CPU diagnostic is environment-specific and is separate from the scientific equality checks.

The earlier P57 addendum is retained byte-for-byte under `retained_P57/`; its original manifest and runner remain available. In the following list, legacy paths are relative to that retained directory. Unless a full path is given, program basenames are in `p56_work/scripts/` and output basenames are in `p56_work/evidence/`. The new `dimension_reduction/` paths are relative to the P58 addendum root:

- **Theorem 20 and Section S6.2:** `p56_work/scripts/upper_87_80_certificate.py` produces the exact polynomial certificate; `root_verify_87_80.py` independently reconstructs its coefficients by rational collocation without importing the producer. `p56_work/evidence/upper_87_80_certificate.json` and `Root_87_80_Independent_P56.json` identify the eight polynomial families, 59 subdivision leaves, 6,639 nonnegative coefficients, 891 unisolvent identity-check points and four rejected certificate mutations. The analytic reduction and policy cost comparison remain part of the proof.
- **Mixed-policy implementation and lower-family controls:** `upper_87_80_operational.py` records exact branch executions in `upper_87_80_operational.json`; `lower_audit_mixed_policy.py` supplies separately written algebraic and feasibility controls in `Lower_Independent_Mixed_Policy_Audit_P56.json`. Finite executions are not a replacement for the continuous-domain theorem or evidence that a maximum observed test ratio is the true worst case.
- **Section S1.1 comparator:** `geo_comparator.py` produces `Geometry_Comparator_P56.json`; `gen_crosscheck_geo.py` produces `Generalization_Crosscheck_Geometry_P56.json` using a separate exact vertex-feasibility oracle, including unequal lengths and weighted means.
- **Sections S5.6–S5.8:** `gen_endpoint_margin_checks.py` produces `Generalization_Checks_P56.json`, with finite controls for weighted endpoint certificates, sharp witness cardinalities, margin certificates and the higher-dimensional counterexample. The statements and proofs establish the universal claims.
- **Section S11.2 and the APEX replay:** `practical_negative_stopping.py` produces `practical_negative_stopping_P56.json`; `root_check_apex.py` verifies the task construction, full-archive verdicts, exported negative witnesses and accounting without importing that producer or its policies. Its output is `Root_APEX_Verification_P56.json`. The unchanged source and earlier policy definitions are obtained from the frozen version 1.0.0 dependency identified by the addendum manifest.
- **Section S11.4 SAT replay:** `practical_sat2024_replay.py` produces `practical_sat2024_replay_P56.json`; `root_check_sat.py` verifies raw CSV parsing, exact means, verdicts, terminal negative witnesses and mixture probabilities without importing the replay producer. Its output is `Root_SAT_Verification_P56.json`. Source acquisition and checksum requirements are recorded in `p56_work/research/practical_SAT2024_protocol.txt` and the addendum README.
- **Section S12.4 diagnostic:** `practical_cpu_diagnostic.py` and `practical_cpu_diagnostic_P56.json` retain the execution protocol and measured local CPU times. These times are neither portable scientific invariants nor measured end-to-end service savings.

- **Sections S5.9–S5.12:** `dimension_reduction/verify_support_decomposition.py` compares exact pair and scalar-interval tests on 2,000 catalogues and nine boundary controls, with a separately labelled numerical LP comparison. `verify_reduction.py` checks 57,963 corresponding prefix verdicts and 12 positive priced-comparator examples, alongside geometric and negative controls. `check_approximation.py` checks 400 rational instances and four boundary controls. `check_three_alternative_projection.py` exhausts 41,664 three-point catalogues, including 423 positive ones, for a supplementary full-information representation result retained only in the research note. This last result is not an acquisition theorem and is not needed for S16–S19. The scripts, retained outputs and fresh replay record identify the precise arithmetic and scope; finite checks do not prove the universal statements.

The author's new addendum code and documentation follow the component-specific licences in Section S9.3. The published 1.0.0 dependency retains its original bytes and notices. The SAT source ZIP and CSV bytes are excluded because a redistribution licence has not been established; the public source URL, hashes, retrieval instructions, code and derived results are supplied. Neither a code audit nor a reproducibility replay is external peer review.
