import fileinput

nums = list(map(int, fileinput.input()))


def gen():
    for i in range(1, len(nums) - 2):
        if sum(nums[i:i + 3]) > sum(nums[i - 1: i + 2]):
            yield 1


print(sum(inc for inc in gen()))
