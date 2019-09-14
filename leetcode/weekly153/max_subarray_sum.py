'''
https://leetcode.com/contest/weekly-contest-153/problems/maximum-subarray-sum-with-one-deletion/
'''
import heapq

inf = -1 * (10 ** 9)

class Solution:
    def solve_for_each_idx(self, arr, reverse=False):
        arr = [a for a in arr] # clone
        if reverse: arr.reverse()
        vals = []
        h = []
        csum = 0
        for a in arr:
            csum += a
            if len(h) > 0:
                best = max(csum, csum - h[0])
                vals.append(best)
            else:
                vals.append(csum)
            heapq.heappush(h, csum)
        if reverse: vals.reverse()
        return vals
    
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return arr[0]
        left = self.solve_for_each_idx(arr)
        right = self.solve_for_each_idx(arr, reverse=True)
        best = max(arr + left + right)
        for i in range(n):
            local = 0
            if i > 0: local += left[i - 1]
            if i < n - 1: local += right[i + 1]
            best = max(best, local)
        return best