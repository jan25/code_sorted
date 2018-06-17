n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
dels = list(map(lambda x: int(x) - 1, input().split()))
dels.reverse()
res = []

done = [False]*n
dist = [[10**8]*n for i in range(n)]
for v in dels:
    sum_dist = 0
    done[v] = True
    for i in range(n):
        for j in range(n):
            if done[i] and done[j]:
               dist[i][v] = min(dist[i][v], min(dist[i][j] + w[j][v], w[i][v]))
               dist[v][j] = min(dist[v][j], min(dist[v][i] + dist[i][j], w[v][j]))
               dist[i][j] = min(dist[i][j], dist[i][v] + dist[v][j])
               sum_dist += dist[i][j] 
    res.append(sum_dist) 

res.reverse()
print (*res)
