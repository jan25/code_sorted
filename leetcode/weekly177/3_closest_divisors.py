'''
https://leetcode.com/contest/weekly-contest-177/problems/closest-divisors/
'''
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        def closest(num):
            for i in range(int(num**0.5), 0, -1):
                if num % i == 0:
                    return i, num // i
            return None
        
        a, b = closest(num + 1), closest(num + 2)
        if abs(a[0] - a[1]) > abs(b[0] - b[1]):
            a, b = b, a
        return [*a]
    
