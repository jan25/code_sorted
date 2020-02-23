'''
https://leetcode.com/contest/weekly-contest-176/problems/product-of-the-last-k-numbers/
'''
class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.last_zero_idx = -1

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0: self.last_zero_idx = len(self.nums) - 1
        if len(self.nums) > 1 and self.nums[-2] > 0:
            self.nums[-1] *= self.nums[-2]

    def getProduct(self, k: int) -> int:
        if len(self.nums) - k <= self.last_zero_idx: return 0
        if len(self.nums) == k: return self.nums[-1]
        if self.nums[-k - 1] == 0: return self.nums[-1]
        return self.nums[-1] // self.nums[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)