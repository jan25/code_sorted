'''
https://leetcode.com/contest/weekly-contest-170/problems/minimum-insertion-steps-to-make-a-string-palindrome/
'''
class Solution:
    def minInsertions(self, s: str) -> int:
        cache = {}
        def dp(l, r):
            if l >= r: return 0
            if (l, r) not in cache:
                sol = dp(l + 1, r) + 1
                sol = min(sol, 1 + dp(l, r - 1))
                if s[l] == s[r]:
                    sol = min(sol, dp(l + 1, r - 1))
                cache[(l, r)] = sol
            return cache[(l, r)]
        
        return dp(0, len(s) - 1)
    