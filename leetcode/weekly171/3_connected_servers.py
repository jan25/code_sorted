'''
https://leetcode.com/contest/weekly-contest-171/problems/number-of-operations-to-make-network-connected/
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        
        ds = [-1] * n
        
        def root(a):
            if ds[a] < 0: return a
            ds[a] = root(ds[a])
            return ds[a]
        
        def uni(a, b):
            a, b = root(a), root(b)
            if a == b: return
            if ds[a] > ds[b]: a, b = b, a
            ds[a] += ds[b]
            ds[b] = a
        
        for c in connections: uni(*c)
        
        return sum(1 for i in range(n) if ds[i] < 0) - 1
        