#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache

lines = [l.strip() for l in fileinput.input()]

vals = dict()
orer = ander = (1 << 36) - 1
for line in lines:
    k, v = line.split(' = ')
    if k == 'mask':
        orer = v.replace('X', '0')
        orer = int(f'0b{orer}', 2)
        ander = v.replace('1', '0').replace('X', '1')
        ander = int(f'0b{ander}', 2)
    else:
        k = int(k[:-1].split('[')[-1])
        v = int(v)
        vals[k] = v & ander | orer

print(sum(vals.values()))