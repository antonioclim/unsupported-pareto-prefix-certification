# Exact finite-corpus best-response control

This English technical note records the finite-corpus method exercised by `scripts/lit_finite_oracle.py`. It is a standard dynamic-programming specialisation to the present certificate problem, not a claim of a new general theorem about search games.

Let the explicit corpus consist of positive archives I_1,...,I_m, with exact realised robust-certificate costs c_i>0 and rational prior probabilities lambda_i. The objective is to minimise the sum of lambda_i C_A(I_i)/c_i over acquisition policies A that remain valid on the whole original completion domain, including negative archives and archives outside the corpus. The corpus is an evaluation distribution; it does not restrict legal completions.

A state consists of the vector of prefix lengths and their observed values. Let H be the set of compatible corpus archives and define M(H)=sum_{i in H} lambda_i/c_i. A state that is robust TRUE on the full completion domain has value zero. Otherwise its continuation value is the minimum, over legal next rows q, of

    price(q) M(H) + sum_z V(state extended by observation z),

where z ranges over the observations of q present in H. Every compatible archive pays for the selected row; its observation partitions H into disjoint classes. Induction in the number of unread rows proves the recurrence. Local randomisation cannot improve the minimum of this linear expectation. If an observation leaves the corpus, full census followed by exact evaluation gives a zero-error terminating fallback on the original domain. A common compulsory setup cost is added separately.

For a fixed prefix-length vector, observed prefix values partition the m corpus members into at most m classes. Histories with the same prefixes have the same remaining legal queries, costs and robust test, so the order used to acquire those observations need not be stored. At most m product_g(n_g+1) states suffice. This is polynomial for a fixed number of configurations and an explicit corpus; it does not make the corpus of all possible archives polynomial-sized.

The executed controls use the manuscript's original two-world triangle family. Exact prefix enumeration computes c_i without assuming the analytic formula, and the best-response dynamic program permits all prefix interleavings. Its results are:

| N | Exact comparator costs | Prior on the two worlds | Exact normalised best response | States |
|---:|---|---|---|---:|
| 12 | 34, 33 | 68/101, 33/101 | 103/101 | 2,522 |
| 16 | 45, 44 | 135/223, 88/223 | 229/223 | 5,474 |
| 20 | 56, 55 | 224/389, 165/389 | 401/389 | 10,122 |
| 24 | 67, 66 | 335/599, 264/599 | 619/599 | 16,850 |

All four reproduce the existing analytic hard-pair values. They do not improve the unrestricted asymptotic lower bound 23/22. A new lower bound would require a verified corpus/prior value exceeding the old bound, or a complete new parametric proof; a floating-point optimisation or grid extrapolation would not suffice.

The broader use of best-response oracles in finite search games is discussed by L. Hellerstein, T. Lidbetter and D. Pirutinsky, “Solving Zero-Sum Games Using Best-Response Oracles with Applications to Search Games,” *Operations Research* 67(3), 731–743 (2019), https://doi.org/10.1287/opre.2019.1853. Primary author text: https://arxiv.org/html/1704.02657v4. The recurrence above is derived explicitly for this project; the cited result does not itself supply its geometric oracle.
