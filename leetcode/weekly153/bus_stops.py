'''
https://leetcode.com/contest/weekly-contest-153/problems/distance-between-bus-stops/
'''
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        total = sum(distance)
        between = sum(distance[start:destination])
        return min(between, total - between)