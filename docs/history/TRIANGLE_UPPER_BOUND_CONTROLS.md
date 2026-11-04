[Documentation index](../README.md)

<a name="heading-history-triangle_upper_bound_controls-historical-triangle-controls-and-adverse-arguments"></a>


# Historical triangle controls and adverse arguments
> Rights: this is manuscript-derived material. Existing manuscript/supplement rights are reserved; moving it under `docs/` does not grant the companion's CC BY documentation licence. Existing component terms govern this reading view.

These are retained P61 mathematical records, not new results or new executions. Current candidate-census and mixed-policy proofs remain in the Essential Supplement, Section S6, read with main Theorems 19 and 20. Successful historical bounds and unsuccessful arguments are retained together.

The historical 873/800 polynomial alias **(C11f)** is distinct from the current candidate-census low-branch polynomial **(C11f)**. Its stable identity here is `historical-873-800`; the current identity is main-Theorem-19/Section-S6.1. Do not infer identity from the printed equation label alone. References to Section S6.1 for the common cube variables use main equation (C11e), whose definitions and domain proof remain authoritative.

<a name="historical-35-32"></a>

<a name="heading-history-triangle_upper_bound_controls-earlier-35-32-certificate"></a>

**Current reader role:** Historical mathematical bounds, unsuccessful arguments and adverse controls; complete retained context outside the central proof route.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


## Earlier 35/32 certificate
P61 supplement lines 1076–1123; exact-extract SHA-256 `8926818e3aaadb9cfcfcbf64f5c0ed3525a06a66e548e7ad603d37404a5142c8`.

The earlier rule uses the two complete continuations and notation of main Section 6, but chooses southeast first with probability

$$
p(G)=\frac{2G}{1+G}.
$$

Set $e=3/32$. The required excess inequality is equivalent to

<a name="historical-35-32-eq-c10"></a>

**Equation (C10).**

$$
A(G)U+B(G)V\le D(G,t),
$$
$$
A(G)=1+e+(e-1)G,\quad
B(G)=e+(2+e)G,\quad
D(G,t)=e(3+t)(1+G).
$$

Here $A(G)>0$ and both sides are affine in $G$, so $G_0=g$ and $G_1=g+t$ suffice. Use the cube parameterisation (C11e) in Section S6.1, with $t=g(1-g)z$ and $H,E,J,U_n,V_n$ as defined there. Its derivation from (C9), coverage of every legal state and the bounds $H,E\ge1$ are unchanged by this mixing rule. It therefore suffices to prove nonnegativity of the two explicit polynomials

<a name="historical-35-32-eq-c11"></a>

**Equation (C11).**

$$
P_j=D(G_j,t)HE-A(G_j)gHU_n-B(G_j)(1-g)V_nE,
\qquad j=0,1.
$$

Their multidegrees are $(5,3,2)$ and $(6,4,2)$. The following exact Bernstein certificate covers the full cube. After affine rescaling of each box, every coefficient at the stated multidegree is at least the displayed positive minimum.

Table S6. Positive Bernstein coefficient minima for the earlier 35/32 certificate.

| Polynomial | $g$ interval | $z$ interval | $w$ interval | Minimum coefficient |
|---|---|---|---|---|
| $P_0$ | $[0,1/2]$ | $[0,1/2]$ | $[0,1/2]$ | $1409/20480$ |
| $P_0$ | $[0,1/2]$ | $[0,1/2]$ | $[1/2,1]$ | $969/20480$ |
| $P_0$ | $[0,1/2]$ | $[1/2,1]$ | $[0,1]$ | $143/15360$ |
| $P_0$ | $[1/2,1]$ | $[0,1]$ | $[0,1]$ | $27/1024$ |
| $P_1$ | $[0,1/2]$ | $[0,1/2]$ | $[0,1]$ | $1/128$ |
| $P_1$ | $[0,1/2]$ | $[1/2,1]$ | $[0,1/2]$ | $53/2048$ |
| $P_1$ | $[0,1/4]$ | $[1/2,1]$ | $[1/2,1]$ | $86967/1048576$ |
| $P_1$ | $[1/4,1/2]$ | $[1/2,3/4]$ | $[1/2,1]$ | $2261/3145728$ |
| $P_1$ | $[1/4,1/2]$ | $[3/4,1]$ | $[1/2,1]$ | $725/1572864$ |
| $P_1$ | $[1/2,1]$ | $[0,1/2]$ | $[0,1]$ | $7/128$ |
| $P_1$ | $[1/2,1]$ | $[1/2,1]$ | $[0,1]$ | $9/1024$ |

Apply the exact power-to-Bernstein conversion stated and proved sufficient in Section S6.1. Tensor Bernstein basis functions are nonnegative and sum to one. The 4 and 7 leaves thus prove positivity at every real point, rather than at sampled grid points. Exact rational arithmetic verifies 288 and 735 leaf coefficients, respectively. Equations (C10)–(C11) prove the randomised upper for every certificate and hence the optimum comparator. This is a computer-assisted polynomial proof step, not proof-assistant verification. Common setup preserves either upper because $F+RC^*\le R(F+C^*)$ for $R\ge1$.

