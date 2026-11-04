<a name="heading-research_notes-triangle_finite_extensions_complete-complete-secondary-finite-triangle-classifications"></a>

# Complete secondary finite-triangle classifications
> Rights: manuscript-derived text retains its existing rights. No new licence is granted by routing it to Markdown.

[Documentation index](../README.md)

This is a complete retained mathematical research note from the audited P61 source. The essential review supplement identifies the results used by the article; the additional results below are preserved as secondary research material. Historical identifiers are retained and are qualified by this note.

**Current reader role:** Complete finite-triangle research note; the five-row proof used by Figure 2 remains in the core supplement, while the further classifications are secondary.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.

<a name="supp-s2"></a>

## S2. Band, triangle and fixed-alphabet proofs
Write $\mathcal T=\mathcal T_1=\{(c,f):0\le f\le c\le1\}$. The endpoint test is proved in main Section 2. For candidate, northwest and southeast prefix lengths $(a,i,j)$, put $t=1-a/N$, $s=1-i/N$ and $r=1-j/N$. The specialisation of the band feasibility theorem in main Section 4 is

$$
1-s-2r-2t>0,\qquad
(1-s-2r-2t)^2>4(s+t)(r+t).
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c1"></a>

Equation (C1).

In particular, every TRUE certificate has $a>3N/4$. These statements retain independent whole-row completions and attainable endpoints.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-1-the-four-row-triangle"></a>

### S2.1. The four-row triangle
At $K=3,N=4,d=1$, the first supercritical interval theorem in main Section 4 gives the exact unit-price ratios $23/22$ randomised and $12/11$ deterministic. Its general tariff and common-setup formulas are stated there; Section S2.6.4 supplies the complete fixed two-world lower proof and upper policies. The historical checks `legacy/p21/review/check_triangle_n4_worlds.py` and `legacy/p21/theory/check_triangle_extension.py` corroborate their declared finite instances; both are executed by the optional historical replay in Section S9.


<a name="heading-research_notes-triangle_finite_extensions_complete-s2-2-exact-five-record-acquisition-on-the-full-triangle"></a>

### S2.2. Exact five-record acquisition on the full triangle
The next result treats $d=1,N=5$, where a certificate may leave the candidate partial.

**Theorem S2.** For $K=3$ and five unit-price records per configuration in $\mathcal T_1$, with finite common setup $F\geq0$,

$$
R_{\mathrm{rand},1}^*(3,5;F)=1+\frac4{5F+67},
\qquad
R_{\mathrm{det},1}^*(3,5;F)=1+\frac1{F+14}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-1"></a>

Equation (B6.1).

The zero-setup values are $71/67$ and $15/14$.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-2-1-feasible-shapes-and-a-complete-upper-policy"></a>

#### S2.2.1. Feasible shapes and a complete upper policy
For these parameters, (B2.2) becomes $Z>0$ and $Z^2>4(10-a-i)(10-a-j)$, where $Z=i+2j+2a-20$. Its componentwise minimal feasible shapes are exactly

$$
(4,5,5),\qquad(5,1,5),\qquad(5,5,3).
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-2"></a>

Equation (B6.2).

The candidate law gives $a\geq4$. At $a=4$, both rivals must be full: the maximal alternatives $(4,4,5)$ and $(4,5,4)$ have respective determinant comparisons $4<8$ and $1<8$, so every smaller shape fails as well. At $a=5$, the maximal shape with both rivals partial, $(5,4,4)$, gives $4=4$, attaining equality rather than strict feasibility. With $j=5$, the criterion reduces to $i>0$; with $i=5$, it reduces to $2j-5>0$, hence $j>5/2$. This proves the classification without treating finite enumeration as the argument. Every certificate costs at least 11, and the only candidate-partial certificate has shape $(4,5,5)$ and cost 14.

Policy A first censuses the candidate. Write $g=p_c-p_f$. A partial northwest prefix of length $i$ requires $g>1-i/5$, while a partial southeast prefix of length $j$ requires $g<2j/5-1$. First-safe screening is compulsory within every candidate-census certificate and identifies opposite crossing sides on positive archives. Degenerate or negative cases use full census.

