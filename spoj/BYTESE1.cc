// http://www.spoj.com/problems/BYTESE1/
/*
  2d grid. shortest path
  dijkstra
  O(NlogN)
*/

#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define ii pair<int,int>
#define all(x) x.begin(),x.end()

const int maxn = 1e2 + 7;
int g[maxn][maxn];
int m, n; // rows cols
int a, b, t;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

struct comp {
	bool operator () (const pair<int, ii > &a, const pair<int, ii > &b) {
		return a.first > b.first;
	}
};

priority_queue< pair<int, ii >, vector<pair<int, ii> >, comp> q;

int dist[maxn][maxn];

int inf = 1e9 + 7;

int ok(int x, int y) {
	return x > 0 && x <= m && y > 0 && y <= n;
}

int solve() {
	q.push(mp(g[1][1], ii(1, 1)));
	for (int i = 0; i < maxn; ++i)
		for (int j = 0; j < maxn; ++j)
			dist[i][j] = inf;
	dist[1][1] = g[1][1];

	while (!q.empty()) {
		int w = q.top().first;
		int x = q.top().second.first;
		int y = q.top().second.second;
		q.pop();
		for (int i = 0; i < 4; ++i) {
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (ok(xx, yy) && dist[xx][yy] > w + g[xx][yy]) {
				dist[xx][yy] = w + g[xx][yy];
				q.push(mp(dist[xx][yy], ii(xx, yy)));
			}
		}
	}
	return dist[a][b];
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int k; cin >> k;
	while (k--) {
		cin >> m >> n;
		for (int i = 1; i <= m; ++i)
			for (int j = 1; j <= n; ++j)
				cin >> g[i][j];
		cin >> a >> b >> t;
		int mind = solve();
		if (mind <= t) {
			cout << "YES\n";
			cout << t - mind << endl;
		}
		else cout << "NO\n";
	}

	return 0;
}
