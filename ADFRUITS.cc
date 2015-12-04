// http://www.spoj.com/problems/ADFRUITS/
/*
  DP; LCS; find LCS;
  O(n * n)
*/

#include <bits/stdc++.h>
using namespace std;
#define ii pair<int, int>

const int maxn = 200 + 7;
string a, b;
int dp[maxn][maxn];

int lcs(int i = a.length() - 1, int j = b.length() - 1) {
	if (i == -1 || j == -1) return 0;
	if (dp[i][j] + 1) return dp[i][j];
	dp[i][j] = max(lcs(i - 1, j), lcs(i, j - 1));
	if (a[i] == b[j]) dp[i][j] = max(dp[i][j], 1 + lcs(i - 1, j - 1));
	return dp[i][j];
}

void solve() {
	stack<ii > st;
	int i = a.length() - 1, j = b.length() - 1;
	st.push(ii(a.length(), b.length());
	while (i + 1 && j + 1) {
		if (a[i] == b[j]) {
			st.push(ii(i, j));
			--j; --i;
		}
		else {
			if (dp[i - 1][j] == dp[i][j]) --i;
			else --j;
		}
	}
	i = 0; j = 0;
	while (!st.empty()) {
		while (i < st.top().first) cout << a[i++];
		while (j < st.top().second) cout << b[j++];
		st.pop();
		if (a.length() - i) cout << a[i];
		++i; ++j;
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (cin >> a >> b) {
		memset(dp, -1, sizeof(dp));
		lcs();
		solve();
	}

	return 0;
}
