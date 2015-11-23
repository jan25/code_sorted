// http://www.spoj.com/problems/MARTIAN/
/*
  DP O(n * m)
  using prefix sum
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 5e2 + 7;

int n, m;
int y[maxn][maxn];
int b[maxn][maxn];

void input(int a[][maxn]) {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			cin >> a[i][j];
}

int DP[maxn][maxn][2];
int vis[maxn][maxn][2];

int tc = 1;

int dp(int r, int c, int dir) {
	if (r == -1 || c == -1) return 0;
	if (vis[r][c][dir] == tc) return DP[r][c][dir];
	vis[r][c][dir] = tc;
	if (dir) return DP[r][c][dir] = max(dp(r, c - 1, 0), dp(r, c - 1, 1)) + b[r][c];
	return DP[r][c][dir] = max(dp(r - 1, c, 0), dp(r - 1, c, 1)) + y[r][c];
}

void solve() {
	tc++;
	for (int i = 0; i < n; ++i) {
		for (int j = 1; j < m; ++j)
			y[i][j] += y[i][j - 1];
	}
	for (int i = 1; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			b[i][j] += b[i - 1][j];
		}
	}

	cout << max(dp(n - 1, m - 1, 0), dp(n - 1, m - 1, 1)) << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		cin >> n >> m;
		if (!n) break;
		input(y);
		input(b);
		solve();
	}

	return 0;
}
