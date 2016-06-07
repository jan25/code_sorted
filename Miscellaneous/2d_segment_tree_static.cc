#include <bits/stdc++.h>
using namespace std;

#define m4 (i << 2)

int n, m;
const int maxn = 1001;
int mat[maxn][maxn];
int sum_mat[maxn][maxn];

int st[5 * maxn * maxn]; // static 2d segment tree

int inf = 1e9 + 7;

int sum(int a, int b, int c, int d) {
  return sum_mat[a][b] - sum_mat[a][d + 1]
          - sum_mat[c + 1][b] + sum_mat[c + 1][d + 1];
}

int build(int i = 0, int a = 0, int b = 0, int c = n - 1, int d = m - 1) {
  if (a > c || b > d) return -inf;
  if (a == c && b == d) {
    return st[i] = mat[a][b];
  }
  int max_i = build(m4 + 1, a, b, (a + c) >> 1, (b + d) >> 1);
  max_i = max(max_i, build(m4 + 2, a, 1 + (b + d) >> 1, (a + c) >> 1, d));
  max_i = max(max_i, build(m4 + 3, 1 + (a + c) >> 1, b, c, (b + d) >> 1));
  max_i = max(max_i, build(m4 + 4, 1 + (a + c) >> 1, 1 + (b + d) >> 1, c, d));
  return st[i] = max_i;
}

int max_int(int a, int b, int c, int d, int i = 0, int x1 = 0, int y1 = 0, int x2 = n - 1, int y2 = m - 1) {
  if (a > x2 || b > y2 || c < x1 || d < y1) return -inf;
  if (a <= x1 && b <= y1 && c >= x2 && d >= y2) return st[i];
  int max_i = max_int(a, b, c, d, m4 + 1, x1, y1, (x1 + x2) >> 1, (y1 + y2) >> 1);
  max_i = max(max_i, max_int(a, b, c, d, m4 + 2, x1, 1 + (y1 + y2) >> 1, (x1 + x2) >> 1, y2));
  max_i = max(max_i, max_int(a, b, c, d, m4 + 3, 1 + (x1 + x2) >> 1, y1, x2, (y1 + y2) >> 1));
  max_i = max(max_i, max_int(a, b, c, d, m4 + 4, 1 + (x1 + x2) >> 1, 1 + (y1 + y2) >> 1, x2, y2));
  return max_i; 
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  cin >> n >> m;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      cin >> mat[i][j];

  for (int i = n - 1; i >= 0; --i) {
    int sumr = 0;
    for (int j = m - 1; j >= 0; --j) {
      sumr += mat[i][j];
      sum_mat[i][j] = sum_mat[i + 1][j] + sumr;
    }
  } 

  build();

  int q; cin >> q;
  while (q--) {
    int r, c; cin >> r >> c;
    int res = 1e9 + 7;
    for (int i = 0; i + r <= n; ++i) {
      for (int j = 0; j + c <= m; ++j) {
        res = min(res, r * c * max_int(i, j, i + r - 1, j + c - 1) - 
                                  sum(i, j, i + r - 1, j + c - 1));
      }
    }
    cout << res << endl;
  }

  return 0;
}
