// http://www.spoj.com/problems/DISQUERY/
// <NlogN, logN>
// Using dp for LCA

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 5;
const int logn = 20;
const int inf = 1e9;

int par[maxn][logn];
int dp[maxn][logn][2]; // min max
int h[maxn];

vector<pair<int, int> > g[maxn];

void dfs(int v, int p) {
  for (int i = 0; i < g[v].size(); ++i) {
    int u = g[v][i].first;
    if (u == p) continue;
    h[u] = h[v] + 1;
    par[u][0] = v;
    
    for (int j = 1; j < logn; ++j)
      if (par[u][j - 1] != -1)
        par[u][j] = par[par[u][j - 1]][j - 1];

    int w = g[v][i].second;

    dp[u][0][1] = dp[u][0][0] = w;
    for (int j = 1; j < logn; ++j) {
      if (par[u][j - 1] == -1) continue;
      dp[u][j][0] = min(dp[u][j - 1][0], dp[par[u][j - 1]][j - 1][0]);
      dp[u][j][1] = max(dp[u][j - 1][1], dp[par[u][j - 1]][j - 1][1]);
    }

    dfs(u, v);
  }
}

int lca(int u, int v) {
  if (h[u] > h[v]) swap(u, v);

  for (int i = logn - 1; i >= 0; --i) {
    if (h[v] - (1 << i) >= h[u]) {
      v = par[v][i];
    }
  }

  if (u == v) return v;

  for (int i = logn - 1; i >= 0; --i) {
    if (par[u][i] != -1 && par[u][i] != par[v][i]) {
      u = par[u][i];
      v = par[v][i];
    }
  }

  return par[v][0];
}

pair<int, int> get_minmax(int u, int p) {
  int up = h[u] - h[p];
  int mini = inf;
  int maxi = -1;
  for (int i = 0; i < logn; ++i) {
    if (up & (1 << i)) {
      mini = min(mini, dp[u][i][0]);
      maxi = max(maxi, dp[u][i][1]);
      u = par[u][i];
    }
  }
  return make_pair(mini, maxi);
}

void query() {
  int k; cin >> k;
  while (k--) {
    int u, v;
    cin >> u >> v;
    int p = lca(u, v);
    pair<int, int> up = get_minmax(u, p);
    pair<int, int> vp = get_minmax(v, p);
    cout << min(up.first, vp.first) << " ";
    cout << max(up.second, vp.second) << endl;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  vector<pair<int, int> > e;

  int n; cin >> n;
  assert(n <= 1e5);
  for (int i = 1; i < n; ++i) {
    int u, v, w;
    cin >> u >> v >> w;
    e.push_back(make_pair(v, u));
    g[v].push_back(make_pair(u, w));
    g[u].push_back(make_pair(v, w));
  } 

  memset(par, -1, sizeof(par));
  for (int i = 0; i <= n; ++i)
    for (int j = 0; j < logn; ++j)
      dp[i][j][0] = inf, dp[i][j][1] = -1;

  h[1] = 0;
  dfs(1, -1);

  query();

  return 0;
}