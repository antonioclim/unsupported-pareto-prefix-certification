# P56 independent review of the sorted-stream comparator

Reviewed final source: `p56_work/scripts/geo_comparator.py`, SHA256 `fa040ca0a651eed14131a31df590281c317938d134079189b2fb9ecef1f3a7ae`.

Outcome: no defect found in the stated mathematical reduction, implementation flow, or tested cases. This is an AI-assisted internal proof/code review, not external peer review or proof-assistant verification.

## Proof checks

1. **Safety reduction.** For fixed candidate prefix, every TRUE state must include each rival's first prefix with L_g not dominating U_A. Increasing the rival prefix preserves this safety. Once a strict witness pair is selected, reducing all other rivals to their safety prefixes preserves both certificate conditions.
2. **Witness orientation.** Under safety, a rival upper corner cannot dominate L_A. An effective scalarisation restriction must be strictly northwest or strictly southeast. Equal coordinates or coincident corners do not introduce an omitted strict witness.
3. **Stream monotonicity.** For a northwest corner, A=L_A,c-U_g,c increases and C=U_g,f-L_A,f decreases as the prefix grows, so C/(A+C) decreases. For a southeast corner, D=U_g,c-L_A,c decreases and E=L_A,f-U_g,f increases, so E/(D+E) increases. All denominators are positive within their respective crossing classes.
4. **Distinct labels.** A single coordinatewise decreasing upper-corner path cannot contain both a northwest and a southeast corner: either chronological direction would require one coordinate to increase. Consequently the best southeast state paired with a northwest state automatically belongs to another rival.
5. **Strictness.** In descending threshold order, the qualifying southeast states have threshold strictly larger than the current northwest threshold. The code evaluates all northwest states in a tied group before inserting any southeast state from the same group. A scalarisation tie therefore never counts as unsupportedness.
6. **Optimization.** For each northwest state, a minimum incremental-price southeast state among all qualifying states minimizes the pair cost. Every feasible pair is covered, and every returned pair is feasible. Prices are accumulated independently of the geometric importance weights.
7. **Unequal lengths and importance weights.** The proof only needs L_g to increase and U_g to decrease, endpoint attainment, independent completion and positive prices. Positive normalized scalar importance weights preserve those properties. The final API checks lengths, positivity and normalization.
8. **Complexity.** For each candidate prefix, construction and scanning of all rival prefix states is O(L), with at most K-1 individually sorted streams merged in O(L log K). There are n_A+1 candidate prefixes. Working storage is O(L), where L=sum_g(n_g+1). Equal N yields O(KN² log K) rational arithmetic/comparison operations. This is an arithmetic count; no unstated unit-bit-cost guarantee is implied.
9. **Scope.** This is a hindsight comparator supplied the full realised archive. It is not an online acquisition policy, a new triangle competitive ratio or measured economic savings. P55 already contains an O(K²N²) pair-frontier comparator, so the new gain is removal of its pairwise K² factor and the explicit generalized implementation.

## Independent finite check

`p56_work/scripts/gen_crosscheck_geo.py` imports the proposed solver, but computes the comparison optimum with a separate general-dimensional exact Fraction oracle. That oracle enumerates vertices of the normalized supporting-weight polytope using rational Gaussian elimination; it does not call the proposed solver's interval oracle, pair logic, arrays or brute-force routine.

The final-source check compared returned optima and returned certificate validity on **100 archives**, including **40 unequal-length/nonuniform-importance-weight archives**, with **57 positive** cases. It exhaustively checked **15,516 prefix states**. All comparisons passed.

Evidence: `p56_work/evidence/Generalization_Crosscheck_Geometry_P56.json`.

The finite corpus does not prove the universal algorithm. The proof checks above address its general logic; the exact enumeration addresses implementation mistakes on the declared instances.
