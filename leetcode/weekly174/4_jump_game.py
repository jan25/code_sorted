'''
https://leetcode.com/contest/weekly-contest-174/problems/jump-game-v/

https://mp.weixin.qq.com/s/kEQ00_WLqDTG6tbsjQ2Xjw This blog has interesting approaches
'''
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        cache = [-1] * n
        
        def dp(i):
            if cache[i] > 0: return cache[i]
            cache[i] = 1
            for dx in [-1, 1]:
                for j in range(i + dx, i + dx * d + dx, dx):
                    if j < 0 or j >= n or arr[j] >= arr[i]: break
                    cache[i] = max(cache[i], 1 + dp(j))
            return cache[i]
            
        return max(dp(i) for i in range(n))
    
