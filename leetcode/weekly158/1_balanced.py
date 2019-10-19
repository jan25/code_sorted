'''
https://leetcode.com/contest/weekly-contest-158/problems/split-a-string-in-balanced-strings/
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) < 2: return len(s)
        r, l = 0, 0
        for i in range(len(s)):
            if s[i] == 'R': r += 1
            else: l += 1
            if r == l: return 1 + self.balancedStringSplit(s[i + 1:])
            