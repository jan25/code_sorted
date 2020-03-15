'''
https://leetcode.com/contest/weekly-contest-178/problems/how-many-numbers-are-smaller-than-the-current-number/
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sl = sorted(list(nums))
        ntoi = {}
        for i, n in enumerate(sl):
            if n not in ntoi:
                ntoi[n] = i
        return [ntoi[n] for n in nums]
    
