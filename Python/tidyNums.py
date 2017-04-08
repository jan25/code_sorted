# https://code.google.com/codejam/contest/3264486/dashboard B
from functools import reduce
def tidy(n, i = 0):
	if i == len(n) - 1: return True
	return n[i] <= n[i + 1] and tidy(n, i + 1)
def reduc(x, y):
	if x == 0: return str(y)
	return str(x) + str(y)
T = int(input())
for tc in range(1, T + 1):
	n = list(map(int, input()))
	while not tidy(n):
		for i in range(len(n) - 1):
			if n[i] > n[i + 1]:
				n[i] -= 1
				for j in range(i + 1, len(n)):
					n[j] = 9
	print ('Case #' + str(tc) + ':', reduce(lambda x, y: reduc(x, y), n))