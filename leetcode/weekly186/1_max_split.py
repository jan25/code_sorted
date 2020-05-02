'''
https://leetcode.com/contest/weekly-contest-186/problems/maximum-score-after-splitting-a-string/
'''
class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(int(c) for c in s)
        zeros = sum(1 if c == '0' else 0 for c in s)
        
        o, z = 0, 0
        max_score = 0
        for c in s[:-1]:
            if c == '1': o += 1
            else: z += 1
            max_score = max(max_score, z + ones - o)
        return max_score
    
