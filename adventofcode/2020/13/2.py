#!/usr/bin/env python3
import fileinput

lines = [l.strip() for l in fileinput.input()]
ids = list(filter(lambda p: p[1] != 'x', enumerate(lines[1].split(','))))
ids = [(int(p[1]), p[0]) for p in ids]

def inv(a, m):
    prod = 1
    for _ in range(m - 2): prod *= a
    return prod % m

M = 1
for i in ids: M *= i[0]

# Convert to
# x = a1modm x = a2modm ...
# and use Chinese remainder theorem
x = 0
for p in ids[1:]:
    m, a = p
    md = M // m
    a *= -1
    while a < 0:
        a += m
    x += a * md * inv(md, m)

print(x % M)