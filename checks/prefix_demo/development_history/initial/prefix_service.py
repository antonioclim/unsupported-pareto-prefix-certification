#!/usr/bin/env python3
"""Exact prefix acquisition for the K=N=3 square model; standard library only.
New implementation prepared for Antonio Clim with AI assistance. BSD-3-Clause.
"""
from fractions import Fraction as Q

GROUPS = ('candidate', 'left', 'right')
N = 3

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and a != b

class PrefixService:
    """A local interface model, not a security boundary or deployed service.

    Requests carry only a group: the service chooses the next unpaid position.
    Prices are public, fixed before disclosure and independent of row values.
    """
    def __init__(self, archive, alphabet, prices, setup=Q(0)):
        self.__archive = {g: tuple(tuple(map(Q, r)) for r in archive[g]) for g in GROUPS}
        self.__cursor = dict.fromkeys(GROUPS, 0)
        self.__prices = {g: tuple(map(Q, prices[g])) for g in GROUPS}
        self.__setup = Q(setup)
        require(self.__setup >= 0, 'setup must be nonnegative')
        allowed = {tuple(map(Q, r)) for r in alphabet}
        require((Q(0), Q(0)) in allowed and (Q(1), Q(1)) in allowed,
                'endpoint-containing alphabet required')
        for g in GROUPS:
            require(len(self.__archive[g]) == len(self.__prices[g]) == N, 'three rows required')
            require(all(r in allowed for r in self.__archive[g]), 'row outside public domain')
            require(all(w > 0 for w in self.__prices[g]), 'prices must be positive')
        self.log = []

    def next_row(self, group):
        if group not in GROUPS:
            raise ValueError('unknown group')
        j = self.__cursor[group]
        if j >= N:
            raise ValueError('group exhausted')
        self.__cursor[group] += 1
        row = self.__archive[group][j]
        charge = self.__prices[group][j]
        self.log.append({'group': group, 'index': j + 1, 'row': [str(x) for x in row],
                         'charge': str(charge)})
        return group, j + 1, row, charge

    def bill(self):
        return self.__setup + sum((Q(r['charge']) for r in self.log), Q(0))

class ObservedState:
    """Only disclosed rows, a query callable and public accounting information."""
    def __init__(self, next_row, prices, setup=Q(0)):
        self.__query = next_row
        self.prices = {g: tuple(map(Q, prices[g])) for g in GROUPS}
        self.setup = Q(setup)
        self.rows = {g: [] for g in GROUPS}
        self.log = []

    def counts(self):
        return tuple(len(self.rows[g]) for g in GROUPS)

    def box(self, group):
        low = tuple(sum((r[j] for r in self.rows[group]), Q(0)) / N for j in (0, 1))
        missing = Q(N - len(self.rows[group]), N)
        return low, tuple(x + missing for x in low)

    def p2_safe(self, group):
        return not dominates(self.box(group)[0], self.box('candidate')[1])

    def robust_true(self):
        if any(not self.p2_safe(g) for g in GROUPS[1:]):
            return False
        candidate = self.box('candidate')[0]
        lo, hi = Q(0), Q(1)
        for g in GROUPS[1:]:
            upper = self.box(g)[1]
            dc, df = (upper[j] - candidate[j] for j in (0, 1))
            slope = dc - df
            if slope == 0:
                if df < 0:
                    return True
            elif slope > 0:
                lo = max(lo, -df / slope)
            else:
                hi = min(hi, -df / slope)
        return lo > hi

    def query(self, group, phase):
        g, j, row, charge = self.__query(group)
        require(g == group and j == len(self.rows[g]) + 1, 'non-prefix response')
        require(charge == self.prices[g][j - 1], 'public price mismatch')
        self.rows[g].append(tuple(row))
        self.log.append({'step': len(self.log) + 1, 'group': g, 'index': j,
                         'row': [str(x) for x in row], 'charge': str(charge),
                         'phase': phase, 'prefix': list(self.counts())})

    def finish(self):
        truth = self.robust_true()
        require(truth or self.counts() == (N, N, N), 'FALSE requires census')
        return {'answer': truth, 'prefix': list(self.counts()), 'queries': len(self.log),
                'paid_cost': str(self.setup + sum((Q(x['charge']) for x in self.log), Q(0))),
                'transcript': self.log}

    def fallback(self):
        for g in GROUPS:
            while len(self.rows[g]) < N:
                self.query(g, 'census_fallback')
                if self.robust_true():
                    return self.finish()
        return self.finish()

def policy_a(client, tail_order):
    """Candidate census, compulsory screening, then a fair last-tail order."""
    require(tuple(tail_order) in (('left', 'right'), ('right', 'left')), 'invalid tail order')
    for _ in range(N):
        client.query('candidate', 'candidate_census')
    for g in GROUPS[1:]:
        while len(client.rows[g]) < N and not client.p2_safe(g):
            client.query(g, 'P2_screening')
            if client.robust_true():
                return client.finish()
        if not client.p2_safe(g):
            return client.fallback()
    if client.robust_true():
        return client.finish()
    for g in GROUPS[1:]:
        while len(client.rows[g]) < 2:
            client.query(g, 'raise_rival_to_two')
            if client.robust_true():
                return client.finish()
    for g in tail_order:
        while len(client.rows[g]) < N:
            client.query(g, 'fair_tail_order')
            if client.robust_true():
                return client.finish()
    return client.fallback()

def policy_b(client):
    """Candidate prefix two, both rival censuses, candidate tail if necessary."""
    for g, count in (('candidate', 2), ('left', 3), ('right', 3)):
        while len(client.rows[g]) < count:
            client.query(g, 'candidate_partial_rival_census')
    if client.robust_true():
        return client.finish()
    client.query('candidate', 'candidate_last_if_needed')
    return client.fallback()

BRANCHES = (('A_LR', Q(8, 23), ('left', 'right')),
            ('A_RL', Q(8, 23), ('right', 'left')),
            ('B', Q(7, 23), None))

def run_branch(archive, alphabet, prices, setup, label, order):
    server = PrefixService(archive, alphabet, prices, setup)
    client = ObservedState(server.next_row, prices, setup)
    result = policy_b(client) if label == 'B' else policy_a(client, order)
    require(result['queries'] <= 9, 'query bound violated')
    require(Q(result['paid_cost']) == server.bill(), 'client/server bill mismatch')
    require(len(server.log) == len(result['transcript']), 'transcript length mismatch')
    for s, c in zip(server.log, result['transcript']):
        require(all(s[k] == c[k] for k in ('group', 'index', 'row', 'charge')), 'transcript mismatch')
    return result
