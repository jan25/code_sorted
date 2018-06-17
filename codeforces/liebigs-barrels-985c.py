n, k, l = map(int, input().split())
a = sorted(list(map(int, input().split())))

st, en = 0, n * k - 1
while st < en:
	mid = (st + en + 1) // 2
	if a[mid] > a[0] + l:
		en = mid - 1
	else:
		st = mid

max_sum = 0
en = n * k - 1
while st >= 0:
	if en - st >= k - 1:
		max_sum += a[st]
		en -= k
		n -= 1
	st -= 1

print (max_sum if n == 0 else 0)