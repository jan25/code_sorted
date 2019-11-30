'''
https://leetcode.com/contest/weekly-contest-164/problems/minimum-time-visiting-all-points/
'''
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
        
        return sum(dist(points[i], points[i - 1]) for i in range(1, len(points)))
