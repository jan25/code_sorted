n, m = map(int, input().split())
grid = [input() for i in range(n)]

def num_neighbors(i, j):
	num = 0
	for di in range(-1, 2):
		for dj in range(-1, 2):
			if di != 0 or di != dj:
				x, y = i + di, j + dj
				if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == '*':
					num += 1
	return num

result = "YES"
for i in range(n):
	for j in range(m):
		dig = ord(grid[i][j]) - 48;
		if grid[i][j] == '.': dig = 0
		if dig >= 0 and dig < 9:
			if num_neighbors(i, j) != dig:
				result = "NO"
print (result)

