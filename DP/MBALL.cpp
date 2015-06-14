/*
  14 july 2015
  easy
*/
#include <bits/stdc++.h>
using namespace std;

#define ll long long
const int N = 1e5 + 1;
ll DP[N][9]; // 2 3 6 7 8

int p[] = {2, 3, 6, 7, 8};

inline void botup() {
	for (int i = 0; i < 5; ++i) DP[0][p[i]] = 1;
	ll val;
	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < 5; ++j) {
			val = 0;
			if (i - p[j] > 0) {
				for (int k = 0; k <= j; ++k) {
					val += DP[i - p[j]][p[k]];
				}
			}
			else if (i - p[j] == 0) val = 1;
			DP[i][p[j]] = val;
		}
	}
}

int main() {
	botup();
	ios::sync_with_stdio(0);
	int t; cin >> t;
	int n;
	ll ans; 
	while (t--) {
		cin >> n;
		ans = 0;
		if (n) for (int i = 0; i < 5; ++i) ans += DP[n][p[i]];
		else ans = 1;
		cout << ans << "\n";
	}

	return 0;
}
