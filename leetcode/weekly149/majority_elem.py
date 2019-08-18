'''
https://leetcode.com/contest/weekly-contest-149/problems/online-majority-element-in-subarray/

Algorithm:
1. Preprocess the arr into a segment tree, each node in the tree stores (element, frequency) for a range of the node
2. Query using preprocessed ST and do a binary search at each node to merge left and right child node solutions
Complexity:
Preprocess: N * logN (logN is because of the binary search we do at each node for merging sub solutions)
Each query: logN * logN (extra logN for binary search at each node)

Status: TLE at 25/27. Is there a better algorithm? or is it py3?
'''
class ST:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)
        self.st = [(-1, 0) for _ in range(4 * self.n)]
        self.bs = {} # elem -> [ia, ib, ic ...]

        self._ds_for_bs()
        self._build(0, self.n - 1)

    def query(self, st, en, i=0, l=0, r=-1):
        if r == -1: r = self.n - 1 # Just fixing python complaints here
        if en < l or st > r: return (-1, 0)
        if st <= l and en >= r:
            return self.st[i]
        m = (l + r) >> 1
        a = self.query(st, en, 2 * i + 1, l, m)
        b = self.query(st, en, 2 * i + 2, m + 1, r)
        ae, af = a[0], a[1] + (self._bs(a[0], m + 1, min(en, r)) if b[0] != -1 else 0)
        be, bf = b[0], b[1] + (self._bs(b[0], max(st, l), m) if a[0] != -1 else 0)
        if af > bf: return (ae, af)
        return (be, bf)

    def _build(self, l, r, i=0):
        if r < l: return (-1, 0)
        if r - l == 0:
            self.st[i] = (self.arr[l], 1)
            return self.st[i]
        m = (l + r) >> 1
        a = self._build(l, m, 2 * i + 1)
        b = self._build(m + 1, r, 2 * i + 2)
        ae, af = a[0], a[1] + self._bs(a[0], m + 1, r)
        be, bf = b[0], b[1] + self._bs(b[0], l, m)
        if af > bf: self.st[i] = (ae, af)
        else: self.st[i] = (be, bf)
        return self.st[i]

    def _bs(self, e, l, r):
        if e == -1: return 0
        if self.bs[e][-1] < l or self.bs[e][0] > r: return 0
        st, en = 0, len(self.bs[e]) - 1
        while st < en: # find >= l
            m = (st + en) >> 1
            if self.bs[e][m] < l: st = m + 1
            else: en = m
        l = st
        st, en = 0, len(self.bs[e]) - 1
        while st < en: # find <= r
            m = (st + en + 1) >> 1
            if self.bs[e][m] <= r: st = m
            else: en = m - 1
        r = st
        if r >= l: return r - l + 1
        return 0

    def _ds_for_bs(self):
        for i, a in enumerate(self.arr):
            if a not in self.bs: self.bs[a] = []
            self.bs[a].append(i)

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.st = ST(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        q = self.st.query(left, right) # elem, freq
        e, f = q[0], q[1]
        return e if f >= threshold else -1
