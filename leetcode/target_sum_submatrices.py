'''
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Algorithm:
1. Make cumulative summed rows - N * N steps
2. Use 1 to go over all rows fixing right and left columns of the matrix - N steps
'''
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        mat = [r[::] for r in matrix]        
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            for j in range(1, m):
                mat[i][j] += mat[i][j - 1]
        
        c = 0
        for i in range(m):
            for j in range(i, m):
                sums = {0:1}
                s = 0
                for k in range(n):
                    s += mat[k][j] - (mat[k][i - 1] if i > 0 else 0)
                    diff = s - target
                    if diff in sums:
                        c += sums[diff]
                    if s not in sums: sums[s] = 1
                    else: sums[s]  += 1
                    
        return c
    