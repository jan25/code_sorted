n, s = map(int, input().split())
points = [list(map(int, input().split())) for i in range(n)]
points = sorted(points, key = lambda a: a[0]*a[0] + a[1]*a[1])

x, y = 0, 0

for p in points:
	x, y = p[0], p[1]
	s += p[2]
	if s >= 10**6: break

import math
print(-1 if s < 10**6 else format(math.sqrt(x*x + y*y), '.7f')) 