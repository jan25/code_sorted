'''
https://leetcode.com/contest/weekly-contest-151/problems/dinner-plate-stacks/

Implementation: Using Fenwick tree with binary search for push op
Better way would be to use Heap instead of keep track of left most index for push op
Both Pop ops take O(1) at Average
'''
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.c = capacity
        self.rm = -1
        self.bit = [0] * 200001

    def push(self, val: int) -> None:
        l, r = 0, self.rm + 1
        while l < r:
            m = (l + r) >> 1
            sm = self._sum(m)
            if sm == (m + 1) * self.c:
                l = m + 1
            else: r = m
        if len(self.stacks) == l:
            self.stacks.append([])
        self.stacks[l].append(val)
        self._add(l, 1)
        self.rm = max(self.rm, l)

    def pop(self) -> int:
        while self.rm >= 0:
            if len(self.stacks[self.rm]) == 0:
                self.rm -= 1
            else: break
        if self.rm < 0: return -1
        self._add(self.rm, -1)
        return self.stacks[self.rm].pop()
        
    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        self._add(index, -1)
        return self.stacks[index].pop()
    
    def _add(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i = i | (i + 1)

    def _sum(self, i):
        s = 0
        while i >= 0:
            s += self.bit[i]
            i = (i & (i + 1)) - 1
        return s


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
