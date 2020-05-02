'''
https://leetcode.com/contest/weekly-contest-186/problems/constrained-subsequence-sum/
'''
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        heap = []
        def push(e, i):
            heapq.heappush(heap, (-1 * e, i))
        
        def pop_max(i):
            while heap:
                m = heapq.heappop(heap)
                if m[1] > i + k: continue
                heapq.heappush(heap, m)
                return -1 * m[0]
        
        n = len(nums) - 1
        max_sum = -10**5
        for i in range(n, -1, -1):
            m = pop_max(i)
            if m:
                m = max(nums[i], m + nums[i])
                max_sum = max(max_sum, m)
                push(m, i)
            else:
                max_sum = max(max_sum, nums[i])
                push(nums[i], i)
        
        return max_sum
        
