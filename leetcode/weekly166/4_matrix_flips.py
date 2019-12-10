'''
https://leetcode.com/contest/weekly-contest-166/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

Number of states in graph would be 2 ** (n * m). In this case 2 ** 9 ~= 1000
We can do a simple BFS and hope to reach 0 matrix from start matrix
To simplify how to store states, we could store matrix in form a integer and do bitwise ops for flips
'''
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        def toi(mat):
            mati = 0
            for i in range(n):
                for j in range(m):
                    mati = (mati << 1) | mat[i][j]
            return mati
        
        def flip_cell(mi, r, c):
            if r < 0 or c < 0 or r >= n or c >= m: return mi
            i = r * m + c
            return mi ^ (1 << i)
        
        def flip(mi, r, c):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 or j == 0:
                        next_r, next_c = r + i, c + j
                        mi = flip_cell(mi, next_r, next_c)
            return mi
        
        q, i = [(toi(mat), 0)], 0
        seen = set()
        while i < len(q):
            f = q[i]; i += 1
            if f[0] == 0: return f[1]
            for r in range(n):
                for c in range(m):
                    next_mati = flip(f[0], r, c)
                    if next_mati not in seen:
                        seen.add(next_mati)
                        q.append((next_mati, f[1] + 1))
            
        return -1