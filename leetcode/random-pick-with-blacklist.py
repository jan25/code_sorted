class Solution:

    def __init__(self, N, blacklist):
        blacklist.sort()
        self.N = N - len(blacklist)
        self.free_pairs = self.prep_free_pairs(N, blacklist)
        self.offsets = [0]
        for pair in self.free_pairs:
            self.offsets.append(pair[1] - pair[0] + 1)
            self.offsets[-1] += self.offsets[-2]

    def prep_free_pairs(self, N, blacklist):
        last_free, pairs = 0, []
        for i in blacklist:
            if i - last_free > 0:
                pairs.append((last_free, i - 1))
            last_free = i + 1
        if last_free < N: pairs.append((last_free, N - 1))
        return pairs

    def pick(self):
        rint = random.randint(0, self.N - 1)
        l, r = 0, len(self.free_pairs) - 1
        while l < r:
            mid = (l + r + 1) >> 1
            if self.offsets[mid] >= rint + 1:
                r = mid - 1
            else: l = mid
        actual_rint = self.free_pairs[l][0]  + rint - self.offsets[l]
        if l > 0 and rint - self.offsets[l] > 0: actual_rint -= 1
        return actual_rint


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
