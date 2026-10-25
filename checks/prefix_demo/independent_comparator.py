#!/usr/bin/env python3
"""Direct finite-completion verifier, independent of online corner predicates.

No import from prefix_service. Complete triples are tested at all candidate
supporting-weight breakpoints, not by the online interval intersection routine.
New implementation prepared for Antonio Clim with AI assistance. BSD-3-Clause.
"""
from fractions import Fraction as Q
from itertools import product
from math import lcm

GROUPS = ('candidate', 'left', 'right')


def good_complete(sums):
    """Equal group lengths: integer coordinate sums replace means exactly."""
    candidate, *rivals = sums
    if any(r[0] <= candidate[0] and r[1] <= candidate[1] and r != candidate for r in rivals):
        return False
    differences = [(r[0] - candidate[0], r[1] - candidate[1]) for r in rivals]
    weights = [(0, 1), (1, 1)]
    for dc, df in differences:
        numerator, denominator = -df, dc - df
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        if denominator > 0 and 0 <= numerator <= denominator:
            weights.append((numerator, denominator))
    supported = any(all(den * df + num * (dc - df) >= 0 for dc, df in differences)
                    for num, den in weights)
    return not supported


class CompletionEnumerator:
    def __init__(self, archive, alphabet):
        self.n = len(archive[GROUPS[0]])
        rational_rows = [tuple(map(Q, r)) for r in alphabet]
        if not rational_rows or any(len(r) != 2 or any(q < 0 or q > 1 for q in r) for r in rational_rows):
            raise ValueError('invalid finite square alphabet')
        rational_archive = {g: tuple(tuple(map(Q, r)) for r in archive[g]) for g in GROUPS}
        allowed = set(rational_rows)
        if any(len(rows) != self.n or any(r not in allowed for r in rows) for rows in rational_archive.values()):
            raise ValueError('archive contains an out-of-alphabet row')
        self.scale = lcm(*(q.denominator for r in rational_rows for q in r))
        self.alphabet = tuple(sorted({tuple(int(q * self.scale) for q in r) for r in rational_rows}))
        self.archive = {g: tuple(tuple(int(Q(x) * self.scale) for x in r) for r in archive[g])
                        for g in GROUPS}
        if any(len(rows) != self.n or any(r not in self.alphabet for r in rows)
               for rows in self.archive.values()):
            raise ValueError('illegal archive')
        self.unknown_sums = [((0, 0),)]
        for m in range(1, self.n + 1):
            # Every ordered completion has one of these sums; duplicate sums
            # may be collapsed because the predicate uses only group means.
            self.unknown_sums.append(tuple(sorted({(s[0] + r[0], s[1] + r[1])
                for s in self.unknown_sums[-1] for r in self.alphabet})))
        self.options = {}
        for gi, g in enumerate(GROUPS):
            for b in range(self.n + 1):
                base = tuple(sum(r[j] for r in self.archive[g][:b]) for j in (0, 1))
                self.options[gi, b] = tuple((base[0] + s[0], base[1] + s[1])
                                             for s in self.unknown_sums[self.n - b])

    def prefix_truth(self, prefix):
        choices = [self.options[i, b] for i, b in enumerate(prefix)]
        evaluated = 0
        for sums in product(*choices):
            evaluated += 1
            if not good_complete(sums):
                return False, evaluated, [list(s) for s in sums]
        return True, evaluated, None

    def all_prefixes(self, prices, setup=Q(0)):
        if Q(setup) < 0 or any(len(prices[g]) != self.n or any(Q(w) <= 0 for w in prices[g]) for g in GROUPS):
            raise ValueError('invalid public tariff or setup')
        records = []
        true_records = []
        for prefix in product(range(self.n + 1), repeat=3):
            truth, evaluated, negative_witness = self.prefix_truth(prefix)
            cost = Q(setup) + sum((sum((Q(x) for x in prices[g][:b]), Q(0))
                                 for g, b in zip(GROUPS, prefix)), Q(0))
            record = {'prefix': list(prefix), 'truth': truth, 'cost': str(cost),
                      'complete_sum_triples_examined': evaluated,
                      'negative_witness_sums': negative_witness}
            records.append(record)
            if truth:
                true_records.append(record)
        minimum = min((Q(r['cost']) for r in true_records), default=None)
        return {'comparator_source': 'independent_exhaustive_prefix_and_legal_completion_mean_enumeration',
                'integer_coordinate_scale': self.scale,
                'means_denominator': self.scale * self.n,
                'possible_unobserved_sum_counts': [len(x) for x in self.unknown_sums],
                'prefixes_examined': len(records),
                'complete_sum_triples_examined': sum(r['complete_sum_triples_examined'] for r in records),
                'C_star': None if minimum is None else str(minimum),
                'minimising_prefixes': [r['prefix'] for r in true_records if Q(r['cost']) == minimum],
                'true_prefixes': [r['prefix'] for r in true_records],
                'all_prefixes': records}
