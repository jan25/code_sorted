'''
https://leetcode.com/contest/weekly-contest-166/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        while n > 0:
            d = n % 10
            s += d; p *= d
            n //= 10
        return p - s
    