'''
https://leetcode.com/contest/weekly-contest-178/problems/rank-teams-by-votes/
'''
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        max_r = len(votes[0])
        counts = defaultdict(lambda: defaultdict(lambda: 0))
        
        for v in votes:
            for i, c in enumerate(v):
                counts[c][i] += 1
                
        class C:
            def __init__(self, i):
                self.i = i
            
            def __lt__(self, j):
                for r in range(max_r):
                    if counts[self.i][r] > counts[j.i][r]:
                        return True
                    if counts[self.i][r] < counts[j.i][r]:
                        return False
                return ord(self.i) < ord(j.i)
        
        sorted_c = [C(c) for c in votes[0]]
        sorted_c.sort()
        return ''.join(c.i for c in sorted_c)
        
