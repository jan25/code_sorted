# import random
# n, m = 2000, 2000
# print (n, m)
# for i in range(n):
# 	s = []
# 	for j in range(m):
# 		# if random.randint(0, 10) % 2 == 1:
# 		s.append('1')
# 		# else:
# 			# s.append('0')
# 	print (''.join(s))

n, m = map(int, input().split())
sums = [0] * m
strs = []
for i in range(n):
	s = input()
	strs.append(s)
	for j in range(len(s)):
		if s[j] == '1': sums[j] += 1
yes = "NO"
for s in strs:
	ones, oks = 0, 0
	for j in range(len(s)):
		if s[j] == '1':
			ones += 1
			oks += 1 if sums[j] > 1 else 0
	if ones == oks:
		yes = "YES"
		break
print (yes)