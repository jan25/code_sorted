'''
https://leetcode.com/contest/weekly-contest-173/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
'''
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        def f(e):
            if veganFriendly == 1 and e[2] == 0: return False    
            return e[3] <= maxPrice and e[4] <= maxDistance
        
        return list(map(lambda a: a[0], sorted(filter(f, sorted(restaurants, key=lambda a: -a[0])), key=lambda a: -a[1])))
        