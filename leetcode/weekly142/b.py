class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sums = [0] * 1002
        for t in trips:
            sums[t[1]] += t[0]
            sums[t[2]] -= t[0]
        for i in range(1, len(sums)):
            sums[i] += sums[i - 1]
            if sums[i] > capacity:
                return False
        return True
        