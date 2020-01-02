'''
https://leetcode.com/contest/weekly-contest-169/problems/jump-game-iii/
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = set()
        
        def walk(i):
            if i < 0 or i >= n: return False
            if arr[i] == 0: return True
            t = False
            if (i, 0) not in vis:
                vis.add((i, 0))
                t = t or walk(i - arr[i])
            if (i, 1) not in vis:
                vis.add((i, 1))
                t = t or walk(i + arr[i])
            return t
            
        return walk(start)
    