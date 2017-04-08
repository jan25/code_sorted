# https://code.google.com/codejam/contest/3264486/dashboard A
import sys
sys.setrecursionlimit(1500)
def flip(l):
	flipped = ''
	for c in l:
		if c == '+': flipped += '-'
		else: flipped += '+'
	return flipped
def rec(l, i, k, res):
	if i + k > len(l):
		if '-' in l[i:]:
			return 'IMPOSSIBLE'
		return str(res)
	if l[i] == '+': return rec(l, i + 1, k, res)
	return rec(l[:i] + flip(l[i:i + k]) + l[i + k:], i + 1, k, res + 1)
N = int(input())
for i in range(1, N + 1):
	seq, k = input().split(' ')
	k = int(k)
	print ('Case #' + str(i) + ': ' + rec(seq, 0, k, 0))