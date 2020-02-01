'''
https://leetcode.com/contest/weekly-contest-173/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
'''
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = 10 ** 10
        d = [[inf] * n for _ in range(n)]
        
        for i in range(n): d[i][i] = 0
        for e in edges:
            d[e[0]][e[1]] = e[2]
            d[e[1]][e[0]] = e[2]
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    nd = d[j][i] + d[i][k]
                    if d[j][k] > nd:
                        d[j][k] = nd
        
        max_v, max_c = -1, inf
        for v in range(n - 1, -1, -1):
            c = 0
            for u in range(n):
                if d[v][u] <= distanceThreshold:
                    c += 1
            
            if c < max_c:
                max_v, max_c = v, c
        
        return max_v
        