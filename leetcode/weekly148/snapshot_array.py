'''
https://leetcode.com/contest/weekly-contest-148/problems/snapshot-array/
'''

class SnapshotArray:

    def __init__(self, length: int):
        self.next_snap_id = 0
        self.n = length
        self.arr = [[(0, 0)] for _ in range(self.n)] # val, last_snap_id

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][1] != self.next_snap_id:
            self.arr[index].append((0, self.next_snap_id))
        self.arr[index][-1] = (val, self.arr[index][-1][1])

    def snap(self) -> int:
        self.next_snap_id += 1
        return self.next_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.arr[index][-1][1]: return self.arr[index][-1][0]
        # binary search algorithm at index
        l, r = 0, len(self.arr[index]) - 1
        while l < r:
            m = (l + r + 1) >> 1
            if self.arr[index][m][1] > snap_id: r = m - 1
            else: l = m
        return self.arr[index][l][0]
