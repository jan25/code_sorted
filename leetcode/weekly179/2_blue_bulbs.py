'''
https://leetcode.com/contest/weekly-contest-179/problems/bulb-switcher-iii/
'''
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        c, max_sofar = 0, -1
        for i in range(len(light)):
            max_sofar = max(max_sofar, light[i])
            c += int(max_sofar == i + 1)
        return c
        
