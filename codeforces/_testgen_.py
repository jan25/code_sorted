n = 10**5
print (n)
import random
dirs = []
d = ['U', 'D', 'L', 'R']
for i in range(n):
	dirs.append(d[random.randint(0, 3)])
print (''.join(dirs))
