/*
  bfs on 2d grid
  good question
*/

#include <bits/stdc++.h>
using namespace std;

int n, m;

int move[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1},
					{1, 1}, {-1, -1}, {-1, 1}, {1, -1}};

string s[200];

typedef pair<int, int> ii;

int ans[200][200];

int a, b;

inline int dist(int x, int y) {
	return abs(x - a) + abs(y - b);
}

inline bool fineMove(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m && s[x][y] != '1' && ans[x][y] > dist(x, y);
}

void bfs(int i, int j) {
	a = i; b = j;
	queue<ii > q; q.push(ii(i, j));
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 8; ++i) {
			int xx = x + move[i][0];
			int yy = y + move[i][1];
			if (fineMove(xx, yy)) q.push(ii(xx, yy)), ans[xx][yy] = dist(xx, yy);
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t; cin >> t;
	while (t--) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i) cin >> s[i];
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) ans[i][j] = INT_MAX;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (s[i][j] == '1') bfs(i, j);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j)
				cout << (s[i][j] == '1' ? 0 : ans[i][j]) << " ";
			cout << "\n";
		}
	}

	return 0;
}
