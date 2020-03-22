'''
https://leetcode.com/contest/weekly-contest-180/problems/design-a-stack-with-increment-operation/
'''
class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.ms = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.ms:
            self.s.append(x)

    def pop(self) -> int:
        if self.s: return self.s.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i >= len(self.s): break
            self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
