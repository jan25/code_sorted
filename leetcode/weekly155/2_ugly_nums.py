'''
https://leetcode.com/contest/weekly-contest-155/problems/ugly-number-iii/
'''
def gcd(a, b):
    if a == 0: return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def u(m, l):
    a, b, c = l
    n = m // a
    if b % a != 0:
        n += (m // b) - (m // lcm(a, b))
    if c % b != 0 and c % a != 0:
        n += (m // c) - (m // lcm(a, c))
        if b % a != 0: n -= (m // lcm(b, c))
    return n

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        abc = sorted([a, b, c])
        l, r = 0, 2 * (10 ** 9)
        while l < r:
            m = (l + r) >> 1
            if u(m, abc) >= n: r = m
            else: l = m + 1
        return l
        