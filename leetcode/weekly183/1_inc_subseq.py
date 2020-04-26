class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = []
        while nums:
            l.append(nums.pop())
            if sum(nums) < sum(l):
                return l
        
