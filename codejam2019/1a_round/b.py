def Solution(n, words):
    t = [] # {a => [next, count]}
    def add(w, i=0):
        if len(w) == 0: return i
        if i >= len(t) or i == -1:
            t.append({})
            i = len(t) - 1
        c = w[0]
        if c not in t[i]:
            t[i][c] = [-1, 0]
        t[i][c][1] += 1
        t[i][c][0] = add(w[1:], t[i][c][0])
        return i
    
    for w in words: add(w)
    
    # returns: count pairs below v
    def dfs(v=0, w=0):
        if v == -1: return w // 2
        count_pairs_below_v = 0
        for key in t[v].keys():
            if t[v][key][1] > 1:
                count_pairs_below_v += dfs(t[v][key][0], t[v][key][1])
        if w - count_pairs_below_v * 2 > 1:
            count_pairs_below_v += 1
        return count_pairs_below_v
        
    return dfs() * 2

for tc in range(int(input())):
    n = int(input())
    words = [input()[::-1] for _ in range(n)]
    print ('Case #%d: %d' % (tc + 1, Solution(n, words)))