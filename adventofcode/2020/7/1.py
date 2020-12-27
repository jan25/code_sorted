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
        inner.append(' '.join(p.split()[1:-1]))
    return out, inner

for l in lines:
    out, inner = parse(l)
    print(out, inner)
    for c in inner: graph[c].add(out)

q = ['shiny gold']
seen = set(q)
while q:
    nextq = []
    for col in q:
        for outercol in graph[col]:
            if outercol in seen: continue
            seen.add(outercol)
            nextq.append(outercol)
    q = nextq

print(len(seen) - 1)
