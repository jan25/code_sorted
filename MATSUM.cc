/**
* 2d BIT
* http://www.spoj.com/problems/MATSUM/
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1025;
int mat[maxn][maxn];
int used[maxn][maxn];
int bit[maxn][maxn];
int n;
int t;

void add(int x, int y, int val) {
  while (x <= n) {
    int yy = y;
    while (yy <= n) {
      bit[x][yy] += val;
      yy += yy & -yy;
    }
    x += x & -x;
  }
}

void setval(int x, int y, int val) {
  if (used[x][y] == t) add(x, y, -mat[x][y]);
  else used[x][y] = t;
  mat[x][y] = val;
  add(x, y, val);
}

int bitsum(int x, int y) {
  int s = 0;
  while (x > 0) {
    int yy = y;
    while (yy > 0) {
      s += bit[x][yy];
      yy -= yy & -yy;
    }
    x -= x & -x;
  }
  return s;
}

int _matsum(int a, int b, int x, int y) {
  return bitsum(x, y) - bitsum(a - 1, y) - 
          bitsum(x, b - 1) + bitsum(a - 1, b - 1);
}

int main() {
  bool printed = false;
  int tc; 
  scanf("%d", &tc);
  while (tc--) {
    t = tc + 1;
    scanf("%d", &n);
    memset(bit, 0, sizeof(bit));
    while (1) {
      char op[4];
      scanf("%s", op);
      if (strcmp(op, "END") == 0) break;
      if (strcmp(op, "SET") == 0) {
        int x, y, val;
        scanf("%d %d %d", &x, &y, &val);
        setval(x + 1, y + 1, val);
      }
      else if (strcmp(op, "SUM") == 0) {
        int a, b, x, y;
        scanf("%d %d %d %d", &a, &b, &x, &y);
        printf("%d\n", _matsum(a + 1, b + 1, x + 1, y + 1));
        printed = true;
      }
    }
    printf("\n");
  } 

  return 0;
}
