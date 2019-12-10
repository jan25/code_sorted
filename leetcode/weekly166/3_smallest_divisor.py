'''
https://leetcode.com/contest/weekly-contest-166/problems/find-the-smallest-divisor-given-a-threshold/
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divided_sum(div):
            s = 0
            for n in nums:
                s += n // div
                if n % div > 0: s += 1
            return s
        
        l, r = 1, max(nums)
        while l < r:
            div = (l + r) >> 1
            if divided_sum(div) > threshold:
                l = div + 1
            else: r = div
        return l
    