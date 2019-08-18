'''
https://leetcode.com/contest/weekly-contest-149/problems/day-of-the-year/
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        yyyy, mm, dd = map(int, date.split('-'))
        leap = yyyy % 4 == 0 and yyyy > 1900
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap: d[1] += 1
        for i in range(1, 12): d[i] += d[i - 1]
        days = dd
        if mm > 1: days += d[mm - 2]
        return days
