from collections import defaultdict


lines = []
with open('input', 'r') as f:
    for line in f: lines.append(line)

graph = defaultdict(set)

def parse(l):
    out, inner = l.split(' contain ')
    out = ' '.join(out.split()[:-1])
    if 'no other' in inner: return out, []
    parts = inner.split(', ')
    inner = []
    for p in parts:
        bag = p.split()[:-1]
        inner.append((int(bag[0]), ' '.join(bag[1:])))
    return out, inner

for l in lines:
    out, inner = parse(l)
    print(out, inner)
    for pair in inner:
        graph[out].add(pair)

def dfs(col):
    bags = 1
    for n, innercol in graph[col]:
        bags += n * dfs(innercol)
    return bags

print(dfs('shiny gold') - 1)
