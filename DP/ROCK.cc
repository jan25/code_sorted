#include <bits/stdc++.h>
using namespace std;

string s;
int pre[210];
int DP[210][210];

int sum(int a, int b) {
  int ones = pre[b] - (a > 0 ? pre[a - 1] : 0);
  int zeros = b - a + 1 - ones;
  return ones - zeros;
}

int dp(int a, int b) {
  if (sum(a, b) > 0) return b - a + 1;
  if (a == b) return 0;
  if (DP[a][b] + 1) return DP[a][b];
  for (int i = a + 1; i <= b; ++i)
    DP[a][b] = max(DP[a][b], dp(a, i - 1) + dp(i, b));
  return DP[a][b];
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int tc; cin >> tc;
  while (tc--) {
    int n; cin >> n;
    cin >> s;
    pre[0] = s[0] == '1';
    for (int i = 1; i < n; ++i)
      pre[i] = pre[i - 1] + (s[i] == '1');
    memset(DP, -1, sizeof(DP));
    cout << dp(0, n - 1) << "\n";
  }

  return 0;
}
