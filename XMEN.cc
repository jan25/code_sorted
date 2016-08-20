#include <bits/stdc++.h>
using namespace std;

struct task {

  int n;
  int* ind;
  int* t;
  const int inf;

  task() : inf(1e9) {
    ind = new int[(int)1e5 + 1];
    t = new int[(int)3e5 + 1];
  }

  void solve() {
    scanf("%d", &n);
    assert(n > 0 && n <= (int)1e5);
    for (int i = 1; i <= n; ++i) {
      int x; scanf("%d", &x);
      ind[x] = i;
    }
    for (int i = 0; i < (int)3e5 + 1; ++i)
      t[i] = 0;
    int ans = 1;
    for (int i = 1; i <= n; ++i) {
      int x; scanf("%d", &x);
      int sol = 1 + (ind[x] > 1 ? get(1, ind[x] - 1) : 0);
      ans = max(ans, sol);
      put(ind[x], sol);
    }
    printf("%d\n", ans);
  }

  void put(int x, int val, int i = 0, int l = 1, int r = (int)1e5) {
    if (x < l || x > r) return ;
    if (r - l < 1) {
      t[i] = val;
      return ;
    }
    int mid = (l + r) >> 1;
    put(x, val, (i << 1) + 1, l, mid);
    put(x, val, (i << 1) + 2, mid + 1, r);
    t[i] = max(t[(i << 1) + 1], t[(i << 1) + 2]);
  }

  int get(int x, int y, int i = 0, int l = 1, int r = (int)1e5) {
    if (y < l || x > r) return -inf;
    if (x <= l && y >= r) return t[i];
    int mid = (l + r) >> 1;
    return max(get(x, y, (i << 1) + 1, l, mid),
                get(x, y, (i << 1) + 2, mid + 1, r));
  }

  ~task() {
    delete[] ind;
    delete[] t;
  }

};

int main() {
  task t;
  int tc; scanf("%d", &tc);
  while (tc--) {
    t.solve();
  } 

  return 0;
}