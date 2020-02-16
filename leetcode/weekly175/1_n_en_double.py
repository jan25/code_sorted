'''
https://leetcode.com/contest/weekly-contest-175/problems/check-if-n-and-its-double-exist/
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for a in arr:
            if a % 2 == 0 and a // 2 in seen: return True
            if 2 * a in seen: return True
            seen.add(a)
        return False
    