#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from functools import lru_cache

rules, msgs = [], []
fill = rules
for l in fileinput.input():
    line = l.strip()
    if line == '8: 42': line = '8: 42 | 42 8'
    if line == "": fill = msgs
    else: fill.append(line)

g = defaultdict(list)
for r in rules:
    n, conds = r.split(': ')
    n = int(n)
    if '"' in conds:
        char = conds.replace('"', '')
        g[n].append(char)
    elif '|' in conds:
        left, right = conds.split(' | ')
        g[n].append(list(map(int, left.split())))
        g[n].append(list(map(int, right.split())))
        assert len(g[n][0]) in {1, 2}
        assert len(g[n][1]) in {1, 2}
    else:
        conds = list(map(int, conds.split()))
        assert len(conds) in {1, 2}
        g[n].append(conds)

# replace '11: 42 31' with '11: 42 31 | 42 11 31'
g[11].append([42, 2020])
g[2020] = [[11, 31]]

def splitvalid(m, c):
    if len(c) == 1:
        return valid(m, c[0])
    a, b = c
    left = False
    for i in range(1, len(m)):
        left = left or (valid(m[:i], a) and valid(m[i:], b))
    return left

@lru_cache(maxsize=None)
def valid(m, n=0):
    conds = g[n]
    if len(conds) == 1 and len(conds[0]) == 1:
        a = conds[0][0]
        if f'{a}'.isdigit(): return valid(m, a)
        if len(m) != 1: return False
        return m == a
    if len(conds) == 1:
        a, b = conds[0]
        return splitvalid(m, [a, b])
    a = conds[0]
    c = conds[1]
    return splitvalid(m, a) or splitvalid(m, c)

print([valid(m) for m in msgs].count(True))
