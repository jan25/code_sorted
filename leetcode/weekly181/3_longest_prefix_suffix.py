'''
https://leetcode.com/contest/weekly-contest-181/problems/longest-happy-prefix/

Algorithm:
Construct longest prefix length for every possible string s[:i]

This same prefix length array is used in KMP algorithm for pattern matching
'''
class Solution:
    def longestPrefix(self, s: str) -> str:
        
        pre, j = [0], 0
        for i in range(1, len(s)):
            if s[i] == s[j]:
                j += 1
                pre.append(j)
            else:
                while j - 1 >= 0 and s[j] != s[i]:
                    j = pre[j - 1]
                if s[i] == s[j]: j += 1
                pre.append(j)
        
        return s[:pre[-1]]