Thus the rule has uniform ratio at most $35/32$ for every archive length, including common setup and endpoint-containing subdomains. The later $873/800$ bound uses a different rule and improves this constant by $1/400$. Both are retained controls for their original rules. Main Theorem 19 gives $12/11$ within the candidate-census class; the unrestricted mixture in Main Theorem 20 improves the upper bound to $87/80$.


<a name="historical-873-800"></a>

<a name="heading-history-triangle_upper_bound_controls-earlier-873-800-certificate"></a>


## Earlier 873/800 certificate
P61 supplement lines 1126–1202; exact-extract SHA-256 `f2028e83539e887f4716c9f0c168b3cdeb9690fc16c1e835443e0ba064345ad8`.

The earlier uniform bound $873/800$ uses $p_{\mathrm{old}}(G)=5G/(4+G)$ throughout $[0,1]$. This rule and its certificate are retained unchanged as a separate control. The candidate-census piecewise rule in main Theorem 19 improves this upper to $12/11$ and uses a different certificate. Main Theorem 20 uses an additional rival-first branch to obtain $87/80$. To state the earlier polynomial independently, put $e=73/800$ and

$$
\begin{aligned}
A_{\mathrm{old}}(G)&=4(1+e)+(e-4)G,\\
B_{\mathrm{old}}(G)&=4e+(5+e)G,\\
D_{\mathrm{old}}(G,t)&=e(3+t)(4+G).
\end{aligned}
$$

Use $t=g(1-g)z$ and $H,E,U_n,V_n$ from (C11e), and let $G_0=g$, $G_1=g+t$. The old certificate polynomials are

$$
P_j^{\mathrm{old}}=D_{\mathrm{old}}(G_j,t)HE
-A_{\mathrm{old}}(G_j)gHU_n
-B_{\mathrm{old}}(G_j)(1-g)V_nE,\qquad j=0,1.
$$

They are the former (C11f) of the $873/800$ proof, not the current low-branch polynomial carrying that equation tag. The coefficient of $U$ is positive on $[0,1]$, and the desired excess inequality is affine in $G$, so the two endpoints suffice. The parametrisation and positivity of its denominators are proved in Section S6.1. Table S7 gives the complete earlier certificate data.

A binary path starts from $[0,1]^3$ and bisects coordinates cyclically in the order $g,z,w$. A bit $0$ selects the lower closed half and a bit $1$ the upper closed half. Each polynomial's paths are prefix-free and their volumes sum to one. Each listed minimum is taken after affine rescaling of its box and conversion to tensor Bernstein form at multidegree $(5,3,2)$ for $P_0$ or $(6,4,2)$ for $P_1$. The displayed positive minima prove positivity over the full boxes, not only at sampled points.

Table S7. Retained dyadic boxes and exact minimum Bernstein coefficients for $P_j^{\mathrm{old}}$, with $e=73/800$.

| Polynomial | Binary path | Minimum coefficient |
|---|---|---|
| $P_0$ | `0000` | $4238153/6553600$ |
| $P_0$ | `000100` | $19/512$ |
| $P_0$ | `000101` | $3017/51200$ |
| $P_0$ | `00011` | $2061/65536$ |
| $P_0$ | `001` | $28031/256000$ |
| $P_0$ | `01` | $513/64000$ |
| $P_0$ | `100000` | $421/32000$ |
| $P_0$ | `100001` | $11873/256000$ |
| $P_0$ | `10001` | $102459/3276800$ |
| $P_0$ | `1001` | $4111/5120$ |
| $P_0$ | `101` | $31501/204800$ |
| $P_0$ | `11` | $243/25600$ |
| $P_1$ | `0000` | $32507251/52428800$ |
| $P_1$ | `000100` | $19/512$ |
| $P_1$ | `000101` | $3017/51200$ |
| $P_1$ | `00011` | $268663/1228800$ |
| $P_1$ | `001` | $88499/819200$ |
| $P_1$ | `010` | $447/51200$ |
| $P_1$ | `0110` | $4525839/13107200$ |
| $P_1$ | `01110` | $754711/39321600$ |
| $P_1$ | `011110` | $12517/1638400$ |
| $P_1$ | `0111110` | $224037189/2684354560$ |
| $P_1$ | `011111100` | $73866983/5033164800$ |
| $P_1$ | `0111111010` | $456427799763/27487790694400$ |
| $P_1$ | `0111111011` | $248807909/201326592000$ |
| $P_1$ | `011111110` | $2247089/419430400$ |
| $P_1$ | `0111111110` | $959632722423/54975581388800$ |
| $P_1$ | `011111111100` | $118829785223/25769803776000$ |
| $P_1$ | `0111111111010` | $24541080492807/14073748835532800$ |
| $P_1$ | `01111111110110` | $5556089682873/17592186044416000$ |
| $P_1$ | `011111111101110` | $51939075801207/17592186044416000$ |
| $P_1$ | `0111111111011110` | $6258026305114877/14411518807585587200$ |
| $P_1$ | `0111111111011111` | $7189481816377647/14411518807585587200$ |
| $P_1$ | `011111111110` | $2030978893/429496729600$ |
| $P_1$ | `0111111111110` | $53056201722667/11258999068426240$ |
| $P_1$ | `0111111111111` | $3064076023/4294967296000$ |
| $P_1$ | `100000` | $439/25600$ |
| $P_1$ | `100001` | $1489/30720$ |
| $P_1$ | `10001` | $135117/524288$ |
| $P_1$ | `1001` | $4111/5120$ |
| $P_1$ | `101` | $2477/12800$ |
| $P_1$ | `110` | $513/51200$ |
| $P_1$ | `11100` | $31361/524288$ |
| $P_1$ | `111010` | $513/51200$ |
| $P_1$ | `11101100` | $2057097/209715200$ |
| $P_1$ | `11101101` | $1819/1966080$ |
| $P_1$ | `1110111` | $48406839/209715200$ |
| $P_1$ | `1111` | $685167/655360$ |

