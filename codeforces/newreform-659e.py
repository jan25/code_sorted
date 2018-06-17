n, m = map(int, input().split())
g = {}
for e in range(m):
    u, v = map(int, input().split())
    if u not in g: g[u] = []
    if v not in g: g[v] = []
    g[u].append(v)
    g[v].append(u)

glob_vis = set()
def bfs(v):
    vis = set([v])
    q = [v]
    qi, e = 0, 0
    while qi < len(q):
        v = q[qi]
        for u in g[v]:
            e += 1
            if u not in vis:
               vis.add(u)
               glob_vis.add(u)
               q.append(u)
        qi += 1
    return [e//2, len(vis)]

min_sep = 0
for v in range(1, n + 1):
    if v not in glob_vis:
        res = bfs(v)
        if res[0] == res[1] - 1:
            min_sep += 1

print (min_sep)

