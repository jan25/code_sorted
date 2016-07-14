// http://www.spoj.com/problems/CHICAGO/

#include <bits/stdc++.h>
using namespace std;

int n;
double g[123][123];
int vis[123];
double dist[123];
int prev[123];
int inf = 1234;

struct node {
  double d;
  int v;

  node (double d, int v) : d(d), v(v) { }

  bool operator < (const node& a) const {
    return d > a.d;
  }

};

double dijk() {
  priority_queue< node, vector<node> > pq;
  for (int i = 1; i <= n; ++i) {
    vis[i] = 0;
    dist[i] = inf;
    pq.push(*(new node(inf, i)));
  }
  dist[1] = 0;
  pq.push(*(new node(0, 1)));
  while (!pq.empty()) {
    int v = pq.top().v;
    double d = pq.top().d;
    pq.pop();
    if (vis[v]) continue;
    vis[v] = 1;
    for (int i = 1; i <= n; ++i) {
      if (!vis[i] && g[v][i]) {
        double w = -log(g[v][i] / 100);
        if (w + d < dist[i]) {
          dist[i] = w + d;
          pq.push(*(new node(dist[i], i)));
          prev[i] = v;
        }
      }
    }
  }
  
  double prob = 1;
  for (int v = n; v != 1; v = prev[v]) {
    prob *= (g[v][prev[v]] / 100);
  }

  return prob * 100;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  while (1) {
    cin >> n;
    if (!n) break;
    int m; cin >> m;
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= n; ++j)
        g[i][j] = 0;
    while (m--) {
      int a, b;
      double w;
      cin >> a >> b >> w;
      g[a][b] = g[b][a] = w;
    }
    cout << fixed << setprecision(6) << dijk() << " percent" << endl;

  }   

  return 0;
}
