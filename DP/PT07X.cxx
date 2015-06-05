// vertex cover with top down comp
// O(n)

#include <bits/stdc++.h>
using namespace std;
#define iOS ios::sync_with_stdio(0)
#define pb push_back

const int N = 100001;
int DP[N][2];

vector<vector<int> > adj;

void dfs(int i, int p) {
	if (adj[i].size() == 1 && p != -1) {
		DP[i][0] = 0;
		DP[i][1] = 1;
		return ;
	}
	DP[i][0] = 0;
	DP[i][1] = 1;
	for (int j = 0; j < adj[i].size(); ++j) {
		if (adj[i][j] != p) {
			dfs(adj[i][j], i);
			DP[i][0] += DP[adj[i][j]][1];
			DP[i][1] += min(DP[adj[i][j]][0], DP[adj[i][j]][1]);
		}
	}
}

int main() {
	iOS;
	int n; cin >> n;
	int a, b;
	adj.resize(n + 1);
	--n; // n-1 edges in tree
	while (n--) {
		cin >> a >> b;
		adj[a].pb(b);
		adj[b].pb(a);
	}
	dfs(1, -1);
	cout << min(DP[1][0], DP[1][1]);

	return 0;
}
