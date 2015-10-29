/*
  chennai icpc online round prob C
  using dp
  minimize inversions in new seq built from old seq
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1000 + 7;
int ar[maxn];
int n;
int dp[maxn][maxn][2][2];

int cnt(int l, int r, int os, int ns) {
	int x;
	if (os) x = ar[r];
	else x = ar[l];
	int less = 0, great = 0;
	for (int i = 0; i < n; ++i) {
		if (i < l || i > r) {
			less += ar[i] < x;
			great += ar[i] > x;
		}
	}
	int ans;
	if (ns) {
		// right put
		ans = less;
	}
	else ans = great;
	return ans;
}


const int inf = 1e8;

int solve(int l, int r, int os, int ns) {
	if (l > r) return inf;
	if (l == r) {
		return cnt(l, r, os, ns);
	}
	if (dp[l][r][os][ns] != -1)
		return dp[l][r][os][ns];
	int ad = cnt(l, r, os, ns);
	int ans = inf;
	int nl, nr;
	if (os) {
		// right pick
		nr = r - 1;
		nl = l;
	}
	else {
		nl = l + 1;
		nr = r;
	}
	for (int i = 0; i < 2; ++i) 
		for (int j = 0; j < 2; ++j)
			ans = min(ans, ad + solve(nl, nr, i, j));	
	
	return dp[l][r][os][ns] = ans;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t; cin >> t;
	while (t--) {
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> ar[i];
		memset(dp, -1, sizeof(dp));
		int ans = inf;
		for (int i = 0; i < 2; ++i) 
			for (int j = 0; j < 2; ++j)
				ans = min(ans, solve(0, n - 1, i, j));
		cout << ans << endl;		
	}

	return 0;
}
