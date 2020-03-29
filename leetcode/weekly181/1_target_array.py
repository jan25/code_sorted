'''
https://leetcode.com/contest/weekly-contest-181/problems/create-target-array-in-the-given-order/
'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        l = []
        for i in range(n):
            l = l[:index[i]] + [nums[i]] + l[index[i]:]
        return l
    
