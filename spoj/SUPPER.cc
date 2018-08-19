// http://www.spoj.com/problems/SUPPER/

#include <bits/stdc++.h>
using namespace std;

struct task {

  const static int maxn = 1e5 + 1;
  int* ar;
  int* dp;
  static int n;

  int* st;

  task() {
    ar = new int[maxn];
    dp = new int[maxn];
    st = new int[3 * maxn];
  }

  int get_max(int x, int y, int i = 0, int l = 1, int r = maxn - 1) {
    if (y < l || x > r) return -1;
    if (x <= l && y >= r) return st[i];
    int mid = (l + r) >> 1;
    return max(get_max(x, y, 2 * i + 1, l, mid), get_max(x, y, 2 * i + 2, mid + 1, r));
  }

  void update(int x, int val, int i = 0, int l = 1, int r = maxn - 1) {
    if (x < l || x > r) return ;
    if (r - l < 1) {
      st[i] = val;
      return ;
    }
    int mid = (l + r) >> 1;
    update(x, val, 2 * i + 1, l, mid);
    update(x, val, 2 * i + 2, mid + 1, r);
    st[i] = max(st[2 * i + 1], st[2 * i + 2]);
  }

  void solve() {
    int nn;
    cin >> nn;
    for (int i = 0; i < 3 * maxn; ++i)
      st[i] = 0;
    int lis = 0;
    for (int i = 0; i < nn; ++i) {
      cin >> ar[i];
      if (ar[i] == 1) dp[i] = 1;
      else dp[i] = 1 + get_max(1, ar[i] - 1);
      update(ar[i], dp[i]);
      lis = max(lis, dp[i]);
    }

    set<pair<int, int> > s;
    set<pair<int, int> >::iterator it;
    vector<int> v;
    for (int i = nn - 1; i >= 0; --i) {
      if (dp[i] == lis) {
        s.insert(make_pair(dp[i], ar[i]));
        v.push_back(ar[i]);
      }
      else {
        it = s.lower_bound(make_pair(dp[i] + 1, ar[i]));
        if (it != s.end() && (*it).first == dp[i] + 1) {
          v.push_back(ar[i]);
          s.insert(make_pair(dp[i], ar[i]));
        }
      }
    }

    sort(v.begin(), v.end());
    cout << v.size() << endl;
    for (int i = 0; i < v.size(); ++i)
      cout << v[i] << " ";
    cout << endl;
    return ;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  task t;

  int tc = 10;
  while (tc--) {
    t.solve();
  } 

  return 0;
}