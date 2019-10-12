'''
https://leetcode.com/contest/weekly-contest-157/problems/play-with-chips/
'''

class Solution:
    def min_cost(self, l, p):
        cost = 0
        for i, c in enumerate(l):
            if c == 0: continue
            cost += c * ((p - i) % 2)
        return cost
    
    def minCostToMoveChips(self, chips: List[int]) -> int:
        uniq_chips = sorted(list(set(chips)))
        n = 1
        mapped = { uniq_chips[0]: 1 }
        for i, c in enumerate(uniq_chips[1:]):
            diff = c - uniq_chips[i] - 1
            if diff > 2: diff = 3 if diff % 2 > 0 else 2
            mapped[c] = n + diff + 1
            n = mapped[c]
        
        places = [0] * 1000
        for c in chips:
            places[mapped[c]] += 1

        min_cost = 10 ** 4 + 1
        for i in range(1, n + 1):
            min_cost = min(min_cost, self.min_cost(places, i))
        return min_cost
        