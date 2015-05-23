/*
    date:   23 05 2015
*/
//bottom up dp. O(n)

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	
	int DP[21][3];
	DP[0][0] = DP[0][1] = DP[0][2] = 0;
	int n, t, a, b, c, d; cin >> t;
	while (t--) {
		cin >> n;
		if (n) {
			cin >> DP[1][0] >> DP[1][1] >> DP[1][2];
			for (int i = 2; i <= n; ++i) {
				cin >> DP[i][0] >> DP[i][1] >> DP[i][2];
				for (int j = 0; j < 3; ++j) {
					DP[i][j] += min(DP[i - 1][(j + 1) % 3],
									DP[i - 1][(j + 2) % 3]);
				}
			}
			cout << min(DP[n][0], min(DP[n][1], DP[n][2]));
		}
		else cout << 0;
		cout << "\n";
	}

	return 0;
}