For $g\leq1/5$, complete the compulsory northwest rival and extend the other until TRUE. For $g\geq3/5$, complete the compulsory southeast rival instead. These exterior policies attain the componentwise minimum candidate-census certificate.

For $1/5<g\leq2/5$, both rival prefixes are at least four. Directly acquire the compulsory cost-13 base $(5,4,4)$, which cannot be TRUE. Reveal the two remaining records in fair random order, stopping after the first if possible. Every cost-14 candidate-census certificate then costs at most $29/2$ in expectation.

For $2/5<g<3/5$, screen and raise northwest and southeast prefixes to at least three and four. If screening already censuses a rival, its census is compulsory and extending the other yields an exact certificate. Otherwise choose northwest-first with probability $1/4$ and southeast-first with probability $3/4$. Complete the chosen rival, test TRUE and extend the other only as needed. No feasible state with both rivals partial is skipped. A cost-13 certificate must be $(5,3,5)$; the two orders cost at most 15 and 13, giving expectation $27/2$. Cost-14 shapes $(5,4,5)$ and $(5,5,4)$ give bounds $57/4$ and $59/4$, respectively. Compulsory screening can only improve these bounds.

Policy B acquires four candidate records and both rivals fully, tests TRUE at cost 14 and otherwise takes the candidate's last record. Both policies are complete on negative inputs. Let $C$ be minimum row cost, excluding setup. Their exhaustive cost envelopes are:

Table S3. Five-row triangle policy bounds by cheapest certificate class.

| Cheapest certificate class | Policy A bound | Policy B bound |
|---|---:|---:|
| $C=11$ | 11 | 15 |
| $C=12$ | 12 | 15 |
| $C=13$ | $27/2$ | 15 |
| $C=14$, no candidate-partial certificate | $59/4$ | 15 |
| $C=14$, candidate-partial certificate exists | 15 | 14 |
| $C=15$ | 15 | 15 |

The first two classes force northwest lengths one or two, hence $g>3/5$ and exact exterior acquisition. If a cheaper candidate-census certificate coexists with $(4,5,5)$, using 15 for B is conservative. Choose A before observations with probability

$$
p_A=\frac{4(F+14)}{5F+67},\qquad
1-p_A=\frac{F+11}{5F+67}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-3"></a>

Equation (B6.3).

For each row of the table, with bounds $A,B$, the target overhead minus the mixture overhead, multiplied by $5F+67$, is

$$
4(F+C)-(5F+67)(B-C)-4(F+14)(A-B).
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-4"></a>

Equation (B6.4).

In table order these expressions are $0,F+15,2,3,0,4F+60$. All are nonnegative for every $F\geq0$, establishing the global randomised upper. For a deterministic upper use A, choose either tail first in the symmetric interior and always southeast first in the asymmetric interior. Every $C\leq13$ archive is acquired exactly, every $C=14$ archive costs at most 15, and census costs 15. This proves the upper $1+1/(F+14)$.

The separate candidate-partial row of the table is essential. Policy A deliberately pays for candidate census, while its retrospective competitor may stop after four candidate records. The cost-15 bound in that row accounts for this discrepancy rather than comparing A only with the best certificate that also censuses the candidate. Policy B restores the necessary balance. The mixture is chosen once before observations using the public setup price; the six affine residuals prove the bound for the entire continuum $F\geq0$, not just for setup values sampled during computational checking.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-2-2-fixed-archives-matching-both-upper-bounds"></a>

#### S2.2.2. Fixed archives matching both upper bounds
Both worlds share candidate records 1–4 equal to $(79/80,1/8)$, northwest record 1 equal to $(51/100,51/100)$, northwest records 2–4 equal to $(13/50,13/50)$, and all southeast records equal to $(1,0)$. Their terminal records and exact certificate sets are:

Table S4. Five-row hard archives and their complete TRUE-prefix sets.

