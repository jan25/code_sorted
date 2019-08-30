'''
https://leetcode.com/contest/weekly-contest-151/problems/invalid-transactions/
'''
class Trans:
    def __init__(self, t):
        self.t = t
        self.invalid = False
        ts = t.split(',')
        self.name = ts[0]
        self.mins = int(ts[1])
        self.amt = int(ts[2])
        self.city = ts[-1]

    def __repr__(self):
        return '%s:%r' % (self.t, self.invalid)

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tl = [Trans(t) for t in transactions]
        tl.sort(key=lambda a: a.mins)
        for i, t in enumerate(tl):
            if t.amt > 1000: t.invalid = True
            for j in range(i - 1, -1, -1):
                tt = tl[j]
                if tt.mins + 60 >= t.mins:
                    if tt.name == t.name and tt.city != t.city:
                        tt.invalid = True
                        t.invalid = True
                else: break
        return [t.t for t in tl if t.invalid]
