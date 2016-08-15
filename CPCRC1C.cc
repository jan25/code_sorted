#include <bits/stdc++.h>
using namespace std;

struct task {

  long long dp[10][2][100];
  int len;
  vector<int> digs;

  task(int a) {
    len = 0;
    while (a) {
      len++;
      digs.push_back(a % 10);
      a /= 10;
    }
    reverse(digs.begin(), digs.end());

    memset(dp, -1, sizeof(dp));
  }

  long long solve(int size = 0, int equal = 1, int sum = 0) {
    if (size == len) {
      return sum;
    }
    if (dp[size][equal][sum] != -1)
      return dp[size][equal][sum];

    long long sol = 0;
    for (int i = 0; i < 10; ++i) {
      if (equal && i > digs[size]) {
        break;
      }
      sol += solve(size + 1, equal && i == digs[size], sum + i);
    }

    return dp[size][equal][sum] = sol;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  while (1) {
    long long b; cin >> b;
    if (b < 0) break;
    if (b > 0) b = (new task(b - 1))->solve();
    long long a; cin >> a;
    a = (new task(a))->solve();
    cout << a - b << endl;
  }

  return 0;
}