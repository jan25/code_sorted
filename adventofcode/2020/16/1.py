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

fields, _, other = groups

def valset(f):
    parts = f.split()
    k = parts[0][:-1]
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

err = 0
for o in other:
    for num in map(int, o.split(',')):
        if num not in allinc: err += num

print(err)

