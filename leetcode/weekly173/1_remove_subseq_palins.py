'''
https://leetcode.com/contest/weekly-contest-173/problems/remove-palindromic-subsequences/
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0: return 0
        if s == s[::-1]: return 1
        return 2
        