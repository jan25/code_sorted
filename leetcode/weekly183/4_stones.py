'''
https://leetcode.com/contest/weekly-contest-183/problems/stone-game-iii/
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        maxScore = [0] * n
        maxScore[-1] = stoneValue[-1]
        if n > 1:
            maxScore[-2] = max(sum(stoneValue[-2:]), stoneValue[-2] - stoneValue[-1])
        if n > 2:
            maxScore[-3] = max(sum(stoneValue[-3:]), stoneValue[-3] - maxScore[-2], sum(stoneValue[-3:-1]) - maxScore[-1])
        
        for i in range(n - 4, -1, -1):
            s, sm = -float('inf'), 0
            for j in range(0, 3):
                sm += stoneValue[i + j]
                s = max(s, sm - maxScore[i + j + 1])
            maxScore[i] = s
        
        diff = maxScore[0]
        if diff == 0: return 'Tie'
        if diff > 0: return 'Alice'
        return 'Bob'
    
