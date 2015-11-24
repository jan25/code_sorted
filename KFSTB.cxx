// http://www.spoj.com/problems/KFSTB/
/*
  DFS --> shortest path dag --> DP
  O(n) time
*/

#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
const int mod = 1e9 + 7;

const int maxn = 1e4 + 7;
vi g[maxn];
vi dag[maxn];
int s, t;
int c, b;
int tc;

int vis[maxn];

void dfs(int v = s) {
	vis[v] = -1;
	for (int i = 0; i < g[v].size(); ++i)
		if (!vis[g[v][i]]) {
			dfs(g[v][i]);
			dag[g[v][i]].pb(v);
		}
		else if (vis[g[v][i]] + 1) {
			dag[g[v][i]].pb(v);
		}
	vis[v] = 1;
}

int DP[maxn];

int dp(int v = t) {
	if (DP[v] + 1) return DP[v];
	int ans = 0;
	for (int i = 0; i < dag[v].size(); ++i) {
		ans += dp(dag[v][i]);
		ans %= mod;
	}
	return DP[v] = ans;
}

void solve() {
	memset(vis, 0, sizeof(vis));
	dfs();

	memset(DP, -1, sizeof(DP));
	DP[s] = 1;
	cout << dp() << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> tc;
	while (tc--) {
		cin >> c >> b >> s >> t;
		for (int i = 1; i <= c; ++i) {
			g[i].clear();
			dag[i].clear();
		}
		for (int i = 0; i < b; ++i) {
			int x, y; cin >> x >> y;
			g[x].pb(y);
		}
		solve();
	}

	return 0;
}
