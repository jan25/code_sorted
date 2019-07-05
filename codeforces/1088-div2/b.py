n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a) - {0})
a.sort()
diff = 0
for i in range(k):
    if i >= len(a):
        print (0)
    else:
        print(max(0, a[i] - diff))
        diff = a[i]