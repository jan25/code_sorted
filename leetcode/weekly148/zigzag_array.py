'''
https://leetcode.com/contest/weekly-contest-148/problems/decrease-elements-to-make-array-zigzag/
'''
def oddSolver(nums, st):
    if len(nums) - 1 - st >= 2:
        l, r = nums[st], nums[st + 2]
        l = min(nums[st + 1] - 1, l)
        r = min(nums[st + 1] - 1, r)
        diff = nums[st] - l + nums[st + 2] - r
        nums[st], nums[st + 2] = l, r
        return diff + oddSolver(nums, st + 2)
    if len(nums) - 1 - st <= 0: return 0
    if nums[st + 1] <= nums[st]:
        diff = nums[st] - (nums[st + 1] - 1)
        nums[st] = nums[st + 1] - 1
        return diff
    return 0

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        odds = oddSolver([*nums], 0)
        evens = oddSolver(nums, 1)
        if nums[0] <= nums[1]:
            evens += nums[1] - nums[0] + 1
        print (odds, evens, nums)
        return min(odds, evens)