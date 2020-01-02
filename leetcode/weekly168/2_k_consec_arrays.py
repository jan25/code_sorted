'''
https://leetcode.com/contest/weekly-contest-168/problems/divide-array-in-sets-of-k-consecutive-numbers/
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = {}
        nums_set = set()
        for n in nums:
            if n not in nums_set:
                nums_set.add(n)
                counts[n] = 0
            counts[n] += 1
        
        nums = sorted(list(nums_set))
        i = 0
        while i < len(nums):
            if counts[nums[i]] == 0:
                i += 1; continue
            for j in range(k):
                if i + j >= len(nums) or counts[nums[i + j]] <= 0:
                    return False
                if j > 0 and i + j > 0 and nums[i + j] != nums[i + j - 1] + 1:
                    return False
                counts[nums[i + j]] -= 1
        return True
        