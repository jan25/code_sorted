'''
https://leetcode.com/contest/weekly-contest-170/problems/xor-queries-of-a-subarray/
'''
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        def bits(a):
            b = []
            while a > 0:
                b.append(a & 1)
                a >>= 1
            return (b + [0]*32)[:32]
    
        def toi(bi):
            while bi[-1] == 0: bi.pop()
            i = 0
            while len(bi) > 0:
                i = (i << 1) + (bi[-1] % 2)
                bi.pop()
            return i
        
        b = [bits(a) for a in arr]
        for i in range(1, len(arr)):
            for j in range(32):
                b[i][j] += b[i - 1][j]
        
        results = []
        for l, r in queries:
            diff = [*b[r]]
            if l > 0:
                for i, bi in enumerate(b[l - 1]):
                    diff[i] -= bi
            results.append(toi(diff))
        return results
    