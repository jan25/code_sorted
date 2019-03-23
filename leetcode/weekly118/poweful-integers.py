class Solution:
    def powerfulIntegers(self, x, y, bound):
        cache = {}
        for i in range(21):
            if (x, i) not in cache:
                cache[(x, i)] = x ** i
            if (y, i) not in cache:
                cache[(y, i)] = y ** i
        
        return self.solve(x, y, bound, cache)

    def solve(self, x, y, bound, cache):
        powerful = set()
        for i in range(21):
            for j in range(21):
                if cache[(x, i)] + cache[(y, j)] <= bound:
                    powerful.add(cache[(x, i)] + cache[(y, j)])
        return list(powerful)
