//http://www.spoj.com/problems/NOVICE63/

#include <bits/stdc++.h>
using namespace std;

struct task {

  long long ncr[61][61];

  task() {
    ncr[0][0] = 1;
    ncr[1][0] = ncr[1][1] = 1;
    for (int i = 2; i < 60; ++i) {
      ncr[i][0] = 1;
      for (int j = 1; j < i; ++j)
        ncr[i][j] = ncr[i - 1][j] + ncr[i - 1][j - 1];
      ncr[i][i] = 1;
    }
  }

  void solve(long long n) {
    int len = 0;
    while ((1LL << len) <= n) len++;
    long long count = len == 2;
    for (int l = 2; l < len; l += 2) {
      count += ncr[l - 1][l / 2];
    }
    cout << count << endl;
  }

};


int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
 
  task t;

  int tc; cin >> tc;
  while (tc--) {
    long long n; cin >> n;
    t.solve(n);
  }

  return 0;
}
