'''
https://leetcode.com/contest/weekly-contest-162/problems/cells-with-odd-values-in-a-matrix/
'''
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * n, [0] * m
        for a, b in indices:
            rows[a] += 1
            cols[b] += 1
        o = 0
        for i in range(n):
            for j in range(m):
                if (rows[i] + cols[j]) % 2 > 0:
                    o += 1
        return o
    