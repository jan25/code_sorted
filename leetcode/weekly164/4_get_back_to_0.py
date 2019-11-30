'''
https://leetcode.com/contest/weekly-contest-164/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
'''
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1: return 1 # edge case
        
        mod = 10**9 + 7
        
        ncr_cache = {}
        def ncr(n, r):
            if r == 0 or n == r: return 1
            if (n, r) not in ncr_cache:
                c = ncr(n - 1, r) + ncr(n - 1, r - 1)
                ncr_cache[(n, r)] = c % mod
            return ncr_cache[(n, r)]
        
        count_cache = {}
        # lr     available left and right moves
        # lmoves allowed LL moves from current position
        # isz    is position at zero
        def count(lr, lmoves=0, isz=True):
            if lr == 0: return int(lmoves == 0)
            if lmoves * 2 >= arrLen: return 0
            if (lr, lmoves, isz) not in count_cache:
                c = 0
                if lmoves * 2 < arrLen - 1:
                    c += count(lr - 2, lmoves, isz) # RL
                if not isz:
                    c += count(lr - 2, lmoves, False) # LR
                c += count(lr - 2, lmoves + 1, False) # RR
                if lmoves > 0:
                    iszz = lmoves == 1
                    c += count(lr - 2, lmoves - 1, iszz) # LL
                count_cache[(lr, lmoves, isz)] = c % mod
            return count_cache[(lr, lmoves, isz)]
        
        ways = 0
        # odd left-right steps are not possible
        for lr in range(0, steps + 1, 2):
            c = count(lr)
            n, r = lr, steps - lr
            ways += c * ncr(n + r, r) # include Stay moves
            if ways >= mod: ways %= mod
        return ways
            