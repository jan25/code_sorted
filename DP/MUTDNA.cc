// http://www.spoj.com/problems/MUTDNA/
/*
	DP O(N) solution
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e6 + 7;
int n;
int dp[maxn][2];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;
	string s; cin >> s;
	dp[0][0] = s[0] != 'B'; // to B
	dp[0][1] = s[0] != 'A'; // to A
	for (int i = 1; i < n; ++i) {
		if (s[i] == 'A') {
			dp[i][0] = min(1 + dp[i - 1][0], 1 + dp[i - 1][1]);
			dp[i][1] = min(1 + dp[i - 1][0], dp[i - 1][1]);
		}
		else {
			dp[i][0] = min(dp[i - 1][0], 1 + dp[i - 1][1]);
			dp[i][1] = min(1 + dp[i - 1][1], 1 + dp[i - 1][0]);
		}
	}

	cout << dp[n - 1][1] << endl;

	return 0;
}
