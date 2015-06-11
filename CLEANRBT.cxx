#include <bits/stdc++.h>
using namespace std;
#define sf scanf
#define pf printf
#define iOS ios::sync_with_stdio(0)
#define pb push_back
#define mp make_pair
#define isin(x, y) (x >= 0 && y >= 0 && x < h && y < w)

const int N = 30;
map<int, pair<int, int> > m;
map<pair<int, int>, int> rm;	
string s[N];
int move[8] = {1, 0, -1, 0, 0, 1, 0, -1};
const int inf = 1e9;
int DP[N][N][1200]; // x vis_hash
int d = 0; // total num of dirty
int w, h;
int v[20]; // visited dirty
int spl[N][N][N][N]; // all pairs shortest path
pair<int, int> t[N][N];
vector<pair<int, int> > D;
int V[N][N];

int hash() {
	int h = 0;
	for (int i = 0; i < 11; ++i) {
		if (v[i]) 
			h |= (1 << (i - 1));
	}
	return h;
}

int sp(int a, int b, int x, int y) { // shortest path
	return spl[a][b][x][y];
}

int dp(int x, int y, int done) {
	if (done == d) return 0;
	int h = hash();
	if (s[x][y] == '*') {
		if (DP[x][y][h] != -1) 
			return DP[x][y][h];
		else {
			v[rm[mp(x, y)]] = 1;
		}
	} 
	int minv = inf;
	for (int i = 1; i <= d; ++i) {
		if (!v[i]) {
			int tmp = minv;
			minv = min(minv, sp(x, y, m[i].first, m[i].second) + 
								dp(m[i].first, m[i].second, done + 1));
		}
	}
	v[rm[mp(x, y)]] = 0;
	return DP[x][y][h] = minv;
}

int bfs(int a, int b, int x, int y) {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			t[i][j] = mp(-1, -1);
		}
	}
	queue<pair<int, int> > q;
	q.push(mp(a, b));
	int nx, ny, nnx, nny;
	V[a][b] = 1;
	while (1) {
		if (q.empty()) break;
		int n = q.size();
		while (n--) {
			nx = q.front().first;
			ny = q.front().second;
			q.pop();
			q.push(mp(nx, ny));
		}
		nx = q.front().first;
		ny = q.front().second;
		q.pop();
		if (nx == x && ny == y) break;
		for (int i = 0; i < 8; i += 2) {
			nnx = nx + move[i];
			nny = ny + move[i + 1];
			if (isin(nnx, nny) && 
						s[nnx][nny] != 'x' && 
								!V[nnx][nny]) {
				q.push(mp(nnx, nny));
				t[nnx][nny] = mp(nx, ny);
				V[nnx][nny] = 1;
			}
		}
	}
	if (nx != x || ny != y) return -1;
	int dist = 0;
	while (t[x][y].first != -1 && t[x][y].second != -1) {
		++dist;
		nx = t[x][y].first;
		y = t[x][y].second;
		x = nx;
	}
	return dist;
}

int main() {
	iOS;

	cin >> w >> h;
	while (w) {
		int x, y;
		int sx, sy;
		
		m.clear();
		rm.clear();
		D.clear();
		d = 0;
		for (int i = 0; i < h; ++i) {
			cin >> s[i];
			for (int j = 0; j < w; ++j) {
				if (s[i][j] == 'o') {sx = i; sy = j;}
				if (s[i][j] == '*') {
					D.pb(mp(i, j));
					m[++d] = make_pair(i, j);
					rm[mp(i, j)] = d;
				}
			}
		}
		D.pb(mp(sx, sy));
		memset(v, 0, sizeof(v));
		memset(DP, -1, sizeof(DP));
		memset(spl, -1, sizeof(spl));
		int a, b; int dist = 0;
		for (int i = 0; i < D.size(); ++i) {
				x = D[i].first; y = D[i].second;
			for (int j = 0; j < D.size(); ++j) {
				a = D[j].first; b = D[j].second;
				memset(V, 0, sizeof(V));
				dist = bfs(a, b, x, y);
				spl[x][y][a][b] = spl[a][b][x][y] = dist;
				if (dist == -1) goto here;
			}
		}
		here:
		int ans;
		if (dist == -1) cout << -1;
		else cout << (ans = dp(sx, sy, 0));
		cout << endl;

		cin >> w >> h;
	}

	return 0;
}

