'''
https://leetcode.com/contest/weekly-contest-152/problems/can-make-palindrome-from-substring/
'''
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        s = [ord(c) - ord('a') for c in s]
        cs = []
        for i, c in enumerate(s):
            a = [0] * 26
            a[c] += 1
            if i > 0:
                for j in range(26):
                    a[j] += cs[-1][j]
            cs.append(a)
        results = []
        for q in queries:
            l, r, k = q
            diff = 0
            if l > 0:
                for i in range(26):
                    diff += (cs[r][i] - cs[l - 1][i]) % 2
            else:
                for d in cs[r]: diff += d % 2
            results.append(diff // 2 <= k)
        return results
