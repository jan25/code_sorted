// http://www.spoj.com/problems/ABA12C/
/*
  DP
  O(k * k * n) space and time too
*/  

#include <bits/stdc++.h>
using namespace std;

const int maxn = 101;
int ar[maxn];
int DP[maxn][maxn][maxn];
int n, k;
int inf = 1e9 + 7;

int dp(int i = k, int np = n, int kg = k) {
	if (i == 0) {
		if (np >= 0 && kg == 0) return 0;
		return inf;
	}
	if (DP[i][np][kg] + 1) return DP[i][np][kg];
	if (ar[i] == -1) return dp(i - 1, np, kg);
	int w = i;
	int ans = dp(i - 1, np, kg);
	int n = np;
	while (n && w <= kg) {
		ans = min(ans, ar[i]*(w/i) + dp(i - 1, n - 1, kg - w));
		w += i;
	}
	return DP[i][np][kg] = ans;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t; cin >> t;
	while (t--) {
		cin >> n >> k;
		for (int i = 1; i <= k; ++i) 
			cin >> ar[i];
		memset(DP, -1, sizeof(DP));
		cout << (dp() >= inf ? -1 : dp()) << endl;
	}

	return 0;
}
