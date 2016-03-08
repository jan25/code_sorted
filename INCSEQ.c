/**
* using k BITs in O(n * k * log(max(S))
* http://www.spoj.com/problems/INCSEQ/
*/

#include <stdio.h>
#include <stdlib.h>
#define maxn 1e5 + 7
#define maxk 51

int n, k;
int mod = 5e6;
int _bit[maxk][(const int)maxn];

int sum(int n, int k) {
  int res = 0;
  while (n > 0) {
    res += _bit[k][n];
    if (res > mod)
      res %= mod;
    n -= n & -n;
  }
  return res;
}

void add(int n, int k, int val) {
  while (n < maxn) {
    _bit[k][n] += val;
    if (_bit[k][n] > mod)
      _bit[k][n] %= mod;
    n += n & -n;
  }
}

int main() {
  scanf("%d %d", &n, &k);
  int ans = 0;
  while (n--) {
    int x;
    scanf("%d", &x);
    ++x;
    add(x, 1, 1);
    int i;
    for (i = 2; i <= k; ++i)
      add(x, i, sum(x - 1, i - 1));
  }
  printf("%d\n", sum(maxn - 1, k));

  return 0;
}
