n, m = map(int, (input().split()))
a = list(map(int, input().split()))

song_band = {song: a[song] for song in range(n)}
buckets = [[] for i in range(m + 1)]

uit = []
for idx in range(n):
    if a[idx] <= m: buckets[a[idx]].append(idx)
    else: uit.append(idx)
bidx = sorted([i for i in range(m + 1)], key=lambda b: len(buckets[b]))

max_min = n // m
min_ops = 0
l = 1
while l <= m and len(uit) > 0:
    if len(buckets[bidx[l]]) >= max_min: l += 1; continue
    song = uit.pop()
    buckets[bidx[l]].append(song)
    song_band[song] = bidx[l] 
    min_ops += 1 

r = l
while l <= m and r <= m:
    if len(buckets[bidx[r]]) <= max_min: r += 1
    elif len(buckets[bidx[l]]) >= max_min: l += 1
    else:
        min_ops += 1
        song = buckets[bidx[r]].pop() 
        buckets[bidx[l]].append(song) 
        song_band[song] = bidx[l]
print (max_min, min_ops)
print (*[song_band[song] for song in sorted(song_band.keys())])
