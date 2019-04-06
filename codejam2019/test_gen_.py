from random import randint

def gen_rand_path(n):
    dirs = []
    for _ in range(n):
        dirs.append('S' if randint(0, 1) == 1 else 'E')
    return ''.join(dirs)

t = 100
print (t)
for _ in range(t):
    n = 1000
    print (n)
    print (gen_rand_path(n))