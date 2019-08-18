'''
https://leetcode.com/contest/weekly-contest-149/problems/number-of-dice-rolls-with-target-sum/
'''

MOD = 7 + (10 ** 9)
memo = {}

def dp(d, rem, nf):
    if d == 0: return 1 if rem == 0 else 0
    if (d, rem) in memo:
        return memo[(d, rem)]
    sub_sol = 0
    for f in range(1, nf + 1):
        if f > rem: break
        sub_sol += dp(d - 1, rem - f, nf)
        if sub_sol >= MOD: sub_sol %= MOD
    memo[(d, rem)] = sub_sol
    return sub_sol

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return dp(d, target, f)
