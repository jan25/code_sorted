/*
  Ford Fulkerson algo
  O(f * (n + m))
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 135;
int g[maxn][maxn];
int par[maxn];
int vis[maxn];

int inf = 1e9 + 7;

bool dfs(int v = 'A') {
  if (v == 'Z') return true;
  if (vis[v]) return false;
  int reached = false;
  for (int i = 'A'; i <= 'z'; ++i) {
    if (g[v][i]) {
      par[i] = v;
      reached = reached || dfs(i);      
    }
  }
  return reached;
}

int ffs() {
  int total_f = 0;
  memset(par, -1, sizeof(par));
  while (dfs()) {
    memset(vis, 0, sizeof(vis));
    int f = inf;
    for (int i = 'Z'; i != 'A'; i = par[i]) {
      f = min(g[par[i]][i], f);
    }
    for (int i = 'Z'; i != 'A'; i = par[i]) {
      g[par[i]][i] -= f;
    }
    total_f += f;
  }
  return total_f;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m; cin >> m;
  char a, b;
  for (int i = 0; i < m; ++i) {
    cin >> a >> b;
    int c; cin >> c;
    g[a][b] += c;
  }
  cout << ffs() << "\n";

  return 0;
}
