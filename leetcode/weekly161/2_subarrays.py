'''
https://leetcode.com/contest/weekly-contest-161/problems/count-number-of-nice-subarrays/
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0, *nums]
        nice = 0
        for i in range(1, len(nums)):
            nums[i] %= 2
            nums[i] += nums[i - 1]
            req = nums[i] - k
            if req < 0: continue
            l = bisect.bisect_left(nums, req, 0, i)
            r = bisect.bisect_left(nums, req + 1, 0, i)
            nice += r - l
        return nice
    