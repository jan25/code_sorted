'''
https://leetcode.com/problems/sum-of-subarray-minimums/

Algorithm:
Using monotonic stack with increasing values
'''
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10**9 + 7
        
        class E:
            def __init__(self, val, c):
                self.val = val
                self.c = c
            
        stk = []
        tot_sum, min_sum = 0, 0
        for a in A:
            if len(stk) == 0 or stk[-1].val < a:
                stk.append(E(a, 1))
                min_sum += a
            else:
                e = E(a, 1)
                while len(stk) > 0 and stk[-1].val >= a:
                    f = stk.pop()
                    min_sum -= f.c * f.val
                    e.c += f.c
                stk.append(e)
                min_sum += e.val * e.c
            tot_sum += min_sum
            if tot_sum >= mod:
                tot_sum %= mod;
        return tot_sum
    
