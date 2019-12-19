'''
https://leetcode.com/contest/weekly-contest-167/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

Algorithm:
1. Preprocess row wise and column wise cumulative sums
2. walk over a diaganol with trying to expand the size of square on its side.
    This is much like two pointer algorithm on a 1D array
3. repeat 2 for all diagonals to figure the largest square
'''
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        
        lr = [[mat[i][j] for j in range(m)] for i in range(n)]
        ud = [[mat[i][j] for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if j > 0:
                    lr[i][j] += lr[i][j - 1]
                if i > 0:
                    ud[i][j] += ud[i - 1][j]
                    
        def find_max_len(lx, ly):
            rx, ry = lx, ly
            s = mat[lx][ly]
            max_len = 0
            while True:
                if s > threshold:
                    s += mat[rx][ry]
                    s -= lr[rx][ly]
                    s -= ud[lx][ry]
                    if ry > 0: s += lr[rx][ry - 1]
                    if rx > 0: s += ud[rx - 1][ry]
                    rx += 1; ry += 1
                else:
                    max_len = max(max_len, lx - rx + 1)
                    lx += 1; ly += 1
                    if lx >= n or ly >= m: break
                    s -= mat[lx][ly]
                    s += lr[lx][ly] + ud[lx][ly]
                    if rx > 0: s -= ud[rx - 1][ly]
                    if ry > 0: s -= lr[lx][ry - 1]
            return max_len
                    
        max_len = 0
        for r in range(n):
            max_len = max(max_len, find_max_len(r, 0))
        for c in range(m):
            max_len = max(max_len, find_max_len(0, c))
        return max_len
