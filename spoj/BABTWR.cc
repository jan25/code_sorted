// http://www.spoj.com/problems/BABTWR/

#include <bits/stdc++.h>
using namespace std;

int n;
int dim[34][3];
int DP[34][3];

pair<int, int> get_dim(int ai, int ao) {
  int l = dim[ai][(ao + 1) % 3];
  int b = dim[ai][(ao + 2) % 3];
  if (l < b) swap(l, b);
  return pair<int, int>(l, b);
}

bool can_be_below(int ai, int ao, int bi, int bo) {
  pair<int, int> adim = get_dim(ai, ao);
  pair<int, int> bdim = get_dim(bi, bo);
  return adim.first > bdim.first && adim.second > bdim.second;
}

int dp(int bi, int ori) {
  if (DP[bi][ori] != -1) return DP[bi][ori];
  int h = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < 3; ++j) {
      if (can_be_below(i, j, bi, ori)) {
        h = max(h, dp(i, j));
      }
    }
  }
  return DP[bi][ori] = dim[bi][ori] + h;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  while (1) {
    cin >> n;
    if (!n) break;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < 3; ++j)
        cin >> dim[i][j];

    dim[n][0] = dim[n][1] = dim[n][2] = 0;

    memset(DP, -1, sizeof(DP));
    cout << dp(n, 0) << "\n";
  }  

  return 0;
}
