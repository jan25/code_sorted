#include <bits/stdc++.h>
using namespace std;

#define ll long long

const int N = 2e5;
const int Z = 1e6;
ll heights[N];
ll min_up[N];
ll min_down[N];

int this_height_works(double h, int n) {
  double max_h = min((double)2 * Z, 2 * heights[0] + h),
      min_h = max(0.0, 2 * heights[0] - h);

  for (int i = 0; i < n - 1; ++i) {
    double next_max_h = min((double)2 * Z, 2 * heights[i + 1] + h),
        next_min_h = max(0.0, 2 * heights[i + 1] - h);

    double possible_max_h = min((double)2 * Z, max_h + 2 * min_up[i]),
        possible_min_h = max(0.0, min_h - 2 * min_down[i]);

    if (possible_min_h > next_max_h || next_min_h > possible_max_h) {
      return 0;
    }

    max_h = min(next_max_h, possible_max_h);
    min_h = max(next_min_h, possible_min_h);
  }

  return 1;
}

int main() {

  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    
    int n, m; cin >> n >> m;
    cin >> heights[0] >> heights[1];
    min_up[0] = min_down[0] = Z;    
    min_up[1] = min_down[1] = Z;

    ll w, x, y, z;
    cin >> w >> x >> y >> z;
    for (int i = 2; i < n; ++i) {
      heights[i] = (w * heights[i - 2] + x * heights[i - 1] + y) % z;

      min_up[i] = min_down[i] = Z;
    }


    for (int i = 0; i < m; ++i) {
      ll a, b, u, d;
      cin >> a >> b >> u >> d;
      if (a > b) swap(a, b), swap(u, d);

      a--; b--;
      for (int j = a; j < b; ++j) {
        min_up[j] = min(min_up[j], u);
        min_down[j] = min(min_down[j], d);
      }
    }

    int l = 0, r = 2 * Z;
    while (l < r) {
      int h = (l + r) >> 1;
      if (this_height_works(h, n)) r = h;
      else l = h + 1;
    }

    // double try_lesser_height = (double)l - 0.5;
    // if (this_height_works(try_lesser_height, n))
    //   cout << try_lesser_height;
    // else cout << l;
    
    cout << (double)l / 2.0 << endl;

    // cout << endl;
  }

  return 0;
}