'''
https://leetcode.com/contest/weekly-contest-148/problems/longest-chunked-palindrome-decomposition/
'''
memo = {}

def dp(s, st, en):
    if st > en: return 0
    if (st, en) in memo: return memo[(st, en)]
    l = 1
    sub_sol = 1
    while l <= (en - st + 1) // 2:
        if s[st:st + l] == s[en - l + 1:en + 1]:
            sub_sol = max(sub_sol, 2 + dp(s, st + l, en - l))
        l += 1 
    memo[(st, en)] = sub_sol
    return sub_sol
    

class Solution:
    def longestDecomposition(self, text: str) -> int:
        return dp(text, 0, len(text) - 1)