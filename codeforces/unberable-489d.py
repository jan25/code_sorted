n, m = map(int, input().split())

rev_d = [{} for i in range(n + 1)]
g = [[] for i in range(n + 1)]

for e in range(m):
  u, v = map(int, input().split())
  if u not in rev_d[v]: rev_d[u] = 0
  rev_d[u] += 1
  g[v].append(v)

pairs = {}
for i in range(1, n + 1):
  for j in g[i]:
    



