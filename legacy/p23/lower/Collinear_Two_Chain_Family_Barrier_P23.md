# A sharp barrier for the collinear candidate–northwest two-chain family

P23 ancillary research note, 23 October 2026.

This is a restricted-family theorem. It does not establish global optimality
of 23/22 or 12/11 for the full acquisition problem. Its purpose is to show
why tuning the existing construction's block proportions cannot improve
those asymptotic constants under the stated skeleton.

## 1. Precisely restricted setting

Consider a sequence of two-world constructions with unit row prices and
zero common setup, normalised by their common row count N. Suppose:

* The southeast rival is asymptotically fully required and has limiting
  upper/complete mean v=(1,0).
* At the shared transcript, the candidate lower mean tends to p=(c,f)
  and the northwest upper mean tends to u=(l,l), where
  0<f<l<c<1 and p lies on segment uv.
* There are exactly two decisive terminal chains of limiting length
  fractions t>0 (candidate) and s>0 (northwest). All earlier revelations
  are identical in both worlds. Their terminal perturbations are o(N)
  in aggregate sums, so the limiting collinearity is shared.
* The candidate chain is unnecessary in one world and the northwest
  chain is unnecessary in the other, with the exact two-chain comparator
  structure: common base fraction W=3-t-s and total certificate fractions
  W+s=3-t and W+t=3-s. Other cheaper certificates are absent.

The P23 three-symbol construction and P22 five-symbol construction satisfy
these assumptions in their N->infinity limits. The assumptions do not
cover arbitrary multiworld constructions, noncollinear limiting states,
different southeast behaviour, more configurations or nonuniform prices.

## 2. Necessary resource inequality

The observed candidate has at most (1-t)N rows and every cost coordinate is
at most one. Thus c<=1-t in the limit. The northwest upper corner has
failure l; with a remaining fraction s its lower failure is l-s. In the
world that stops without its chain, robust Pareto safety requires
l-s>=f in the limit. (Strict finite inequalities may relax to equality.)
Since the northwest lower corner is diagonal and below the candidate in
cost, failure separation is necessary; coordinate equality at the limit
does not invalidate the weak necessary inequality.

Collinearity gives

    f = l(1-c)/(1-l).

Therefore

    s <= l-f = l(c-l)/(1-l)
      <= l(1-t-l)/(1-l),

or equivalently

    s/l + t/(1-l) <= 1.

Cauchy–Schwarz yields

    (sqrt(s)+sqrt(t))^2 <= s/l+t/(1-l) <= 1.

This is a necessary inequality for every skeleton in the restricted class.

## 3. Sharp two-chain ratio ceiling

The exact restricted-pair randomised excess is

    E(t,s) = ts/[t(3-s)+s(3-t)]
           = 1/[3(1/t+1/s)-2].

Put a=sqrt(t), b=sqrt(s). Since a+b<=1,

    1/t+1/s = 1/a^2+1/b^2 >= 8/(a+b)^2 >= 8.

The first inequality follows, for example, from
(a+b)^2(a^2+b^2)>=8a^2b^2. Hence E(t,s)<=1/22.

The deterministic excess is

    min(t,s)/(3-min(t,s)) <= (1/4)/(3-1/4) = 1/11,

because a+b<=1 implies min(t,s)<=1/4.

Equality in both bounds requires t=s=1/4; equality in the resource
inequality then gives l=1/2, c=3/4 and f=1/4. The explicit P23 archives
approach exactly these values and attain the limiting restricted-pair
ratios 23/22 and 12/11. Thus these constants are sharp for this limiting
two-chain family.

The result places no ceiling on the full acquisition problem. In particular,
a stronger global lower bound could use a different family. Conversely,
the family barrier supplies no global upper algorithm.

## 4. Scope of verification

The companion standard-library checker evaluates the resource inequalities
and ratio ceilings exactly on a finite rational parameter grid, and checks
the unique equality skeleton. The universal claim follows from the algebra
above. No numerical optimisation output is used as a proof or claimed as
a global maximum.
