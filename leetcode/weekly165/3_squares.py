'''
https://leetcode.com/contest/weekly-contest-165/problems/count-square-submatrices-with-all-ones/
'''
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        
        def first_try():
            for i in range(r):
                for j in range(1, c):
                    mat[i][j] += mat[i][j - 1]

            for j in range(c):
                for i in range(1, r):
                    mat[i][j] += mat[i - 1][j]

            def ones(ar, ac, br, bc):
                if br > r - 1 or bc > c - 1: return 0
                s = mat[br][bc]
                if ac > 0: s -= mat[br][ac - 1]
                if ar > 0: s -= mat[ar - 1][bc]
                if ar > 0 and ac > 0: s += mat[ar - 1][ac - 1]
                return s

            sq = 0
            # This should take 300 ** 3 ops
            # TLEed for some reason though :(
            for s in range(0, min(r, c)):
                area = (s + 1) ** 2
                for i in range(r):
                    for j in range(c):
                        if area == ones(i, j, i + s, j + s):
                            sq += 1
            return sq
        
        def second_try():
            cache = [[0] * c for _ in range(r)]
            sq = 0
            for i in range(c):
                cache[0][i] = mat[0][i]
                sq += cache[0][i]
            for i in range(1, r):
                cache[i][0] = mat[i][0]
                sq += cache[i][0]
            
            for i in range(1, r):
                for j in range(1, c):
                    if mat[i][j] == 1:
                        # Should take 300 ** 2 ops
                        # This is a super smart idea
                        # had to lookup the 2D grid figure to understand
                        cache[i][j] = 1 + min(cache[i - 1][j - 1], cache[i][j - 1], cache[i - 1][j])
                        sq += cache[i][j]
                    
            return sq
        
        return second_try()
            
        