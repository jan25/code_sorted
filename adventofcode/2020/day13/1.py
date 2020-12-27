#!/usr/bin/env python3
import fileinput

lines = [l.strip() for l in fileinput.input()]
n = int(lines[0])
ids = list(map(int, filter(lambda l: l != 'x', lines[1].split(','))))

bus, diff = 0, float('inf')
for i in ids:
    d = i * (n // i) + i - n
    if d < diff:
        bus = i
        diff = d

print(bus * diff)