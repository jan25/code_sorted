// http://www.spoj.com/problems/SAFECRAC/
/*
  matrix exp. O(logN) per query
*/  

#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll mod = 1e9 + 7;

ll g[10][10] = {
	{0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
	{0, 0, 1, 0, 1, 0, 0, 0, 0, 0},
	{0, 1, 0, 1, 0, 1, 0, 0, 0, 0},
	{0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
	{0, 1, 0, 0, 0, 1, 0, 1, 0, 0},
	{0, 0, 1, 0, 1, 0, 1, 0, 1, 0},
	{0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
	{1, 0, 0, 0, 1, 0, 0, 0, 1, 0},
	{0, 0, 0, 0, 0, 1, 0, 1, 0, 1},
	{0, 0, 0, 0, 0, 0, 1, 0, 1, 0}
};

ll n;

ll tmp[10][10];

void copy(ll a[][10], ll b[][10]) {
	for (ll i = 0; i < 10; ++i)
		for (ll j = 0; j < 10; ++j)
			a[i][j] = b[i][j];
}

void mul(ll a[][10], ll b[][10]) {
	for (ll i = 0; i < 10; ++i) {
		for (ll j = 0; j < 10; ++j) {
			tmp[i][j] = 0;
			for (ll k = 0; k < 10; ++k) {
				tmp[i][j] += a[i][k] * b[k][j];
				if (tmp[i][j] >= mod) tmp[i][j] %= mod;
			}
		}
	}
}

ll tg[10][10];

void solve() {
	ll ans[10][10];
	memset(ans, 0, sizeof(ans));
	for (ll i = 0; i < 10; ++i)
		ans[i][i] = 1;
	copy(tg, g);
	while (n) {
		if (n % 2) {
			mul(ans, tg);
			copy(ans, tmp);
		}
		mul(tg, tg);
		copy(tg, tmp);
		n >>= 1;
	}
	ll pans = 0;
	for (ll i = 0; i < 10; ++i) {
		for (ll j = 0; j < 10; ++j) {
			pans += ans[i][j];
			if (pans >= mod) pans %= mod;
		}
	}
	printf("%lld\n", pans);
}

int main() {
	ll t;
	scanf("%lld", &t);
	while (t--) {
		scanf("%lld", &n);
		--n;
		solve();
	}

	return 0;
}