There are 12 boxes and 864 coefficients for $P_0$, and 36 boxes and 3,780 coefficients for $P_1$. The smallest coefficients are respectively $513/64000$ and $5556089682873/17592186044416000$. The exact program `check_improved_upper.py` constructs the expanded polynomials and the certificates by rational arithmetic and dyadic subdivision. The separately implemented `check_improved_upper_independent.py` evaluates the unexpanded formula at rational tensor nodes on each box, inverts Bernstein collocation matrices and recovers all 4,644 coefficients. It also checks the box partition and the exact minimum on each box. The executable results are preserved in `Improved_Upper_Exact_Certificate.json` and `Improved_Upper_Independent_Check.json`.


<a name="adverse-9-8"></a>

<a name="heading-history-triangle_upper_bound_controls-unsuccessful-9-8-threshold-argument"></a>


## Unsuccessful 9/8 threshold argument
P61 supplement lines 1205–1212; exact-extract SHA-256 `0359019fc8dc4e778bd8d9c5f681e8c1cabbd71853f73734729075aacb5b2fc2`.

A simpler threshold $1/3$ does not prove the stronger attempted $9/8$ bound when candidate-partial certificates are admitted. The necessary-inequality relaxation permits

$$
t=1/20,\quad g=29/100,\quad s=0,\quad r=29/100,\quad G=g+t,
$$

which satisfies (C9), yet gives $(t+r)/(3-t-s-r)=17/133>1/8$ in the southeast-first excess envelope. This is a failure of that upper-bound argument, not a counterexample to every possible $9/8$ policy or a claim that every envelope is attained by its policy. The optimised threshold in main Section 6 includes candidate-partial comparators.


<a name="adverse-131-120"></a>

<a name="heading-history-triangle_upper_bound_controls-unsuccessful-131-120-envelope"></a>


## Unsuccessful 131/120 envelope
P61 supplement lines 1246–1262; exact-extract SHA-256 `f6a3bd69e5d59588499129c9f7dee3e6431f7394e2c3817155a661682ff9fd52`.

A separate exact control rules out one plausible parameter choice for a proposed upper bound. The rule $p(G)=6G/(5+G)$ does not prove $131/120$ through (C8)–(C9). Take

$$
g=G=\frac{13}{25},\qquad t=0,\qquad
U=\frac{337993}{700000},\qquad V=\frac4{125}.
$$

Its feasibility determinant is $7/1562500>0$ and $p(G)=13/23$. The excess envelope is

$$
\frac{1223710}{13336987}
=\frac{11}{120}+\frac{138343}{1600438440}
>\frac{11}{120}.
$$

This is a failure of that proposed envelope bound, not a lower bound on every policy or on the rule's realised worst-case cost.


<a name="candidate-tariff-controls"></a>

<a name="heading-history-triangle_upper_bound_controls-full-candidate-and-tariff-controls"></a>


## Full-candidate and tariff controls
P61 supplement lines 1265–1272; exact-extract SHA-256 `25e6c241233fb1683c34dab53f659b9b2ea467c7c882589477386c4baa2b3440`.

Main Theorem 17 and Corollary 18 state the realised full-candidate obstruction and the necessary partial-observation probability. Section S2.7 gives equations (C11g)–(C11j), the complete proof, the all-$N$ padding argument and the positive-price extension, which yields

$$
\mathbb E C_{\mathcal A}(\mathrm U)\ge W+Y+X\Pr\{\text{candidate fully read at TRUE}\}.
$$

In its $N=12$ tariff control, pricing the final candidate row at $M>0$ and all other rows at one leaves a TRUE certificate of cost $34$ while any candidate-census certificate costs at least $34+M$. These are restrictions on a specified policy class, not a stronger unrestricted randomised lower bound. The current checker `checks/candidate/check_candidate_census_obstruction.py` reconstructs the rows and independently tests scalarisation-weight intervals on 332,235 prefixes in seven declared finite instances. It retains the nonpositive $q=1$ control and computes both continuation costs. The general statements follow from the analytic proof in Section S2.7.


