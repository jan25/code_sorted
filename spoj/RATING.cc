#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 7;
pair<pair<int, int>, int> c[maxn * 3];
int bit[maxn];
int bit2[maxn];
int ans[maxn * 3];

void add(int x, int val, int* bit) {
  while (x < maxn) {
    bit[x] += val;
    x += x & -x;
  }
}

int sum(int x, int* bit) {
  int res = 0;
  while (x > 0) {
    res += bit[x];
    x -= x & -x;
  }
  return res;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n; cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> c[i].first.first >> c[i].first.second;
    c[i].second = i;
  }
  sort(c, c + n);
  int p = -1;
  int cs = 0;
  for (int i = 0; i < n; ++i) {
    if (c[i].first.first != p) {
      for (int j = 1; j <= cs; ++j) {
        add(c[i - j].first.second, -1, bit2);
        add(c[i - j].first.second, 1, bit);
      }
      cs = 0;
      p = c[i].first.first;  
    }
    ans[c[i].second] = sum(c[i].first.second, bit) +
                        sum(c[i].first.second - 1, bit2);
    add(c[i].first.second, 1, bit2);
    ++cs;
  }
  for (int i = 0; i < n; ++i)
    cout << ans[i] << endl;

  return 0;
}