| World | Candidate tail | Northwest tail | TRUE-prefix set | Minimum cost |
|---|---|---|---|---:|
| A | $(0,0)$ | $(13/50,13/50)$ | $(4,5,5),(5,5,5)$ | 14 |
| B | $(1,0)$ | $(1,1)$ | $(5,i,5)$, $1\leq i\leq5$ | 11 |

The candidate lower corner after four records is $(79/100,1/10)$, and its upper corner is $(99/100,3/10)$. The candidate law excludes shorter prefixes. In A, an incomplete southeast upper corner has failure at least $1/5$, while northwest upper failures are at least $31/100$; the failure axis therefore prevents TRUE until southeast census. Every northwest prefix at most four has upper coordinate sum at least $229/250>89/100$, while complete southeast sum is one. Equal weights prevent TRUE until northwest census.

At $(4,5,5)$, northwest failure $31/100>3/10$ and southeast cost $1>99/100$ ensure robust nondomination. Weight $5/16$ on the complete northwest point gives the rival mixture

$$
(251/320,31/320)<(79/100,1/10)
\qquad\text{coordinatewise}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-5"></a>

Equation (B6.5).

Thus this state is TRUE, as is its full-candidate extension; A's entire list follows.

In B, even complete rivals support the four-record candidate lower corner at equal weights, so candidate census is compulsory. Southeast census is compulsory by the same failure-axis argument, and an unread northwest rival is domination-unsafe. At $(5,1,5)$, northwest lower failure $51/500>1/10$ and southeast cost $1>99/100$ ensure safety. Northwest upper corner is $(451/500,451/500)$. Weight $21/200$ on it gives the mixture

$$
(98971/100000,9471/100000)<(99/100,1/10)
\qquad\text{coordinatewise}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-6"></a>

Equation (B6.6).

Monotonicity proves B's whole list.

The worlds agree until candidate record 5 or northwest record 5 is disclosed. Let $q$ be the common probability that the candidate terminal is reached first. Almost-sure soundness forces a TRUE certificate on these positive inputs. Every valid algorithm therefore has expected row costs at least $14+q$ in A and $15-4q$ in B. These bounds allow arbitrary adaptive interleaving: reaching the northwest terminal first requires all four northwest records beyond its compulsory first one. Including setup and balancing gives

$$
q=\frac{4(F+14)}{5F+67},\qquad
\max\left\{\frac{F+14+q}{F+14},
\frac{F+15-4q}{F+11}\right\}
\geq1+\frac4{5F+67}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-b6-7"></a>

Equation (B6.7).

A deterministic first choice gives lower $1+1/(F+14)$. Together with the complete upper policies, this proves Theorem S2.

All records belong to a six-symbol alphabet containing both endpoints. The endpoint lemma preserves these exact TRUE sets on that known independent alphabet, while the full-triangle upper policies remain valid. Both exact ratios consequently also hold on that alphabet and the uniform $1/400$ triangular grid. This does not assert minimum alphabet cardinality; the separate three-symbol theorem has a different first nonempty-length behaviour.

For arbitrary unequal row prices, let $W$ include setup, candidate records 1–4, northwest record 1 and every southeast record; let $x$ price the candidate terminal and $y$ be the total price of northwest records 2–5. The comparators are $W+y$ and $W+x$. The same two-world argument yields lower bounds of the form (B4.7), but no matching global unequal-price theorem at $N=5$ is asserted.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-3-a-smallest-possible-observation-alphabet"></a>

### S2.3. A smallest possible observation alphabet
Let the common public row domain be

$$
\mathcal S=\{(0,0),(1,0),(1,1)\}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c2"></a>

Equation (C2).

**Theorem S3.** No common alphabet with fewer than three vectors admits a GOOD instance in two objectives. For the particular alphabet (C2), positive instances with common row count $N$ and any $K\ge3$ configurations exist exactly when $N\ge5$. At $K=3,N=5$, every positive archive requires full census, so both competitive optima equal one for arbitrary public positive row prices and common setup.

