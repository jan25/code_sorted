#!/usr/bin/python3
import fileinput

groups = [[]]

for l in fileinput.input():
    line = l.strip()
    if 'ticket' in line: continue
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)

fields, your, other = groups

def valset(f):
    parts = f.split(': ')
    k = parts[0]
    parts = parts[1].split()
    st, en = map(int, parts.pop().split('-'))
    include = set()
    for i in range(st, en + 1): include.add(i)
    parts.pop() # or
    st, en = map(int, parts.pop().split('-'))
    for i in range(st, en + 1): include.add(i)
    return k, include

kvs = dict()
allinc = set()
for f in fields:
    k, v = valset(f)
    kvs[k] = v
    allinc = allinc.union(v)

def get_incs(t):
    incs = []
    for num in t:
        incs.append(set())
        for k, v in kvs.items():
            if num in v: incs[-1].add(k)
    return incs

allkeys = list(kvs.keys())
valid = None
for o in other:
    ok = True
    parts = list(map(int, o.split(',')))
    for num in parts:
        if num not in allinc:
            ok = False
            break
    if not ok: continue
    incs = get_incs(parts)
    if not valid:
        valid = incs
        continue
    for i in range(len(allkeys)):
        valid[i] = valid[i].intersection(incs[i])

while True:
    ones = {i for i, s in enumerate(valid) if len(s) == 1}
    if len(ones) == len(valid): break
    oneset = set()
    for i in ones: oneset = oneset.union(valid[i])
    for i in range(len(valid)):
        if i not in ones:
            valid[i] = valid[i] - oneset

prod = 1
for names, val in zip(valid, map(int, your[0].split(','))):
    if 'departure' in names.pop():
        prod *= val

print(prod)
