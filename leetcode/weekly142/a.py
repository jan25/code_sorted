class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        tot = sum(count)
        l = tot // 2
        r = l + ((1 + tot) % 2)
        print(l, r)
        s, n = 0, 0
        mn, mx, me, med, mo = 300.0, -1.0, 0.0, 0.0, 0
        for i, v in enumerate(count):
            if v == 0: continue
            if mn > i: mn = i
            if mx < i: mx = i
            s += v * i
            if l > n and l <= n + v:
                med += i
            if r > n and r <= n + v:
                med += i
            n += v
            if count[mo] < v: mo = i
        print(med)
        med /= 2
        me = s / tot
        return [mn, mx, me, med, mo]