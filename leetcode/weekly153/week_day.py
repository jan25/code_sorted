'''
https://leetcode.com/contest/weekly-contest-153/problems/day-of-the-week/
'''
class Solution:
    def is_leap(self, y):
        if y % 4 == 0:
            if y % 400 == 0: return True
            if y % 100 == 0: return False
            return True
        return False
    
    def days(self, year, month=12, day=31):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap(year): days[1] += 1
        if month > 1: day += sum(days[:month - 1])
        return day

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day = self.days(year, month, day)
        for y in range(1971, year): day += self.days(y)
        return ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"][day % 7]
 