#include <bits/stdc++.h>
using namespace std;

struct task {

  int vis[1000][1000];
  string g[1000];
  int n, m;

  task() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
      cin >> g[i];
  }

  void solve() {
    int cc = 0;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        vis[i][j] = 0;
    int it = 1;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int x = i, y = j;
        while (can_move(x, y)) {
          vis[x][y] = it;
          x += dx(g[x][y]);
          y += dy(g[x][y]);
        }
        if (!inside(x, y)) ++cc;
        else if (vis[x][y] == it) ++cc;
        ++it;
      }
    }
    cout << cc << "\n";
  }

  int dx(char c) {
    if (c == 'N') return -1;
    if (c == 'S') return 1;
    return 0;
  }

  int dy(char c) {
    if (c == 'E') return 1;
    if (c == 'W') return -1;
    return 0;
  }

  bool can_move(int x, int y) {
    return inside(x, y) && !vis[x][y];
  }

  bool inside(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  task t;
  t.solve();

  return 0;
}
