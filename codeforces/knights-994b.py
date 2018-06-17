from heapq import heappush, heappop

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

heap = []
sort_p = sorted([i for i in range(n)], key=lambda x: p[x])

som_k = 0
soms = []
for i in range(n):
  ci = c[sort_p[i]]
  p[sort_p[i]] = (som_k + ci)
  som_k += ci
  heappush(heap, ci)
  if len(heap) > k:
    som_k -= heappop(heap)

print (*p)
