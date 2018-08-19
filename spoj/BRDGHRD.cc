/**
* Longest Non Decreasing Sub-Seq
* O(NlogN)
* http://www.spoj.com/problems/BRDGHRD/
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 7;
pair<int, int> b[maxn];
int candies[maxn];

int ceiling(int x, int l, int r) {
  while (l < r) {
    int mid = (l + r) >> 1;
    if (candies[mid] > x) r = mid;
    else l = mid + 1;
  }
  return l;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  while (t--) {
    int n; cin >> n;
    for (int i = 0; i < n; ++i)
      cin >> b[i].first;
    for (int i = 0; i < n; ++i)
      cin >> b[i].second;
    sort(b, b + n);

    int len = 1;
    candies[0] = b[0].second;
    for (int i = 1; i < n; ++i) {
      int x = b[i].second;
      if (x < candies[0]) candies[0] = x;
      else if (x >= candies[len - 1]) candies[len++] = x;
      else candies[ceiling(x, 0, len - 1)] = x;
    }
    cout << len << endl;
  }

  return 0;
}
