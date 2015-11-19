// http://www.spoj.com/problems/PROSCORE
/*
  bitwise. easy
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t; cin >> t;
	int tc = 1;
	while (t--) {
		cout << "Case " << tc++ << ": ";
		int n, p; cin >> n >> p;
		int g[11][11];
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < p; ++j) {
				cin >> g[i][j];
			}
		}
		int ans = 0;
		int cond = 1;
		for (int i = 0; i < p; ++i) {
			int tmp = 0;
			for (int j = 0; j < n; ++j) {
				if (g[j][i]) {
					tmp = 1;
					break;
				}
			}
			cond = cond && tmp;
		}
		ans |= (cond << 2);
		int a = 1, b = 1;
		for (int i = 0; i < n; ++i) {
			int sum = 0;
			for (int j = 0; j < p; ++j) {
				sum += g[i][j];
			}
			a = a && (sum > 0);
			b = b && (sum < p);
		}
		ans |= (a << 1);
		ans |= b;
		cout << ans << endl;
	}
	return 0;
}
