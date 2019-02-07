class Solution:
    def flipgame(self, fronts: 'List[int]', backs: 'List[int]') -> 'int':
        same_sides = {}
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                if fronts[i] not in same_sides:
                    same_sides[fronts[i]] = 0
                same_sides[fronts[i]] += 1
            
        min_side = 2345
        for i in range(len(fronts)):
            f, b = fronts[i], backs[i]
            if f == b: continue
            if f not in same_sides:
                min_side = min(min_side, f)
            if b not in same_sides:
                min_side = min(min_side, b)
        if min_side == 2345: min_side = 0
        return min_side