import sys

print('? %d %d' % (0, 0))
sys.stdout.flush()
agtb = int(input())

a, b = 0, 0
ops = 29
for i in range(ops, -1, -1):
    c = a | (1 << i)
    d = b
    print('? %d %d' % (c, d))
    sys.stdout.flush()
    x = int(input())
    
    c = a
    d = b | (1 << i)
    print('? %d %d' % (c, d))
    sys.stdout.flush()
    y = int(input())

    if x != y:
        if y == 1:
            a = a | (1 << i)
            b = b | (1 << i)
    else:
        if agtb == 1: # a > b
            a = a | (1 << i)
        else:
            b = b | (1 << i)
        agtb = x

print('! %d %d' % (a, b))
sys.stdout.flush()