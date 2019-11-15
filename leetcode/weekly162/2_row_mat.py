'''
https://leetcode.com/contest/weekly-contest-162/problems/reconstruct-a-2-row-binary-matrix/
'''
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        u, l = [0] * n, [0] * n
        
        ci = sorted(list(range(n)), key=lambda i: -1 * colsum[i])
        for i in ci:
            cs = colsum[i]
            if cs == 2:
                if upper == 0 or lower == 0:
                    return []
                u[i] = 1; l[i] = 1
                upper -= 1; lower -= 1
            elif cs == 1:
                if upper > 0:
                    u[i] = 1; upper -= 1
                    l[i] = 0
                elif lower > 0:
                    l[i] = 1; lower -= 1
                    u[i] = 0
                else: return []
            else:
                u[i] = 0; l[i] = 0
        
        if upper + lower > 0: return []
        
        return [u, l]
    