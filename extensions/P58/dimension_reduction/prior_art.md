# Prior-art audit: objective reduction and paid-prefix certification

Research date: 25 October 2026. This is an internal research note, not an edit to the canonical SICOMP manuscript. The search establishes substantial prior art; it does not establish exhaustive novelty clearance.

## Conclusions for the parent

1. Objective reduction, redundant-objective elimination, error-controlled objective subset selection, PCA/MVU reduction and positive linear objective extraction are established research topics. Do not present these broad ideas as new.
2. An especially close current preprint is Löhne and Zillmann, *Low-Rank Multi-Objective Linear Programming*, arXiv:2508.20880v3, revised 25 September 2026. It proves exact rank-based reduction with a transformed ordering cone. A generic rank-two factorisation/cone argument therefore needs attribution and careful delimitation.
3. Preservation of nondominance or the efficient set is not sufficient to preserve the paper's predicate: nondominated AND unsupported under every nonzero nonnegative weight, with ties counting as support.
4. A potentially distinct target is preservation of every admissible completion, every prefix certificate, its disclosure price, the retrospective comparator and the information available to an adaptive policy. None of the sources inspected here establishes that entire paid-prefix equivalence. This is a research-positioning observation, not a proof of novelty.
5. Any preprocessing that reads hidden objectives to discover a reduction must be charged or supplied as genuinely public prior information. Empirical low rank of realised complete means does not prove low rank of all legal unseen completions.

## Verified sources and relevance

### Brockhoff and Zitzler (2009)

Brockhoff, D., & Zitzler, E. (2009). Objective reduction in evolutionary multiobjective optimization: Theory and applications. *Evolutionary Computation, 17*(2), 135–166. https://doi.org/10.1162/evco.2009.17.2.135

Primary author PDF: https://www.cmap.polytechnique.fr/~dimo.brockhoff/publicationListFiles/bz2009c.pdf

Verified refs: `turn101view0`; `turn102view1`; `turn102view2`. Root must open the source before citing a child ref.

The paper develops objective-set conflict and exact/approximate dominance preservation. Its δ-MOSS formulation minimises retained objective count under an allowed error; k-EMOSS minimises error under an objective-count limit. Both are NP-hard. The exact algorithm has stated complexity O(m² k 2^k), with m solutions and k objectives; heuristic algorithms are provided. This is objective selection rather than arbitrary feature extraction. The author PDF includes an errata page, which should be retained when reading definitions. In particular, its 2009 critique of early PCA approaches must not be attributed unchanged to every later PCA method.

Relevant locations: PDF pp. 3–4 (selection versus extraction; earlier work), pp. 10–13 (formulations and algorithms), pp. 27–29 (hardness proofs).

### Saxena et al. (2013)

Saxena, D. K., Duro, J. A., Tiwari, A., Deb, K., & Zhang, Q. (2013). Objective reduction in many-objective optimization: Linear and nonlinear algorithms. *IEEE Transactions on Evolutionary Computation, 17*(1), 77–99. https://doi.org/10.1109/TEVC.2012.2185847

Primary institutional record: https://scholars.cityu.edu.hk/en/publications/objective-reduction-in-many-objective-optimization-linear-and-non/

Verified ref: `turn101view1`. The Aalto record omits Zhang, whereas CityU and the publisher-indexed record identify all five authors; use the five-author list.

The work presents PCA and maximum-variance-unfolding approaches, an error measure and sensitivity analyses, including tests up to 50 objectives and two applications. Its claim of reduction to two or three objectives is conditional on that many objectives being essential, not a universal claim that every many-objective problem admits such reduction. The abstract distinguishes reduced representations retaining four or more objectives as potentially useful too. This inspected evidence is the primary institutional abstract/metadata, not a full independent re-audit of its proofs.

### Cheung et al. (2016)

Cheung, Y.-M., Gu, F., & Liu, H.-L. (2016). Objective extraction for many-objective optimization problems: Algorithm and test problems. *IEEE Transactions on Evolutionary Computation, 20*(5), 755–772. https://doi.org/10.1109/TEVC.2016.2519758

Primary institutional record: https://scholars.hkbu.edu.hk/en/publications/objective-extraction-for-many-objective-optimization-problems-alg-2/

Author PDF: https://www.comp.hkbu.edu.hk/~ymc/papers/journal/TEVC2519758_publication_version.pdf

Verified refs: `turn109search1`, `turn106search49`, `turn108search24`. Direct PDF opening timed out; publisher-version content was indexed by search. Do not claim complete full-text inspection.

This is especially relevant to proposed aggregation maps: reduced objectives are linear combinations of original objectives, selected to increase conflict. The reported guarantee concerns Pareto solutions of the reduced problem also being Pareto solutions of the original. That direction alone does not imply retention of every original Pareto point or preservation of its supported/unsupported label. A detailed comparison requires the full assumptions of its theorems, not only the abstract.

### Zhen et al. (2020)

