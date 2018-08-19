/**
* http://www.spoj.com/problems/TRAFFICN/
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e4 + 7;
vector<pair<int, int> > g[maxn];
vector<pair<int, int> > rg[maxn];
int dists[maxn];
int distt[maxn];
int vis[maxn];
int inf = 1061109567;
int n, m, k;
int s, t;

void dijk(int s, vector<pair<int, int> >* g, int* dist) {
  for (int i = 1; i <= n; ++i) dist[i] = inf;
  memset(vis, 0, sizeof(vis));
  dist[s] = 0;
  vis[s] = 1;
  queue<int> q;
  q.push(s);
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    vis[v] = 0;
    for (int i = 0; i < g[v].size(); ++i) {
      int vv = g[v][i].first;
      if (dist[vv] > dist[v] + g[v][i].second) {
        dist[vv] = dist[v] + g[v][i].second;
        if (!vis[vv]) {
          vis[vv] = 1;
          q.push(vv);
        }
      }
    }
  }
}

int minDist(int u, int v) {
  return min(distt[u] + dists[v], distt[v] + dists[u]);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int tc; cin >> tc;
  while (tc--) {
    cin >> n >> m >> k;
    cin >> s >> t;
    for (int i = 1; i <= n; ++i) {
      g[i].clear();
      rg[i].clear();
    }
    while (m--) {
      int a, b;
      cin >> a >> b;
      int w; cin >> w;
      g[a].push_back(make_pair(b, w));
      rg[b].push_back(make_pair(a, w));
    }
    dijk(s, g, dists);
    dijk(t, rg, distt);
    int ans = dists[t];
    while (k--) {
      int u, v, w;
      cin >> u >> v >> w;
      ans = min(ans, minDist(u, v) + w);
    }
    cout << (dists[t] < inf ? ans : -1) << endl;
  } 

  return 0;
}
