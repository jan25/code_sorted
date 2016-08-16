// http://www.spoj.com/problems/TRANCLS/
// using all pairs shortest path algorithm
// N^3 steps per test case

#include <bits/stdc++.h>
using namespace std;

const int N = 100;
int inf = 1234;

int g[N][N];

void solve() {
  int n; cin >> n;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      g[i][j] = inf;

  for (int i = 0; i < n; ++i) {
    int a, b; cin >> a >> b;
    g[a][b] = 1;
  }

  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (g[i][k] + g[k][j] < g[i][j])
          g[i][j] = g[i][k] + g[k][j];
      }
    }
  }

  int e = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (g[i][j] < inf && g[i][j] > 1) e++;
    } 
  }

  cout << (e) << endl;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int tc; cin >> tc;
  for (int i = 1; i <= tc; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }

  return 0;
}