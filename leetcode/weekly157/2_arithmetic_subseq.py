'''
https://leetcode.com/contest/weekly-contest-157/problems/longest-arithmetic-subsequence-of-given-difference/
'''
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest = {}
        for a in arr:
            p = a - difference
            if p not in longest:
                if a not in longest:
                    longest[a] = 1
            else:
                if a not in longest:
                    longest[a] = longest[p] + 1
                else:
                    longest[a] = max(longest[a], longest[p] + 1)
        return max(longest.values())
        