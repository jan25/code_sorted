// http://www.spoj.com/problems/COUNT/

#include <bits/stdc++.h>
using namespace std;

struct task {

  const int N;
  const int mod;
  int** DP;

  task() : N(5001), mod(1988) {
    DP = new int*[N];
    for (int i = 0; i < N; ++i) {
      DP[i] = new int[N];
      for (int j = 0; j < N; ++j)
        DP[i][j] = -1;
    }
  }

  int dp(int n, int k) {
    if (k == 0) return 1;
    if (DP[n][k] != -1) return DP[n][k];
    int count = 0;
    for (int i = 0; i * (k + 1) <= n; ++i) {
      count += dp(n - i * (k + 1), k - 1);
      if (count > mod) count %= mod;
    }
    return DP[n][k] = count;
  }

  void solve(int n, int k) {
    cout << dp(n - k, k - 1) << endl;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  task t;

  int n, k;
  while ((cin >> n >> k) && n && k) {
    t.solve(n, k);
  }

  return 0;
}
