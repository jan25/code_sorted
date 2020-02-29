'''
https://leetcode.com/contest/weekly-contest-177/problems/number-of-days-between-two-dates/
'''
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, 12): days[i] += days[i - 1]
            
        def days_until(y, d=None, m=None):
            if d is None: d = 31
            if m is None: m = 12
            is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            if m > 1: d += days[m - 2]
            if m > 2 and is_leap: d += 1
            return d
        
        if date1 > date2:
            date1, date2 = date2, date1
        ay, am, ad = map(int, date1.split('-'))
        by, bm, bd = map(int, date2.split('-'))
        
        d = sum(days_until(y=y) for y in range(ay, by))
        d += days_until(d=bd, m=bm, y=by)
        d -= days_until(d=ad, m=am, y=ay)
            
        return d
    