With two symbols $x,y$, every mean lies on their segment. If $y-x$ has opposite-sign components, a positive normal makes every mean tie. A zero component gives an axis normal. If both components have the same strict sign, orient the segment positively: every mean above the smallest realised segment parameter is dominated, and the smallest is supported. One symbol is immediate. This proves cardinality minimality without assigning a ratio to the empty smaller classes.

For (C2), every mean is $(m/N,n/N)$ with integers $0\le n\le m\le N$. A GOOD candidate requires a strictly northwest and a strictly southeast rival. The latter requires $n\ge1$ and $m\le N-1$; the former has integer coordinates satisfying $n+1\le y\le x\le m-1$, hence $m-n\ge2$. No $N\le3$ qualifies. At $N=4$ only candidate numerator $(3,1)$ remains, with possible strict crossing witnesses $(2,2)$ and $(4,0)$. Equal weights support them. Every other nondominating rival also has coordinate sum at least four, so additional configurations cannot remove that support.

At $N=5$, candidate numerator $(4,1)$ and rivals $(2,2),(5,0)$ are nondominated, while their mixture with northwest weight $2/5$ is $(19/5,4/5)<(4,1)$. These numerators are realised by rows from (C2). Zero padding gives every larger $N$ by positive common scaling; extra all-$(1,1)$ configurations permit every $K\ge3$.

For the exact five-row statement, the only possible candidate numerators are $(3,1),(4,1),(4,2)$. The first has no strict witness pair. For $(4,1)$, the southeast point must be $(5,0)$, and a northwest $(x,y)$ gives determinant $5-x-y$; only $(2,2)$ is strictly feasible. For $(4,2)$, the northwest point must be $(3,3)$, and a southeast $(5,r)$ gives determinant $1-r$; only $r=0$ works. Thus the only positive triples, up to exchanging rival labels, are

$$
((4,1),(2,2),(5,0)),\qquad
((4,2),(3,3),(5,0)).
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c3"></a>

Equation (C3).

Every proper prefix is below a state with exactly one final row unread. Omitting the southeast final $(1,0)$ gives lower corner $(4,0)$, which dominates the candidate. Omitting a northwest $(1,1)$ gives lower corner $(1,1)$ or $(2,2)$ and again domination; omitting a northwest zero gives upper corner $(3,3)$ or $(4,4)$ and support by weights $(1,1)$ or $(1,0)$, respectively. A candidate final zero or $(1,0)$ makes its upper corner dominated by the northwest point; a candidate final $(1,1)$ leaves lower corner $(3,0)$ or $(3,1)$, supported by $(0,1)$ or $(1,1)$. These exhaust the feasible symbols. Full census is therefore the only TRUE prefix, regardless of row order or positive prices. This differs from the continuous triangle's five-row values $71/67$ and $15/14$, because the public input class changes.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-4-six-rows-a-deterministic-optimum-and-a-randomised-interval"></a>

### S2.4. Six rows: a deterministic optimum and a randomised interval
**Theorem S4.** On the continuous triangle at $N=6$,

$$
R_{\mathrm{det}}^*(3,6;F)=1+\frac1{F+16},\qquad
R_{\mathrm{rand}}^*(3,6;F)\ge1+\frac5{6F+98}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c12"></a>

Equation (C12).

The deterministic policy also bounds the randomised optimum above. At zero setup the interval is therefore $103/98\le R_{\mathrm{rand}}^*(3,6)\le17/16$; randomised equality is not claimed.

Equation (C1) gives the componentwise minimal shapes

$$
(5,5,6),\quad(6,1,6),\quad(6,5,5),\quad(6,6,4).
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c13"></a>

Equation (C13).

Indeed $a\ge5$. At $a=5$, $j\le5$ fails even at $i=6$, while $j=6$ requires $i^2>24$. At $a=6$, $j=6$ allows every $i\ge1$; $j=5$ requires $i^2>20$; $j=4$ requires $i^2>32$; $j\le3$ fails. Thus $C^*\ge13$.

