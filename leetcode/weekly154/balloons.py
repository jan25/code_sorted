'''
https://leetcode.com/contest/weekly-contest-154/problems/maximum-number-of-balloons/
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = {}
        for c in text:
            if c not in m: m[c] = 0
            m[c] += 1
        ans = len(text)
        for c in 'lo':
            if c in m: m[c] //= 2
        for c in 'balon':
            if c in m: ans = min(ans, m[c])
            else: ans = 0
        return ans