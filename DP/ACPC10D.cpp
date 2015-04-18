/*
**	Author: Abhilash
**	Date:	18.04.2015
*/
// Bottom up computation
//
#include <bits/stdc++.h>
#define sf							scanf
#define pf 							printf
typedef long long ll;
using namespace std;
const ll N = 1e6+3;
const ll inf = 1e18;

ll DP[N][3];
ll cost[N][3];

ll n;

ll move[4][2] = {{1, -1}, {0, 1}, {1, 1}, {1, 0}};

ll dp() {
	DP[n][0] = cost[n][0]+cost[n][1];
	DP[n][1] = cost[n][1];
	DP[n][2] = inf;
	ll r, c, ans;
	for (int i = n-1; i >= 1; --i) {
		for (int j = 2; j >= 0; --j) {
			ans = inf;
			for (int k = 0; k < 4; ++k) {
				r = i + move[k][0];
				c = j + move[k][1];
				if (c >= 0 && c <= 2) {
					ans = min(ans, cost[i][j] + DP[r][c]);
				}
			}
			DP[i][j] = ans;
		}
	}
	return DP[1][1];
}

int main() {
	sf("%lld", &n);
	ll T = 1;
	while (n) {
		for (int i = 0; i < n; ++i) 
			sf("%lld %lld %lld", &cost[i+1][0],
						&cost[i+1][1],
						&cost[i+1][2]);
		pf("%lld. %lld\n", T++, dp());
		sf("%lld", &n);
	}
	
	return 0;
}
