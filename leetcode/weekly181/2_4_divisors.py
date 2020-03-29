'''
https://leetcode.com/contest/weekly-contest-181/problems/four-divisors/
'''
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def numDivs(a):
            d, s = 0, 0
            for i in range(1, max(nums)):
                if i*i > a: break         
                if a % i == 0:
                    d += 1
                    s += i
                    if i * i != a:
                        d += 1
                        s += a // i
            return d, s
        
        sumDivs = 0
        for a in nums:
            d, s = numDivs(a)
            if d == 4:
                sumDivs += s
        return sumDivs
    
