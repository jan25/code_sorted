'''
https://www.hackerrank.com/contests/hourrank-18/challenges/super-six-substrings/submissions/code/1301089841
Level: Medium
O(1) space
O(N) time
bottom up dp
'''

#!/bin/python3
import sys
s = input().strip()
def toInt(c):
	return ord(c) - ord('0')
ans = 0
memo = [0 for x in range(6)]
for i in range(len(s)):
	temp = [0 for x in range(6)]
	if toInt(s[i]) > 0: temp[toInt(s[i]) % 6] = 1;
	if 0 == toInt(s[i]): ans += 1
	for y in range(len(memo)):
		temp[((y * 10) + toInt(s[i])) % 6] += memo[y]
	memo = temp
	ans += memo[0];
print (ans)