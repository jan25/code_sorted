'''
https://leetcode.com/contest/weekly-contest-161/problems/check-if-it-is-a-good-array/
'''
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            if a == 0: return b
            return gcd(b % a, a)
        
        g = nums[0]
        for a in nums[1:]:
            if g == 1: return True
            g = gcd(g, a)
        
        return g == 1
    