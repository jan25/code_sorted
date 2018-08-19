#include <bits/stdc++.h>
using namespace std;

#define mid ((l + r) >> 1)

const int N = 2e4 + 7;
int a[N];
int st[4 * N];
int n, k;
int allset = (1 << 30) - 1; 

void build(int i = 0, int l = 0, int r = n - 1) {
  if (r - l < 1) {
    st[i] = a[l];
    return ;
  }
  build((i << 1) + 1, l, mid);
  build((i << 1) + 2, mid + 1, r);
  st[i] = st[(i << 1) + 1] & st[(i << 1) + 2];
}

int getand(int x, int y, int i = 0, int l = 0, int r = n - 1) {
  if (x > r || y < l) return allset;
  if (x <= l && y >= r) return st[i];
  return getand(x, y, (i << 1) + 1, l, mid) &
          getand(x, y, (i << 1) + 2, mid + 1, r);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int t; cin >> t;
  while (t--) {
    cin >> n >> k;
    int complete_and = allset;
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
      complete_and &= a[i];
    }
    build();
    int kk = 2 * k + 1;
    for (int i = 0; i < n; ++i) {
      if (kk >= n) {
        cout << complete_and;
      }
      else {
        int l = (i - k + n) % n;
        int r = (i + k) % n;
        cout << (l < r ? getand(l, r) : (getand(0, r) & getand(l, n - 1)));
      }
      if (i < n - 1) cout << " ";
    }
    cout << "\n";
  } 

  return 0;
}
