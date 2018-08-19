// http://www.spoj.com/problems/COMCB/

#include <bits/stdc++.h>
using namespace std;

int d[8][2] = {{-1, -2}, {1, -2},
                    {-2, -1}, {2, -1},
                    {-2, 1}, {2, 1},
                    {-1, 2}, {1, 2}};

struct task {

  int n, m;

  int vis[30][30];

  task() {
    cin >> n >> m;
  }

  void solve() {
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        if (path_exists(i, j)) {
          print_path(i, j);
          return ;
        }
      }
    }
    cout << -1 << endl;
  }

  void print_path(int x, int y) {
    while (!outside(x, y)) {
      cout << (char)(y + 'A' - 1);
      cout << x;
      if (vis[x][y] == 34) break;
      int xx = x + d[vis[x][y]][0];
      int yy = y +  d[vis[x][y]][1];
      x = xx; y = yy;
    }
    cout << endl;
  }

  bool path_exists(int x, int y) {
    memset(vis, -1, sizeof(vis));
    dfs(x, y);
    return complete();
  }

  void dfs(int x, int y) {
    if (vis[x][y] != -1 || outside(x, y)) return ;
    vis[x][y] = 34;
    if (complete()) return ;
    for (int i = 0; i < 8; ++i) {
      int xx = x + d[i][0];
      int yy = y + d[i][1];
      dfs(xx, yy);
      if (complete()) {
        vis[x][y] = i;
        return ;
      }
    }
    vis[x][y] = -1;
  }

  bool outside(int x, int y) {
    return x < 1 || x > n || y < 1 || y > m;
  }

  bool complete() {
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= m; ++j)
        if (vis[i][j] == -1) return false;
    return true;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int tc; cin >> tc;
  while (tc--) {
    task t;
    t.solve();
  }

  return 0;
}
