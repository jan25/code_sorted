#!/usr/bin/env python3
import fileinput
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]

count_alls, ing_count = 0, defaultdict(int)
allergens = defaultdict(set)
for l in lines:
    ings, alls = l.split(' (contains ')
    ings = ings.split()
    for ing in ings: ing_count[ing] += 1
    alls = alls[:-1].split(', ')
    count_alls += len(ings)
    for a in alls:
        if a not in allergens: allergens[a] = set(ings)
        else: allergens[a] = allergens[a].intersection(ings)
    
while True:
    ones = [a for a in allergens if len(allergens[a]) <= 1]
    if len(ones) == len(allergens.keys()): break
    for a in allergens:
        if len(allergens[a]) <= 1: continue
        for one in ones:
            allergens[a] -= allergens[one]

pairs = [(k, v.pop()) for k, v in allergens.items() if len(v) == 1]
print(','.join(map(lambda p: p[1], sorted(pairs))))
