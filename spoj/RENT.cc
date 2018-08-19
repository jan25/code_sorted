// http://www.spoj.com/problems/RENT/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e4 + 14;

int dp[maxn];

typedef struct {
  int s, f;
  int cost;
} order_details;

order_details order[maxn];

bool with_f(const order_details& a, const order_details& b) {
  return a.f < b.f;
}

int bs(int s, int r) {
  int l = 0;
  while (l < r) {
    int mid = (l + r + 1) >> 1;
    if (order[mid].f > s) r = mid - 1;
    else l = mid;
  }
  return l;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  order[0].s = order[0].f = -1;
  order[0].cost = 0;

  int tc; cin >> tc;
  while (tc--) {
    int n; cin >> n;
    for (int i = 1; i <= n; ++i) {
      cin >> order[i].s; 
      cin >> order[i].f;
      order[i].f += order[i].s;
      cin >> order[i].cost;
    }
    sort(order + 1, order + n + 1, with_f);
    dp[0] = order[0].cost;
    for (int i = 1; i <= n; ++i) {
      dp[i] = dp[bs(order[i].s, i - 1)] + order[i].cost;
      dp[i] = max(dp[i], dp[i - 1]);
    }
    cout << dp[n] << "\n";
  } 

  return 0;
}
