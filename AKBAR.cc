#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e6 + 7;
int vis[maxn];

vector<int> g[maxn];

bool dfs(int v, int s, int m, int p = -1) {
  if (vis[v] > 0 && vis[v] != m) return false;
  else vis[v] = m;
  if (s == 0) return true;
  bool res = true;
  for (int i = 0; i < g[v].size(); ++i)
    if (p != g[v][i]) res = res && dfs(g[v][i], s - 1, m, v);
  return res;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  while (t--) {
    int n, r, m;
    cin >> n >> r >> m;
    for (int i = 1; i <= n; ++i)
      g[i].clear();
    while (r--) {
      int a, b; cin >> a >> b;
      g[a].push_back(b);
      g[b].push_back(a);
    }
    memset(vis, 0, sizeof(vis));
    string ans = "Yes";
    while (m--) {
      int k, s; cin >> k >> s;
      if (!dfs(k, s, m + 1)) {
        ans = "No";
        break;
      }
    }
    for (int i = 1; i <= n; ++i) {
      if (!vis[i]) {
        ans = "No";
        break;
      }
    }
    cout << ans << endl;
  } 

  return 0;
}
