#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

const int BIN_LEN = 23;
const int N = 4194305;
int arr[N / 4];
int dict[N << 1] = {0};

unordered_map<int, int> memo[BIN_LEN];

int dp(int m, int n) {
  // cout << m << ' ' << n << endl;
  if (n < 0) return dict[m] ? m : -1;
  if (memo[n].find(m) != memo[n].end()) return memo[n][m];
  // if (dict[m]) {
  //   return memo[n][m] = m;
  // }
  if ((1 << n) & m) {
    memo[n][m] = dp(m ^ (1 << n), n - 1);
  } else {
    memo[n][m] = max(dp(m ^ (1 << n), n - 1), dp(m, n - 1));
  }
  return memo[n][m];
}


int main() {

  int n; cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
    dict[arr[i]] = 1;
  }

  for (int i = 0; i < BIN_LEN; ++i) {
    for (int j = 0; j < N; ++j) {
      memo[i][j] = dp(j, i);
    }
  }

  // for (int i = 0; i < n; ++i) {
  //   cout << dp((arr[i]), BIN_LEN - 1) << ' ';
  // }

  return 0;
}