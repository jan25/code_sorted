/*
  16 aug 2015
  
  Lowest common ancestor. using Heavy light Decomposition
*/

#include <bits/stdc++.h>
using namespace std;
#define iOS ios::sync_with_stdio(0);
#define vi vector<int>
#define pb push_back
#define mp make_pair

const int maxn = 1e3 + 7;

int n;
int root;
int par[maxn];
vi adj[maxn];

int heavy[maxn];
int size[maxn];
int chain[maxn];
int head[maxn];

int height[maxn];

void dfs(int v) {
	size[v] = 1;
	for (int i = 0; i < adj[v].size(); ++i) {
		int c = adj[v][i];
		height[c] = height[v] + 1;
		dfs(c);
		size[v] += size[c];
		if (heavy[v] == -1 || size[c] > size[heavy[v]]) {
			heavy[v] = c;
		}
	}
}

void hld() {
	memset(heavy, -1, sizeof(heavy));
	height[root] = 1;
	dfs(root);
	memset(chain, 0, sizeof(chain));
	int cnum = 1;
	memset(head, 0, sizeof(head));
	for (int i = 1; i <= n; ++i) {
		if (par[i] == -1 || heavy[par[i]] != i) {
			int j = i;
			while (j != -1) {
				chain[j] = cnum;
				head[j] = i;
				j = heavy[j];
			}
			++cnum;
		}
	}
}

int lca(int a, int b) {
	while (chain[a] != chain[b]) {
		if (height[head[a]] < height[head[b]]) 
			swap(a, b);

		a = par[head[a]];
	}
	return height[a] < height[b] ? a : b;
}

int main() {
	iOS;
	// freopen("input.txt", "r", stdin);
	int t; cin >> t;
	for (int tc = 1; tc <= t; ++tc) {
		cin >> n;
		memset(par, -1, sizeof(par));
		for (int i = 1; i <= n; ++i) {
			adj[i].clear();
			int e; cin >> e;
			while (e--) {
				int v; cin >> v;
				adj[i].pb(v);
				par[v] = i;
			}
		}
		for (int i = 1; i <= n; ++i)
			if (par[i] == -1) {
				root = i;
				break;
			}

		hld();

		cout << "Case " << tc << ": \n";
		int m; cin >> m;
		while (m--) {
			int a, b;
			cin >> a >> b;
			cout << lca(a, b) << "\n";
		}
	}

	return 0;
}
