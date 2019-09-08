'''
https://leetcode.com/contest/weekly-contest-152/problems/prime-arrangements/
'''
MOD = (10**9) + 7
class Solution:
    def is_prime(self, a):
        for i in range(2, a + 1):
            if i * i > a: break
            if a % i == 0: return 0
        return 1

    def nf(self, a):
        f = 1
        for i in range(2, a + 1):
            f *= i
            if f >= MOD: f %= MOD
        return f

    def numPrimeArrangements(self, n: int):
        p = sum([self.is_prime(i) for i in range(2, n + 1)])
        return (self.nf(p) * self.nf(n - p)) % MOD
