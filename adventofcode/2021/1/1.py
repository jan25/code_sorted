import fileinput

nums = list(map(int, fileinput.input()))
print(sum(1 for a, b in zip(nums, nums[1:]) if a < b))
