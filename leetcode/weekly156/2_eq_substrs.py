'''
https://leetcode.com/contest/weekly-contest-156/problems/get-equal-substrings-within-budget/
'''
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diffs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        for i in range(1, n):
            diffs[i] += diffs[i - 1]
        diffs = [0, *diffs]
        maxSubLen = 0
        for i in range(1, n + 1):
            minCost = diffs[i] - maxCost
            l = bisect.bisect_left(diffs, minCost, hi=i)
            if l == i: continue
            maxSubLen = max(maxSubLen, i - l)
        return maxSubLen
            