'''
https://leetcode.com/contest/weekly-contest-160/problems/tiling-a-rectangle-with-the-fewest-squares/

Idea: bruteforce + hueristic for pruning
bruteforce - fill the area bottom up; find the bottom most left position to fill
hueristic  - use lower bound of min number of squares used to fill an area. Use this as a pruning mechanism
Refer here for more https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/415423/No-magic-a-dfs-solution-with-heuristic
'''
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.count = n * m
        
        # lower bound min number of squares given a area to fill
        area = n * m
        dp = [-1] * (area + 1)
        dp[0] = 0
        for a in range(1, area + 1):
            dp[a] = 1 + min(dp[a - s ** 2] for s in range(1, int(math.sqrt(a)) + 1))
        
        def place(heights, used, area_left):
            # without this hueristic, the program times out
            if used + dp[area_left] >= self.count:
                return
            
            min_x = 0
            min_h = heights[0]
            filled = True
            for x in range(n):
                if min_h > heights[x]:
                    min_x = x
                    min_h = heights[x]
                if heights[x] < m:
                    filled = False
            if filled:
                self.count = min(self.count, used)
                return
                
            min_ex = min_x + 1
            while min_ex < n and heights[min_ex] == min_h:
                min_ex += 1
            
            side = min(m - min_h, min_ex - min_x)
            for s in range(1, side + 1):
                h = [*heights]
                for x in range(min_x, min_x + s):
                    h[x] += s
                place(h, 1 + used, area_left - s * s)
        
        place([0] * n, 0, area)
        return self.count
                
            