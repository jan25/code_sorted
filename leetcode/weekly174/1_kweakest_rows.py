'''
https://leetcode.com/contest/weekly-contest-174/problems/the-k-weakest-rows-in-a-matrix/
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        rows = list(range(n))
        ones = [sum(r) for r in mat]
        
        return sorted(rows, key=lambda i: ones[i])[:k]
        