Zhen, L., Li, M., Peng, D., & Yao, X. (2020). Objective reduction for visualising many-objective solution sets. *Information Sciences, 512*, 278–294. https://doi.org/10.1016/j.ins.2019.04.014

Primary publisher page: https://www.sciencedirect.com/science/article/pii/S0020025519303147

Verified refs: `turn106search0`, `turn106search1`.

Their ORV method sequentially represents objective vectors using positively correlated others and removes a vector with small representation error. Its goal is a lower-dimensional visualisation that retains dominance and distribution as far as possible. This is close prior art for linear-reconstruction ideas and shows why an empirical visualisation should not be described as exact universal two-dimensional certification. The inspected publisher text does not establish paid-prefix certificate or cost preservation.

### Löhne and Zillmann (2026 preprint version)

Löhne, A., & Zillmann, P. (2026). *Low-rank multi-objective linear programming* (Version 3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2508.20880

Primary abstract: https://arxiv.org/abs/2508.20880

Primary full text: https://arxiv.org/pdf/2508.20880

Verified refs: `turn111view0`, `turn111view1`.

Originally submitted August 2025; v3 is dated 25 September 2026. The paper factors a linearly dependent objective matrix and transforms a multiobjective linear programme into an equivalent lower-dimensional vector linear programme with a nonstandard ordering cone. The reduced dimension equals the matrix rank. This directly overlaps with broad exact rank-reduction claims. It also identifies conic combinations as a classical sufficient mechanism for nonessential objectives. The setting is linear optimisation over a polyhedron, not the paper's finite, paid-prefix, unsupported-point certification problem. Do not claim journal acceptance: only the preprint status was verified. A lower-rank approximation is discussed, but that does not give a blanket exact preservation result for a finite catalogue's unsupported label.

### Earlier redundancy literature

Gal, T., & Leberling, H. (1977). Redundant objective functions in linear vector maximum problems and their determination. *European Journal of Operational Research, 1*(3), 176–184. https://doi.org/10.1016/0377-2217(77)90025-X

Primary publisher URL: https://www.sciencedirect.com/science/article/abs/pii/037722177790025X

Verified ref: `turn102search0`. It develops relative/absolute redundancy and methods to remove objectives without changing the efficient solution set for multicriteria linear programmes. This is historical prior art for exact redundancy; it is not an unsupported-point query-cost theorem.

Agrell, P. J. (1997). On redundancy in multi criteria decision making. *European Journal of Operational Research, 98*(3), 571–586. https://doi.org/10.1016/0377-2217(95)00340-1

Primary publisher URL: https://www.sciencedirect.com/science/article/pii/0377221795003401

Verified ref: `turn103search0`. It develops conflict-based redundancy, a linear-case test and a correlation-based probabilistic approach for the nonlinear case. Only the primary abstract and metadata were inspected.

### Order dimension

Dushnik, B., & Miller, E. W. (1941). Partially ordered sets. *American Journal of Mathematics, 63*(3), 600–610. https://doi.org/10.2307/2371374

Original article scan hosted academically: https://fa.ewi.tudelft.nl/~hart/set_theory/material/dushnik_miller-partially_ordered_sets.pdf

Verified metadata: `turn103search44`; DOI independently confirmed in the AMS publisher bibliography at https://www.ams.org/journals/proc/1975-052-01/S0002-9939-1975-0373988-0/home.html (`turn103search5`). Direct scan opening timed out.

Classical order dimension is the appropriate conceptual background for impossibility of faithfully embedding every dominance order into the plane. A specific counterexample should still be proved self-contained in this research note. Do not conflate preserving all pairwise order relations with merely preserving one nominated candidate's Boolean label.

## A self-contained distinction: dominance preservation does not preserve unsupportedness

Take A=(3/5,3/5), B=(0,1), C=(1,0), minimising both coordinates. All three points are nondominated; A is unsupported because for any normalised weights at least one of B,C has score at most 1/2, while A has score 3/5.

Apply the strictly increasing transformation x→x³ to each coordinate. Every pairwise dominance relation is preserved. Yet A becomes (27/125,27/125), and weights (1/2,1/2) give it score 27/125 < 1/2, so it is supported. This elementary constructed counterexample is independent of the cited papers. Therefore, a dominance-preserving objective-reduction theorem cannot automatically establish the SICOMP predicate.

## Scope of any proposed new result

The strongest defensible research direction is to make reduction a proof-carrying transformation: specify the mapping and legal-domain correspondence; prove preservation of nondominance and full scalarisation support including ties/axis weights; prove both directions of every compatible completion; preserve the query alphabet, order and publicly known costs; then derive identical positive certificates and comparator costs. Establish which assumptions are classical geometric structure and which statement actually adds the paid observation model.

A universal n→2 result for arbitrary objectives is not supported by the literature inspected. The available work makes redundancy, approximation error, ordering cones, essential objectives or sampling assumptions explicit. Nor does absence of an exact matching prefix theorem from this bounded search establish its novelty.