Census the candidate, screen safely and choose northwest first if its full gap $G\le1/3$, southeast otherwise. For candidate-census certificates, partial northwest and southeast lengths require $G>1-i/6$ and $G<j/3-1$, respectively. If $C^*\le15$, its shape is $(6,i,6)$ with $i\le3$; the policy chooses southeast and attains $C^*$. At cost 16, candidate-census shapes $(6,4,6)$ and $(6,6,4)$ force the correct order and cost at most 16; shape $(6,5,5)$ costs at most 17 in either order. A candidate-partial cost-16 shape is $(5,5,6)$. Its lower gap satisfies

$$
(g-1/3)(5/6-g)>1/18,
\quad\text{equivalently}\quad 1/2<g<2/3.
$$

The full gap is no smaller, so southeast is selected and the TRUE extension $(6,5,6)$ costs at most 17. Remaining positive archives have $C^*\ge17$ and cost at most 18. This proves the deterministic upper in (C12), including all-input census fallback.

Two pairs of fixed worlds supply the lower bounds. All southeast rows are $(1,0)$. For pair D, the first five candidate rows are $(249/250,3/10)$; northwest rows 1–2 are $(19/25,19/25)$, rows 3–4 are $(7/50,7/50)$ and row 6 is $(1,1)$. For pair Q, the first five candidate rows are $(249/250,3/25)$; northwest row 1 is $(61/100,61/100)$ and rows 2–5 are $(7/25,7/25)$.

Table S5. Six-row hard pairs, exact TRUE prefixes and certificate costs.

| Pair and world | Candidate row 6 | Variable northwest row | Exact TRUE prefixes | $C^*$ |
|---|---|---|---|---|
| D, U | $(0,0)$ | Row 5: $(37/50,37/50)$ | $(a,i,6)$, $a,i\ge5$ | $16$ |
| D, V | $(1,0)$ | Row 5: $(1,1)$ | $(6,i,6)$, $i\ge2$ | $14$ |
| Q, A | $(0,0)$ | Row 6: $(7/25,7/25)$ | $(5,6,6),(6,6,6)$ | $17$ |
| Q, B | $(1,0)$ | Row 6: $(1,1)$ | $(6,i,6)$, $i\ge1$ | $13$ |

For pair D, candidate lower point after five rows is $(83/100,1/4)$. Before northwest row 5, its upper diagonal is at least $19/30>25/42$, where $25/42=p_f/(1-p_c+p_f)$ is the support threshold with southeast $(1,0)$. This forces northwest prefix five in U and candidate census in V. In V, one northwest row dominates the full candidate, forcing prefix two. Southeast prefix five fails: U's determinant with complete northwest is $-189/5000$, while V's southeast lower corner $(5/6,0)$ dominates candidate $(299/300,1/4)$. At the least U state the P2 margins are $1/150,1/300$ and determinant $11/5000$; at the least V state the margins are both $1/300$ and determinant $127/7500$. Monotonicity proves the listed sets. If candidate row 6 precedes northwest row 5 with probability $\theta$, row costs are at least $16+\theta$ and $14+3(1-\theta)$. Deterministic $\theta\in\{0,1\}$ gives the matching lower $1+1/(F+16)$.

For pair Q, candidate lower point is $(83/100,1/10)$. Before the northwest final row its upper diagonal is at least $91/200>10/27$, the corresponding support threshold. Thus A requires northwest census and B candidate census. B needs at least one northwest row, since an unread rival can dominate. Until southeast census, both rival upper failures exceed $1/10$, so the failure axis supports the candidate lower point. At A's least state the northwest mean is $(67/200,67/200)$, P2 is strict and determinant $191/20000>0$. At B's least state the northwest lower and upper points are $(61/600,61/600)$ and $(187/200,187/200)$, with P2 margins $1/600,1/300$ and determinant $203/60000>0$. These checks establish the second exact lists. Candidate-first probability $\theta$ gives row-cost bounds $17+\theta$ and $18-5\theta$. Balancing at $\theta=5(F+17)/(6F+98)$ proves (C12). Arbitrary interleaving is allowed: reaching a decisive northwest row first necessarily buys its preceding rows. The archives are fixed before private coins.

