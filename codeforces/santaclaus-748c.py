n = int(input())
moves = input()

rev = { 'R':'L', 'U':'D', 'L':'R', 'D':'U' }
seen = set()
min_pts = 1
for move in moves:
	if rev[move] in seen:
		min_pts += 1
		seen = set()
	seen.add(move)
print (min_pts)
