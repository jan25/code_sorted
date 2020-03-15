'''
https://leetcode.com/contest/weekly-contest-179/problems/frog-position-after-t-seconds/
'''
from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if not edges: return float(1 == target)
        if target == 1: return 0
        
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        out = []
        vis = set()
        
        def dfs(v):
            if v in vis: return False
            if v == target: return True
            vis.add(v)
            out.append(len(g[v]))
            for u in g[v]:
                if dfs(u): return True
            out.pop()
            return False
        
        if not dfs(1): return 0
        if len(out) > t: return 0
        if len(out) < t and len(g[target]) != 1: return 0
        for i in range(1, len(out)):
            out[i] -= 1
        
        if len(out) == 1: return 1 / out[0]
        return 1 / reduce(lambda a, b: a * b, out)
        