<a name="heading-research_notes-triangle_finite_extensions_complete-s2-5-a-sharp-barrier-within-a-restricted-two-chain-family"></a>

### S2.5. A sharp barrier within a restricted two-chain family
The following ancillary result concerns a precisely specified asymptotic construction family. It does not place a ceiling on the global acquisition problem or provide a global upper policy.

Consider unit row prices, zero setup and a sequence of two fixed-world constructions normalised by their common row count $N$. Assume that the southeast rival is asymptotically fully required with limiting mean $v=(1,0)$. At the common transcript the candidate lower mean tends to $p=(c,f)$ and the northwest upper mean to $u=(\ell,\ell)$, where $0<f<\ell<c<1$ and $p$ lies on the segment $uv$. There are exactly two decisive terminal chains of limiting length fractions $t>0$ for the candidate and $s>0$ for the northwest rival. All earlier revelations agree between the worlds, and terminal perturbations are $o(N)$ in aggregate sums. The candidate chain is unnecessary in one world and the northwest chain in the other. Finally, assume the exact two-chain comparator structure: common base fraction $W=3-t-s$, certificate fractions $W+s=3-t$ and $W+t=3-s$, and no cheaper alternative certificates.

**Theorem S5.** Within this restricted family, the limiting restricted-pair competitive ratios are at most $23/22$ for randomisation and $12/11$ deterministically. Both ceilings are sharp and require the limiting resource skeleton $t=s=1/4$, $\ell=1/2$, $c=3/4$, $f=1/4$.

The observed candidate uses at most $(1-t)N$ rows with cost coordinates at most one, hence $c\le1-t$. In the world stopping without the northwest chain, that rival's lower failure tends to $\ell-s$. Its lower cost is below the candidate's, so robust Pareto safety requires $\ell-s\ge f$ in the limit. Strict finite inequalities may relax to equality; additional nonnegative candidate failure observations can only strengthen this necessary constraint. Collinearity gives

$$
f=\frac{\ell(1-c)}{1-\ell},\qquad
s\le\ell-f=\frac{\ell(c-\ell)}{1-\ell}
\le\frac{\ell(1-t-\ell)}{1-\ell}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c14"></a>

Equation (C14).

Equivalently, $s/\ell+t/(1-\ell)\le1$. Weighted Cauchy–Schwarz therefore yields

$$
(\sqrt{s}+\sqrt{t})^2
\le\frac{s}{\ell}+\frac{t}{1-\ell}\le1.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c15"></a>

Equation (C15).

Under the assumed exact comparator structure, the restricted-pair randomised excess is

$$
\frac{ts}{t(3-s)+s(3-t)}
=\frac1{3(1/t+1/s)-2}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c16"></a>

Equation (C16).

Writing $a=\sqrt t$, $b=\sqrt s$, (C15) gives $a+b\le1$ and
$1/t+1/s=1/a^2+1/b^2\ge8/(a+b)^2\ge8$. For example, the first inequality follows from $(a+b)^2(a^2+b^2)-8a^2b^2=(a-b)^2(a^2+4ab+b^2)\ge0$. Thus (C16) is at most $1/22$. The deterministic excess is

$$
\frac{\min(t,s)}{3-\min(t,s)}
\le\frac{1/4}{3-1/4}=\frac1{11}.
$$

<a name="eq-research_notes-triangle_finite_extensions_complete-c17"></a>

Equation (C17).

Equality requires $t=s=1/4$. Equality in (C15) then requires $\ell=1/2$, and the resource and collinearity equalities give $c=3/4$, $f=1/4$. The binary-coordinate construction in main Section 5, proved fully in Section S2.7, approaches this skeleton and attains both limiting restricted-pair ratios, establishing sharpness within the stated family.

The assumptions exclude arbitrary multiworld constructions, noncollinear limiting states, different southeast behaviour, more configurations and nonuniform prices. A stronger global lower bound could use a different construction. This barrier explains why changing only the block proportions of the present collinear family cannot improve its asymptotic constants; it is not global optimality.

